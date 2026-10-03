# Personal learning

Fishing Intelligence learns from **accepted fishing evidence**, not catch counts alone.

## Denominator first

`ProspectAttempt` and recorded effort are the preferred denominator. A condition that appears in many catches is not automatically advantageous if most fishing effort also occurred under that condition.

## Performance metrics

CPLH and similar metrics are available only when the denominator is valid. Metric quality follows denominator quality (`EXACT`, `ESTIMATED` or `MIXED` as applicable). Unknown or non-positive line hours do not produce a numeric CPLH.

## Comparable population

Every pattern names its population: target/species scope, location/prospect class, method, time period and material context dimensions. Unlike fishing is not pooled merely because records share a species label.

## Context similarity

Similarity is explainable by dimension—such as target, season, tide, time/daylight, wind, temperature, depth, structure, method and presentation—not one opaque score. Missing dimensions remain `UNKNOWN`.

## Private mark intelligence

Marks are compared using context fit, evidence quality, effort-normalised outcome and freshness. Blanks and unsuccessful effort remain evidence. Catch totals alone do not rank a mark.

The reference implementation uses a transparent lexicographic comparison rather than a hidden global weighting formula.

## Hypotheses and experiments

When evidence is insufficient to distinguish explanations, the analyst can propose a bounded experiment. The experiment states the hypothesis, material confounders and what observation would be informative. It does not present a suggested test as causal proof.
