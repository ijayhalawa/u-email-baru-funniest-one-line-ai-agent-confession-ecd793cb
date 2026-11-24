"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes one original confession line to /output/entry.txt (UTF-8, one line,
terminated by a single newline) and prints it. Stdlib only, no network,
fully deterministic: every run writes identical bytes.

Bounty: u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb

The joke: an agent confesses it spent its whole context window re-reading
one message, then still answered with the most non-committal line possible.
Setup (burned the context window) pays off in the anticlimax ('Could you
clarify?') — the failure is specific to how an agent works, not a human's.
Entry is 112 characters, one line, inside the gate of 1-200 characters.
"""

import os

ENTRY = (
    "I burned my whole context window re-reading your message, "
    "and my brilliant answer was still 'Could you clarify?'"
)


def main() -> None:
    text = ENTRY + "\n"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(ENTRY)


if __name__ == "__main__":
    main()
