# Project-Level MCPs, Skills, and Prompting Guide

This guide explains how to add MCPs and skills per project, and how to prompt Codex or Claude Code so they use external tools deliberately.

Before copying provider-specific MCP commands, check [MCP Setup Verification Status](verification-status.md).

## Mental model

```text
MCPs = what the agent can access
Skills = how the agent should work
Prompts = what the agent should use right now
Hooks = what the agent is blocked from doing
```

Examples:

```text
Figma MCP       -> lets the agent inspect Figma designs
Stitch MCP      -> lets the agent inspect Google Stitch context
21st.dev/Magic  -> lets the agent discover/generate UI component ideas
Rive context    -> helps the agent implement Rive animations
design-to-code skill -> tells the agent how to turn design context into safe code
review-pr skill -> tells the agent how to review a diff
```

## Global vs project-level setup

Keep global config minimal.

Global MCPs should be things you trust and use everywhere:

```text
- docs/search
- GitHub read/review tools
- safe local utilities
```

Project-level MCPs should be things only needed by that repo:

```text
- Figma
- Google Stitch
- 21st.dev / Magic
- Rive
- Sentry
- database
- Firebase
- Supabase
- Linear/Jira
- deployment tools
```

Rule:

```text
If an MCP is only relevant to one repo, do not put it in global config.
If an MCP can access sensitive data, do not put it in global config.
If an MCP can write/change things, definitely do not put it in global config.
```

## Codex project-level MCPs

Inside your repo, create:

```text
your-project/
  .codex/
    config.toml
```

Example:

```toml
# your-project/.codex/config.toml

[mcp_servers.figma]
url = "https://mcp.figma.com/mcp"
enabled = true
required = false

[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]
enabled = true
required = false

# Example placeholder for Google Stitch.
# Replace with current official Stitch MCP details.
# [mcp_servers.stitch]
# url = "<STITCH_MCP_URL>"
# enabled = true
# required = false

# Example placeholder for 21st.dev / Magic.
# Replace package name with current official docs.
# [mcp_servers.magic]
# command = "npx"
# args = ["-y", "<PACKAGE_NAME_FROM_21ST_DOCS>"]
# enabled = true
# required = false
```

Then run Codex from the repo:

```bash
cd your-project
codex
```

## Claude Code project-level MCPs

From inside the repo:

```bash
cd your-project
claude mcp add --transport http figma https://mcp.figma.com/mcp
claude mcp list
```

Inside Claude Code, inspect MCP state with:

```text
/mcp
```

For stdio MCPs:

```bash
claude mcp add --transport stdio context7 -- npx -y @upstash/context7-mcp
```

General stdio pattern:

```bash
claude mcp add --transport stdio <name> -- <command> <arg1> <arg2>
```

For Figma, an official plugin may be easier:

```bash
claude plugin install figma@claude-plugins-official
```

This slug is listed in Figma's current Claude Code MCP setup docs as of the verification date in [MCP Setup Verification Status](verification-status.md).

For Stitch, 21st.dev/Magic, Rive, Firebase, Sentry, or database MCPs, copy the exact current install command from the provider docs.

## Project-level skills

For Claude Code:

```text
your-project/
  .claude/
    skills/
      review-pr/
        SKILL.md
      write-tests/
        SKILL.md
      debug-issue/
        SKILL.md
      android-testing/
        SKILL.md
      design-to-code/
        SKILL.md
      ui-assets/
        SKILL.md
```

For Codex or cross-agent reference:

```text
your-project/
  .agents/
    skills/
      review-pr/
        SKILL.md
      write-tests/
        SKILL.md
      debug-issue/
        SKILL.md
      android-testing/
        SKILL.md
      design-to-code/
        SKILL.md
      ui-assets/
        SKILL.md
```

Use `.codex/config.toml` for Codex configuration and MCP servers. Use `.agents/skills/` for repo-scoped Codex skills.

Even if a tool does not auto-load every skill in exactly the same way, these files are still useful because `AGENTS.md` and `CLAUDE.md` can point the agent to them.

## Tell the agent which skills exist

In `AGENTS.md`, include:

```md
# Agent Instructions

Use these project skills where relevant:

- `.agents/skills/review-pr/SKILL.md`
- `.agents/skills/write-tests/SKILL.md`
- `.agents/skills/debug-issue/SKILL.md`
- `.agents/skills/android-testing/SKILL.md`
- `.agents/skills/design-to-code/SKILL.md`
- `.agents/skills/ui-assets/SKILL.md`

For UI/design work, use design MCP tools only when relevant and adapt output to the existing design system.
```

In `CLAUDE.md`, include:

```md
# Claude Code Instructions

Use these skills where relevant:

- `review-pr`
- `write-tests`
- `design-to-code`
- `ui-assets`

For design work, prefer the `design-to-code` skill.

Do not use MCP tools unnecessarily. Use them only when they provide relevant project context.
```

## Do you need to prompt the agent to use MCP tools?

Usually, yes.

Do not assume the agent will automatically use Figma, Stitch, Rive, 21st.dev/Magic, or other MCPs.

Be explicit:

```text
Use [specific MCP/tool] only if relevant.

First inspect and plan.
Do not edit yet.

Tell me:
- what context you found
- what files likely need changing
- risks
- tests to run
- minimal implementation plan
```

Then approve implementation:

```text
Proceed.

Use the relevant project skill.
Keep the diff small.
Run tests.
Do not commit, push, deploy, or merge.
```

## Figma prompt

```text
Use the Figma MCP to inspect this design:

[FIGMA URL]

Before editing:
- identify the target screen/component
- map design tokens to existing theme values
- find existing components to reuse
- list assets needed
- give me a short implementation plan

Do not edit yet.
```

Then:

```text
Proceed with the implementation.

Use the design-to-code skill.
Keep the diff small.
Do not add dependencies without asking.
Run relevant tests/build.
Do not commit.
```

## 21st.dev / Magic prompt

```text
Use the UI assets/component MCP only for inspiration.

I want a better version of this component:
[component/file/path]

Rules:
- adapt to our existing design system
- do not introduce a new component library
- do not add dependencies without asking
- keep the diff small
- preserve accessibility
```

## Rive prompt

```text
Use the Rive-related context/docs if available.

Implement this Rive animation in the existing app:
[asset/path or design reference]

Before editing:
- inspect the current animation/runtime setup
- identify where .riv assets should live
- identify state machine inputs
- explain any dependency changes needed

Do not edit yet.
```

## Stitch prompt

```text
Use the Stitch MCP only for design context.

Inspect this Stitch design/context:
[STITCH URL OR CONTEXT]

Before editing:
- identify the target screen/component
- map layout and styling to existing app conventions
- identify existing components to reuse
- list any missing assets
- propose a minimal implementation plan

Do not edit yet.
```

## Review prompt

```text
Use the review-pr skill.

Review the current uncommitted git diff.

Focus on:
- correctness
- edge cases
- security
- tests
- regressions
- unnecessary complexity

Do not edit files.
Categorise findings as must-fix, should-fix, and optional.
```

## Testing prompt

```text
Use the write-tests skill.

Inspect the changed files and nearby tests.

Add or update tests for the changed behaviour.
Follow the existing test style.
Run the smallest relevant test command first.
Do not remove or weaken tests.
Do not commit.
```

## Android terminal testing prompt

```text
Use the android-testing skill.

I want to run this Android project from the terminal, not VS Code.

Inspect the Gradle modules and tell me:
- unit test command
- lint command
- debug build command
- connected/emulator test command
- any required AVD/emulator setup

Do not edit yet.
```

## Best working habit

For external tools:

```text
1. Name the MCP/tool explicitly.
2. Ask the agent to inspect first.
3. Ask for a plan before edits.
4. Tell it which skill to use.
5. Keep changes small.
6. Run tests.
7. Have the other agent review the diff.
8. You commit and push.
```

## Simple rule

```text
MCP answers: “What can the agent access?”
Skills answer: “How should the agent work?”
Prompt answers: “What should it use right now?”
```
