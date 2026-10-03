# Event context enrichment

## Purpose
Attach useful environmental and positional context to fishing events without confusing model/prediction data with direct observations.

## Context envelope
A catch, effort segment, attempt start/end, move or note may reference a `ContextSnapshot` containing only actually available fields such as:
- event time and precision;
- position and accuracy/source;
- tide prediction and station/datum;
- observed water level where available;
- wind/gust/wave/swell/pressure observations or forecasts;
- moon/daylight state;
- water temperature or current observations when actually sourced;
- source IDs, issue/observation times, retrieval time and freshness.

Each field keeps its own source context. A single snapshot may therefore mix `CONTEMPORANEOUS_INSTRUMENT`, `CONTEMPORANEOUS_USER`, provider forecast and unknown values.

## Offline behaviour
Capture available local/instrument context immediately. Network-dependent enrichment may remain `PENDING_ENRICHMENT`.

When historical provider data are attached after connectivity returns, mark them `RETROSPECTIVE_SOURCE_RECONSTRUCTION`; never rewrite them as contemporaneous observations merely because their timestamp matches the event.

## Separation rules
- Tide prediction is not observed water level.
- Tide phase is not local current speed/direction.
- Forecast is not observation.
- Device GPS is not a planned waypoint.
- Missing data remains unavailable/unknown; do not synthesize a complete context envelope.
