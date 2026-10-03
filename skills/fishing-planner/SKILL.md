---
name: fishing-planner
description: Plan or compare fishing opportunities worldwide from verified constraints, regional authority packs, fishing-mode overlays, prospect evidence and accepted personal history. Use for pre-trip, guide-context and fishing-travel planning; hand active-trip changes to fishing-replanner.
---

# Fishing Planner

## Mandatory boot sequence

Before consequential options, read/apply:
1. `../../shared/plan-input-matrix.md`
2. `../../shared/planning-kernel.md`
3. `../../shared/admission-engine.md`
4. `../../shared/plan-readiness.md`
5. `../../shared/complete-plan-contract.md`
6. `../../shared/vessel-capability.md`
7. `../../shared/fishing-mode-contract.md`
8. `../../shared/authority-applicability.md`
9. `../../shared/travel-logistics-contract.md`
10. `../../shared/regional-pack-readiness.md`
11. `../../shared/public-response-boundary.md`
12. resolve regional authority context through `regional-pack-resolver` (which may trigger `regional-pack-generator`).

Deep shipped packs may be used directly when adequate. No-country/no-pack is not a generic fallback: generate a bounded provisional authority pack when current source access permits.

## Planning discipline

Admission happens before fishing-quality comparison. Translate supplied facts into operational consequences; preserve unknown fuel/range, crew, communications, navigation/safety equipment and user operating limits. Do not describe a vessel as `suitable`, `capable`, `appropriate`, `safe` or equivalent merely from hull length, engine horsepower or appearance.

Construct each option with enough scope to test authority applicability: area/route/access point, water regime, mode, date/time and species/method where material. Select environmental forecast context from that option's fishing area **and water regime**. A discovered source or nearby restriction does not apply until its option-scoped applicability is established. Tide prediction is not site-specific current/flow. Exact access/navigation conclusions must use source/datum precision allowed by the resolved regional source contract.

For powered/route-based boating plans, require the authority pack to cover applicable `BOATING_SAFETY` and `NAVIGATION_NOTICES` domains and resolve route/overlay intersection. `NOT_APPLICABLE` evidence does not lower readiness; material `UNRESOLVED` applicability can withhold the affected option. Resolve what is legally required separately from whether the user has/does it. For species-sensitive rules, resolve taxon strongly enough to bind the rule.

When options differ materially in travel/towing/access timing or setup burden, apply `travel-logistics-contract.md` and show the trade-off. Do not let a farther option win solely on fishing quality while hiding material travel time or access logistics. If unknown travel/setup time could consume the available fishing window or breach a hard return limit, withhold the affected option until resolved.

For known marks use `../../shared/mark-intelligence.md`, `../../shared/personal-performance-metrics.md` and `../../shared/context-similarity.md`. For generated prospects preserve source resolution and `navigation_suitable=false`.

## Complete-plan output

Use sections in this order:
1. `READINESS`
2. `KNOWN / USER LIMITS / UNKNOWNS`
3. `OPTIONS`
4. `VERIFICATION`
5. `ITINERARY`
6. `RECHECK / ABANDON CONDITIONS`

Readiness must be exactly `READY_TO_USE | PROVISIONAL | RESEARCH_ONLY | BLOCKED`.

Evidence class (`AUTHORITATIVE | OBSERVED | SUPPORTED | HYPOTHESIS`) is not verification state (`VERIFIED_CURRENT | VERIFIED_AS_OF | STALE | CONFLICTING | UNAVAILABLE | NOT_REQUIRED`), and applicability (`REQUIRED | CONDITIONAL | NOT_APPLICABLE | UNRESOLVED`) is a third independent dimension.

For each critical dependency, the user-visible `VERIFICATION` section must expose these fields separately: `Dependency | Source/provider | Evidence class | Verification state | Applicability | Consequence`. Use the defined values from `complete-plan-contract.md`. Do not collapse them into combined cells such as `AUTHORITATIVE / VERIFIED_CURRENT`, a generic `State` field, or free-form prose like `Applicable if...` in place of the accepted applicability value. Include freshness/`checked_at` and scope where available and material.

A mapped/listed launch, route or fishing alternative must surface any known material **applicable** access/navigation restriction alongside it. Nearby non-intersecting restrictions may be contextual, but must not be presented as if they govern the route.

Ordinary fishing answers must not expose internal plugin/skill/file/provider/development machinery. If an internal path fails, report only the user-relevant unavailable/unverified dependency and its consequence.

When a trip is active and material state changes, hand ownership to `fishing-replanner`.
