#!/usr/bin/env python3
"""Print the entry line for make.fun's "The Best Advice I Ever Got" bounty.

The line is the whole entry: one sentence, under 200 characters, about
the best advice the writer ever received. This one is a real moment —
a father watching his son rehearse an apology — and advice that only
makes sense once you have tried the easy version and found it hollow.
Revised to let the last clause land on its own: "just" for the spoken
voice, and an em dash before the final instruction so it hits like a
door closing instead of trailing off after a comma.
"""

import os

LINE = "My father, watching me rehearse an apology, said sorry is just a word until you change the thing you did — so change the thing first."


def main():
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
