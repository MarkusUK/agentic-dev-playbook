# 04 - Use Design MCPs

Use this when you want the agent to use Figma, Stitch, 21st.dev/Magic, Rive, or other design tools.

## Important rule

Be explicit.

Do not assume the agent will automatically use external tools.

```text
MCP answers: “What can the agent access?”
Skills answer: “How should the agent work?”
Prompt answers: “What should it use right now?”
```

## Figma prompt

```text
Use the Figma MCP to inspect this design:

[FIGMA URL]

Before editing or generating code:
- identify the target screen/component
- map design tokens to existing theme values
- find existing components to reuse
- list assets needed
- identify missing states
- identify accessibility issues
- give me a short implementation/design plan

Do not edit yet.
Do not write production code yet.
```

## Stitch prompt

```text
Use the Stitch MCP only for design context and ideation.

Inspect this Stitch design/context:

[STITCH URL OR CONTEXT]

Before editing or generating code:
- identify the target screen/component
- map layout and styling to existing app conventions
- identify existing components to reuse
- list missing assets
- list accessibility concerns
- propose a minimal implementation/design plan

Do not edit yet.
Do not write production code yet.
```

## 21st.dev / Magic prompt

```text
Use the 21st.dev/Magic MCP only for component inspiration.

I want a better version of this UI/component:

[component, screen, or design description]

Rules:
- adapt ideas to our existing design system
- do not introduce a new component library
- do not add dependencies without asking
- preserve accessibility
- keep components simple and maintainable
- compare options before recommending one

Do not edit production code yet.
```

## Rive prompt

```text
Use Rive-related context/docs if available.

I want motion/animation ideas for:

[screen/component/interaction]

Before implementation:
- propose 3 animation concepts
- identify which should be Rive and which should be native/platform animation
- identify required .riv assets
- identify state machine inputs
- explain performance/accessibility risks
- include reduced-motion fallback guidance

Do not write production code yet.
```

## Compare with/without 21st.dev prompt

```text
Using the selected design direction, compare two approaches:

A. Without 21st.dev/Magic:
- Use only our own design system and standard platform components.

B. With 21st.dev/Magic:
- Use it only for component inspiration and layout ideas.
- Do not introduce a new component library unless clearly justified.

Compare:
- visual quality
- originality
- implementation complexity
- dependency risk
- accessibility risk
- consistency with brand
- long-term maintainability

Then recommend whether 21st.dev/Magic should be used for this project.
```
