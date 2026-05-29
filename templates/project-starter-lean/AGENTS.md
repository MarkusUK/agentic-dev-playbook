# Agent Instructions

These instructions apply to Codex and other coding agents in this repo.

## Read First

Before changing code, read:

- `docs/architecture.md`
- `docs/testing.md`
- `docs/release.md`
- `design-start/README.md`

## Workflow

```text
Codex = implement
Claude Code = review
You = approve
CI = enforce
GitHub PR = final audit trail
```

## Must Not Do

- Do not commit, push, merge, deploy, or publish unless explicitly told.
- Do not touch `.env`, `.env.*`, `*.key`, `*.keystore`, `secrets/**`, production config, or signing files unless explicitly requested.
- Do not add dependencies without explaining why.
- Do not overwrite design-system files, theme tokens, or shared components casually.

## Must Do

- Inspect existing files before editing.
- Work on a feature branch.
- Keep changes small and reviewable.
- Match existing project patterns.
- Run relevant tests/checks before finishing.
- Update docs when behaviour or setup changes.

## Commands

Replace these with real project commands:

```text
Tests: command discovery needed
Lint: command discovery needed
Typecheck: command discovery needed
Build: command discovery needed
Run app: command discovery needed
```

## Design and UI Work

Before implementing new UI, use `design-start/` to clarify:

- target user and workflow
- brand direction and tone
- colour, typography, spacing, and component feel
- first screens and states
- accessibility requirements
- implementation handoff

Use the `design-to-code` and `ui-assets` skills when relevant. Treat generated UI or MCP output as inspiration, then adapt it to this repo's architecture and design system.

## Skills

Use these project skills when relevant:

- `.agents/skills/review-pr/SKILL.md`
- `.agents/skills/write-tests/SKILL.md`
- `.agents/skills/design-to-code/SKILL.md`
- `.agents/skills/ui-assets/SKILL.md`

## Final Response

End coding tasks with:

```text
Summary:
Files changed:
Commands run:
Tests/checks:
Risks/follow-ups:
```
