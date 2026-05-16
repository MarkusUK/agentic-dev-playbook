# Project-level MCP note

Run project-specific `claude mcp add ...` commands from inside the repo that needs the tool. Keep global/default MCP access minimal.

# Claude Code MCP Commands

Run these from terminal.

## Figma

Preferred:

```bash
claude plugin install figma@claude-plugins-official
```

Manual:

```bash
claude mcp add --transport http figma https://mcp.figma.com/mcp
claude mcp list
```

Inside Claude Code:

```text
/mcp
```

## Google Stitch

Check current Google Stitch MCP docs, then use the official endpoint/package.

HTTP pattern:

```bash
claude mcp add --transport http stitch <STITCH_MCP_URL>
```

Stdio pattern:

```bash
claude mcp add --transport stdio stitch -- npx -y <STITCH_MCP_PACKAGE>
```

## 21st.dev / Magic MCP

Check 21st.dev docs for the current package name.

Typical pattern:

```bash
claude mcp add --transport stdio magic -- npx -y <PACKAGE_NAME_FROM_21ST_DOCS>
```

## Manage MCPs

```bash
claude mcp list
claude mcp get figma
claude mcp remove figma
```
