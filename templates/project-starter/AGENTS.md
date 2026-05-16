# Agent Instructions

These instructions apply to Codex and other coding agents working in this repository.

## Read first

Before making changes, read:

- `docs/agent-rules.md`
- `docs/testing.md`
- `docs/architecture.md`
- `docs/release.md`
- `docs/codex-setup.md`
- `docs/mcp-security.md`

## Core rules

- Inspect before editing.
- Work only on a feature branch.
- Keep changes small and reviewable.
- Do not commit, push, merge, deploy, or publish unless explicitly told.
- Do not touch secrets, `.env` files, credentials, production config, signing keys, generated files, or lockfiles unless the task explicitly requires it.
- Do not add dependencies without explaining why.
- Prefer minimal, targeted changes over broad rewrites.
- Run relevant tests before finishing.
- Summarise changed files and commands run.

## Project MCPs and skills

Project-specific MCPs should live in `.codex/config.toml`, not global config, unless they are safe and useful everywhere. Codex skills should live in `.agents/skills/`.

Use these skills where relevant:

- `.agents/skills/review-pr/SKILL.md`
- `.agents/skills/write-tests/SKILL.md`
- `.agents/skills/debug-issue/SKILL.md`
- `.agents/skills/android-testing/SKILL.md`
- `.agents/skills/design-to-code/SKILL.md`
- `.agents/skills/ui-assets/SKILL.md`

For design/UI work, use MCP tools such as Figma, Stitch, 21st.dev/Magic, or Rive only when relevant. Always adapt external output to the existing design system.

For full guidance, read:

- `docs/project-level-mcps-and-skills.md`
- `docs/mcp-security.md`
- `docs/skills-anatomy.md`

## Expected workflow

1. Inspect the repo and relevant files.
2. Propose a short implementation plan.
3. Wait for approval if the task is risky or broad.
4. Implement the smallest useful change.
5. Run relevant tests, type checks, linters, and builds.
6. Report:
   - what changed
   - why it changed
   - tests run
   - known risks or follow-ups

## Done means

- Code compiles or builds.
- Relevant tests pass, or failures are clearly explained.
- Edge cases are considered.
- Docs are updated when behaviour changes.
- Diff is small enough for human review.
