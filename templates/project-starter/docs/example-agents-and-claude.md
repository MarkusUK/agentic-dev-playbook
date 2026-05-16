# Example AGENTS.md and CLAUDE.md

The starter ships generic scaffolds. This page shows what a **filled-in**
`AGENTS.md` and `CLAUDE.md` look like for a real project, so you can see
what "good" looks like before adapting one for your own repo.

The example uses a fictional polyglot project called **Tide**:

- **Mobile** — Flutter / Dart, Riverpod for state, Dio for HTTP.
- **Backend** — Python 3.12, FastAPI, SQLAlchemy 2.x (async), Alembic.
- **Database** — PostgreSQL 16, run locally via Docker Compose.

Polyglot is the interesting case because the `AGENTS.md` has to make
clear which commands belong to which side of the project. Adapt the
shape, not the words — the discipline transfers to any stack.

## What makes these files effective

Before the example, the five habits that matter most:

1. **Front-load constraints.** The first thing the agent reads should
   be what it must not do, not background information.
2. **Name protected files explicitly** by path or glob. "Don't touch
   secrets" is too vague; `.env`, `backend/secrets/**`,
   `mobile/android/key.properties` is enforceable.
3. **List real commands** with the working directory. In a polyglot
   repo, `poetry run pytest` is useless without knowing it runs from
   `backend/`.
4. **Keep them short enough that the agent will re-read them.** Under
   ~200 lines is the sweet spot. Push detail into `docs/` and link.
5. **Do not duplicate the README.** The README is for humans browsing
   GitHub. `AGENTS.md` is operational instructions for an agent.

## Anti-patterns to avoid

- Inlining a 1000-line architecture description. Link to
  `docs/architecture.md` instead.
- Listing every file in the repo. The agent can grep.
- Vague rules like "write good code" or "be careful". Unenforceable.
- Stale commands. If you renamed a directory six months ago, fix
  `AGENTS.md` the same day.
- Secrets in either file. Use environment variable names, never values.
- A wall of "always" and "never" with no priority order. Group
  must-not, must, should, optional.

## Example AGENTS.md

````markdown
# Tide — Agent Instructions

Tide is a small mobile + API project. Mobile is Flutter, backend is
FastAPI, data lives in PostgreSQL. These instructions apply to Codex
and any other coding agent working in this repo.

## Must not do

- Commit, push, merge, or deploy unless I explicitly say so.
- Edit any of these without an explicit task:
  - `.env`, `.env.*`, `backend/secrets/**`
  - `mobile/android/key.properties`, `mobile/android/*.jks`
  - `backend/alembic/versions/*.py` for migrations already on `main`
    (released migrations are immutable — add a new revision instead)
  - `pubspec.lock`, `backend/poetry.lock` (do not regenerate casually)
- Run database commands against anything other than the local Docker
  Postgres. Never connect to staging or production without my approval.
- Add a new Python or Dart dependency without explaining why in the
  diff.

## Must do before editing

1. Work on a feature branch (`feature/<short-name>`).
2. Read `docs/architecture.md` for the relevant side (mobile or backend).
3. Bring the local stack up:

   ```bash
   docker compose -f infra/docker-compose.yml up -d postgres
   ```

4. Inspect nearby code and tests; match existing patterns rather than
   introducing new ones.

## Repo layout

```text
tide/
  mobile/                  # Flutter app
    lib/
      features/<feature>/  # screens, widgets, state per feature
      data/                # API clients, DTOs
      core/                # theme, routing, shared widgets
    test/
    pubspec.yaml
  backend/                 # FastAPI service
    app/
      api/                 # route handlers
      services/            # business logic
      models/              # SQLAlchemy ORM models
      schemas/             # Pydantic request/response models
      db/                  # session, engine, base
    tests/                 # pytest
    alembic/
      versions/            # migration scripts (immutable once merged)
    pyproject.toml
  infra/
    docker-compose.yml     # local Postgres
  docs/
```

## Stack

```text
Mobile:    Flutter 3.x, Dart 3.x, Riverpod (state), Dio (HTTP)
Backend:   Python 3.12, FastAPI, SQLAlchemy 2.x async, Alembic
Database:  PostgreSQL 16 (Docker for local, managed for prod)
Tests:     pytest + pytest-asyncio (backend), flutter_test (mobile)
Tooling:   ruff + mypy (backend), dart analyze (mobile)
Packaging: Poetry (backend), pub (mobile)
```

## Commands

Backend (run from `backend/`):

```bash
poetry install
poetry run pytest                              # unit + integration
poetry run pytest tests/api -k auth            # focused subset
poetry run ruff check .
poetry run mypy app
poetry run alembic upgrade head                # apply migrations locally
poetry run alembic revision --autogenerate -m "describe change"
poetry run uvicorn app.main:app --reload       # dev server on :8000
```

Mobile (run from `mobile/`):

```bash
flutter pub get
flutter test
flutter analyze
flutter run                                    # needs emulator or device
flutter build apk --debug
```

Database (run from repo root):

```bash
docker compose -f infra/docker-compose.yml up -d postgres
docker compose -f infra/docker-compose.yml exec postgres psql -U tide tide
```

## MCPs and skills

Project MCPs (`.codex/config.toml`):

- `context7` — current FastAPI, SQLAlchemy, Flutter, Riverpod docs.
- `figma` — design context for mobile screens.

Skills (`.agents/skills/`):

- `review-pr` — diff review checklist.
- `write-tests` — `pytest` or `flutter_test` depending on which side changed.
- `debug-issue` — diagnose before fixing.
- `design-to-code` — turn Figma frames into Flutter widgets.

Prompt explicitly when you want a tool used; do not assume.

## Common pitfalls in this codebase

- **SQLAlchemy async sessions.** Always go through the dependency in
  `app/db/session.py`. Do not create raw sessions inside route handlers.
- **Alembic autogenerate.** It misses constraint, enum, and index
  changes. Always review the generated script before committing.
- **Pydantic v2 vs v1.** This project is v2. Use `model_dump()` not
  `dict()`, `model_validate()` not `parse_obj()`.
- **Flutter rebuilds.** Use Riverpod's `select` to avoid rebuilding the
  whole screen on small state changes.
- **CORS and emulator host.** An Android emulator reaches the backend
  on `http://10.0.2.2:8000`, not `localhost`. iOS simulator uses
  `localhost`. Backend CORS allows both during development.
- **Database resets.** `docker compose down -v` deletes the volume.
  Use it intentionally, not as a debugging reflex.

## Done means

- Backend: `pytest`, `ruff`, and `mypy` all pass.
- Mobile: `flutter test` and `flutter analyze` pass.
- New behaviour has a test on whichever side it lives.
- If the change crosses both sides, an integration test covers the
  contract.
- Diff is small enough for one-sitting review.

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

# Tide — Claude Code Instructions

Shared rules are in `AGENTS.md` (imported above). This file adds
Claude-specific behaviour on top.

## Default stance

- **Review-first.** Run `git status` and `git diff` before editing
  anything.
- **Do not edit during review** unless I explicitly ask.
- **Categorise findings** as `Must fix`, `Should fix`, `Optional`.
- For changes that touch both `mobile/` and `backend/`, propose
  splitting into two PRs unless they are genuinely coupled (e.g. a
  new API endpoint and its client).

## Subagents

Project subagents (`.claude/agents/`):

- `reviewer` — independent diff review pass.
- `sql-reviewer` — extra pass for anything touching
  `backend/alembic/versions/` or raw SQL.

Subagents have isolated context and their own tool limits. Prefer
them over inline prompts when the role is well-defined.

## Hooks

`.claude/settings.json` and `.claude/hooks/` block destructive shell
commands (`rm -rf`, `git push origin main`, force pushes, deployment
commands) before the Bash tool runs. If a hook blocks you, do not
retry — tell me what you were trying to do and why.

## Skills

Use these when the prompt matches:

- `review-pr` — for diff and PR review.
- `write-tests` — for adding tests on either side.
- `debug-issue` — for diagnosing a bug before proposing a fix.
- `design-to-code` — for turning Figma frames into Flutter widgets.

Do not invoke MCP tools (Figma, Context7, etc.) unless I name them
in the prompt.

## Model preference

Use Sonnet by default. Switch to Opus for:

- Alembic migration design.
- Auth or session changes on either side.
- Anything that touches both `mobile/` and `backend/` at once.

See `docs/model-selection.md` for the broader rule.
````

## What to copy, what to adapt

Reuse this **structure** verbatim:

- "Must not do" first, then "Must do before editing", then layout,
  stack, commands.
- Real paths and globs in protected-files lists.
- Working directory shown alongside each command in a polyglot repo.
- "Common pitfalls" drawn from real incidents, not theoretical risks.
- `Done means` checklist and final response format.

Replace this **content** entirely for your project:

- Stack, paths, commands, dependencies.
- MCP and skill list — only include the ones you actually have configured.
- Common pitfalls — yours will be specific to your stack and history.
- Subagent names — only list ones you have actually created.

The Tide example happens to be Flutter + FastAPI + Postgres. A
Next.js + tRPC + Prisma project, or a Rust service with a React admin
panel, would look very different at the file level but the discipline
is the same: front-load constraints, name protected files, list real
commands, keep it short.
