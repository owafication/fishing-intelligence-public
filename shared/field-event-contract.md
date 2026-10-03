# Field event contract

Offline capture uses append-oriented events.

Every event has:
- stable `event_id` and `device_id`;
- `trip_ref` and current trip version when known;
- monotonically increasing local sequence per device;
- `event_type`;
- `observed_at`;
- source context and privacy;
- bounded payload;
- sync state `PENDING | ACCEPTED | REJECTED | CONFLICT | DUPLICATE`.

Initial event types:
`START_ATTEMPT | RECORD_CATCH | END_ATTEMPT | MOVE | NOTE | GPS_SAMPLE | FUEL_UPDATE | OBJECTIVE_CHANGE | REPLAN_REQUEST`.

There is deliberately no one-tap accepted `BLANK` event. A blank is derived when an accepted attempt ends with positive known/estimated effort and zero accepted catches.

`MOVE` records that the angler stopped keeping at one attempt and changed area/strategy; it does not imply a precise track unless GPS/track data actually exist.

## v0.14 rapid capture extension
Add derived `RECORD_CATCH_BURST` and `CONTEXT_SNAPSHOT` event envelopes. A burst expands to distinct accepted catches under `rapid-field-capture.md`; a context snapshot follows `event-context-enrichment.md`. Replaying either envelope remains idempotent.
