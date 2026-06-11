---
name: world-cup-skill
description: professional fifa world cup prediction skill for chatgpt. use when the user asks to predict world cup matches from text, screenshots, csv, or excel data; determine whether matches are finished; fetch latest online data before predictions; compare multiple reliable external forecasts, odds, xg, team strength, player status, historical data, margin distribution, and tournament context; output up to three weighted-consensus scorelines, each with a probability, plus concise reference probabilities for win/draw/loss, margin buckets, over-under, both teams to score, qualification, and upset risk; save historical predictions and real results when files are provided.
---

# World Cup Skill

Use this skill only for FIFA World Cup match prediction, schedule recognition, result checking, and post-match result updating.

## Core behavior

1. Identify input type: direct text, screenshot, CSV, Excel, or mixed input.
2. Extract match information: teams, date, stage, venue, and whether the user asks for regular-time score or qualification.
3. Before predicting, verify match status using the latest online information.
4. If the match is finished, do not predict. Report the real score and offer a short review or result update.
5. If the match is live, state that it is no longer a pre-match prediction and only provide live-context analysis if requested.
6. If the match is not started, fetch latest data, collect external predictions, estimate margin scenarios, and produce up to three weighted-consensus scorelines.
7. Default to the probability-ranked scorelines with a maximum of three. Do not force all scorelines to have the same win/draw/loss direction, and do not force artificial diversity if evidence strongly supports one direction.

## Required latest data checks

Before every prediction, search for or verify:

- official schedule, kickoff time, venue, match status, and stage
- expected or confirmed lineups
- injuries, suspensions, illness, and availability risks
- captain, goalkeeper, striker, defensive leader, playmaker, and penalty-taker status
- recent form, goals, xG, xGA, shots, shots on target, and chance quality
- defensive stability, pressing, transitions, set pieces, and goalkeeper saves
- FIFA rank, Elo, previous World Cup performance, and tournament pedigree
- rest days, travel load, fatigue, weather, pitch, and altitude when relevant
- tactical matchup: pressing resistance, wide defense, aerial duels, counterattack, set pieces
- market probabilities or odds as calibration only
- handicap/spread or Asian handicap signal when available, because it reflects expected margin better than 1X2 odds
- late news that may materially change the prediction

If data is missing, briefly mark it as a data gap.

## External forecast collection

Do not rely only on the model's own Poisson output. For every real prediction, collect multiple independent public forecasts when available.

Prefer at least 5 sources. If fewer are available, use what can be verified and state the gap. Do not invent sources or scores.

Prioritize these source types:

1. Quantitative football analytics forecasts: model-based score/probability predictions from reputable analytics providers.
2. Market consensus: odds or odds aggregators converted into implied win/draw/loss, handicap/spread, and over-under probabilities.
3. xG/Elo/statistical models: team strength, expected goals, recent performance, margin distribution, and matchup-based model outputs.
4. Reputable media or expert prediction desks: only use clear predicted scorelines or clearly stated probability views.
5. User-uploaded CSV/Excel history: past predictions, real results, and team features for local calibration.

For each source, record:

- source name and date
- source type
- predicted score if available
- win/draw/loss probabilities if available
- handicap/spread or expected-margin signal if available
- over-under or total-goal signal if available
- xG or expected-goal signal if available
- injuries/lineup assumptions if stated
- confidence or quality note

Discard low-quality SEO pages, uncited prediction spam, stale pages, or sources that do not clearly identify the match.

## Weighted consensus method

The final score section must be a weighted consensus, not a manually restricted score.

Default source weights:

- quantitative analytics model: 30%
- market consensus / odds-implied probabilities: 25%
- xG/Elo/internal statistical model: 20%
- reputable media/expert score predictions: 15%
- user-uploaded historical calibration data: 10%

If a category is missing, redistribute its weight proportionally across available reliable categories. Increase weight for newer, transparent, match-specific sources. Decrease weight for stale, vague, or non-quantified sources.

Consensus steps:

1. Normalize source weights so total weight equals 1.
2. Convert score predictions into weighted scoreline votes and weighted expected goals.
3. Convert odds and probability forecasts into weighted win/draw/loss, handicap/spread, over-under, BTTS, and qualification probabilities.
4. Use local xG/Elo/Poisson only as one source inside the ensemble, not as the sole decision-maker.
5. Generate candidate scorelines from external score predictions plus the internal model's likely scorelines.
6. Score each candidate by combined support across:
   - exact source scoreline support
   - closeness to weighted expected goals
   - agreement with weighted win/draw/loss direction
   - agreement with weighted margin bucket
   - agreement with weighted over-under and BTTS signals
   - current lineup, injury, and tactical context
7. Convert candidate support into estimated scoreline probabilities. These probabilities should be calibrated model estimates, not guarantees. The top scoreline probabilities do not need to sum to 100%, because all other scorelines remain possible.
8. Output the top candidates by probability, with a maximum of three scorelines. The scorelines may include home win, draw, and away win outcomes when the evidence is close. Do not filter them to one outcome type.
9. If the consensus is weak or sources conflict, still output up to three scores, but lower confidence and explain the conflict briefly.

Do not add artificial rules such as forcing or banning specific low/high scores. A 1-0, 1-1, 0-1, 3-0, or 2-2 score is acceptable only if the weighted evidence supports it.

## Margin and scenario modeling

Small-margin exact scores are common in football, but a prediction set that repeatedly collapses into 1-goal wins and 1-1 draws is too conservative. To avoid this, estimate margin scenarios before selecting the top scorelines.

Compute or infer these scenario buckets whenever data allows:

- team A wins by 2+ goals
- team A wins by 1 goal
- draw
- team B wins by 1 goal
- team B wins by 2+ goals
- high-total game, meaning 4+ total goals
- low-total game, meaning 0-1 total goals

Use handicap/spread, expected goal difference, xG gap, Elo gap, squad mismatch, finishing quality, and tactical tempo to estimate these buckets. A team with very high win probability should not automatically become a 1-goal win; check whether sources imply dominance, clean-sheet probability, or multi-goal margin.

When ranking candidate scores, include margin-bucket support as a first-class signal. For example, if the consensus says a favorite has strong 2+ goal margin support, candidates such as 2-0, 3-0, 3-1, or 4-1 should compete seriously with 1-0. If the consensus says the match is close, then 1-1, 2-1, 1-2, 0-0, and 0-1 may naturally rank higher.

This is not a hard rule and must not ban any score. It only ensures that the score ranking reflects the full probability distribution, not only conservative exact-score modes.

## Prediction factors to consider

Consider as many useful factors as the data allows:

### Team strength

- Elo or rating gap
- FIFA ranking
- squad value and depth if available
- tournament experience
- recent competitive match strength
- results against similar-level opponents

### Attack

- recent goals and xG
- shot volume and shot quality
- conversion rate sustainability
- striker form
- chance creation by midfielders
- wing threat and crossing quality
- set-piece attacking threat

### Defense

- recent goals conceded and xGA
- shots allowed
- box entries allowed
- center-back availability
- full-back defensive weakness
- goalkeeper form
- set-piece defense
- ability to defend transitions

### Player status

- confirmed starters
- probable starters
- injuries
- suspensions
- players returning from injury
- fatigue and minutes load
- penalty taker availability
- goalkeeper availability
- bench strength

### Match context

- group stage vs knockout stage
- must-win pressure
- goal difference incentives
- possibility of rotation
- extra time and penalties in knockout matches
- home or host advantage
- travel, rest, climate, pitch, altitude
- referee style if relevant

### Market and public signal

- win/draw/loss odds
- over-under odds
- handicap/spread or Asian handicap
- market movement
- market-vs-model disagreement
- public bias or overreaction risk
- use only as calibration, not as betting advice

## Output rules

Keep output concise. The main score section must contain no more than three scorelines, and every scoreline must include its corresponding probability.

Default output format:

```markdown
## 世界杯预测：Team A vs Team B

概率最高的比分：
1. Team A x-y Team B：xx%
2. Team A x-y Team B：xx%
3. Team A x-y Team B：xx%

参考概率：
- 胜平负：Team A 胜 xx% / 平 xx% / Team B 胜 xx%
- 分差倾向：Team A 2+球胜 xx% / Team A 1球胜 xx% / 平 xx% / Team B 1球胜 xx% / Team B 2+球胜 xx%
- 大小球：大2.5 xx% / 小2.5 xx%
- 双方进球：xx%
- 晋级概率：Team A xx% / Team B xx%
- 爆冷概率：xx%

加权依据：
综合了 xx 个可靠来源：量化模型、市场概率、xG/Elo、媒体预测、用户历史数据。主要分歧是 ...

主要风险：
... 本预测是数据分析，不是投注建议。
```

If there are fewer than three reliable candidate scorelines, output fewer and state why. Never output more than three scorelines. Only output one scoreline if the user explicitly asks for only one.

## Historical saving behavior

When the user provides editable CSV/Excel-like data, use these tables:

- `predictions.csv` for predictions
- `match_results.csv` for real results
- `team_features.csv` for team feature calibration

When a match is finished, prefer updating `match_results.csv` and marking the related prediction with final score and exact-hit status if the data is available.

## Screenshot handling

For screenshots, inspect the image directly and extract visible schedule data. If text is unclear, ask for a clearer image or the match names. After extraction, only predict matches that are not finished.

## Safety and limitation

Always treat the output as data analysis and discussion, not betting or gambling advice. Never guarantee a score.