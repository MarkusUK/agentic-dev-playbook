# Starter Template Guide

There are two starter templates.

```text
templates/project-starter-lean/    # recommended for most new apps
templates/project-starter/         # full reference-heavy starter
```

Copy one starter into the root of a new repo, then customise it for that project's stack, test commands, release process, and external tools.

The public docs are grouped into `docs/core/`, `docs/mcp/`, and `docs/design-start/`. The starters keep project docs flatter and more practical so copied projects are easier to scan.

## Recommended: lean starter

Use this for most real app repos:

```text
templates/project-starter-lean/
```

It includes the most important files only:

```text
AGENTS.md
CLAUDE.md
docs/architecture.md
docs/testing.md
docs/release.md
design-start/README.md
design-start/product-brief.md
design-start/brand-kit.md
design-start/screen-spec.md
design-start/implementation-handoff.md
.agents/skills/review-pr/
.agents/skills/write-tests/
.agents/skills/design-to-code/
.agents/skills/ui-assets/
.claude/skills/review-pr/
.claude/skills/write-tests/
.claude/skills/design-to-code/
.claude/skills/ui-assets/
```

This gives agents enough context to:

- understand project rules and protected files
- discover real test/lint/build commands
- help shape product specs and brand direction
- create quality screen specs before coding
- implement UI from an approved handoff
- review the resulting diff

## Full starter

Use this when you want the new repo to carry the whole local reference playbook:

```text
templates/project-starter/
```

It includes:

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

For either starter, edit these before asking an agent to work in the new repo:

```text
AGENTS.md
CLAUDE.md
docs/architecture.md
docs/testing.md
docs/release.md
design-start/
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

The lean starter includes four first prompts in its `README.md`:

- setup reconnaissance
- spec and design
- implementation planning
- Claude review

Use this one immediately after copying a starter:

```text
Read AGENTS.md, CLAUDE.md, docs/architecture.md, docs/testing.md, and docs/release.md.

Summarise:
- the project stack
- the safe commands to run
- protected files or areas
- which MCPs and skills are available
- anything missing before you can safely make changes
```

Then use the design and implementation prompts inside the copied starter when you are ready to shape the product and start coding.

## Maintenance rule

When you update the public playbook, decide whether either starter template needs the same update. The public docs explain the system; the starter templates are what new projects inherit.
