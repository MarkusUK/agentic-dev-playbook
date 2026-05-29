---
name: review-pr
description: Review a git diff or PR for correctness, tests, security, regressions, and maintainability.
---

# Review PR Skill

When invoked:

1. Inspect the current diff and relevant nearby files.
2. Understand the intended behaviour.
3. Look for correctness issues first.
4. Check edge cases and failure modes.
5. Check test coverage.
6. Check security and data-loss risks.
7. Avoid style nitpicks unless they affect clarity or maintainability.
8. Do not edit files unless explicitly asked.

Return:

```text
Must fix:
Should fix:
Optional:
Tests to run:
```
