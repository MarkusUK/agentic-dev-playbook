# Security Policy

This repository contains documentation, starter templates, MCP examples, and agent skills. The main risks are accidental secret exposure, over-broad MCP access, and unsafe shared automation.

## Supported versions

The latest `main` branch is the supported version.

## Reporting a security issue

If you find a security issue, open a private security advisory on GitHub if available, or contact the repository owner privately.

Do not open a public issue containing secrets, tokens, private URLs, customer data, or exploit details.

## Security expectations

- Do not commit `.env` files, API keys, OAuth tokens, signing keys, keystores, production credentials, or private customer data.
- Prefer project-level MCP config over global config.
- Prefer read-only MCP access where possible.
- Treat MCP output as untrusted until cross-checked.
- Review `.mcp.json`, `.codex/config.toml`, `.agents/skills/`, and `.claude/skills/` before committing them.
- Use environment variable references for credentials.

For the full checklist, see `docs/mcp/security.md`.
