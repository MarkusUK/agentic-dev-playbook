---
name: design-to-code
description: Convert screen specs, Figma, screenshots, mockups, or brand-kit guidance into production UI while preserving the existing app architecture and design system.
---

# Design to Code Skill

Use this skill when implementing UI from `design-start/`, Figma, screenshots, mockups, or generated design references.

## Before Editing

1. Read `design-start/brand-kit.md`, `design-start/screen-spec.md`, and `design-start/implementation-handoff.md` if present.
2. Inspect existing app architecture and UI components.
3. Identify design tokens, themes, typography, icons, and reusable components.
4. Ask only blocking questions.

## Rules

- Do not blindly paste generated UI.
- Reuse existing components and design tokens where possible.
- Do not overwrite design-system files unless explicitly requested.
- Make responsive behaviour explicit.
- Include loading, empty, error, and success states when relevant.
- Use accessible labels, contrast, and focus states.
- Keep the diff small.

## Done Means

```text
Design source:
Implementation summary:
Files changed:
Commands run:
Follow-ups:
```
