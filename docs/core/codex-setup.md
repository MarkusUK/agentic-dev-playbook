# Codex Setup Notes

Codex uses project instructions, config, skills, MCP servers, sandboxing, and approvals to decide what it can safely do.

## AGENTS.md hierarchy

Use `AGENTS.md` for project instructions that Codex and other coding agents should read.

Useful locations:

```text
~/.codex/AGENTS.md         # personal defaults across projects
./AGENTS.md                # project instructions
```

Codex also supports `AGENTS.override.md` in the Codex home directory for global overrides. Keep global instructions short and generic; put project facts in the repo.

## Config

Codex config and MCP servers live in:

```text
~/.codex/config.toml       # user-level Codex config
.codex/config.toml         # project-level Codex config, when supported by your workflow
```

Use config for:

- model defaults
- sandbox settings
- approval policy
- MCP servers
- skill enable/disable settings

## Skills

Repo-scoped Codex skills live in:

```text
.agents/skills/<skill-name>/SKILL.md
```

User-level Codex skills live in:

```text
~/.agents/skills/<skill-name>/SKILL.md
```

Use skills for repeated workflows such as review, testing, debugging, and design-to-code.

## Sandboxing and approvals

The safe default for local work is:

```text
workspace-write filesystem access
approval prompts for risky or out-of-sandbox actions
network off unless needed
```

Use stricter settings for risky repositories. Use broader settings only when the task genuinely requires them and you understand the blast radius.

## Practical defaults

For new projects:

```text
Codex implements on a feature branch.
Codex does not commit, push, deploy, or publish unless explicitly told.
Codex runs focused tests before finishing.
Claude Code reviews the diff before you merge.
CI enforces the shared checks.
```

## When to use Codex

Use Codex for:

- implementing scoped changes
- reading and editing across the repo
- running tests and fixing failures
- local browser/app verification
- turning design specs into code

Use another review pass when the change touches security, data loss, auth, billing, deployment, or broad architecture.
