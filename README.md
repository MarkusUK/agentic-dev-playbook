# Agentic Dev Playbook

A GitHub-ready documentation repo and reusable project starter for safer, higher-quality work with Codex, Claude Code, MCPs, skills, hooks, design workflows, and interactive mockups.

## What this repo is for

Use this as:

```text
1. A personal/team playbook
2. A GitHub Pages documentation site
3. A starter template source for new projects
4. A lightweight GitHub Wiki companion
```

## Recommended coding workflow

```text
Codex = implement
Claude Code = review
You = approve
CI = enforce
GitHub PR = final audit trail
```

## Folder structure

```text
docs/                         # MkDocs/GitHub Pages documentation
templates/project-starter/    # Files to copy into new projects
mkdocs.yml                    # MkDocs Material config
.github/workflows/            # GitHub Pages deployment workflow
.github/ISSUE_TEMPLATE/       # Public repo issue templates
```

Repository URL:

```text
https://github.com/MarkusUK/agentic-dev-playbook
```

GitHub Pages URL:

```text
https://markusuk.github.io/agentic-dev-playbook/
```

## Start quickly

Read:

```text
docs/quickstart.md
```

Then copy the starter template into a new project and customise the project-specific files.

## Use the starter in a new project

Copy:

```text
templates/project-starter/
```

into your new repo, then customise:

```text
AGENTS.md
CLAUDE.md
docs/testing.md
docs/architecture.md
docs/release.md
docs/project-level-mcps-and-skills.md
docs/mcp-security.md
```

## Run docs locally

Install MkDocs Material:

```bash
pip install -r requirements.txt
```

Serve locally:

```bash
mkdocs serve
```

Build:

```bash
mkdocs build --strict
```

## Publish to GitHub Pages

1. Create a new GitHub repo.
2. Push this folder.
3. Confirm `repo_url` and `site_url` in `mkdocs.yml`.
4. Review `LICENSE` and change it if MIT is not what you want.
5. In GitHub, go to **Settings -> Pages**.
6. Set source to **GitHub Actions**.
7. The included workflow will publish the MkDocs site.

## Useful docs

- `docs/quickstart.md` - shortest setup path
- `docs/templates.md` - how to use the starter template
- `docs/mcp/mcp-primer.md` - short MCP, skills, hooks, and prompt primer
- `docs/core/codex-setup.md` - Codex config, approvals, sandboxing, and AGENTS.md
- `docs/core/claude-code-setup.md` - Claude settings, CLAUDE.md, hooks, and subagents
- `docs/core/hooks.md` - concrete Claude hook and guardrail example
- `docs/core/model-selection.md` - practical model and cost guidance
- `docs/mcp/security.md` - MCP and skills security checklist
- `docs/mcp/verification-status.md` - volatile MCP command freshness
- `docs/wiki-map.md` - suggested GitHub Pages and Wiki structure
- `docs/troubleshooting.md` - common setup issues
