# Hooks and Guardrails

Hooks are useful when a rule should be enforced automatically instead of merely suggested in `AGENTS.md` or `CLAUDE.md`.

## Starter example

This template includes:

```text
.claude/settings.json
.claude/hooks/block-dangerous-commands.py
```

The example blocks risky `Bash` tool calls before they run. Edit it to match this project.

## Good uses

- Block direct pushes to protected branches.
- Block broad destructive shell commands.
- Warn when generated files are edited.
- Run lightweight checks after edits.

## Keep hooks boring

Good hooks are short, deterministic, local, easy to explain, and easy to disable while debugging.

Do not rely on hooks as your only protection. CI should still enforce shared checks.
