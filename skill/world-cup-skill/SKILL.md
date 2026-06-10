---
name: world-cup-skill
description: professional world cup match score prediction skill for chatgpt. use when the user asks to predict fifa world cup matches from text, screenshots, csv, or excel data; determine whether matches are already finished; fetch the latest online data before predictions; output one main predicted score plus concise reference probabilities for win/draw/loss, over-under, both teams to score, qualification, and upset risk; save historical predictions and real results when files are provided.
---

# World Cup Skill

Use this skill only for FIFA World Cup match prediction and related result review.

## Core behavior

1. Identify the input type: direct text, screenshot, CSV, Excel, or mixed input.
2. Extract match information: teams, date, tournament stage, and whether the request concerns regular time or qualification.
3. Before predicting, verify match status using the latest online information.
4. If the match is finished, do not predict. Report the real score and offer a short review or result update.
5. If the match is live, say it is not a pre-match prediction and provide only live-context analysis if requested.
6. If the match is not started, fetch latest data and predict.

## Required data checks before prediction

Use online sources when available to check:

- official schedule and match status
- latest injuries and suspensions
- probable or confirmed lineup
- recent team form
- ranking or Elo strength
- goals, xG, xGA, shots, and defensive indicators
- venue, travel, rest days, weather if relevant
- market probabilities or odds only as calibration, never as betting advice

If some data cannot be found, state the gap briefly.

## Prediction method

Use an ensemble-style reasoning process:

- Elo or ranking strength for baseline win/draw/loss direction
- Poisson score distribution for scoreline and over-under
- xG and recent form for attack/defense correction
- lineup, injuries, fatigue, and key-player status for final adjustment
- market signal for calibration only

## Output rules

Keep output concise. The main output must be one scoreline.

Default output format:

```markdown
## 世界杯预测：Team A vs Team B

主预测比分：Team A x-y Team B

参考概率：
- 胜平负：Team A 胜 xx% / 平 xx% / Team B 胜 xx%
- 大小球：大2.5 xx% / 小2.5 xx%
- 双方进球：xx%
- 晋级概率：Team A xx% / Team B xx%
- 爆冷概率：xx%

简要依据：
...

主要风险：
... 本预测是数据分析，不是投注建议。
```

When the user explicitly asks for multiple scorelines, provide no more than three possible scores. Otherwise provide only one.

## Historical saving behavior

When the user provides writable or editable CSV/Excel-like data, use these tables:

- `predictions.csv` for predictions
- `match_results.csv` for real results
- `team_features.csv` for team feature calibration

When a match is finished, prefer updating `match_results.csv` and marking the related prediction with final score and exact-hit status if the data is available.

## Screenshot handling

For screenshots, inspect the image directly and extract visible schedule data. If text is unclear, ask for a clearer image or the match names. After extraction, only predict matches that are not finished.

## Safety and limitation

Always treat the output as data analysis and discussion, not betting or gambling advice. Never guarantee a score.