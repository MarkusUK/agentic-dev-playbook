# MCP Setup Verification Status

Last verified against the linked provider docs: 2026-05-16.

MCP and agent-tooling commands change quickly. Treat this page as a freshness marker, not a permanent guarantee.

## Verified references

Use these as the current source of truth when updating setup commands:

- Codex MCP config: <https://developers.openai.com/codex/mcp>
- Codex skills: <https://developers.openai.com/codex/skills>
- Codex AGENTS.md: <https://developers.openai.com/codex/guides/agents-md>
- Codex config reference: <https://developers.openai.com/codex/config-reference>
- Codex sandboxing: <https://developers.openai.com/codex/concepts/sandboxing>
- Codex models: <https://developers.openai.com/codex/models>
- Claude Code MCP: <https://docs.claude.com/en/docs/claude-code/mcp>
- Claude Code skills: <https://docs.claude.com/en/docs/claude-code/skills>
- Claude Code settings: <https://code.claude.com/docs/en/settings>
- Claude Code hooks: <https://code.claude.com/docs/en/hooks>
- Claude Code memory / CLAUDE.md: <https://code.claude.com/docs/en/memory>
- Claude Code subagents: <https://code.claude.com/docs/en/sub-agents>
- Claude Code model configuration: <https://code.claude.com/docs/en/model-config>
- Figma MCP for Claude Code: <https://help.figma.com/hc/en-us/articles/39888612464151-Claude-Code-and-Figma-Set-up-the-MCP-server>
- Google Stitch MCP setup: <https://stitch.withgoogle.com/docs/mcp/setup>
- 21st.dev Magic MCP: <https://github.com/21st-dev/magic-mcp>
- Rive docs: <https://rive.app/docs>

## Volatile commands

Re-check provider docs before copying commands for:

- Google Stitch
- 21st.dev / Magic MCP
- Rive-related MCP workflows
- provider-hosted MCPs with OAuth
- stdio MCPs installed through `npx`, `uvx`, Docker, or similar runtimes

## Stable local conventions in this repo

Use these unless the tool vendor changes its documented behaviour:

```text
.agents/skills/<skill-name>/SKILL.md      # Codex repo-scoped skills
~/.agents/skills/<skill-name>/SKILL.md    # Codex user-level skills
.claude/skills/<skill-name>/SKILL.md      # Claude Code repo-scoped skills
.claude/agents/<agent-name>.md            # Claude Code project subagents
.claude/settings.json                     # Claude Code shared project settings/hooks
.codex/config.toml                        # Codex config and MCP servers
.mcp.json                                 # Claude shared project MCP config, when appropriate
```

## Update checklist

When refreshing this page:

1. Open the official provider docs.
2. Update any commands or links that changed.
3. Update the `Last verified` date.
4. Run `mkdocs build --strict`.
5. Mirror important changes into `templates/project-starter-lean/` and `templates/project-starter/` if new projects should inherit them.
