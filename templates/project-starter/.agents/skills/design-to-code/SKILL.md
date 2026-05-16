---
name: design-to-code
description: Convert Figma, Stitch, or other design context into production code while preserving the existing app architecture and design system.
---

# Design to Code Skill

Use this skill when implementing UI from Figma, Google Stitch, screenshots, 21st.dev/Magic components, or other design sources.

## Before editing

1. Inspect the current app architecture.
2. Identify the target screen/component.
3. Find existing components to reuse.
4. Map colours, spacing, typography, icons, and assets to the existing design system.
5. Identify whether design MCP tools are available.
6. Ask only blocking questions.

## Rules

- Do not blindly paste generated UI.
- Do not overwrite design-system files unless explicitly requested.
- Do not add dependencies without explaining why.
- Prefer existing tokens and components.
- Keep the diff small.
- Use accessible labels, contrast, and focus states.
- Make responsive behaviour explicit.
- For Android, prefer existing Compose/XML patterns already used in the repo.
- For web, prefer existing component library and styling system.

## Done means

- UI implemented.
- Assets handled correctly.
- Relevant tests/build run.
- Diff reviewed for unnecessary complexity.

End with:

```text
Design source:
- ...

Implementation summary:
- ...

Files changed:
- ...

Commands run:
- ...

Follow-ups:
- ...
```
