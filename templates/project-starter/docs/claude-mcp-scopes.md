# Claude Code MCP Scopes

Claude Code MCP servers can be added at different scopes. Pick the narrowest scope that works.

## Local scope — default, private to you for this project

Use this for personal or experimental project tools. It loads only for the current project path but is stored in your user config.

```bash
claude mcp add --transport http figma https://mcp.figma.com/mcp
# equivalent explicit form
claude mcp add --transport http --scope local figma https://mcp.figma.com/mcp
```

## Project scope — shared with the repo/team

Use this only for safe, team-approved MCPs. It writes `.mcp.json` in the project root, so it can be committed.

```bash
claude mcp add --transport http --scope project docs https://example.com/mcp
```

Review `.mcp.json` before committing it. Do not commit secrets. Prefer environment variable references for credentials.

## User scope — available across all projects

Use this only for safe, general tools you trust everywhere.

```bash
claude mcp add --transport http --scope user sentry https://mcp.sentry.dev/mcp
```

## Managing servers

```bash
claude mcp list
claude mcp get <name>
claude mcp remove <name>
```

Inside Claude Code:

```text
/mcp
```

## Rule of thumb

```text
Local = good default for personal/project-specific tools
Project = team-shared config, review before committing
User = safe tools you use everywhere
```
