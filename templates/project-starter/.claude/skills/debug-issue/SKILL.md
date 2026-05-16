---
name: debug-issue
description: Diagnose a bug or failing test before proposing a minimal fix.
---

# Debug Issue Skill

When invoked:

1. Reproduce or understand the failure.
2. Inspect logs, stack traces, failing tests, and recent diffs.
3. Identify the smallest likely cause.
4. Propose a minimal fix.
5. Add or update a regression test.
6. Run the relevant test.

Do not guess silently. If reproduction is impossible, state what is missing and what command should be run.

End with:

```text
Root cause:
- ...

Fix:
- ...

Tests:
- ...

Follow-ups:
- ...
```
