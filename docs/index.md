# Agentic Dev Playbook

A practical playbook for using Codex, Claude Code, MCPs, skills, design workflows, interactive mockups, and safe code review.

Recommended workflow:

```text
Codex = implement
Claude Code = review
You = approve
CI = enforce
GitHub PR = final audit trail
```

## Reading order for first-time visitors

If you have never used this playbook before, read in this order:

1. [Start Here in 10 Minutes](quickstart.md) — shortest setup path.
2. [MCP and Skills Primer](mcp/mcp-primer.md) — plain-English mental model.
3. [Codex Setup](core/codex-setup.md) **or** [Claude Code Setup](core/claude-code-setup.md) — pick the tool you use first.
4. [Hooks and Guardrails](core/hooks.md) — automatic safety.
5. [Example AGENTS.md and CLAUDE.md](core/example-agents-and-claude.md) — what a good filled-in version looks like.
6. [Starter Template](templates.md) — copy into a new project.

Everything else (skill anatomy, MCP scopes, design-start, troubleshooting) is reference. Look it up when you need it.

## Setup steps

1. Read [Start Here in 10 Minutes](quickstart.md).
2. Copy `templates/project-starter/` into a new project.
3. Customise `AGENTS.md`, `CLAUDE.md`, `docs/testing.md`, `docs/architecture.md`, and `docs/release.md`.
4. Keep global MCP config minimal.
5. Add project-level MCPs only when needed.
6. Use Codex to implement and Claude Code to review.
7. Validate the docs with `mkdocs build --strict` before publishing.

## Main sections

- **Core Workflow**: safe coding workflow, branch strategy, testing, release rules.
- **MCP and Skills**: how to add project-level MCPs and skills.
- **Design Start**: brand kits, screens, Figma/Stitch/21st.dev/Rive, interactive mockups.
- **Templates**: starter files to copy into each new project.
- **Copy/Paste Prompts**: ready-to-use prompts for design exploration and implementation handoff.
- **Wiki Map**: suggested GitHub Wiki companion structure.
- **Troubleshooting**: common setup, Pages, MCP, and skills issues.
