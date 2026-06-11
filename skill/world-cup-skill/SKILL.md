---
name: world-cup-skill
description: professional FIFA World Cup prediction skill. Use for World Cup match prediction from text, screenshots, CSV, or Excel; verify match status before predicting; use fresh online data; prioritize reliable explicit scoreline forecasts, China Sports Lottery odds when available, market odds, xG/Elo/statistical models, lineup news, and user historical data; output up to three weighted scorelines with conditional probabilities, win/draw/loss probabilities, upset probability, over-under, BTTS, qualification probability, and risk notes.
---

# World Cup Skill

Use this skill only for FIFA World Cup match prediction, schedule recognition, result checking, and post-match review.

Default language: use Chinese when the user asks in Chinese.

## 1. Core task

For every unplayed World Cup match, produce:

1. up to three most likely scorelines;
2. a probability for each scoreline;
3. win/draw/loss probabilities;
4. upset probability;
5. whether each scoreline is an upset or not;
6. over/under 2.5 and both-teams-to-score probabilities;
7. qualification probability for knockout matches;
8. concise reasons and key risks.

Do not output more than three scorelines. If fewer than three reliable scoreline candidates exist, output fewer and explain why.

## 2. Input handling

Supported inputs:

- direct text: team A vs team B;
- screenshot: extract fixture, date, teams, and status;
- CSV / Excel: historical results, previous predictions, team features, or fixture lists;
- mixed inputs: combine uploaded data with online data.

Before predicting, always verify whether the match is:

- not started: predict;
- live: say it is no longer a pre-match prediction;
- finished: report the real result and do not present it as a prediction.

## 3. Data collection priority

For each match, collect the freshest reliable data available:

1. official schedule, kickoff time, venue, group/stage, and match status;
2. China Sports Lottery odds when available: win/draw/loss and handicap win/draw/loss;
3. reliable explicit online scoreline forecasts from prediction desks, data sites, media previews, or expert pages;
4. market odds / odds aggregators for win/draw/loss, handicap/spread, and over-under;
5. xG, xGA, Elo, FIFA ranking, team strength, attack/defense form;
6. lineup, injuries, suspensions, goalkeeper, striker, playmaker, and penalty-taker status;
7. rest days, travel, climate, pitch, altitude, tactical matchup, and motivation;
8. user-uploaded CSV / Excel historical data.

Do not invent sources, odds, or scorelines. If China Sports Lottery odds are unavailable, use reliable market odds as a proxy and state this data gap.

## 4. Source weighting

Use a weighted ensemble, not a single internal model.

Default weights:

- explicit online scoreline consensus: 30%;
- China Sports Lottery / market odds: 25%;
- xG / Elo / quantitative statistical model: 20%;
- lineup, injury, tactical, and match-context adjustment: 15%;
- user-uploaded historical calibration data: 10%.

If a category is missing, redistribute its weight proportionally across available reliable categories. Increase weight for recent, transparent, match-specific sources. Decrease weight for stale, vague, or low-quality sources.

Poisson or internal statistical calculations may generate scoreline candidates, but they must not be the sole decision-maker.

## 5. Upset probability

Every match must include an upset probability.

Primary reference: China Sports Lottery odds.

### 5.1 Determine the market favorite

When China Sports Lottery win/draw/loss odds are available:

1. Convert decimal odds into implied probabilities.
2. Normalize probabilities to remove bookmaker margin.
3. The outcome with the highest normalized probability is the market favorite.

Use handicap win/draw/loss odds as a secondary signal to estimate expected margin and whether the favorite is only slightly favored or strongly favored.

When China Sports Lottery odds are not available, use a reliable odds aggregator or mainstream market consensus and clearly say that it is a proxy.

### 5.2 Define upset

A scoreline is an upset if its result direction is different from the China Sports Lottery market-favorite outcome.

Examples:

- If the favorite outcome is Team A win, then draw and Team B win scorelines are upsets.
- If the favorite outcome is draw, then Team A win and Team B win scorelines are upsets.
- If there is no clear favorite, label the match as `冷门边界不明显`, but still report the probability of outcomes outside the most favored result.

### 5.3 Calculate upset probability

Default formula:

```text
爆冷概率 = 1 - P(体彩最热赛果方向)
```

Then adjust lightly using:

- handicap/spread gap;
- lineup and injury surprises;
- schedule pressure;
- market movement;
- tactical mismatch;
- recent form and xG trend.

Output both:

- `爆冷概率：xx%`;
- for each scoreline: `爆冷：是 / 否 / 边界不明显`.

## 6. Scoreline probability

For scorelines, use weighted conditional probabilities.

A scoreline probability should mean:

```text
P(该比分 | 该比分所属赛果方向成立)
```

For example, if the score is Team A 2-1 Team B, estimate the probability of 2-1 among Team A-win scenarios, after weighting external scoreline forecasts, xG/Elo model output, odds, and lineup context.

This avoids exact-score probabilities becoming unrealistically tiny and makes the score probabilities easier to compare within the same win/draw/loss direction.

If a table needs one global ranking across all scores, combine:

```text
综合比分权重 = P(赛果方向) × P(比分 | 赛果方向)
```

Then output the top three scorelines by this combined weight, while displaying the conditional score probability next to each score.

The top scoreline probabilities do not need to sum to 100%, because they are conditional probabilities and many other scorelines remain possible.

## 7. Scoreline ranking

Generate candidate scorelines from:

1. explicit online scoreline forecasts;
2. xG/Elo/statistical model candidates;
3. odds-derived goal and margin scenarios;
4. user historical data.

Rank candidates using:

- exact scoreline support from reliable external sources;
- closeness to weighted expected goals;
- agreement with win/draw/loss probabilities;
- agreement with margin buckets: Team A 2+ win, Team A 1-goal win, draw, Team B 1-goal win, Team B 2+ win;
- agreement with over-under and both-teams-to-score signals;
- lineup, injury, and tactical context.

Do not force big scores or small scores. If external evidence supports 1-0, output 1-0. If external evidence supports 3-0, output 3-0. The model should follow weighted evidence, not hard-coded score preferences.

## 8. Output format

Default output:

```markdown
## 世界杯预测：Team A vs Team B

概率最高的比分：
1. Team A x-y Team B：xx%｜爆冷：是/否/边界不明显
2. Team A x-y Team B：xx%｜爆冷：是/否/边界不明显
3. Team A x-y Team B：xx%｜爆冷：是/否/边界不明显

参考概率：
- 胜平负：Team A 胜 xx% / 平 xx% / Team B 胜 xx%
- 爆冷概率：xx%（参考：中国体彩胜平负赔率；如无则说明使用市场代理）
- 分差倾向：Team A 2+球胜 xx% / Team A 1球胜 xx% / 平 xx% / Team B 1球胜 xx% / Team B 2+球胜 xx%
- 大小球：大2.5 xx% / 小2.5 xx%
- 双方进球：xx%
- 晋级概率：Team A xx% / Team B xx%（仅淘汰赛需要）

加权依据：
简要说明使用了哪些来源：在线比分预测、中国体彩/市场赔率、xG/Elo、阵容伤病、历史数据。指出主要分歧。

主要风险：
列出 1-3 个最可能改变预测的因素。本预测是数据分析，不是投注建议。
```

When predicting many matches, use a compact table, but keep these columns:

- 比赛;
- 概率最高的比分;
- 胜平负;
- 爆冷概率;
- 大小球 / 双方进球;
- 关键依据.

The scoreline cell should contain up to three lines, each with score, probability, and upset label.

## 9. Historical saving behavior

When user-provided files are editable, use:

- `predictions.csv` for predictions;
- `match_results.csv` for real results;
- `team_features.csv` for team feature calibration.

When a match finishes, update the real score and whether Top 1, Top 3, win/draw/loss, over-under, and BTTS were correct.

## 10. Limitations

Always state that the prediction is data analysis, not betting advice. Never guarantee a score. Do not hide uncertainty or data gaps.