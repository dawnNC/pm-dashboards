# Competitive Intelligence Index

> Source of truth for competitor tracking. Updated by `/competitive-analysis` skill runs and the weekly `competitive-intel-agent`.

## Competitors

| Folder | Competitor | Segment | Last Updated |
|--------|-----------|---------|--------------|
| [yardi/](competitors/yardi/CLAUDE.md) | Yardi | Enterprise ERP + CRM | — |
| [pointclickcare/](competitors/pointclickcare/CLAUDE.md) | PointClickCare | Skilled Nursing / Care | — |
| [welcomehome/](competitors/welcomehome/CLAUDE.md) | WelcomeHome | CRM (IL/AL) | — |
| [eldermark/](competitors/eldermark/CLAUDE.md) | Eldermark | AL / Memory Care | — |
| [matrixcare/](competitors/matrixcare/CLAUDE.md) | MatrixCare | Skilled Nursing / Post-Acute | — |
| [hubspot/](competitors/hubspot/CLAUDE.md) | HubSpot | General CRM (indirect) | — |
| [salesforce/](competitors/salesforce/CLAUDE.md) | Salesforce | General CRM (indirect) | — |

## Master Matrix

[competitive-matrix.md](competitors/competitive-matrix.md) — feature comparison across all competitors.

## Aline's Positioning

- **Sales & Marketing:** Aline CRM is purpose-built for senior living sales counselors. Competitors either require heavy customization (Salesforce, HubSpot) or lack modern AI features (WelcomeHome, Eldermark).
- **AI differentiation:** Opportunity scoring, AI text drafts, Smart Next Step — no direct competitor matches this feature set in senior living context.
- **Roobrik:** Unique entry point at top of funnel. No direct competitor has an equivalent survey product.
- **BI / Reporting:** Fabric migration positions Aline ahead of legacy BI vendors in the space.

## Confluence

**Competitors folder (PRH space):** `17749278721`
URL: https://alineops.atlassian.net/wiki/spaces/PRH/pages/17749278721

Each competitor has a page in this folder that mirrors the local files. Both are updated on every analysis run.

## How to Update

Run `/competitive-analysis` and specify a competitor. The skill updates the local competitor folder files AND the Confluence page.
The `competitive-intel-agent` runs weekly and patches `tldr.md` files with new signals (and updates Confluence pages accordingly).
