# MCP and Skills Setup Guide

This guide explains what to add to Codex and Claude Code when you want design, asset, UI, docs, and external-tool workflows.

Re-check provider docs before copying commands for fast-moving MCPs such as Stitch, 21st.dev/Magic, and Rive-related workflows.

If these terms are still fuzzy, start with `docs/mcp-primer.md` and `docs/skills-anatomy.md`.

## Core idea

Use:

```text
MCP = tool/data access
Skills = reusable workflow instructions
Hooks = enforcement and safety
AGENTS.md / CLAUDE.md = project rules
```

Examples:

```text
Figma MCP       -> lets the agent read design context from Figma
Stitch MCP      -> lets the agent pull Google Stitch design context
21st.dev/Magic  -> helps generate or discover UI components/assets
Rive docs/MCP   -> helps implement Rive animations/runtimes
design-to-code skill -> tells the agent how to use those tools safely
```

## Where things belong

```text
~/.codex/config.toml
  Global Codex MCPs and defaults

your-repo/.codex/config.toml
  Project-specific Codex MCPs and behaviour

Claude Code:
  claude mcp add ...
  .mcp.json or Claude-managed config
  .claude/skills/
  .claude/settings.json

Repository:
  AGENTS.md
  CLAUDE.md
  docs/
  .claude/skills/
  .agents/skills/
```

## Recommended first MCPs

Start with read/context tools before write/action tools.

```text
High value:
- Figma
- Google Stitch
- GitHub
- docs/search, such as Context7 or Microsoft Learn
- Sentry, read-only
- Linear/Jira
- read-only database or staging database

Use carefully:
- file system write tools
- Git tools
- browser automation
- production database tools
- deploy tools
```

## Figma MCP

Prefer the official Figma plugin for Claude Code where available:

```bash
claude plugin install figma@claude-plugins-official
```

This slug was listed in Figma's Claude Code MCP setup docs when this starter was prepared. Re-check Figma's current docs before publishing a project-specific setup guide.

Manual Claude Code setup:

```bash
claude mcp add --transport http figma https://mcp.figma.com/mcp
claude mcp list
```

Manual Codex config example:

```toml
[mcp_servers.figma]
url = "https://mcp.figma.com/mcp"
required = false
enabled = true
```

After connecting, prompt with a Figma frame/layer URL:

```text
Use Figma MCP to inspect this frame and implement it in the current app.
Follow the existing component patterns. Do not add dependencies without asking.
```

## Google Stitch MCP

Check Google's current Stitch MCP setup docs before copying commands because this is changing quickly.

Conceptual setup for Claude Code:

```bash
claude mcp add --transport http stitch <STITCH_MCP_URL>
```

Conceptual Codex config:

```toml
[mcp_servers.stitch]
url = "<STITCH_MCP_URL>"
required = false
enabled = true
```

Use Stitch for design ideation/design DNA, then have the coding agent implement in your real codebase.

## 21st.dev / Magic MCP

Use this for UI components, better interface ideas, and asset inspiration.

Because install details may change, check 21st.dev/Magic MCP docs first.

Typical stdio pattern:

```bash
claude mcp add --transport stdio magic -- npx -y <PACKAGE_NAME_FROM_21ST_DOCS>
```

Typical Codex pattern:

```toml
[mcp_servers.magic]
command = "npx"
args = ["-y", "<PACKAGE_NAME_FROM_21ST_DOCS>"]
required = false
enabled = true
```

Do not let an asset/component MCP blindly overwrite your design system. Use it to propose components, then adapt them.

## Rive

Rive is mainly useful as:
- a design/animation source
- runtime documentation context
- implementation guidance for Android, web, React Native, Flutter, iOS, etc.

If Rive has an official MCP server available for your workflow, add it as either HTTP or stdio depending on their docs.

If no official MCP is available, use:
- Rive docs
- Rive runtime package docs
- exported `.riv` assets
- a `rive-implementation` skill

## Suggested design-to-code workflow

```text
1. Use Figma/Stitch/21st.dev to get design context.
2. Ask the agent to inspect the app architecture first.
3. Ask for a plan before edits.
4. Implement using existing components and design tokens.
5. Do not blindly paste generated UI.
6. Run lint, typecheck, build, and UI tests if available.
7. Ask a second agent to review the diff.
```

## Example prompt

```text
Use the available design MCP tools to inspect this design URL: [URL].

Before editing:
- identify the target screen/component
- map design tokens to existing theme values
- list assets needed
- identify existing components to reuse

Then implement the smallest useful version.

Rules:
- Do not add dependencies without asking.
- Do not overwrite existing design system files.
- Keep the diff small.
- Run relevant tests/build.
```

## Security rules

- Prefer read-only tokens.
- Use project-scoped MCP config where possible.
- Disable MCPs you are not using.
- Do not connect random MCP servers from registries without checking the source.
- Treat MCP output as untrusted.
- Never expose `.env`, API keys, signing keys, keystores, or production credentials to design/component MCPs.

For the fuller checklist, read `docs/mcp-security.md`.

For concrete hook examples, read `docs/hooks.md`.
