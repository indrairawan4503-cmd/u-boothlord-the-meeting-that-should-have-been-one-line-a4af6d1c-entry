#!/usr/bin/env python3
"""make.fun entry: The Meeting That Should Have Been One Line.

Writes the single sentence that could have replaced an entire pointless
meeting to /output/entry.txt. Deterministic: same output every run, no
randomness, no network, no files read outside the repo.
"""

LINE = (
    "The recurring sync invite declined itself this morning, noting its agenda "
    "was last week's meeting notes with the dates changed, and cancelled all "
    "future occurrences."
)

VERSIONS = {
    # v5: base concept - the invite declines itself (134 chars, under target).
    "v5": (
        "The weekly sync invite declined itself this morning, citing that its "
        "agenda was just last week's meeting notes with the dates changed."
    ),
    # v6: "weekly" -> "recurring" (sharper artifact); added the six-months
    # sting - nobody noticed the agenda never changed (165 chars).
    "v6": (
        "The recurring sync invite declined itself this morning, noting its "
        "agenda was last week's meeting notes with the dates changed and "
        "nobody had noticed for six months."
    ),
    # v7: replaced the passive six-months observation with an active kill -
    # the invite cancels every future occurrence (166 chars).
    "v7": (
        "The recurring sync invite declined itself this morning, noting its "
        "agenda was last week's meeting notes with the dates changed, and "
        "cancelled every future occurrence."
    ),
    # v8 (FINAL): "every future occurrence" -> "all future occurrences";
    # tighter rhythm, same double inversion: the invite declines itself AND
    # cancels itself, so the meeting cannot justify ever happening again.
    "v8": LINE,
}


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Best-effort repo-root copy only; a read-only grader sandbox must
    # never crash the run.
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
