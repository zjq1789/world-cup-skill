<div align="center">

# World Cup Skill

<p align="center">
  <img src="docs/images/world-cup-hero.svg" alt="World Cup" />
</p>

> *Less guesswork, more data. Not just one scoreline — the top three most supported scores.* ⚽📊

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Standard-green)](#installation)
[![World Cup](https://img.shields.io/badge/Scope-FIFA%20World%20Cup-brightgreen)](#overview)
[![Prediction](https://img.shields.io/badge/Output-Top%203%20Scores-orange)](#examples)
[![Data](https://img.shields.io/badge/Data-Live%20Search%20%2B%20CSV%20%2F%20Excel-blue)](#data-capabilities)

<br>

**A ChatGPT Skill for FIFA World Cup score prediction: identify fixtures, verify match status, fetch fresh online data, combine historical data, and output the top three weighted-consensus scorelines.**

</div>

---

## Overview

World Cup Skill is designed for FIFA World Cup prediction workflows. It focuses on:

- fixture recognition from text, screenshots, CSV, or Excel files;
- checking whether a match is already finished before predicting;
- collecting multiple reliable forecast sources;
- combining model forecasts, odds, xG/Elo, media predictions, and user-provided historical data;
- outputting the top three most supported scorelines;
- saving predictions and real match results for later review.

This project is for sports analytics and discussion only. It is not betting advice.

---

## Examples

```text
User ❯ Predict Argentina vs France in the World Cup. Give the top three scores.

World Cup Skill ❯
## World Cup Prediction: Argentina vs France

Top three scorelines:
1. Argentina 2-1 France: 13.6%
2. Argentina 1-1 France: 12.4%
3. Argentina 1-2 France: 9.8%

Reference probabilities:
- W/D/L: Argentina 39% / Draw 28% / France 33%
- Over/Under: Over 2.5 46% / Under 2.5 54%
- Both teams to score: 52%
- Qualification: Argentina 53% / France 47%
- Upset risk: 18%
```

---

## Installation

In any Agent Skills compatible environment, ask:

```text
Install this skill: https://github.com/zjq1789/world-cup-skill
```

You can also manually copy the repository root or `skill/world-cup-skill/` into your skills directory.

---

## Core Modules

| Module | Purpose |
|---|---|
| Multimodal fixture parsing | Read matches from text, screenshots, CSV, or Excel |
| Match status check | Avoid post-match prediction and report real results |
| Latest data search | Check schedule, lineups, injuries, rankings, xG, odds |
| Forecast source collection | Use analytics models, market probabilities, xG/Elo, media predictions |
| Weighted consensus | Rank the top three scorelines by combined evidence |
| Historical tracking | Save predictions and match results for review |
| Post-match leaderboard | Track exact score, W/D/L, over-under, and BTTS accuracy |

---

## Growth Roadmap

- Daily prediction pages under `predictions/`.
- Public post-match leaderboard under `results/leaderboard.md`.
- Screenshot-to-prediction demo.
- Accuracy charts and review reports.
- Community-submitted data sources via GitHub Issues.

---

## Disclaimer

Football is highly uncertain. Red cards, penalties, injuries, weather, refereeing, and tactical changes can significantly affect outcomes. This project is for data analysis and discussion only, not betting advice.
