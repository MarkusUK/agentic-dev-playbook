# Hooks and Guardrails

Hooks are useful when a rule should be enforced automatically instead of merely suggested in `AGENTS.md` or `CLAUDE.md`.

## What hooks are good for

Use hooks to:

- block dangerous shell commands
- block direct pushes to protected branches
- warn when generated files are edited
- run lightweight checks after edits
- add dynamic context to a session

Do not use hooks as a replacement for CI. Hooks are local guardrails; CI is the final shared enforcement layer.

## Claude Code example

The starter includes a minimal project-level example:

```text
templates/project-starter/.claude/settings.json
templates/project-starter/.claude/hooks/block-dangerous-commands.py
```

The example blocks risky `Bash` tool calls before they run. It is intentionally conservative and easy to edit.

## Example hook settings

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/block-dangerous-commands.py"
          }
        ]
      }
    ]
  }
}
```

## Example blocked commands

```text
rm -rf /
git push origin main
git push --force
terraform apply
kubectl delete
```

Tune the list per project. A frontend toy project and a production backend should not have identical guardrails.

## Keep hooks boring

Good hooks are:

- short
- deterministic
- local
- easy to explain
- easy to disable while debugging

Avoid hooks that call remote services unless you really need them.
