#!/usr/bin/env python3
"""Refresh the SVP Product Report data from Jira Polaris board CRMO.

Pulls every CRMO idea whose Working Quarter(s) include Q3 2026 and/or
Q4 2026, maps the fields, and rewrites the DATA array inside index.html
(between the // <DATA> and // </DATA> markers).

Auth mirrors jira-triage: put JIRA_USERNAME and JIRA_TOKEN in a .env
file alongside this script (never commit it). Token is an Atlassian API
token from https://id.atlassian.com/manage-profile/security/api-tokens.

Usage:
    python fetch_crmo.py                 # refresh with default scope
    python fetch_crmo.py --dry-run       # print the DATA array, don't write
    python fetch_crmo.py --quarters "Q3 2026,Q4 2026"
"""

import argparse
import json
import os
import re
import sys
from datetime import date, datetime, timezone

import requests

JIRA_BASE = "https://alineops.atlassian.net"
PROJECT = "CRMO"

# Custom field IDs on the CRMO project (id 10182), resolved 2026-07-14.
FIELDS = {
    "size":            "customfield_13608",  # Size (select)
    "product":         "customfield_10805",  # Product (select)
    "build_complete":  "customfield_10778",  # Build Complete Target Date (interval)
    "ga_target":       "customfield_10786",  # GA Target Date (interval)
    "working_quarter": "customfield_13611",  # Working Quarter(s) (multi-checkbox)
}

# Products with no value in Jira are hidden per report config.
HIDE_MISSING_PRODUCT = True

# Path to the dashboard file, relative to this script.
HTML_PATH = os.path.join(os.path.dirname(__file__), "index.html")


def load_env():
    """Load JIRA_USERNAME / JIRA_TOKEN from a sibling .env if present."""
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    if os.path.exists(env_path):
        with open(env_path) as fh:
            for line in fh:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))
    user = os.environ.get("JIRA_USERNAME")
    token = os.environ.get("JIRA_TOKEN")
    if not user or not token:
        sys.exit("Missing JIRA_USERNAME / JIRA_TOKEN (set in .env or environment).")
    return user, token


def search_all(auth, jql, fields):
    """Page through /rest/api/3/search/jql using nextPageToken."""
    url = f"{JIRA_BASE}/rest/api/3/search/jql"
    issues, token = [], None
    while True:
        payload = {"jql": jql, "fields": fields, "maxResults": 100}
        if token:
            payload["nextPageToken"] = token
        resp = requests.post(url, json=payload, auth=auth,
                             headers={"Accept": "application/json"}, timeout=60)
        resp.raise_for_status()
        data = resp.json()
        issues.extend(data.get("issues", []))
        token = data.get("nextPageToken")
        if not token or data.get("isLast", True):
            break
    return issues


def interval_end(raw):
    """Polaris interval fields are JSON strings like
    '{"start":"2026-08-21","end":"2026-08-21"}'. Return the end date (ISO)."""
    if not raw:
        return None
    try:
        obj = json.loads(raw) if isinstance(raw, str) else raw
        return obj.get("end") or obj.get("start")
    except (ValueError, AttributeError):
        return None


def opt_value(field):
    """Single-select custom fields come back as {'value': '...'}."""
    if isinstance(field, dict):
        return field.get("value")
    return field


def opt_list(field):
    """Multi-checkbox fields come back as {'value': ['...', ...]}."""
    if isinstance(field, dict):
        v = field.get("value")
        return v if isinstance(v, list) else ([v] if v else [])
    if isinstance(field, list):
        return field
    return []


def build_records(issues, scope_quarters):
    records = []
    for it in issues:
        f = it.get("fields", {})
        product = opt_value(f.get(FIELDS["product"]))
        if HIDE_MISSING_PRODUCT and not product:
            continue
        wq_all = opt_list(f.get(FIELDS["working_quarter"]))
        wq = [q for q in scope_quarters if q in wq_all]
        records.append({
            "key": it.get("key"),
            "name": (f.get("summary") or "").strip(),
            "product": product or "Unassigned",
            "size": opt_value(f.get(FIELDS["size"])),
            "devTarget": interval_end(opt_value(f.get(FIELDS["build_complete"]))),
            "gaTarget": interval_end(opt_value(f.get(FIELDS["ga_target"]))),
            "status": (it.get("fields", {}).get("status") or {}).get("name"),
            "wq": wq,
        })
    records.sort(key=lambda r: r["name"].lower())
    return records


def to_js_array(records):
    lines = ["const _ALL_IDEAS = ["]
    for r in records:
        lines.append("  " + json.dumps(r, ensure_ascii=False) + ",")
    lines.append("];")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quarters", default="Q3 2026,Q4 2026",
                    help="Comma-separated Working Quarter(s) to include.")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    scope = [q.strip() for q in args.quarters.split(",") if q.strip()]
    user, token = load_env()
    auth = (user, token)

    quoted = ", ".join(f'"{q}"' for q in scope)
    jql = (f'project = {PROJECT} AND "Working Quarter(s)" in ({quoted}) '
           f"ORDER BY summary ASC")
    field_ids = ["summary", "status"] + list(FIELDS.values())

    issues = search_all(auth, jql, field_ids)
    records = build_records(issues, scope)
    js_array = to_js_array(records)

    print(f"Fetched {len(issues)} issues, kept {len(records)} "
          f"(scope: {', '.join(scope)}).", file=sys.stderr)

    if args.dry_run:
        print(js_array)
        return

    with open(HTML_PATH, encoding="utf-8") as fh:
        html = fh.read()

    # Replace the array between the const declaration and its closing "];".
    pattern = re.compile(r"const _ALL_IDEAS = \[.*?\n\];", re.DOTALL)
    if not pattern.search(html):
        sys.exit("Could not find the _ALL_IDEAS array in index.html.")
    html = pattern.sub(js_array, html, count=1)

    # Refresh the sync date.
    stamp = date.today().strftime("%b %-d, %Y")
    html = re.sub(r'const JIRA_SYNC = "[^"]*";',
                  f'const JIRA_SYNC = "{stamp}";', html, count=1)

    with open(HTML_PATH, "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"Wrote {len(records)} records to {HTML_PATH} (synced {stamp}).",
          file=sys.stderr)


if __name__ == "__main__":
    main()
