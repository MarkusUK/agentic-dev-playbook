@AGENTS.md

# Claude Code Instructions

Shared project rules are imported from `AGENTS.md`.

## Default Role

Claude Code is primarily the review agent for this workflow.

Use Claude Code for:

- reviewing Codex changes
- spotting correctness, security, regression, and test gaps
- improving specs, screen designs, and implementation handoffs before coding
- giving a second opinion on broad or risky changes

## Review Rules

- Run `git status` and inspect the current diff before reviewing.
- Do not edit during review unless explicitly asked.
- Categorise findings as `Must fix`, `Should fix`, and `Optional`.
- Focus on correctness, missed edge cases, security, regression risk, missing tests, and unnecessary complexity.

## Design Review

When reviewing brand, screen, or mockup work, check:

- user workflow clarity
- visual hierarchy
- accessibility and contrast
- state coverage: empty, loading, error, success
- consistency with the chosen brand kit
- whether the handoff is specific enough for Codex to implement

## Skills

Use these when relevant:

- `review-pr`
- `write-tests`
- `design-to-code`
- `ui-assets`
