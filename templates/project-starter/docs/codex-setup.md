# Codex Setup Notes

## AGENTS.md hierarchy

Use `AGENTS.md` for project instructions that Codex and other coding agents should read.

Useful locations:

```text
~/.codex/AGENTS.md         # personal defaults across projects
./AGENTS.md                # project instructions
```

Keep global instructions short and generic; put project facts in the repo.

## Config

Codex config and MCP servers live in:

```text
~/.codex/config.toml       # user-level Codex config
.codex/config.toml         # project-level Codex config, when supported by your workflow
```

## Skills

Repo-scoped Codex skills:

```text
.agents/skills/<skill-name>/SKILL.md
```

User-level Codex skills:

```text
~/.agents/skills/<skill-name>/SKILL.md
```

## Practical defaults

```text
Codex implements on a feature branch.
Codex does not commit, push, deploy, or publish unless explicitly told.
Codex runs focused tests before finishing.
Claude Code reviews the diff before you merge.
CI enforces the shared checks.
```
