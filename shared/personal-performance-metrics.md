# Personal performance metrics

## Purpose
Provide transparent personal fishing metrics while keeping the denominator, population and evidence quality visible.

## Supported derived metrics
- accepted catches;
- kept/released counts where recorded;
- positive-attempt rate;
- catches per line hour (`CPLH`) when line-hours are known;
- catches per fishing hour when only person/time effort is known and explicitly labelled as such;
- exposure by tide stage, season, method, prospect/location class and other supported context dimensions.

## CPLH
`CPLH = accepted catches / accepted line-hours`.

Line-hours are the sum of active line time across deployed lines when that information is actually recorded. Do not infer two line-hours merely because two people were present. If line count/exposure cannot be reconstructed, CPLH is unavailable rather than estimated from trip duration alone.

Metric quality is `EXACT | ESTIMATED | MIXED | UNAVAILABLE` and is derived from the underlying effort quality.

## Population and comparability
Every metric names its population: species/target, location or prospect scope, method, time period and material context filters. Do not compare unlike populations just because the resulting number has the same unit.

## Presentation
Do not collapse evidence into an unexplained global fishing score. Show denominator, sample size, material exclusions and coverage when a metric is used for planning or pattern claims.
