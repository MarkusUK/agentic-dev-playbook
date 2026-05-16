# Agentic Dev Workflow Reference

This is the reusable reference guide for starting new projects with Codex, Claude Code, MCP, skills, hooks, and safe code review.

## Recommended setup

```text
Codex = implement
Claude Code = review
You = approve
CI = enforce
GitHub PR = final audit trail
```

## Repo setup

Add:

```text
AGENTS.md
CLAUDE.md
docs/
  agent-rules.md
  testing.md
  architecture.md
  release.md
.claude/
  skills/
    write-tests/
      SKILL.md
    review-pr/
      SKILL.md
    debug-issue/
      SKILL.md
    android-testing/
      SKILL.md
    design-to-code/
      SKILL.md
    ui-assets/
      SKILL.md
```

Codex-style skills:

```text
.agents/
  skills/
    write-tests/
      SKILL.md
    review-pr/
      SKILL.md
    debug-issue/
      SKILL.md
    android-testing/
      SKILL.md
    design-to-code/
      SKILL.md
    ui-assets/
      SKILL.md
```

## Main rules

```text
- Inspect before editing.
- Work on a feature branch only.
- Keep changes small and reviewable.
- Do not commit, push, deploy, or merge unless explicitly told.
- Do not touch secrets, .env files, credentials, production config, or generated files.
- Do not add dependencies without explaining why.
- Run relevant tests before finishing.
- Summarise changed files and commands run.
```

## Development workflow

```text
1. Create feature branch.
2. Ask Codex to inspect and plan.
3. Let Codex implement.
4. Run tests/typecheck/lint.
5. Ask Claude Code to review the diff.
6. Apply only agreed fixes.
7. Run tests again.
8. Commit yourself.
9. Push and open PR.
10. Let CI and/or another agent review the PR.
```

## Command flow

```bash
git checkout main
git pull
git checkout -b feature/my-change
codex
```

Ask Codex:

```text
Inspect the repo first. Do not edit yet.

I want to implement [task].

Give me:
- likely files to change
- risks
- tests to run
- minimal implementation plan
```

Then:

```text
Proceed with the implementation. Keep the diff small. Run relevant tests. Do not commit.
```

Review with Claude Code:

```bash
claude
```

Ask Claude:

```text
Review the current uncommitted git diff as a senior engineer.

Focus on:
- correctness
- edge cases
- security
- regressions
- missing tests
- unnecessary complexity

Do not edit files yet. Categorise findings as must-fix, should-fix, and optional.
```

After fixes:

```bash
npm test
npm run lint
npm run typecheck
git diff
git add .
git commit -m "feat: implement my change"
git push -u origin feature/my-change
```

Use your project-specific test commands.

## CLI vs desktop vs IDE

Use CLI for serious repo work.

Use desktop apps for orchestration, multiple sessions, and visual diff review.

Use IDE extensions for quick help while editing.

Use cloud/web tasks for delegated parallel work, PRs, and lower-risk tasks that do not need local secrets or local-only services.

## MCP usage

MCP gives coding agents access to external systems.

Good first MCPs:

```text
- GitHub: issues, PRs, CI status
- Linear/Jira: tickets
- docs/search: current docs
- Figma: frontend/design work
- Sentry: production errors, read-only
- database: read-only staging/replica only
```

Start read-only wherever possible.

Avoid giving agents broad write access early on.

## Skills

Skills are reusable procedures.

Good starter skills:

```text
debug-issue
write-tests
review-pr
android-testing
design-to-code
ui-assets
```

Use skills when you repeatedly paste the same instructions or checklist. Invoke explicitly as `$write-tests` in Codex or `/write-tests` in Claude Code, depending on the tool you are using.

## Hooks and safety automation

Use hooks or shell wrappers to block dangerous commands and enforce quality gates.

Block:

```text
rm -rf
direct pushes to main
deploy commands
edits to .env / secrets
production database writes
credential files
```

Allow:

```text
reading repo files
editing feature branch files
running tests
running linters
creating PR descriptions
reviewing diffs
```

## Android AVD testing from terminal

You do not need VS Code to run Android emulators or Android tests.

List AVDs:

```bash
emulator -list-avds
```

Start an AVD:

```bash
emulator -avd <AVD_NAME>
```

Check devices:

```bash
adb devices
```

Build:

```bash
./gradlew assembleDebug
```

Run unit tests:

```bash
./gradlew test
```

Run instrumentation tests:

```bash
./gradlew connectedAndroidTest
```

View logs:

```bash
adb logcat
```

Install APK:

```bash
adb install -r app/build/outputs/apk/debug/app-debug.apk
```

## Best quality pattern

```text
Codex writes the code.
Claude reviews the diff.
Codex or you apply fixes.
Claude reviews again.
You commit.
CI verifies.
```

For important work, reverse the roles sometimes:

```text
Claude implements.
Codex reviews.
```

## Golden rule

Do not optimise for agent autonomy first.

Optimise for:

```text
small changes
clear plans
testable diffs
independent review
human-controlled commit/push/merge
```

## Project-level MCPs and skills

For project-specific MCPs and skills, read:

```text
docs/project-level-mcps-and-skills.md
```

Core rule:

```text
MCP answers: “What can the agent access?”
Skills answer: “How should the agent work?”
Prompt answers: “What should it use right now?”
```

Keep global MCP config minimal. Add tools like Figma, Stitch, 21st.dev/Magic, Rive, Sentry, Firebase, databases, and Linear/Jira per repo/project only when needed.

When you want an agent to use an external tool, say so explicitly:

```text
Use the Figma MCP to inspect this design: [URL]

Before editing:
- identify the target component
- map design tokens to existing theme values
- find components to reuse
- list risks
- propose a minimal plan

Do not edit yet.
```


## Design start and interactive mockups

For early product/UI work, use:

```text
design-start/
```

Recommended design flow:

```text
idea -> brand directions -> screen specs -> optional interactive mockup -> implementation plan -> small coded slice -> review
```

Interactive React/Tailwind mockups are worth using during the design stage when you want to test navigation, screen hierarchy, onboarding, dashboard layouts, forms, empty states, and basic motion.

Treat mockups as prototypes, not production code. Once a mockup direction is selected, ask the coding agent to inspect the real repo and create a stack-specific implementation plan.
