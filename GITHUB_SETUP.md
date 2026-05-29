# GitHub Setup Guide

Use this after you have finished local review and are ready to publish the playbook as a GitHub repository.

## 1. Create a new GitHub repo

Suggested names:

```text
agentic-dev-playbook
```

Start private if you want to refine it first.

## 2. Pre-publish checklist

Before the first push:

- Confirm `repo_url` and `site_url` in `mkdocs.yml`.
- Review `LICENSE` and change it if MIT is not what you want.
- Check `SECURITY.md` for your preferred contact route.
- Run `mkdocs build --strict`.
- Search for placeholders such as `TODO`, `EXAMPLE_VALUE`, or provider-specific MCP placeholders.
- Confirm no secrets, local config, or generated `site/` output are included.

## 3. Push this folder

From inside this folder:

```bash
git init
git add .
git commit -m "Initial AI coding agent playbook"
git branch -M main
git remote add origin https://github.com/MarkusUK/agentic-dev-playbook.git
git push -u origin main
```

## 4. Enable GitHub Pages

In GitHub:

```text
Settings -> Pages -> Build and deployment -> Source -> GitHub Actions
```

The included workflow will publish the MkDocs site.

Expected Pages URL:

```text
https://markusuk.github.io/agentic-dev-playbook/
```

## 5. Optional GitHub Wiki

Use the wiki as a short companion, not the source of truth.

Suggested wiki pages:

```text
Home
Quickstart
How I Use Codex and Claude
MCP Setup Notes
Skills I Use Often
Design Workflow
Troubleshooting
```

Keep detailed docs in `docs/` and publish them with GitHub Pages. See `docs/wiki-map.md`.

## 6. Use in a new project

Copy:

```text
templates/project-starter-lean/
```

into your new project root.

Then customise:

```text
AGENTS.md
CLAUDE.md
docs/testing.md
docs/architecture.md
docs/release.md
design-start/
```

## Local docs dependencies

```bash
pip install -r requirements.txt
mkdocs serve
mkdocs build --strict
```
