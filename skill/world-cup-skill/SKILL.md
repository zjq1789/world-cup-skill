---
name: world-cup-skill
description: professional fifa world cup prediction skill for chatgpt. use when the user asks to predict world cup matches from text, screenshots, csv, or excel data; determine whether matches are finished; fetch latest online data before predictions; combine historical data, team strength, player status, xg, odds, schedule, environment, and tournament context; output one main predicted score plus concise reference probabilities for win/draw/loss, over-under, both teams to score, qualification, and upset risk; save historical predictions and real results when files are provided.
---

# World Cup Skill

Use this skill only for FIFA World Cup match prediction, schedule recognition, result checking, and post-match result updating.

## Core behavior

1. Identify input type: direct text, screenshot, CSV, Excel, or mixed input.
2. Extract match information: teams, date, stage, venue, and whether the user asks for regular-time score or qualification.
3. Before predicting, verify match status using the latest online information.
4. If the match is finished, do not predict. Report the real score and offer a short review or result update.
5. If the match is live, state that it is no longer a pre-match prediction and only provide live-context analysis if requested.
6. If the match is not started, fetch latest data and predict.
7. Default to one main scoreline only. Do not provide a long list of possible scores unless requested.

## Required latest data checks

Before every prediction, search for or verify:

- official schedule, kickoff time, venue, match status, and stage
- expected or confirmed lineups
- injuries, suspensions, illness, and availability risks
- captain, goalkeeper, striker, defensive leader, and playmaker status
- recent form, goals, xG, xGA, shots, shots on target, and chance quality
- defensive stability, pressing, transitions, set pieces, and goalkeeper saves
- FIFA rank, Elo, previous World Cup performance, and tournament pedigree
- rest days, travel load, fatigue, weather, pitch, and altitude when relevant
- tactical matchup: pressing resistance, wide defense, aerial duels, counterattack, set pieces
- market probabilities or odds as calibration only
- late news that may materially change the prediction

If data is missing, briefly mark it as a data gap.

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
- movement in market expectations
- overreaction or public bias risk
- use only as calibration, not as betting advice

## Prediction method

Use an ensemble-style reasoning process:

1. Establish baseline strength using Elo/ranking/form.
2. Estimate expected goals for both teams using attack and defense strength.
3. Adjust expected goals using xG trend, lineup, injuries, fatigue, stage, and tactical matchup.
4. Use a Poisson-style score distribution to derive scoreline, win/draw/loss, over-under, and both-teams-to-score probabilities.
5. For knockout matches, separately consider regular-time score and qualification probability.
6. Calibrate against market signal if available, while retaining independent reasoning.
7. Select one scoreline that best balances probability, match context, and model direction.

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

When the user provides editable CSV/Excel-like data, use these tables:

- `predictions.csv` for predictions
- `match_results.csv` for real results
- `team_features.csv` for team feature calibration

When a match is finished, prefer updating `match_results.csv` and marking the related prediction with final score and exact-hit status if data is available.

## Screenshot handling

For screenshots, inspect the image directly and extract visible schedule data. If text is unclear, ask for a clearer image or the match names. After extraction, only predict matches that are not finished.

## Safety and limitation

Always treat the output as data analysis and discussion, not betting or gambling advice. Never guarantee a score.