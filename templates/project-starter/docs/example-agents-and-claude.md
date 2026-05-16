# Example AGENTS.md and CLAUDE.md

The starter ships generic scaffolds. This page shows what a **filled-in**
`AGENTS.md` and `CLAUDE.md` look like for a real project, so you can see what
"good" looks like before adapting one for your own repo.

The example uses a fictional project called **Hanami** — an Android habit
tracker built with Jetpack Compose, Hilt, Room, and Coroutines. Adapt the
shape, not the words: a Next.js app or a Python service would have very
different commands and protected files but the same structure.

## What makes these files effective

Before the example, the five habits that matter most:

1. **Front-load constraints.** The first thing the agent reads should be what
   it must not do, not background information.
2. **Name protected files explicitly** by path or glob. "Don't touch secrets"
   is too vague; `secrets.properties`, `*.keystore`, `app/google-services.json`
   is enforceable.
3. **List real commands**, not placeholders. `./gradlew :app:test --tests "*HabitDaoTest"`
   beats "run the tests".
4. **Keep them short enough that the agent will actually re-read them.** Under
   ~200 lines is the sweet spot. Push detail into `docs/` and link from here.
5. **Do not duplicate the README.** The README is for humans browsing GitHub.
   `AGENTS.md` is operational instructions for an agent.

## Anti-patterns to avoid

- Inlining a 1000-line architecture description. Link to `docs/architecture.md` instead.
- Listing every file in the repo. The agent can grep.
- Vague rules like "write good code" or "be careful". Unenforceable.
- Stale commands. If you renamed a Gradle module six months ago, fix
  `AGENTS.md` the same day.
- Secrets in either file. Use environment variable names, never values.
- A wall of "always" and "never" with no priority order. Group must-not, must,
  should, optional.

## Example AGENTS.md

````markdown
# Hanami — Agent Instructions

Hanami is an Android habit tracker built with Jetpack Compose. These
instructions apply to Codex and any other coding agent working in this repo.

## Must not do

- Commit, push, merge, deploy, or publish unless I explicitly say so.
- Edit any of these without an explicit task:
  - `secrets.properties`
  - `*.keystore`, `*.jks`
  - `app/google-services.json`, `app/GoogleService-Info.plist`
  - `app/proguard-rules.pro`
  - `gradle/libs.versions.toml` (coordinate dependency bumps with me first)
  - `app/src/main/java/dev/markus/hanami/data/db/migrations/*` (released
    Room migrations are immutable — add a new one instead)
- Add a new third-party dependency without explaining why in the diff message.
- Use `GlobalScope` or `runBlocking` in production code.
- Mock the Room DAO in tests — use an in-memory Room database.
- Remove or weaken a failing test to make the build pass.

## Must do before editing

1. Read `docs/architecture.md` and the relevant feature module's `README.md`.
2. Work on a feature branch (`feature/<short-name>`).
3. Inspect nearby code and tests before writing new code; match the
   existing patterns rather than introducing new ones.
4. Keep diffs small enough that I can review them in one sitting.

## Tech stack

```text
Language:        Kotlin 2.x
UI:              Jetpack Compose, Material 3
DI:              Hilt
Persistence:     Room (SQLite)
Concurrency:     Kotlin Coroutines + Flow
Navigation:      Jetpack Navigation Compose
Build:           Gradle (Kotlin DSL), version catalog
Min SDK:         26   Target SDK: 35
Unit tests:      JUnit 5, Turbine, MockK (for non-Room collaborators only)
UI tests:        Compose UI test + Espresso
```

## Where things live

```text
app/src/main/java/dev/markus/hanami/
  data/                  # Room entities, DAOs, repositories, migrations
  domain/                # Use cases, pure Kotlin, no Android imports
  ui/
    theme/               # Material 3 tokens — do not scatter colors elsewhere
    feature/
      habits/            # Habit list, detail, create/edit
      reflection/        # Daily reflection flow
      onboarding/
      settings/
  di/                    # Hilt modules
  HanamiApp.kt           # Application class
```

Feature modules follow MVI-lite: `<Feature>ViewModel` exposes a `StateFlow<UiState>`
and a single `onEvent(Event)` function. Look at `HabitListViewModel` as the
reference implementation.

## Commands

```bash
# Unit tests (fast)
./gradlew :app:testDebugUnitTest

# Single test class
./gradlew :app:testDebugUnitTest --tests "*HabitDaoTest"

# Lint + Detekt
./gradlew :app:lintDebug detekt

# Debug build
./gradlew :app:assembleDebug

# Instrumented tests (need a running emulator or device)
./gradlew :app:connectedDebugAndroidTest
```

The full Android emulator workflow lives in `docs/testing.md`.

## MCPs and skills

Project MCPs are in `.codex/config.toml`:

- `figma` — read design context for screens we are building.
- `context7` — current docs for Compose, Hilt, Room.

Skills (`.agents/skills/`):

- `review-pr` — diff review checklist.
- `write-tests` — add or improve tests matching repo style.
- `debug-issue` — diagnose before fixing.
- `android-testing` — emulator/AVD workflow.
- `design-to-code` — turn Figma context into Compose UI.

Prompt explicitly when you want a tool used; do not assume.

## Common pitfalls in this codebase

- **Recomposition cost.** Hoist individual fields, do not pass whole
  `UiState` objects into leaf composables. Run the Compose compiler
  metrics report if a list scrolls badly.
- **Room migrations.** Released schemas are immutable. Add a new
  migration in `data/db/migrations/` and update `Hanami_Database.kt`.
- **CoroutineScope.** Use `viewModelScope` inside ViewModels and
  injected `@ApplicationScope CoroutineScope` for app-wide work. Never
  `GlobalScope`.
- **Theme tokens.** All colors, spacings, shapes, and typography live in
  `ui/theme/`. Do not inline hex values in feature code.
- **Hilt and previews.** `@HiltViewModel` does not work in `@Preview`.
  Use the `Preview*` ViewModel factories in `ui/preview/`.

## Done means

- Code compiles: `./gradlew :app:assembleDebug` passes.
- Unit tests pass: `./gradlew :app:testDebugUnitTest`.
- Lint + Detekt pass.
- New behaviour has a test.
- Diff is small enough for one-sitting review.
- I have approved any new dependency.

## Final response format

End every coding task with:

```text
Summary:
Files changed:
Commands run:
Tests: passed / failed / skipped (with reason)
Risks / follow-ups:
```
````

## Example CLAUDE.md

````markdown
@AGENTS.md

# Hanami — Claude Code Instructions

Read `AGENTS.md` first (imported above). This file adds Claude-specific
behaviour on top of the shared project rules.

## Default stance

- **Review-first.** Before editing, run `git status` and `git diff` and
  describe what you see.
- **Do not edit during review** unless I explicitly ask.
- **Categorise review findings** as `Must fix`, `Should fix`, `Optional`.
- For large tasks, propose a split into smaller PRs rather than one big diff.

## Use subagents for focused roles

Project subagents are in `.claude/agents/`:

- `reviewer` — independent diff review pass. Use before I commit.
- `compose-perf-checker` — run after touching list/grid screens.

Subagents are isolated and have their own tool limits. Prefer them over
inline prompts when the role is well-defined.

## Hooks

Project hooks live in `.claude/settings.json` and `.claude/hooks/`. They
block destructive commands (`rm -rf`, `git push origin main`, etc.)
before the Bash tool runs. If a hook blocks you, do not retry the
command — tell me what you were trying to do.

## Skills

Use these skills where the prompt matches:

- `review-pr` — for diff and PR review.
- `write-tests` — for adding tests.
- `debug-issue` — for diagnosing a bug before proposing a fix.
- `design-to-code` — for turning Figma frames into Compose.
- `ui-assets` — when sourcing components from 21st.dev or similar.

Do not invoke MCP tools (Figma, Stitch, etc.) unless I name them in
the prompt.

## Model preference

Use Sonnet by default. Switch to Opus for:

- Room migration design
- Architecture changes that touch more than one feature module
- Security or auth review

See `docs/model-selection.md` for the broader rule.
````

## What to copy, what to adapt

Reuse this **structure** verbatim:

- "Must not do" first, then "Must do before editing", then stack, then commands.
- Real paths and globs in protected-files lists.
- A short "Common pitfalls" section based on bugs you have already hit.
- `Done means` checklist and final response format.

Replace this **content** entirely for your project:

- Stack, paths, commands, dependencies.
- MCP and skill list — only include the ones you actually have configured.
- Common pitfalls — these should come from your real incident history.
- Subagent names — only list ones you have created.

If your project is not Android, the most useful diff is in the commands and
protected files. The discipline is the same.
