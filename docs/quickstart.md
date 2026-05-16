# Start Here in 10 Minutes

Use this path when you want to start a new project with Codex, Claude Code, MCPs, and skills without reading the whole playbook first.

## 1. Copy the starter

Copy this folder into the root of your new project:

```text
templates/project-starter/
```

Keep the files you need and delete anything that is irrelevant to the stack you are using.

## 2. Customise the project facts

Edit these first:

```text
AGENTS.md
CLAUDE.md
docs/architecture.md
docs/testing.md
docs/release.md
```

Replace generic commands such as `npm test`, `./gradlew test`, or `./gradlew connectedAndroidTest` with the real commands for that repo.

## 3. Choose the agent workflow

Recommended default:

```text
Codex = implement
Claude Code = review
You = approve
CI = enforce
GitHub PR = final audit trail
```

Use Codex for implementation, local exploration, and test fixes. Use Claude Code for review, risk spotting, and an independent pass over the diff.

## 4. Add only the MCPs you need

Keep global MCP config minimal. Add project-level MCPs only when they provide useful context for the current repo.

Use this rule:

```text
MCP answers: What can the agent access?
Skills answer: How should the agent work?
Prompt answers: What should it use right now?
```

Read:

- [MCP and Skills](mcp/mcp-and-skills.md)
- [MCP and Skills Primer](mcp/mcp-primer.md)
- [Project-Level MCPs and Skills](mcp/project-level-mcps-and-skills.md)
- [SKILL.md Anatomy](mcp/skills-anatomy.md)
- [MCP and Skills Security](mcp/security.md)

## 5. Use skills for repeated workflows

The starter includes skills for:

```text
review-pr
write-tests
debug-issue
android-testing
design-to-code
ui-assets
```

Codex repo-scoped skills live in:

```text
.agents/skills/<skill-name>/SKILL.md
```

Claude Code repo-scoped skills live in:

```text
.claude/skills/<skill-name>/SKILL.md
```

## 6. Make the first task small

Start with a bounded task, for example:

```text
Read AGENTS.md, docs/architecture.md, and docs/testing.md.
Then inspect the repo and propose the smallest safe plan for adding [feature].
Use project skills only if relevant.
```

After the first implementation, ask for a review:

```text
Review the current diff for correctness, regression risk, security, and missing tests.
Do not edit files unless I ask.
```

## 8. Know the tool-specific setup

Read these when you want the details behind the defaults:

- [Codex Setup Notes](core/codex-setup.md)
- [Claude Code Setup Notes](core/claude-code-setup.md)
- [Hooks and Guardrails](core/hooks.md)
- [Model Selection](core/model-selection.md)

## 9. Validate before publishing

Before publishing this playbook or using the starter in a real project, run:

```bash
python -m pip install -r requirements.txt
mkdocs build --strict
```

For project repos, use the project-specific test, lint, type-check, and build commands from `docs/testing.md`.
