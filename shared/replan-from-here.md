# Replan from here handoff

`REPLAN_REQUEST` packages a bounded current-state snapshot for `fishing-replanner`. It may include current time, GPS/user-reported position, completed attempts, catch/blank outcomes, remaining fuel if actually known, changed objective and app-visible source freshness.

The app does not calculate or as accepted accept a replacement trip itself. Fishing Intelligence resolves the base version, refreshes critical dependencies when possible, re-runs remaining-option admission and returns the replan result.

If offline, the request can remain queued. The UI must not present a queued/unprocessed request as an accepted replan.
