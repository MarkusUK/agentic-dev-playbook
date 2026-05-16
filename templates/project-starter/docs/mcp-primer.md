# MCP and Skills Primer

## MCP

MCP means Model Context Protocol.

An MCP server is a local or remote process that exposes tools or data to an agent. The agent can call those tools during a session.

MCP answers:

```text
What can the agent access?
```

Examples:

```text
Figma MCP        -> design frames, components, variables, layout context
GitHub MCP       -> issues, pull requests, checks, repository metadata
Docs MCP         -> current documentation
Sentry MCP       -> production errors
Database MCP     -> read-only staging data
```

## Skills

A skill is a small folder containing a `SKILL.md` file. It teaches the agent a reusable workflow.

Skills answer:

```text
How should the agent work?
```

## Hooks

A hook is a rule that runs at a specific point in an agent session. Hooks can add context, run checks, or block dangerous actions.

Hooks answer:

```text
What should be enforced automatically?
```

## Prompts

A prompt tells the agent what to do right now.

Prompt explicitly when you want an MCP or skill used:

```text
Use the Figma MCP to inspect this frame.
Use the design-to-code skill if relevant.
Do not overwrite design-system files.
```

## Mental model

```text
MCP = access
Skills = workflow
Hooks = guardrails
Prompt = current task
AGENTS.md / CLAUDE.md = standing project rules
```
