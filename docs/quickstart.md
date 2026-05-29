# Start Here in 10 Minutes

Use this page to copy the starter into a new project and make the minimum edits needed before using agents.

Goal:

```text
Copy starter -> customise project facts -> confirm commands -> ready to spec, design, and code
```

This page is not the full design/spec workflow. It gets the repo ready so Codex and Claude Code have useful project instructions instead of generic placeholders.

## 1. Copy the starter

For most new apps, copy the lean starter:

```text
templates/project-starter-lean/
```

into your new project root.

Use the full starter only if you want the new repo to carry the complete local reference docs:

```text
templates/project-starter/
```

Keep what fits your project. Delete anything that is clearly irrelevant.

## 2. Customise the required files

Edit these before asking an agent to change code:

```text
AGENTS.md
CLAUDE.md
docs/architecture.md
docs/testing.md
docs/release.md
```

Replace starter defaults with real project information:

- stack and package managers
- test, lint, build, and run commands
- protected files and folders
- branch, PR, release, and deploy rules
- known risks or project-specific gotchas
- MCPs and skills actually available in this repo

For commands, the aim is simple: remove fake placeholders.

If you know the command, write it down. If you do not know it yet, mark
that as a setup task and let the no-code reconnaissance step find it.

Example:

```text
Tests: npm test
Lint: npm run lint
Build: command discovery needed
```

The purpose is to stop agents trying to run placeholder commands such as
`<your test command>`. Real commands are useful. Fake commands are noise.

The no-code reconnaissance prompt in step 6 asks the agent to inspect
files such as `package.json`, `pyproject.toml`, `pubspec.yaml`,
`Cargo.toml`, `Makefile`, or `README.md` and identify the real commands.

Useful references:

- [Starter Template Guide](templates.md)
- [Example AGENTS.md and CLAUDE.md](core/example-agents-and-claude.md)

## 3. Use the default agent workflow

Recommended default:

```text
Codex = implement
Claude Code = review
You = approve
CI = enforce
GitHub PR = final audit trail
```

Codex is the main coding agent. Claude Code is the independent review pass before you commit or merge.

## 4. Keep MCP config lean

Default/user-level config usually lives here:

```text
Codex:       ~/.codex/config.toml
Claude Code: ~/.claude/ settings and Claude-managed MCP config
```

Project-level config usually lives here:

```text
Codex:       .codex/config.toml
Claude Code: .mcp.json, .claude/settings.json, .claude/skills/
```

Recommended:

- Keep global config limited to tools you trust and use everywhere.
- Put repo-specific tools in project-level config.
- Prefer read-only MCPs first.
- Disable or remove MCPs you are not actively using.
- Never put secrets directly in config files; use environment variables.

Mental model:

```text
MCP = what the agent can access
Skills = how the agent should work
Prompt = what it should use right now
```

Read later:

- [MCP and Skills Primer](mcp/mcp-primer.md)
- [Project-Level MCPs and Skills](mcp/project-level-mcps-and-skills.md)
- [MCP and Skills Security](mcp/security.md)

## 5. Check the skills are relevant

The lean starter includes:

```text
review-pr
write-tests
design-to-code
ui-assets
```

The full starter also includes extra reference skills such as `debug-issue` and `android-testing`.

Delete skills you do not need. Keep skills you expect to use repeatedly.

Locations:

```text
Codex:       .agents/skills/<skill-name>/SKILL.md
Claude Code: .claude/skills/<skill-name>/SKILL.md
```

## 6. Run a no-code reconnaissance prompt

Open Codex or Claude Code in the project and ask:

```text
Read AGENTS.md, CLAUDE.md, docs/architecture.md, docs/testing.md, and docs/release.md.

Do not edit files yet.

Tell me:
- what stack this project uses
- which commands are available
- which files or folders are protected
- what information is still missing from the setup
- what the safest next step should be
```

Fix anything it identifies before starting real work.

## 7. You are ready to spec, design, or code

After this setup, choose the next workflow:

- For product shape, brand, screens, and implementation handoff: [Design Start Workflow](design-start/README.md)
- For MCP and skills setup: [MCP and Skills](mcp/mcp-and-skills.md)
- For the first coding task: ask Codex to implement one small approved slice, then ask Claude Code to review the diff.

Recommended next step for a new product:

```text
Start Here in 10 Minutes
-> Design Start Workflow
-> Implementation Handoff
-> Codex implements
-> Claude Code reviews
```

Use [Design Start Workflow](design-start/README.md) to work with the agents on the spec, product direction, logo/brand kit, first screens, mockups, and implementation handoff before writing production code.

Good first coding prompt:

```text
Use the approved brief/spec/design handoff.
Inspect the repo first.
Propose the smallest safe implementation plan.
Do not commit.
```

## 8. Optional deeper setup

Read these when you want more detail:

- [Codex Setup Notes](core/codex-setup.md)
- [Claude Code Setup Notes](core/claude-code-setup.md)
- [Hooks and Guardrails](core/hooks.md)
- [Model Selection](core/model-selection.md)
