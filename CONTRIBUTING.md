# Contributing

Thanks for improving this playbook.

## What belongs here

- Safer Codex and Claude Code workflows.
- Clear MCP and skills setup guidance.
- Starter-template improvements for new projects.
- Design-to-code and interactive mockup workflows.
- Corrections to volatile setup commands.

## Before changing docs

Check whether the change should be mirrored in:

```text
docs/
templates/project-starter/
README.md
GITHUB_SETUP.md
```

The public docs explain the playbook. The starter template is what new projects inherit.

## Style

- Prefer practical checklists and copy/paste examples.
- Keep security guidance conservative.
- Label volatile provider commands with a verification date.
- Avoid committing secrets, local config, or generated docs output.
- Keep examples generic unless they are clearly marked as examples.

## Validation

Before opening a pull request, run:

```bash
python -m pip install -r requirements.txt
mkdocs build --strict
```

If you cannot run those commands, explain why in the pull request.
