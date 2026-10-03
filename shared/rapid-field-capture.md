# Rapid field capture contract

## Purpose
Preserve high-value fishing evidence immediately when the user is busy, wet-handed, offline or in a fast bite, then enrich it later without changing what was originally observed.

## Capture-first rule
A field action should keep the smallest truthful event before asking for optional detail. Required information for a time-sensitive catch is limited to the event identity, trip/session/attempt context when known, observed time, outcome/count, source context and privacy.

Optional details such as species, fisher, length, weight, lure, method, photo, bottom type and notes may be attached later as a version or enrichment. Deferred detail must never replace or sharpen the original observed time, position or source context without evidence.

## Burst capture
`RECORD_CATCH_BURST` is a derived field envelope for a fast sequence of catches.

It may contain:
- positive integer `count`;
- one observed time or bounded observed-time range;
- optional fisher/team attribution;
- optional common species/method/location context;
- optional per-catch exceptions.

On acceptance it expands to distinct accepted `CATCH` records with stable IDs. The burst envelope itself is retained as source context. Do not create one accepted catch with `quantity > 1` when individual catches are required for limits, personal bests or later correction.

## Unknowns
Unknown species remains unknown. Missing length/weight is not zero. A suggested species from image analysis stays proposed until accepted under the species-identification contract.

## Interaction objective
Prefer one or two short actions over a complete form. In chat, compact statements such as `3 barra released, same spot` may create a burst candidate when trip context is unambiguous; otherwise preserve the ambiguity rather than inventing fields.
