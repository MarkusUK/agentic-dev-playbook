# Minimal Setup

The shortest path from "no setup" to a safe first agent session in an
existing repo. No starter template, no skills, no MCPs, no hooks. Add
those later when you actually need them.

If you are starting a brand-new project, use the fuller
[Start Here in 10 Minutes](quickstart.md) instead — it bundles the
starter template.

## 1. Drop one file in your repo root

Pick the one matching your tool. Both are short. Adjust the commands
under **Commands** to match your project.

### AGENTS.md (Codex)

```markdown
# Agent Instructions

## Must not do

- Commit, push, merge, deploy, or publish unless I explicitly say so.
- Touch `.env`, `*.key`, `*.keystore`, `secrets/**`, or production config.
- Add a new dependency without explaining why.

## Must do

- Work on a feature branch.
- Inspect existing code and tests before writing new code.
- Match existing patterns; do not introduce new ones unprompted.
- Run tests after changes.
- Keep diffs small.

## Commands

- Tests: `<your test command>`
- Lint:  `<your lint command>`
- Build: `<your build command>`

## End every task with

Summary, files changed, commands run, tests passed/failed, risks.
```

### CLAUDE.md (Claude Code)

```markdown
@AGENTS.md

## Claude-specific

- Review-first. Run `git status` and `git diff` before editing.
- Do not edit during review unless I ask.
- Categorise findings as Must fix / Should fix / Optional.
```

If you only use one tool, drop only one file. If you use both, drop
both — `CLAUDE.md` imports `AGENTS.md` via the `@AGENTS.md` line.

## 2. Install the CLI

### Codex

```bash
npm install -g @openai/codex
codex login
```

### Claude Code

```bash
npm install -g @anthropic-ai/claude-code
claude
```

First run will walk you through authentication.

## 3. First safe prompt

Open the CLI in your repo and paste:

```text
Read AGENTS.md (and CLAUDE.md if present).

Inspect the repo and tell me:
- the stack and main directories
- where tests live and how to run them
- anything that looks risky or fragile

Do not edit any files yet.
```

This is a no-write reconnaissance pass. It confirms the agent has
loaded your rules and understands the repo before it touches anything.

## 4. Then a small change

```text
Implement [one small, well-scoped task].

Rules:
- Stay on the current branch.
- Keep the diff small.
- Add or update tests for the changed behaviour.
- Run the test command and report results.
- Do not commit.
```

Review the diff yourself. Commit yourself. The agent should not push.

## When to upgrade

Reach for the full [Start Here in 10 Minutes](quickstart.md) and the
[Starter Template](templates.md) when you find yourself:

- pasting the same multi-step instructions into prompts repeatedly →
  add a **[skill](mcp/skills-anatomy.md)**.
- wanting the agent to pull external context (Figma, Sentry, current
  docs) → add an **[MCP](mcp/mcp-primer.md)**.
- worrying about destructive shell commands slipping through →
  add a **[hook](core/hooks.md)**.
- managing multiple projects with similar conventions → adopt the
  **[starter template](templates.md)**.

Until then, the single `AGENTS.md` or `CLAUDE.md` plus a careful first
prompt is enough to get real value with very little ceremony.
