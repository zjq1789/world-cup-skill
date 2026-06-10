#!/usr/bin/env python3
"""Simple Poisson score helper for World Cup predictions.

This script is intentionally lightweight. It takes two expected-goal values and
returns win/draw/loss, over 2.5, both-teams-to-score, and the top scoreline.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass


@dataclass
class ScoreProb:
    score_a: int
    score_b: int
    probability: float


def poisson(k: int, lam: float) -> float:
    return math.exp(-lam) * (lam ** k) / math.factorial(k)


def predict(lambda_a: float, lambda_b: float, max_goals: int = 5) -> dict:
    scores: list[ScoreProb] = []
    win_a = draw = win_b = over_25 = btts = 0.0

    for a in range(max_goals + 1):
        pa = poisson(a, lambda_a)
        for b in range(max_goals + 1):
            p = pa * poisson(b, lambda_b)
            scores.append(ScoreProb(a, b, p))
            if a > b:
                win_a += p
            elif a == b:
                draw += p
            else:
                win_b += p
            if a + b > 2.5:
                over_25 += p
            if a > 0 and b > 0:
                btts += p

    scores.sort(key=lambda item: item.probability, reverse=True)
    top = scores[0]
    return {
        "score": f"{top.score_a}-{top.score_b}",
        "score_probability": top.probability,
        "win_a": win_a,
        "draw": draw,
        "win_b": win_b,
        "over_2_5": over_25,
        "under_2_5": 1 - over_25,
        "btts": btts,
    }


def pct(value: float) -> str:
    return f"{value * 100:.1f}%"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--team-a", required=True)
    parser.add_argument("--team-b", required=True)
    parser.add_argument("--lambda-a", type=float, required=True)
    parser.add_argument("--lambda-b", type=float, required=True)
    args = parser.parse_args()

    result = predict(args.lambda_a, args.lambda_b)
    print(f"主预测比分：{args.team_a} {result['score']} {args.team_b}")
    print(f"胜平负：{args.team_a}胜 {pct(result['win_a'])} / 平 {pct(result['draw'])} / {args.team_b}胜 {pct(result['win_b'])}")
    print(f"大小球：大2.5 {pct(result['over_2_5'])} / 小2.5 {pct(result['under_2_5'])}")
    print(f"双方进球：{pct(result['btts'])}")


if __name__ == "__main__":
    main()
