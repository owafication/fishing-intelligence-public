# Prospect Intelligence

## Purpose
Turn resolution-qualified spatial evidence into fishing **search areas**, never navigation instructions or catch predictions.

## Prospect pipeline
1. Resolve a source contract and dataset identity.
2. Require explicit spatial resolution/accuracy before deriving geometry. Coverage polygons without recoverable cell size are discovery-only.
3. Extract or accept structure evidence such as local relief, contour break, channel edge, intertidal drain or a documented artificial structure.
4. Classify the structure observation separately from fishing relevance.
5. Combine structure with target/species knowledge, environment and personal evidence to form a `GENERATED_PROSPECT` hypothesis.
6. Apply legal/closure exclusion overlays before a prospect can enter a trip candidate.
7. Preserve source resolution, output resolution, uncertainty, evidence class and `navigation_suitable=false`.
8. Record later fishing effort/outcomes against the prospect without silently promoting the hypothesis.

## Source hierarchy
Prefer the most specific usable source whose scope and metadata are clear:
- user-owned sounder/track/mark evidence (private by default),
- survey/grid data with explicit dataset resolution,
- regional compilation such as nthaus30 for broad terrain,
- low-tide imagery for intertidal structure reference,
- coverage polygons for discovery only.

## Fishing relevance
A geomorphic feature is not automatically a productive fishing location. Terrain/structure evidence may support `SUPPORTED` structure classification while the proposition “worth fishing for species X under condition Y” remains `HYPOTHESIS` until separately supported or observed.
