# Shared Agent Rules

Use this file as the common instruction source for Codex, Claude Code, and other coding agents.

## Golden workflow

```text
Codex = implement
Claude Code = review
You = approve
CI = enforce
GitHub PR = final audit trail
```

## Safety rules

Agents may:

- read repository files
- edit files on a feature branch
- run local tests
- run linters
- run formatters
- create draft PR descriptions
- review diffs

Agents may not, unless explicitly authorised:

- commit
- push
- merge
- deploy
- publish packages
- delete branches
- modify production infrastructure
- write to production databases
- change secrets or credentials
- edit `.env`, signing keys, certificates, or token files

## Protected files and areas

Treat these as high risk:

```text
.env
.env.*
*.pem
*.key
*.keystore
*.jks
google-services.json
GoogleService-Info.plist
production config
deployment scripts
database migrations
generated files
lockfiles
```

Do not modify them without explicit task context.

## Implementation standards

- Inspect before editing.
- Keep diffs small.
- Prefer existing patterns in the repo.
- Add tests for behaviour changes.
- Avoid speculative abstractions.
- Avoid broad rewrites unless requested.
- Do not add dependencies casually.
- Explain dependency additions.
- Prefer simple, readable code.
- Leave the codebase better, but do not mix unrelated clean-up into feature work.

## Final response checklist for agents

Every coding task should end with:

```text
Summary:
- ...

Files changed:
- ...

Commands run:
- ...

Tests:
- Passed / failed / not run with reason

Risks:
- ...
```
