#!/usr/bin/env python3
"""World Cup score helper with calibrated scoreline selection.

The highest individual Poisson cell often collapses to 1-0, 1-1, or 0-1.
This helper keeps the Poisson distribution, but chooses a representative
scoreline using expected goals, win direction, over-under, BTTS, and margin.
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

    @property
    def total(self) -> int:
        return self.score_a + self.score_b

    @property
    def margin(self) -> int:
        return self.score_a - self.score_b

    @property
    def btts(self) -> bool:
        return self.score_a > 0 and self.score_b > 0


def poisson(k: int, lam: float) -> float:
    return math.exp(-lam) * (lam ** k) / math.factorial(k)


def build_distribution(lambda_a: float, lambda_b: float, max_goals: int) -> list[ScoreProb]:
    scores: list[ScoreProb] = []
    for a in range(max_goals + 1):
        pa = poisson(a, lambda_a)
        for b in range(max_goals + 1):
            scores.append(ScoreProb(a, b, pa * poisson(b, lambda_b)))
    return scores


def summarize(scores: list[ScoreProb]) -> dict:
    win_a = sum(s.probability for s in scores if s.score_a > s.score_b)
    draw = sum(s.probability for s in scores if s.score_a == s.score_b)
    win_b = sum(s.probability for s in scores if s.score_a < s.score_b)
    over_25 = sum(s.probability for s in scores if s.total > 2.5)
    btts = sum(s.probability for s in scores if s.btts)
    return {
        "win_a": win_a,
        "draw": draw,
        "win_b": win_b,
        "over_2_5": over_25,
        "under_2_5": 1 - over_25,
        "btts": btts,
    }


def direction_score(score: ScoreProb, summary: dict) -> float:
    if score.score_a > score.score_b:
        return summary["win_a"]
    if score.score_a < score.score_b:
        return summary["win_b"]
    return summary["draw"]


def choose_representative_score(scores: list[ScoreProb], lambda_a: float, lambda_b: float, summary: dict) -> ScoreProb:
    total_xg = lambda_a + lambda_b
    expected_margin = lambda_a - lambda_b
    top_prob = max(s.probability for s in scores)

    best: tuple[float, ScoreProb] | None = None
    for s in scores:
        if s.score_a > 5 or s.score_b > 5:
            continue

        # Start with normalized probability, but do not let it dominate.
        score = 0.48 * (s.probability / top_prob)

        # Match the model's direction and likely margin.
        score += 0.22 * direction_score(s, summary)
        margin_error = abs(s.margin - expected_margin)
        score += 0.13 * max(0.0, 1.0 - margin_error / 3.0)

        # Match total expected goals. This prevents automatic low-score collapse.
        total_error = abs(s.total - total_xg)
        score += 0.22 * max(0.0, 1.0 - total_error / 3.0)

        # Respect over/under and both-teams-to-score signals.
        if summary["over_2_5"] >= 0.52 and s.total >= 3:
            score += 0.12
        if summary["over_2_5"] <= 0.42 and s.total <= 2:
            score += 0.08
        if summary["btts"] >= 0.55 and s.btts:
            score += 0.10
        if summary["btts"] <= 0.45 and not s.btts:
            score += 0.06

        # Strong favorites should not default to 1-0 if their xG is high.
        if abs(expected_margin) >= 0.75:
            favored_goals = s.score_a if expected_margin > 0 else s.score_b
            if favored_goals >= 2:
                score += 0.10
            if favored_goals <= 1 and total_xg >= 2.7:
                score -= 0.12

        # Penalize very low scores in open games unless the distribution demands it.
        if total_xg >= 2.7 and s.total <= 1:
            score -= 0.20
        if total_xg >= 2.9 and s.total == 2 and summary["over_2_5"] >= 0.52:
            score -= 0.07

        # Avoid unrealistic shootouts unless expected goals are high.
        if total_xg < 2.6 and s.total >= 4:
            score -= 0.10
        if total_xg < 2.3 and s.total >= 3:
            score -= 0.10

        if best is None or score > best[0]:
            best = (score, s)

    assert best is not None
    return best[1]


def predict(lambda_a: float, lambda_b: float, max_goals: int = 6) -> dict:
    scores = build_distribution(lambda_a, lambda_b, max_goals)
    summary = summarize(scores)
    chosen = choose_representative_score(scores, lambda_a, lambda_b, summary)
    scores.sort(key=lambda item: item.probability, reverse=True)
    return {
        "score": f"{chosen.score_a}-{chosen.score_b}",
        "score_probability": chosen.probability,
        "top_poisson_score": f"{scores[0].score_a}-{scores[0].score_b}",
        "top_poisson_probability": scores[0].probability,
        **summary,
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
    print(f"Poisson最高单格：{result['top_poisson_score']} ({pct(result['top_poisson_probability'])})")


if __name__ == "__main__":
    main()
