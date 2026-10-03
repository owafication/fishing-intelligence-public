# Jurisdiction and regional pack contract

A regional/jurisdiction pack adapts the common Fishing Intelligence kernel to one bounded place, legal/authority stack and water regime. It does not fork the planner.

A pack declares:
- geographic/water-regime scope;
- applicable authority layers;
- source contracts by authority domain;
- fisheries/licence/permit model;
- closures/protected/special-area overlays;
- access and mode-specific operational overlays;
- navigation/safety/environment/tide or water-level authority where applicable;
- species/taxonomy assumptions;
- unit/timezone/datum handling;
- source freshness/failure/reuse status;
- pack source context and readiness.

Packs may be `CURATED` or `GENERATED_PROVISIONAL`; both use the same common planner/admission contracts. Generated packs never self-promote to curated source.

Readiness uses `REFERENCE_READY | PLANNING_READY | PROSPECT_READY | INSUFFICIENT`.
