# 06 - Interactive Mockups

Interactive mockups are useful during design, especially for app flows.

They help you test:

```text
- navigation
- screen hierarchy
- layout feel
- onboarding
- dashboard interactions
- form flows
- empty/loading/error states
- basic motion ideas
```

But treat them as design prototypes, not production code.

## When to use React/Tailwind mockups

Use React/Tailwind mockups when:

```text
- you want quick clickable screens
- you want to compare design directions
- you want to test a user flow
- you want a visual reference before native implementation
- you are still deciding layout and brand
```

Avoid treating the mockup as final production code if your app is actually Android, iOS, Flutter, React Native, etc.

## Desktop tools are useful here

Use desktop/IDE tools when you want:

```text
- built-in preview windows
- visual inspection
- side-by-side agent sessions
- diffs
- rapid UI iteration
```

CLI is still useful for:

```text
- running the app
- tests
- lint
- git
- Android emulator/AVD
```

## Copy/paste prompt: create interactive mockup

```text
Create an interactive prototype/mockup for the selected design direction.

Purpose:
- explore layout, navigation, and interaction
- not production code

Use:
- React
- Tailwind
- simple local state
- no backend
- no unnecessary dependencies
- accessible HTML where possible

Screens to include:
1. Onboarding
2. Home/dashboard
3. Detail screen
4. Create/edit flow
5. Settings/profile

Interactions:
- clickable navigation between screens
- sample data
- empty state
- simple form interaction
- light/dark mode toggle if useful
- basic animation only if it helps explain the concept

Design direction:
[Paste selected design direction / brand kit]

Important:
- Keep it in a single file if possible.
- Make it easy to preview.
- Make it visually polished but not over-engineered.
- Clearly label this as a prototype, not production implementation.
```

## Copy/paste prompt: compare mockup variants

```text
Create 3 interactive mockup variants for this app concept:

[Paste app idea and brand direction]

Variant A:
Minimal, calm, accessible.

Variant B:
Premium/editorial, more distinctive.

Variant C:
Dark-mode-first, atmospheric.

For each:
- use the same core screens
- use the same sample data
- vary layout, colour, density, and interaction style
- keep implementation simple
- make it easy to compare

After generating, explain:
- strongest variant
- risks of each
- which is easiest to implement
- which best fits the target audience
```

## Copy/paste prompt: convert mockup into production plan

```text
This interactive mockup is the selected design reference:

[Paste mockup summary or file path]

Now inspect the actual codebase.

Do not edit yet.

Create an implementation plan to translate this prototype into the real app stack:

Actual stack:
[Android Jetpack Compose / SwiftUI / Flutter / React Native / web / etc.]

Include:

1. Which parts of the mockup are design-only
2. Which parts map to real app components
3. Theme/token changes needed
4. Reusable components to create
5. Screens to implement first
6. Tests/build commands
7. Accessibility checks
8. Risks
9. Minimal Phase 1 implementation plan

Do not commit, push, deploy, or merge.
```
