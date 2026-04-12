# Bi-Weekly Update — Workflow Spec

> Dawn's version. Covers all 4 teams. Publishes to Confluence PRH space.
> Run every two weeks, typically at the end of a sprint cycle.
> Invoke by asking Claude to "run the bi-weekly update" or "prep the bi-weekly."

---

## What This Produces

A structured update document published to Confluence covering:
- Sprint progress and completion across all 4 teams
- Customer call insights from the past 2 weeks
- Competitive signals from the past 2 weeks
- Key decisions and risks
- What's coming next sprint

---

## Step 1 — Gather Jira Sprint Status (all 4 teams)

For each team, pull the current sprint's issues and summarize:

| Team | Jira Project | Board |
|------|-------------|-------|
| Sprinters (Roobrik) | ROOB | Look up active sprint |
| Accelerators (AI) | AA | Look up active sprint |
| Helix (BI) | PBI | Board 146 — Data Team Scrum Board |
| L&B | ARMS | Look up active sprint |

For each team, produce:
- **Completed this sprint:** issues moved to Done
- **In progress:** issues still active
- **Blocked / at risk:** anything flagged or overdue
- **Carried over:** issues not completed from prior sprint

Group by initiative where possible (read team CLAUDE.md files for initiative names).

---

## Step 2 — Synthesize Customer Insights

Read Confluence PRH > Customers folder (ID: `17748688902`).
Find all call summary pages created or updated in the past 14 days.

For each call found, extract:
- Customer name
- Key themes discussed
- Feature requests surfaced
- Open action items

Produce a 3–5 bullet synthesis: "What customers are telling us this fortnight."

---

## Step 3 — Competitive Signals

Read `competitive/competitors/*/tldr.md` files — check "Recent Signals" sections.
Identify any signals dated within the past 14 days.

Also check Confluence PRH > Competitors folder (ID: `17749278721`) for any recently updated pages.

Produce a 2–4 bullet summary of notable competitive movements.

---

## Step 4 — Draft the Update Document

Structure:

```markdown
# Bi-Weekly Update — [Date Range]

*Prepared: YYYY-MM-DD*

## Sprint Summary

### Sprinters — Roobrik
**Completed:** [list]
**In Progress:** [list]
**Blocked:** [list if any]

### Accelerators — AI
[same structure]

### Helix — BI / Fabric
[same structure]

### L&B
[same structure]

## Customer Insights
[3–5 bullets from Step 2]

## Competitive Signals
[2–4 bullets from Step 3]

## Key Decisions This Fortnight
[Any notable product, technical, or process decisions made — pull from Jira comments, meeting notes if available]

## Risks & Watch Items
[Anything that needs attention before next sprint]

## Coming Up Next
[Next sprint priorities across teams — infer from backlog or in-progress items]
```

---

## Step 5 — Publish to Confluence

Publish the draft to Confluence PRH space.

- **Parent page:** Ask Dawn where she wants these to live, or default to a "Bi-Weekly Updates" page under PRH root
- **Title:** `Bi-Weekly Update — [start date] to [end date]`
- **Version note:** "Generated from Jira + Confluence data"

After publishing, provide the Confluence URL and ask: "Anything to add or change before sharing?"

---

## Notes

- Do not fabricate sprint data — if a Jira query returns nothing, say so and ask Dawn to check
- Customer insights are only as good as the call summaries in Confluence — if calls haven't been logged, note the gap
- Keep the tone factual and brief — this is a status update, not a narrative
