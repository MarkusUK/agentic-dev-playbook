#!/usr/bin/env python3
"""Block high-risk Claude Code Bash commands before they run."""

import json
import re
import sys


BLOCK_PATTERNS = [
    (r"\brm\s+-rf\s+(/|\*|\.|~)", "Refusing broad recursive deletion."),
    (r"\bgit\s+push\s+origin\s+main\b", "Refusing direct push to main."),
    (r"\bgit\s+push\b.*\s--force\b", "Refusing force push."),
    (r"\bterraform\s+apply\b", "Refusing terraform apply from agent session."),
    (r"\bkubectl\s+delete\b", "Refusing kubectl delete from agent session."),
    (r"\b(firebase|vercel|netlify)\s+deploy\b", "Refusing deployment command."),
]


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0

    command = (
        payload.get("tool_input", {}).get("command")
        or payload.get("tool_input", {}).get("cmd")
        or ""
    )

    for pattern, reason in BLOCK_PATTERNS:
        if re.search(pattern, command, flags=re.IGNORECASE):
            print(
                json.dumps(
                    {
                        "hookSpecificOutput": {
                            "hookEventName": "PreToolUse",
                            "permissionDecision": "deny",
                            "permissionDecisionReason": reason,
                        }
                    }
                )
            )
            return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
