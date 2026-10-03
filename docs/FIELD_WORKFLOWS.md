# Field workflows

The field model prioritises preserving time-sensitive evidence with minimal interaction, then enriching it later.

## Start an attempt

Record the attempt/prospect/location, target/method when known, observed start time and privacy. Exact location is optional; user-reported or approximate position retains its precision/source context.

## Record catches quickly

A catch event timestamps immediately. Optional details such as length, weight, lure, photo or confirmed species can be added later.

Burst input is supported for compact reports such as `3 barra released, same spot`. A positive count expands into individual catch candidates linked to the same attempt/context. Zero or negative counts fail instead of creating nonsensical records.

## Record effort and blanks

Effort can be duration, casts, trolling minutes, bait-soak minutes or another declared measure with quality `EXACT | ESTIMATED | UNKNOWN`. Ending an attempt with positive effort and no accepted catch can derive `BLANK`. Absence of a catch entry alone is not a blank.

## Context enrichment

When the host has context, an event may be enriched with GPS, tide, weather or other environmental data. Each field retains its own source, observed/issued time, capture mode, precision and freshness. Missing context stays missing.

## Move / end attempt

`MOVE` records that the angler stopped keeping at one attempt and changed area/strategy. It does not imply a precise track. End-attempt should preserve elapsed effort where possible and record the move-on reason as an observation, not proof that the location is poor.

## Offline events

Offline field events are append-oriented pending state. Sync resolves the accepted trip/version, deduplicates stable event IDs, validates privacy/parents/base version, promotes valid events through normal contracts and returns per-event results. Replaying an accepted event must not create a second catch or effort record.

## Replan from here

A replan request can include current time, completed attempts, current objective, return deadline, user/instrument position, remaining fuel if actually known, conditions and source freshness. Completed history is frozen; only the remaining future sequence changes.

## User-visible state

A companion UI should distinguish synced accepted state, pending offline events, conflicts requiring review and expired Trip Pack components. Large forms should not block preservation of a time-sensitive catch/event.
