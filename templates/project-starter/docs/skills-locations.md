# Codex and Claude Skills Locations

## Codex

Use this repo-scoped location for Codex skills:

```text
.agents/skills/<skill-name>/SKILL.md
```

Codex also supports user-level skills at:

```text
~/.agents/skills/<skill-name>/SKILL.md
```

Use `.codex/config.toml` for Codex configuration and MCP servers. Do not put Codex skills under `.codex/skills/` unless you are using a legacy/private convention and explicitly telling the agent to read them manually.

Codex project instructions usually live in `AGENTS.md`. Personal global instructions can live in `~/.codex/AGENTS.md`.

## Claude Code

Use this repo-scoped location for Claude Code skills:

```text
.claude/skills/<skill-name>/SKILL.md
```

For shared plugin-style setups, Claude plugins can bundle skills, agents, hooks, MCP servers, and other components.

Claude Code project instructions live in `CLAUDE.md` or `.claude/CLAUDE.md`. Personal global instructions live in `~/.claude/CLAUDE.md`. Private project notes can live in `CLAUDE.local.md`, which should stay gitignored.

Project-level Claude subagents live in:

```text
.claude/agents/<agent-name>.md
```

## Recommended project template

```text
AGENTS.md
CLAUDE.md
.agents/skills/        # Codex skills
.claude/skills/        # Claude Code skills
.claude/agents/        # Claude Code subagents
.claude/settings.json  # Shared Claude settings/hooks, if needed
.codex/config.toml     # Codex project MCP/config, if needed
.mcp.json              # Claude shared project MCP config, if needed
```

For SKILL.md structure and selection behaviour, read `docs/skills-anatomy.md`.
