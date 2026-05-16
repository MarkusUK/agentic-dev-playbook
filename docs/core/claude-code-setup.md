# Claude Code Setup Notes

Claude Code uses several layers of project guidance and configuration. This page keeps the common pieces in one place.

## CLAUDE.md hierarchy

Claude Code reads `CLAUDE.md`, not `AGENTS.md`.

Useful locations:

```text
~/.claude/CLAUDE.md        # personal defaults across projects
./CLAUDE.md                # project instructions
./.claude/CLAUDE.md        # alternative project instructions location
./CLAUDE.local.md          # private local project notes, gitignored
```

If a repo already has `AGENTS.md`, use `CLAUDE.md` to import it:

```markdown
@AGENTS.md

## Claude Code

Prefer review-first workflows. Do not edit during review unless explicitly asked.
```

## Settings

Project settings that should be shared can live in:

```text
.claude/settings.json
```

Personal local overrides should live in:

```text
.claude/settings.local.json
```

Keep `settings.local.json` out of git.

## Hooks

Hooks can block or react to tool calls. Use them for lightweight local guardrails, such as blocking direct pushes to `main`.

See [Hooks and Guardrails](hooks.md).

## Subagents

Subagents are specialized Claude Code agents with their own instructions and tool limits.

Project-level subagents live in:

```text
.claude/agents/<agent-name>.md
```

The starter includes an example review subagent. Use subagents when a repeated task has a focused role, such as reviewing diffs, researching docs, or checking test coverage.

## Skills

Project-level skills live in:

```text
.claude/skills/<skill-name>/SKILL.md
```

Use skills for reusable workflows. Use subagents for reusable roles.

## Useful commands

```text
/memory
/mcp
/model
/config
```

Use `/memory` when Claude does not seem to be reading the expected `CLAUDE.md`.
