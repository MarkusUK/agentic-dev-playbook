# SKILL.md Anatomy

Skills turn repeated instructions into reusable workflows.

## Basic shape

```text
skill-name/
  SKILL.md
  scripts/       # optional
  references/    # optional
  assets/        # optional
```

The `SKILL.md` file starts with frontmatter:

```markdown
---
name: write-tests
description: Add or improve tests for changed behaviour using this repository's existing testing patterns.
---

# Write Tests Skill

1. Inspect changed code and nearby tests.
2. Identify the behaviour being tested.
3. Prefer existing test style.
4. Add the smallest useful coverage.
5. Run the relevant test command.
```

## How a skill is selected

The `description` is the important matching text. Agents use it to decide whether the skill fits the prompt.

Use clear, narrow descriptions:

```text
Review a git diff or PR for correctness, tests, security, regressions, and maintainability.
```

## Codex locations

```text
.agents/skills/<skill-name>/SKILL.md
~/.agents/skills/<skill-name>/SKILL.md
```

Codex can invoke skills explicitly with `$skill-name`, or implicitly when the prompt matches the skill description.

## Claude Code locations

```text
.claude/skills/<skill-name>/SKILL.md
```

Claude Code can invoke skills explicitly with `/skill-name`, or implicitly when the prompt matches the skill description.

## What belongs in a skill

Use a skill for repeatable procedure:

- review checklist
- testing workflow
- debugging workflow
- design-to-code process
- release checklist

Do not hide secrets, credentials, or surprising commands in skills.
