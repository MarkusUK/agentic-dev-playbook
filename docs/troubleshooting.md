# Troubleshooting

Use this when the setup looks right but the agent, docs site, or MCP tools are not behaving as expected.

## MkDocs command not found

Install the docs dependencies:

```bash
python -m pip install -r requirements.txt
```

Then run:

```bash
mkdocs serve
mkdocs build --strict
```

## GitHub Pages does not publish

Check:

- GitHub Pages source is set to GitHub Actions.
- The workflow in `.github/workflows/deploy-docs.yml` ran on `main`.
- The build step passed `mkdocs build --strict`.
- `mkdocs.yml` has the correct `repo_url`.

## Agent ignores a skill

Check:

- The skill exists at `.agents/skills/<skill-name>/SKILL.md` for Codex.
- The skill exists at `.claude/skills/<skill-name>/SKILL.md` for Claude Code.
- The skill has a clear `name` and `description` in frontmatter.
- Your prompt names the skill or describes a task that clearly matches it.

Prompt example:

```text
Use the write-tests skill if it is relevant. Inspect nearby tests first, then add the smallest useful coverage.
```

## MCP server does not appear

Check:

- The MCP config is in the right scope for the tool.
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
2. Confirm the server name matches your prompt. If the server is named `figma-desktop`, prompting for `figma` may be ambiguous.
3. Restart the agent session after changing MCP config.
4. Re-run the provider's current install command from official docs.
5. If the server uses environment variables, print only variable names, not values, and confirm they exist.
6. Ask the agent to list available MCP tools before asking it to use one.

Prompt example:

```text
Check which MCP tools are available in this session. Do not edit files.
If Figma is unavailable, explain what config or authentication step appears to be missing.
```

## MCP output looks wrong

Treat MCP output as untrusted context. Ask the agent to cross-check against the repo, official docs, tests, or source files before editing.

## The starter feels too broad

Delete irrelevant sections. The starter is meant to be adapted per project, not preserved as a museum piece.

Good deletions include:

- Android testing guidance in a web-only project.
- Design MCP sections in a backend-only project.
- Skills you do not use.
- Release instructions that do not match the repo.

## Unsure whether an MCP belongs global or project-level

Use project-level by default.

Global MCPs should be safe, low-risk, and useful everywhere. Anything that can access sensitive project data, write to external systems, or only helps one repo should be project-level.
