# Starter Template Guide

The starter template is the reusable payload for new projects.

```text
templates/project-starter/
```

Copy its contents into the root of a new repo, then customise it for that project's stack, test commands, release process, and external tools.

The public docs are grouped into `docs/core/`, `docs/mcp/`, and `docs/design-start/`. The starter intentionally keeps most project docs flat under `templates/project-starter/docs/` so copied projects are easier to scan.

## What is included

```text
AGENTS.md                         # Codex/general agent instructions
CLAUDE.md                         # Claude Code-specific instructions
docs/agent-rules.md               # Shared rules for all coding agents
docs/testing.md                   # Test, lint, build, and Android guidance
docs/architecture.md              # Architecture context template
docs/release.md                   # Release and PR safety guidance
docs/agent-workflow-reference.md  # Full agent workflow reference
docs/codex-setup.md               # Codex config, AGENTS.md, skills, sandboxing
docs/claude-code-setup.md         # Claude settings, CLAUDE.md, hooks, subagents
docs/example-agents-and-claude.md # Worked AGENTS.md and CLAUDE.md example
docs/model-selection.md           # Model and effort selection notes
docs/hooks.md                     # Hook and guardrail examples
docs/mcp-primer.md                # Plain-English MCP, skills, hooks primer
docs/mcp-and-skills.md            # MCP and skills setup guide
docs/project-level-mcps-and-skills.md
docs/claude-mcp-scopes.md
docs/skills-locations.md
docs/skills-anatomy.md
docs/mcp-security.md
docs/troubleshooting.md
.claude/settings.json             # Minimal shared Claude settings and hook example
.claude/agents/                   # Starter Claude Code subagents
.agents/skills/                   # Codex repo-scoped skills
.claude/skills/                   # Claude Code repo-scoped skills
config-examples/                  # MCP examples for Codex and Claude
design-start/                     # Design discovery and handoff workflow
```

## First files to edit

Edit these before asking an agent to work in the new repo:

```text
AGENTS.md
CLAUDE.md
docs/architecture.md
docs/testing.md
docs/release.md
docs/project-level-mcps-and-skills.md
```

Remove stack-specific sections that do not apply. For example, delete Android emulator guidance if the project is web-only.

## What to keep private

Do not commit personal credentials, `.env` files, OAuth tokens, signing keys, keystores, production config, or local-only agent settings.

Project-specific MCP config can be committed only when it is safe for the team and contains no secrets. Prefer environment variables for credentials.

## What to customise for each repo

- Real test, lint, type-check, build, and run commands.
- Protected files or directories that agents should not change casually.
- Architecture boundaries and ownership notes.
- MCPs that are actually useful for the project.
- Skills that match repeated local workflows.
- Release and deployment rules.

## Suggested first prompt

```text
Read AGENTS.md, CLAUDE.md, docs/architecture.md, docs/testing.md, and docs/release.md.

Summarise:
- the project stack
- the safe commands to run
- protected files or areas
- which MCPs and skills are available
- anything missing before you can safely make changes
```

## Maintenance rule

When you update the public playbook, decide whether the starter template needs the same update. The public docs explain the system; the starter template is what new projects inherit.
