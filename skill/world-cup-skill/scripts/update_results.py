#!/usr/bin/env python3
"""Append a finished World Cup match result to match_results.csv."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

FIELDS = [
    "match_id",
    "tournament",
    "stage",
    "match_date",
    "team_a",
    "team_b",
    "score_a",
    "score_b",
    "aet",
    "penalties",
    "xg_a",
    "xg_b",
    "red_cards_a",
    "red_cards_b",
    "notes",
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="match_results.csv")
    for field in FIELDS:
        parser.add_argument(f"--{field.replace('_', '-')}", default="")
    args = parser.parse_args()

    path = Path(args.file)
    exists = path.exists()
    row = {field: getattr(args, field) for field in FIELDS}

    with path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if not exists:
            writer.writeheader()
        writer.writerow(row)

    print(f"updated {path}")


if __name__ == "__main__":
    main()
