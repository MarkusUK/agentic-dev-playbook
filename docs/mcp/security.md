# MCP and Skills Security

MCP servers and skills can make agents much more useful, but they also expand what the agent can read, infer, or do. Add them deliberately.

## Core rule

```text
Least privilege first.
Project-level before global.
Read-only before write-capable.
Explicit prompt before automatic use.
```

## What never belongs in the repo

Do not commit:

- `.env` files
- API keys
- OAuth tokens
- signing keys
- keystores
- production credentials
- personal local settings
- private customer data

Use environment variable references for credentials, and document the variable names without documenting the secret values.

## Review MCPs before trusting them

Before adding an MCP server, check:

- Who maintains it.
- What data it can read.
- Whether it can write or mutate external systems.
- Whether it runs local commands.
- Whether it shells out through `npx`, `uvx`, Docker, or another runtime.
- Whether it requires broad OAuth scopes.
- Whether it is pinned to a known package/version where practical.

Treat public registries and random examples as starting points, not proof of safety.

## Prefer project scope

Use global MCP config only for tools you trust and use everywhere.

Use project-level config for:

- Figma or design tools tied to one product.
- Sentry, Firebase, Linear, Jira, or database access.
- Internal APIs.
- Anything with write access.
- Anything with sensitive data access.

## Skills are instructions, not magic

Skills should be readable, small, and easy to audit. They should say:

- when to use the skill
- what files or context to inspect
- what commands are safe to run
- what output the agent should return
- what the agent must not do

Do not hide sensitive commands or credentials inside skills.

## Prompt MCP use explicitly

Do not assume an agent will use the right external tool automatically. Say which tool is allowed and why.

Example:

```text
Use the Figma MCP only to inspect the linked frame. Do not overwrite design-system files. Adapt the result to the existing components.
```

## Review before committing shared config

Before committing `.mcp.json`, `.codex/config.toml`, `.agents/skills/`, or `.claude/skills/`, check:

- No secrets are present.
- Commands are understandable.
- Package names are correct.
- The access level is appropriate.
- The README or docs explain how to disable or remove the tool.

## If in doubt

Keep the MCP local, disabled, or out of the repo until you understand the risk. A missing MCP is usually easier to fix than an over-broad one.
