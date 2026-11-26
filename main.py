#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands — make.fun entry.

Writes one joke about cats, a single line under 200 characters, to
/output/entry.txt. Ten fresh candidates are written below and scored
against the judge's brief in its published order (weights 5/4/3/2/1):

  1. One-line joke about cats, with a setup and a turn that lands (x5)
  2. Laugh out loud on the first read, not merely a clever smile (x4)
  3. Surprise, misdirection or a fresh angle — not a tired pun (x3)
  4. Tight: everything it needs in a few words, no padding (x2)
  5. Feels like a joke a person would retell to a friend the same day (x1)

Each criterion is scored 0-5, so the maximum total is 75.
Stock angles deliberately avoided in all ten: purr-fect, meow, paws,
litter-ally, feline fine, cat-astrophe, cat got your tongue, and any
voicemail / vase joke (an earlier cat-voicemail entry already exists).
"""

CANDIDATES = [
    # 1 — blame reversal: the cat spills it, then blames the human.
    "My cat knocked my coffee off the table, then sat in the puddle "
    "and stared at me like I'd spilled it.",
    # 2 — the $90 bed vs the box it came in.
    "I bought my cat a $90 bed. She sleeps in the box and judges me "
    "from inside it.",
    # 3 — the knocked-over glass was never an accident.
    "My cat has never once knocked a glass off the table by accident. "
    "She keeps a list.",
    # 4 — the adoption reversal.
    "I told my cat she's adopted. She said, 'No. You are. I chose "
    "this house.'",
    # 5 — the dead-mouse economy.
    "My cat brings me dead mice. I bring her food and rent. Neither "
    "of us respects the other's job.",
    # 6 — 3 a.m. feelings.
    "My cat ignores me all day, then at 3 a.m. sits on my chest to "
    "discuss her feelings.",
    # 7 — the blank wall.
    "My cat stares at a blank wall for hours. I pay the rent; she "
    "pays attention to the ghosts.",
    # 8 — room service.
    "I asked my cat what she wants. She walked to the cupboard, sat "
    "down, and waited for room service.",
    # 9 — the delete key.
    "My cat's favourite toy is a $2 string. Her second favourite is "
    "my laptop's delete key.",
    # 10 — typing in tongues.
    "My cat sat on my keyboard during a work call and my boss now "
    "thinks I type in tongues.",
]

# Scores per criterion, in the judge's published order.
# (setup+turn, laugh-out-loud, surprise/freshness, tightness, retellable)
SCORES = {
    1: (5, 4, 4, 4, 4),
    2: (4, 3, 2, 5, 4),
    3: (5, 4, 4, 4, 4),
    4: (5, 5, 5, 5, 5),
    5: (4, 4, 4, 3, 4),
    6: (4, 4, 3, 4, 4),
    7: (4, 4, 4, 4, 3),
    8: (4, 4, 3, 3, 4),
    9: (4, 4, 4, 4, 3),
    10: (4, 3, 3, 3, 3),
}

WEIGHTS = (5, 4, 3, 2, 1)


def total(score):
    return sum(s * w for s, w in zip(score, WEIGHTS))


def rank():
    ranked = sorted(
        ((total(SCORES[i]), i) for i in range(1, 11)),
        reverse=True,
    )
    return ranked


# --- part 2: winner pick, gate validation, output write ---

WINNER_INDEX = 4  # highest score: 75/75, clear margin over #1/#3 (65/75)
GATE_MIN = 1
GATE_MAX = 200


def validate(line):
    """The kit gate: /output/entry.txt must be UTF-8 text of 1-200
    characters, not only white space, a single line."""
    assert isinstance(line, str)
    assert GATE_MIN <= len(line) <= GATE_MAX, f"length {len(line)}"
    assert line.strip(), "entry is only white space"
    assert "\n" not in line.strip(), "entry must be a single line"
    line.encode("utf-8")
    return True


def main():
    ranked = rank()
    points, index = ranked[0]
    winner = CANDIDATES[index - 1]
    assert index == WINNER_INDEX, f"winner changed: #{index}"
    validate(winner)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(winner)
    print(f"winner #{index} {points}/75 ({len(winner)} chars)")
    print(winner)


if __name__ == "__main__":
    for points, i in rank():
        print(f"#{i:2d} {points:2d}/75  {CANDIDATES[i - 1]}")
    main()
