# Agentic Dev Project Starter

A reusable setup for producing safer, higher-quality code with Codex, Claude Code, Git branches, tests, reviews, MCP, skills, and hooks.

Recommended workflow:

```text
Codex = implement
Claude Code = review
You = approve
CI = enforce
GitHub PR = final audit trail
```

Copy these files into the root of a new project and adjust the commands, stack details, and repo-specific rules.

## Included

```text
AGENTS.md                         # Codex/general agent instructions
CLAUDE.md                         # Claude Code-specific instructions
docs/agent-rules.md               # Shared rules for all coding agents
docs/testing.md                   # General and Android CLI testing guidance
docs/architecture.md              # Architecture context template
docs/release.md                   # Release and PR safety guidance
docs/agent-workflow-reference.md  # Full reference guide from the recommended setup
docs/codex-setup.md               # Codex config, AGENTS.md, skills, sandboxing
docs/claude-code-setup.md         # Claude settings, CLAUDE.md, hooks, subagents
docs/model-selection.md           # Model and effort selection notes
docs/hooks.md                     # Hook and guardrail examples
docs/mcp-primer.md                # Plain-English MCP, skills, hooks primer
docs/skills-anatomy.md            # SKILL.md frontmatter and selection guide
docs/mcp-security.md              # MCP and skills security checklist
docs/troubleshooting.md           # Common setup and agent-tooling issues
.claude/settings.json             # Minimal shared Claude settings and hook example
.claude/agents/                   # Starter Claude Code subagents
.claude/skills/                   # Starter Claude Code skills
.agents/skills/                    # Starter Codex-style skills
```

## First thing to customise

Edit:

```text
docs/architecture.md
docs/testing.md
docs/release.md
docs/mcp-security.md
docs/model-selection.md
AGENTS.md
CLAUDE.md
```

Replace placeholder commands such as `npm test`, `./gradlew test`, or `./gradlew connectedAndroidTest` with your real project commands.

## MCP and design tooling

See `docs/mcp-and-skills.md` plus `config-examples/` for Codex and Claude MCP setup patterns for Figma, Stitch, 21st.dev/Magic, and Rive-oriented workflows.

Read `docs/mcp-security.md` before committing any shared MCP config or new skills.

## Project-level MCPs and skills

See `docs/project-level-mcps-and-skills.md` for:

- adding MCPs per project
- adding Codex and Claude skills
- prompting agents to use external tools
- examples for Figma, Stitch, 21st.dev/Magic, Rive, review, testing, and Android terminal workflows
- security and scoping decisions for repo-level tools


## Design start workflow

See `design-start/` for a step-by-step design workflow with copy/paste prompts for:

- brand discovery
- three design directions
- Figma/Stitch/21st.dev/Rive MCP exploration
- brand kit creation
- screen specs
- interactive React/Tailwind mockups
- implementation handoff to Codex/Claude
