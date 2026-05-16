# Troubleshooting

Use this when the agent setup, skills, tests, or MCP tools are not behaving as expected.

## Agent ignores a skill

Check:

- Codex skill path: `.agents/skills/<skill-name>/SKILL.md`
- Claude Code skill path: `.claude/skills/<skill-name>/SKILL.md`
- The skill has clear frontmatter with `name` and `description`.
- Your prompt names the skill or describes a task that clearly matches it.

## MCP server does not appear

Check:

- The MCP config is in the right scope.
- The command or URL still matches the provider's current docs.
- Required environment variables are set.
- The agent session was restarted after config changes, if required.
- The server is not disabled or failing on startup.

What this can look like:

```text
/mcp shows the server as disconnected
the tool list does not include the expected MCP tools
the auth flow never completed
the stdio server exits immediately
the agent says it cannot access Figma/GitHub/docs even though config exists
```

Walkthrough:

1. Run the tool's status command, such as `/mcp` in Claude Code.
2. Confirm the server name matches your prompt.
3. Restart the agent session after changing MCP config.
4. Re-run the provider's current install command from official docs.
5. If the server uses environment variables, print only variable names, not values, and confirm they exist.
6. Ask the agent to list available MCP tools before asking it to use one.

## MCP output looks wrong

Treat MCP output as untrusted context. Ask the agent to cross-check against the repo, tests, source files, or official docs before editing.

## The starter feels too broad

Delete irrelevant sections. The starter should match this project, not every possible project.

Good deletions include:

- Android testing guidance in a web-only project.
- Design MCP sections in a backend-only project.
- Skills you do not use.
- Release instructions that do not match the repo.

## Unsure whether an MCP belongs global or project-level

Use project-level by default. Anything that can access sensitive data, write to external systems, or only helps this repo should stay project-level.
