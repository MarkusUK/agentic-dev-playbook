# Testing and Checks

Replace placeholders with real project commands.

## Commands

```text
Install dependencies: command discovery needed
Run app locally: command discovery needed
Tests: command discovery needed
Focused test: command discovery needed
Lint: command discovery needed
Typecheck: command discovery needed
Build: command discovery needed
```

## Rule for Agents

- Run the smallest relevant check first.
- Run broader checks before finishing if the change is user-facing or cross-cutting.
- Do not weaken or delete tests just to make the suite pass.
- If a check cannot run, explain why and what should be run next.

## What Requires Tests

- New behaviour
- Bug fixes
- API or data model changes
- Authentication, billing, permissions, or data-loss risks
- Complex UI state changes

## Manual UI Checks

For screen/design work, verify:

- desktop and mobile layout
- loading, empty, error, and success states
- keyboard/focus behaviour where relevant
- contrast and readable text
- no overlapping text or controls
