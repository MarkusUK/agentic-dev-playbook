# Release and PR Rules

## Branching

Work on feature branches:

```text
feature/<short-name>
fix/<short-name>
```

Do not commit, push, merge, deploy, or publish unless explicitly told.

## Before Commit

Check:

- Diff is small and reviewable.
- Relevant tests/checks have run.
- Docs are updated when behaviour or setup changes.
- No secrets or local-only config are included.
- Dependency changes are intentional and explained.

## PR Checklist

- Summary of change
- Screenshots or screen recordings for UI changes
- Tests/checks run
- Known risks or follow-ups
- Any design/spec handoff link or summary

## Before Merge

Claude Code or another reviewer should review:

- correctness
- regression risk
- security and data-loss risk
- missing tests
- unnecessary complexity
