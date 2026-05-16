# Claude Code Setup Notes

## CLAUDE.md hierarchy

Useful locations:

```text
~/.claude/CLAUDE.md        # personal defaults across projects
./CLAUDE.md                # project instructions
./.claude/CLAUDE.md        # alternative project instructions location
./CLAUDE.local.md          # private local project notes, gitignored
```

If this repo also has `AGENTS.md`, use `CLAUDE.md` to import it:

```markdown
@AGENTS.md

## Claude Code

Prefer review-first workflows. Do not edit during review unless explicitly asked.
```

## Settings

Shared project settings:

```text
.claude/settings.json
```

Private local overrides:

```text
.claude/settings.local.json
```

Keep `settings.local.json` out of git.

## Subagents

Project-level subagents live in:

```text
.claude/agents/<agent-name>.md
```

Use subagents for reusable roles. Use skills for reusable workflows.

## Useful commands

```text
/memory
/mcp
/model
/config
```
