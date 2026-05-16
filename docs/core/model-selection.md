# Model Selection

Model choice affects quality, latency, and cost. Keep the default simple and only upgrade when the task needs it.

Last verified: 2026-05-16.

## Claude Code

Good default:

```text
Sonnet for most implementation, review, and debugging work.
```

Use Opus when the task needs deeper reasoning:

```text
architecture decisions
large refactors
ambiguous bugs
multi-step planning
security-sensitive review
```

Use Haiku for simple, bounded tasks:

```text
small summaries
formatting
simple subagent checks
low-risk repetitive tasks
```

Claude Code supports model aliases such as `sonnet`, `opus`, and `haiku`. Use `/model` inside a session to switch.

## Codex

For local Codex CLI and IDE work, use the recommended default unless you have a reason to pin a model.

When pinning locally, set `model` in Codex config:

```toml
model = "gpt-5.5"
```

If that model is not available in your account, use `gpt-5.4`.

Use higher reasoning effort for:

- hard debugging
- architecture
- cross-cutting refactors
- security-sensitive work

Use lower effort for:

- small edits
- formatting
- narrow test fixes
- quick summaries

## Practical rule

```text
Cheap/fast for routine.
Strong/deep for ambiguous or high-risk.
Review pass before merge.
```

If cost matters, make tasks smaller before reaching for a stronger model.
