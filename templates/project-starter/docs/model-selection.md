# Model Selection

Model choice affects quality, latency, and cost. Keep the default simple and only upgrade when the task needs it.

## Claude Code

Good default:

```text
Sonnet for most implementation, review, and debugging work.
```

Use Opus for complex architecture, ambiguous bugs, broad refactors, and security-sensitive review.

Use Haiku for simple summaries, formatting, and low-risk repetitive tasks.

## Codex

Use the recommended default unless you have a reason to pin a model.

For local Codex CLI and IDE work, model defaults can be set in Codex config:

```toml
model = "gpt-5.5"
```

If that model is not available in your account, use `gpt-5.4`.

## Practical rule

```text
Cheap/fast for routine.
Strong/deep for ambiguous or high-risk.
Review pass before merge.
```
