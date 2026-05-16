# Claude Code Instructions

These instructions apply to Claude Code in this repository.

## Shared project rules

Follow:

- `docs/agent-rules.md`
- `docs/testing.md`
- `docs/architecture.md`
- `docs/release.md`
- `docs/claude-code-setup.md`
- `docs/mcp-security.md`

## Claude-specific behaviour

- Prefer review-first workflows.
- Before editing, inspect the current git status and relevant diff.
- When reviewing, categorise findings as:
  - Must fix
  - Should fix
  - Optional
- Do not edit during review unless explicitly asked.
- Do not commit, push, merge, deploy, or publish unless explicitly told.
- For large tasks, suggest splitting into smaller PRs.

## Project MCPs and skills

Project-specific MCPs should be added only when the current repo needs them.

Use these skills where relevant:

- `review-pr`
- `write-tests`
- `debug-issue`
- `android-testing`
- `design-to-code`
- `ui-assets`

Do not use MCP tools unnecessarily. Use them only when they provide relevant project context.

For design/UI work, use design tools such as Figma, Stitch, 21st.dev/Magic, or Rive only when relevant. Adapt output to the existing app architecture and design system.

For full guidance, read:

- `docs/project-level-mcps-and-skills.md`
- `docs/mcp-security.md`
- `docs/skills-anatomy.md`

## Default review focus

When reviewing changes, focus on:

- correctness
- missed edge cases
- security
- regression risk
- missing tests
- unnecessary complexity
- maintainability
