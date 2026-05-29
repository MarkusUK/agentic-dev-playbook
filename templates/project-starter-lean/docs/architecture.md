# Architecture Notes

Replace this file with project-specific facts before serious agent work.

## Project Overview

```text
Name:
Purpose:
Target users:
Main platforms:
```

## Tech Stack

```text
Frontend:
Backend:
Database:
Auth:
Hosting/deploy:
Package manager:
```

## Repository Structure

```text
src/ or app/:
tests/:
docs/:
assets/:
```

## Important Patterns

- Where should new screens/components live?
- Where should business logic live?
- Where should API calls/data access live?
- What naming conventions matter?
- What existing components or tokens should agents reuse?

## Protected Areas

Agents should not change these casually:

```text
.env
.env.*
secrets/**
production config
generated files
lockfiles unless dependency changes are approved
```

## Known Risks / Gotchas

```text
List anything agents should be careful about, or write "none known yet".
```
