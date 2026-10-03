# Dynamic replanning contract

## Core invariant
A replan changes the **future of an active trip**, not its completed history.

A valid replan has:
- `trip_ref`
- `trip_state_version`
- current active-trip state with `observed_at`
- changed facts with source context
- completed attempt refs frozen as history
- remaining planned steps from the base version
- refreshed verification states when material
- a new candidate trip version
- a separate `ReplanEvent` explaining the delta

## Trigger states
- `NO_CHANGE`: current state does not materially change the remaining admitted sequence.
- `REPLAN_AVAILABLE`: alternatives improve fit or reflect new outcomes, but the accepted remaining sequence is still admissible.
- `REPLAN_REQUIRED`: the accepted remaining sequence is no longer admissible or cannot meet a hard constraint.
- `BLOCKED`: a required current-state or critical dependency is unavailable/conflicting such that a valid remaining plan cannot be constructed.

`REPLAN_REQUIRED` is not an emergency label.

## History
Completed attempts, catches, effort and observations remain immutable historical versions. Corrections use the ordinary evidence-correction contract; replanning itself does not edit them.

## Output
Expose:
1. trigger and reason;
2. current-state source context and important unknowns;
3. remaining-option admission changes;
4. revised sequence;
5. what was removed/retained/added and why;
6. readiness and recheck conditions.
