# 08 - Implementation Handoff

Use this after you have chosen a design direction, screen specs, and possibly a mockup.

## Copy/paste prompt for Codex

```text
We have selected this design direction and brand kit:

[Paste final brand kit and screen spec]

Now inspect the codebase.

Do not edit yet.

Tell me:

1. Existing architecture and UI framework
2. Where theme/design tokens should live
3. Where reusable components should live
4. Which files are likely to change
5. Which screens should be built first
6. What tests/build commands should be run
7. Accessibility risks
8. Implementation risks
9. Minimal Phase 1 implementation plan

Use the design-to-code skill.
Do not commit, push, deploy, or merge.
```

Then:

```text
Proceed with Phase 1 only:

- create/update the design tokens/theme
- create base reusable components
- implement the first screen only
- keep the diff small
- run relevant tests/build
- do not commit
```

## Copy/paste prompt for Claude review

```text
Use the review-pr skill.

Review the current uncommitted git diff.

This work implements the selected design direction:

[Paste short design summary]

Focus on:
- correctness
- consistency with the brand kit
- accessibility
- UI state coverage
- unnecessary dependencies
- maintainability
- tests/build risks

Do not edit files.
Categorise findings as must-fix, should-fix, and optional.
```
