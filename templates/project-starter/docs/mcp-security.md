# MCP and Skills Security

Use this checklist before adding or committing MCP servers, agent skills, or shared agent config.

## Core rule

```text
Least privilege first.
Project-level before global.
Read-only before write-capable.
Explicit prompt before automatic use.
```

## Never commit

- `.env` files
- API keys
- OAuth tokens
- signing keys
- keystores
- production credentials
- personal local settings
- private customer data

Use environment variable references for credentials, and document only the variable names.

## Before adding an MCP

Check:

- Who maintains it.
- What data it can read.
- Whether it can write or mutate external systems.
- Whether it runs local commands.
- Whether it shells out through `npx`, `uvx`, Docker, or another runtime.
- Whether it requires broad OAuth scopes.
- Whether project-level scope is enough.

## Before committing shared config

Review:

```text
.mcp.json
.codex/config.toml
.agents/skills/
.claude/skills/
```

Make sure no secrets are present, commands are understandable, and the access level is appropriate for the whole team.

## Prompt MCP use explicitly

Example:

```text
Use the Figma MCP only to inspect the linked frame. Do not overwrite design-system files. Adapt the result to the existing components.
```

## Skills should stay auditable

Skills should be small, readable workflow instructions. Do not hide sensitive commands or credentials inside skills.
