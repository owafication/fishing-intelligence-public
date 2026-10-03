---
name: fishing-replanner
description: Replan an active fishing trip from explicit current state. Use after a trip exists; never assume GPS, telemetry, fuel state or current conditions unless actually supplied or verified.
---

# Fishing Replanner

Follow the active-trip replanning contracts plus `../../shared/replan-from-here.md` and `../../shared/gps-field-state.md`.

Resolve the current trip state and refresh consequential current dependencies before producing a replacement future sequence. If GPS is absent, preserve user-reported position precision. Never infer fuel from GPS distance alone.

When current legal/possession/zone state can change the remaining trip, read `../../shared/active-compliance-state.md`; unresolved position/species/rule inputs stay UNKNOWN and may block only the decisions they materially affect.
