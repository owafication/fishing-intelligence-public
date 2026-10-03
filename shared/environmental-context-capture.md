# Environmental context capture

Fishing observations may reference environmental context, but capture timing matters.

## Capture modes
`CONTEMPORANEOUS_USER | CONTEMPORANEOUS_INSTRUMENT | RETROSPECTIVE_USER | RETROSPECTIVE_SOURCE_RECONSTRUCTION | IMPORT`.

Keep capture mode separate from evidence class. An official historical observation can be `AUTHORITATIVE` while still being a retrospective reconstruction attached after the trip.

## Precision
Timestamp precision: `EXACT | APPROXIMATE | DATE_ONLY | UNKNOWN`. Location precision must likewise reflect what was actually known. Do not backfill exact tide/weather/current from memory.

## Source reconstruction
If historical environmental data are retrieved later, retain source ID, checked/retrieved time, observation/model time, and uncertainty. Do not represent reconstructed conditions as the angler's direct observation.

## Event enrichment
For automatic per-event capture and offline/backfill semantics, follow `event-context-enrichment.md`. Context may be partial and every field retains its own source/freshness.
