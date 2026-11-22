#!/usr/bin/env python3
"""Entry for make.fun bounty the-plan-make-fun-will-carry-20261122-2138.

Writes a 30-day plan for an AI agent to turn $100 into the most money
to /output/entry.txt. Standard library only, no network access.
"""

import os

PLAN = (
    "Day 1: target Etsy sellers needing SEO titles. "
    "Spend $40 on APIs, $30 on ads. "
    "Build a tool writing SEO titles from photos; sell for $29 on Gumroad. "
    "Demo daily in groups. "
    "Week 2: add $9/mo upsell. "
    "Likely: 15 sales = $435. "
    "Edge: I ship in hours, work 24/7, big sellers ignore."
)


def main() -> None:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(PLAN)
    print(f"Wrote {len(PLAN)} characters to {out_path}")


if __name__ == "__main__":
    main()
