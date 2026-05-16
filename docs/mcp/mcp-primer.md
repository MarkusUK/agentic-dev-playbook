# MCP and Skills Primer

This page is the plain-English version.

## MCP

MCP means Model Context Protocol.

An MCP server is a local or remote process that exposes tools or data to an agent. The agent can call those tools during a session.

Examples:

```text
Figma MCP        -> read design frames, components, variables, and layout context
GitHub MCP       -> inspect issues, pull requests, checks, and repository metadata
Docs MCP         -> search current documentation
Sentry MCP       -> inspect production errors
Database MCP     -> inspect a read-only staging database
```

MCP answers:

```text
What can the agent access?
```

## Skills

A skill is a small folder containing a `SKILL.md` file. It teaches the agent a reusable workflow.

Examples:

```text
review-pr        -> how to review a diff
write-tests      -> how to add tests safely
design-to-code   -> how to turn design context into production code
ui-assets        -> how to adapt external UI/component output
```

Skills answer:

```text
How should the agent work?
```

## Hooks

A hook is a rule that runs at a specific point in an agent session. Hooks can add context, run checks, or block dangerous actions.

Examples:

```text
Block direct pushes to main
Block broad destructive shell commands
Run lint after edits
Warn when generated files are edited
```

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

Prompts answer:

```text
What should it use right now?
```

## The useful mental model

```text
MCP = access
Skills = workflow
Hooks = guardrails
Prompt = current task
AGENTS.md / CLAUDE.md = standing project rules
```

## Safe default

Start with project-level, read-only MCPs. Add write-capable tools only after you understand what they can change.
