# Active compliance state

## Purpose
Track the fishing-relevant consequences of currently verified rules during an active trip without becoming legal, navigation or emergency authority.

## Inputs
A `ComplianceState` may use:
- applicable jurisdiction/water regime;
- current official species/method/season/area rules;
- licence/permit state supplied or verified for the trip;
- protected/closed-area geometry;
- current position only when actually available with usable precision;
- accepted kept-catch records;
- fisher/crew count when actually supplied and relevant to a rule.

## Derived states
For each consequential rule return `CLEAR | APPROACHING_LIMIT | AT_LIMIT | EXCEEDED | UNKNOWN | STALE | NOT_APPLICABLE` plus the authoritative rule/source ref and checked-at/effective state.

Do not calculate a possession/bag-limit status when species identity, applicable rule, fisher count or kept-catch count is materially unresolved.

## Spatial compliance
Zone proximity or inside/outside assessment requires actual position source context, usable accuracy and authoritative geometry. Without those, return `UNKNOWN`; do not infer position from the planned route or a saved mark.

Background geofence alerts are a companion-app capability only when the actual app runtime/permissions are present. The plugin itself does not claim continuous monitoring.

## Replanning
A newly failed or unresolved hard legal/access constraint may trigger ordinary replan admission. Compliance state does not label the trip safe or replace official advice/enforcement.
