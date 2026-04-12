# Sprint Planning — Workflow Spec

> Dawn's version. Run at the start of each sprint for any of the 4 teams.
> Invoke by asking Claude to "help me prep sprint planning for [team]" or "run sprint planning for [team]."

---

## What This Produces

A sprint planning doc that gives the team a clear picture of:
- What's being committed this sprint and why
- How it maps to active initiatives
- Dependencies and risks called out upfront
- Success criteria defined before work starts

---

## Step 1 — Identify the Team

Ask which team this sprint planning is for (Sprinters / Accelerators / Helix / L&B), or infer from context.

Load the relevant team CLAUDE.md for:
- Active initiatives list
- Jira project key and board

---

## Step 2 — Pull Backlog Candidates

Query Jira for backlog-ready issues:
```
project = [PROJECT_KEY] AND sprint is EMPTY AND status != Done ORDER BY priority ASC
```

Also pull any issues explicitly flagged for next sprint (labels, sprint field, or "ready for sprint" status).

Group candidates by initiative.

---

## Step 3 — Pull Velocity Context

Check the last 2 completed sprints:
```
project = [PROJECT_KEY] AND sprint in closedSprints() ORDER BY startDate DESC
```

Note:
- Story points completed per sprint (if using points)
- Number of issues completed
- Carry-over rate (how much wasn't finished)

Use as a calibration guide — don't over-commit based on optimistic estimates.

---

## Step 4 — Draft the Sprint Plan

```markdown
# Sprint Planning — [Team] — Sprint [N] — [Start Date]

## Sprint Goal
[1–2 sentences: what does a successful sprint look like? What's the headline outcome?]

## Committed Issues

| Issue | Summary | Initiative | Points | Owner | Notes |
|-------|---------|-----------|--------|-------|-------|
| | | | | | |

**Total points committed:** [N]
**Last sprint velocity:** [N] pts / [N] issues

## Initiative Coverage

| Initiative | Issues this sprint | Status |
|-----------|-------------------|--------|
| [Initiative] | [N issues] | On track / At risk |

## Dependencies

[Any cross-team dependencies, external blockers, or prerequisites — be explicit]

## Risks

[What could prevent sprint completion? Flag early.]

## What's NOT in this sprint (and why)

[Explicitly note high-priority items that didn't make the cut — helps explain tradeoffs]

## Success Criteria

By end of sprint:
- [ ] [Specific, verifiable outcome]
- [ ] [Specific, verifiable outcome]
```

---

## Step 5 — Optional: Publish to Confluence

Offer to publish the sprint plan to Confluence PRH space under the team's section.

Title: `Sprint Planning — [Team] — [Sprint Start Date]`

---

## Notes

- The sprint goal is the most important part — don't skip it
- If velocity data isn't available from Jira, ask Dawn to estimate
- Dependencies and risks should be raised *before* the meeting, not during it
- "What's NOT in this sprint" prevents the team from feeling ambushed when items stay in backlog
