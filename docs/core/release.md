# Release and PR Safety Guide

## Branching

Work from a feature branch:

```bash
git checkout main
git pull
git checkout -b feature/my-change
```

## Before committing

Run relevant checks:

```bash
git status
git diff
```

Then run project checks, for example:

```bash
npm test
npm run lint
npm run typecheck
npm run build
```

For Android:

```bash
./gradlew test
./gradlew lint
./gradlew assembleDebug
```

## Commit rule

Agents should not commit unless explicitly instructed.

Human-controlled commit:

```bash
git add .
git commit -m "feat: describe change"
```

## Push rule

Agents should not push unless explicitly instructed.

Human-controlled push:

```bash
git push -u origin feature/my-change
```

## PR checklist

PR should include:

- summary of change
- linked issue/ticket
- screenshots or recordings for UI work
- tests run
- risk areas
- rollback notes if relevant

## Before merge

- CI passes.
- Human review complete.
- Agent review findings resolved or consciously dismissed.
- No secrets or generated junk included.
