# Prospect attempt and effort contract

## ProspectAttempt
A `PROSPECT_ATTEMPT` represents one bounded fishing attempt at a prospect/location/method. Fields include stable ID, session ref, optional prospect/location refs, start/end precision, target species, method, outcome, move-on reason, privacy and version.

## Attempt outcomes
`NOT_RECORDED | BLANK | CATCH | INTERRUPTED | UNKNOWN`.
A session can be `MIXED` when different attempts have different outcomes.

## Blank rule
Classify an attempt `BLANK` only when:
1. positive fishing effort is recorded as exact or estimated, and
2. zero accepted catch observations link to that attempt.
If effort is unknown, use `UNKNOWN`/`NOT_RECORDED`, not `BLANK`.

## Effort
Effort may include duration minutes, casts, trolling minutes, bait-soak minutes or another declared measure. Every value has quality `EXACT | ESTIMATED | UNKNOWN`. Missing is not zero.

## Move-on evidence
`move_on_reason` records what ended the attempt (planned time, conditions, no response, target achieved, equipment issue, etc.) as an observation/user report. It is not automatically evidence that the location is poor.

Invariant: `BLANK requires positive` exact/estimated fishing effort and zero accepted catches.

## Line-hours and performance metrics
When line exposure is actually known, effort may include active line-minutes/line-hours in addition to duration. Do not derive line-hours from crew count alone. Personal rate metrics follow `personal-performance-metrics.md`.
