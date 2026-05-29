# Lean Agentic Project Starter

Copy this starter into a new app repo when you want the smallest useful setup for:

```text
Codex = implement
Claude Code = review
You = approve
```

It includes only the core agent instructions, essential project docs, a compact design/spec workflow, and the most useful skills for first implementation work.

## Copy into a new repo

Copy the contents of this folder into your app repo root:

```text
templates/project-starter-lean/
```

Then edit the project facts before asking agents to change code.

## Edit first

```text
AGENTS.md
CLAUDE.md
docs/architecture.md
docs/testing.md
docs/release.md
design-start/README.md
design-start/brand-kit.md
design-start/screen-spec.md
design-start/implementation-handoff.md
```

## Keep or delete

Keep:

- `review-pr` if you want repeatable review guidance.
- `write-tests` if you want agents to add tests consistently.
- `design-to-code` if you will build UI from screen specs, mockups, Figma, or screenshots.
- `ui-assets` if you will use generated assets, icons, Rive, Figma, or component inspiration.

Delete anything irrelevant to the project.

## First prompts

Use these prompts to start the agent workflow without having to invent the first message each time.

### 1. Setup reconnaissance

```text
Read AGENTS.md, CLAUDE.md, docs/architecture.md, docs/testing.md, docs/release.md, and design-start/README.md.

Do not edit files yet.

Tell me:
- what project facts are missing
- what commands are available
- what design/spec decisions should be made before coding
- the safest next step
```

### 2. Spec and design

Use before writing production code:

```text
Read ideas.md if it exists, then read AGENTS.md, docs/architecture.md, and design-start/README.md.

Do not write production code yet.

Help me turn this idea into:
- a product brief
- brand direction
- first screen list
- key user flows
- risks and open questions

App idea:
[paste idea]
```

### 3. Implementation planning

Use after the brief, brand, screen spec, and handoff are approved:

```text
Read AGENTS.md, docs/architecture.md, docs/testing.md, and design-start/implementation-handoff.md.

Do not edit yet.

Propose:
- files likely to change
- existing patterns to reuse
- risks
- tests/checks to run
- the smallest safe implementation plan
```

### 4. Claude review

Use after Codex has made changes:

```text
Read CLAUDE.md and review the current diff.

Focus on:
- bugs
- missing tests
- regression risk
- security or data-loss risk
- unnecessary complexity
- whether the change matches the approved spec/design
```

## Recommended next workflow

```text
Customise starter
-> design-start/README.md
-> brand-kit.md
-> screen-spec.md
-> implementation-handoff.md
-> Codex implements
-> Claude Code reviews
```
