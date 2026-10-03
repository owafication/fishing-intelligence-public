# Compliance decision support

Fishing Intelligence can derive an **active compliance state** from current authoritative rules plus actual recorded trip/catch state. This is decision support, not legal advice, enforcement or continuous monitoring.

## Resolution order

`jurisdiction/water regime -> current rule authority -> species/method/season/area rules -> licence/permit -> protected-area overlays -> mode-specific overlays -> admission`

## Licence/permit state

A prior fishing history does not prove a current licence/permit. Relevant status remains explicit, for example verified held/not required, required but unverified, exemption unverified or unavailable.

## Possession/bag/boat projections

A projection can compare current accepted catch state against a verified applicable rule. If species identity, fisher allocation, location/jurisdiction, rule freshness or another necessary input is unresolved, the projection remains unresolved rather than inventing a remaining allowance.

## Zones and closures

A closure/zone test requires adequate position/geometry and current authoritative zone/rule data. Missing current position does not justify a zone-clear result. A newly failed/unresolved hard constraint can trigger ordinary replan admission.

## No background-monitoring claim

The core skills plugin does not continuously watch location/rules in the background. It evaluates the current inputs available when invoked.
