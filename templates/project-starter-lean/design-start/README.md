# Design Start Workflow

Use this before writing production UI code.

Goal:

```text
idea -> product brief -> brand kit -> screen spec -> implementation handoff -> code
```

This is intentionally lightweight. The point is to help the agents produce better screen designs before Codex starts coding.

## Recommended Agent Flow

1. Use Codex or Claude Code to clarify the product brief.
2. Ask for 2-3 design directions.
3. Pick or combine one direction.
4. Create a small brand kit.
5. Write first-screen specs with states.
6. Optionally use Figma, screenshots, 21st.dev/Magic, Stitch, Rive, or other MCP/tools for inspiration.
7. Produce an implementation handoff.
8. Ask Codex to implement the smallest approved slice.
9. Ask Claude Code to review the diff.

## Start Prompt

```text
Read AGENTS.md, CLAUDE.md, docs/architecture.md, docs/testing.md, and design-start/README.md.

Do not write production code yet.

Help me turn this app idea into:
- a short product brief
- 2-3 visual/brand directions
- first screen ideas
- key user flows
- risks and open questions

App idea:
[paste idea]
```

## Files in This Folder

```text
product-brief.md
brand-kit.md
screen-spec.md
implementation-handoff.md
```

Fill these in as the design direction becomes clearer.
