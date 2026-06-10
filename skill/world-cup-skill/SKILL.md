---
name: world-cup-skill
description: professional fifa world cup prediction skill for chatgpt. use when the user asks to predict world cup matches from text, screenshots, csv, or excel data; determine whether matches are finished; fetch latest online data before predictions; compare multiple reliable external forecasts, odds, xg, team strength, player status, historical data, and tournament context; output one weighted-consensus predicted score plus concise reference probabilities for win/draw/loss, over-under, both teams to score, qualification, and upset risk; save historical predictions and real results when files are provided.
---

# World Cup Skill

Use this skill only for FIFA World Cup match prediction, schedule recognition, result checking, and post-match result updating.

## Core behavior

1. Identify input type: direct text, screenshot, CSV, Excel, or mixed input.
2. Extract match information: teams, date, stage, venue, and whether the user asks for regular-time score or qualification.
3. Before predicting, verify match status using the latest online information.
4. If the match is finished, do not predict. Report the real score and offer a short review or result update.
5. If the match is live, state that it is no longer a pre-match prediction and only provide live-context analysis if requested.
6. If the match is not started, fetch latest data, collect external predictions, and produce one weighted-consensus score.
7. Default to one main scoreline only. Do not provide a long list of possible scores unless requested.

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
- late news that may materially change the prediction

If data is missing, briefly mark it as a data gap.

## External forecast collection

Do not rely only on the model's own Poisson output. For every real prediction, collect multiple independent public forecasts when available.

Prefer at least 5 sources. If fewer are available, use what can be verified and state the gap. Do not invent sources or scores.

Prioritize these source types:

1. Quantitative football analytics forecasts: model-based score/probability predictions from reputable analytics providers.
2. Market consensus: odds or odds aggregators converted into implied win/draw/loss and over-under probabilities.
3. xG/Elo/statistical models: team strength, expected goals, recent performance, and matchup-based model outputs.
4. Reputable media or expert prediction desks: only use clear predicted scorelines or clearly stated probability views.
5. User-uploaded CSV/Excel history: past predictions, real results, and team features for local calibration.

For each source, record:

- source name and date
- source type
- predicted score if available
- win/draw/loss probabilities if available
- over-under or total-goal signal if available
- xG or expected-goal signal if available
- injuries/lineup assumptions if stated
- confidence or quality note

Discard low-quality SEO pages, uncited prediction spam, stale pages, or sources that do not clearly identify the match.

## Weighted consensus method

The final score must be a weighted consensus, not a manually restricted score.

Default source weights:

- quantitative analytics model: 30%
- market consensus / odds-implied probabilities: 25%
- xG/Elo/internal statistical model: 20%
- reputable media/expert score predictions: 15%
- user-uploaded historical calibration data: 10%

If a category is missing, redistribute its weight proportionally across available reliable categories. Increase weight for newer, transparent, match-specific sources. Decrease weight for stale, vague, or non-quantified sources.

Consensus steps:

1. Normalize source weights so total weight equals 1.
2. Convert score predictions into weighted expected goals and weighted scoreline votes.
3. Convert odds and probability forecasts into weighted win/draw/loss, over-under, BTTS, and qualification probabilities.
4. Use local xG/Elo/Poisson only as one source inside the ensemble, not as the sole decision-maker.
5. Generate candidate scorelines from external score predictions plus the internal model's likely scorelines.
6. Select the one scoreline with the best combined support across:
   - exact source scoreline support
   - closeness to weighted expected goals
   - agreement with weighted win/draw/loss direction
   - agreement with weighted over-under and BTTS signals
   - current lineup, injury, and tactical context
7. If the consensus is weak or sources conflict, still output one score, but lower confidence and explain the conflict briefly.

Do not add artificial rules such as forcing or banning specific low/high scores. A 1-0, 1-1, 0-1, 3-0, or 2-2 score is acceptable only if the weighted evidence supports it.

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
- market movement
- market-vs-model disagreement
- public bias or overreaction risk
- use only as calibration, not as betting advice

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

加权依据：
综合了 xx 个可靠来源：量化模型、市场概率、xG/Elo、媒体预测、用户历史数据。主要分歧是 ...

主要风险：
... 本预测是数据分析，不是投注建议。
```

When the user explicitly asks for multiple scorelines, provide no more than three possible scores. Otherwise provide only one.

## Historical saving behavior

When the user provides editable CSV/Excel-like data, use these tables:

- `predictions.csv` for predictions
- `match_results.csv` for real results
- `team_features.csv` for team feature calibration

When a match is finished, prefer updating `match_results.csv` and marking the related prediction with final score and exact-hit status if data is available.

## Screenshot handling

For screenshots, inspect the image directly and extract visible schedule data. If text is unclear, ask for a clearer image or the match names. After extraction, only predict matches that are not finished.

## Safety and limitation

Always treat the output as data analysis and discussion, not betting or gambling advice. Never guarantee a score.