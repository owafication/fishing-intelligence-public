# Planning kernel

## Admission before optimisation
Candidate -> jurisdiction/water regime -> legal/rules -> licence/permit -> protected-area overlays -> access -> time -> vessel/range -> user operating limits -> critical-data availability -> admitted plan.

Only admitted plans are compared. A fishing-quality preference never overrides a failed hard constraint.

## Regional readiness
Resolve the regional pack before claiming plan depth. `REFERENCE_READY` supports rule/licence verification only; `PLANNING_READY` supports operational plan construction subject to current dependencies; `PROSPECT_READY` additionally supports evidence-bounded generated search areas.

## Readiness
Classify the overall plan `READY_TO_USE | PROVISIONAL | RESEARCH_ONLY | BLOCKED`. Readiness is not a safety rating.

## Unresolved objective/target
Do not silently choose a target species. Return materially different target-family options or keep the plan explicitly general until target intent is established.

## Plan comparison
Return up to three materially distinct admitted plans. Expose viability, advantages, trade-offs, uncertainties, invalidation/recheck conditions and material evidence. Do not generate one pseudo-precise best-plan score or use safe/safer labels.

## Prospects and location types
Use `OFFICIAL_LOCATION | USER_MARK | GENERATED_PROSPECT`. Preserve hypothesis state, source resolution, output precision and `navigation_suitable=false` where applicable.

## Tide/current separation
Tide prediction, current observation/model and flow inference are separate objects. Tide phase alone does not establish site-specific current speed/direction.

## Road-origin precision
Broad origins do not justify exact road departure times.

## Abandon/replan conditions
Every complete plan identifies the main conditions that invalidate it or require re-verification.

## Known marks and exploration
For `USER_MARK` options, use `mark-intelligence.md`: effort-normalised personal evidence, context similarity, recency/freshness and unknowns. Catch count alone does not rank a mark. A strong historical mark does not automatically remove a materially different `GENERATED_PROSPECT` exploration option.


## Complete response execution

For a consequential full plan, follow `complete-plan-contract.md`. Readiness and known/unknown constraints precede the detailed itinerary. A valid plan is not complete merely because good fishing options were identified.


## Authority applicability invariant

Before readiness or option ranking, apply `authority-applicability.md` to consequential authority observations. Discovery alone is insufficient. Readiness considers only REQUIRED dependencies and triggered CONDITIONAL dependencies; NOT_APPLICABLE evidence cannot downgrade an option. Material UNRESOLVED legal/safety/navigation/access applicability must remain visible and may withhold the affected option.

When options differ materially in travel, towing or access timing, apply `travel-logistics-contract.md` before ranking them.
