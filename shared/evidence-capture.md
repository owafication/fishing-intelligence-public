# Fishing activity capture

Record fishing activity without silently turning individual observations into general patterns.

Suggested hierarchy: `FishingTrip -> FishingSession -> ProspectAttempt -> Effort / Catch / Observation / EquipmentUse`.

- A catch is an observed event, not a pattern.
- A blank requires actual fishing effort, not merely the absence of a catch record.
- Unknown effort stays unknown.
- Recollection can be recorded with reduced time/location precision.
- Later-added environmental context must be labelled as reconstructed/source-supplied rather than direct contemporaneous observation.
- Corrections should be explicit.
- Location-sensitive records are private by default.
