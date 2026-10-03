---
name: regional-pack-generator
description: Generate a provisional regional fishing authority pack on demand when no adequate curated pack exists. Uses current official sources, coverage/freshness/conflict checks and never self-promotes generated material into a curated permanent pack.
---

# Regional Pack Generator

Read `../../shared/generated-regional-pack-contract.md`, `../../shared/global-authority-stack.md`, `../../shared/authority-applicability.md`, `../../shared/source-contract-registry.md`, `../../shared/authority-evidence.md`, `../../shared/species-taxonomy-resolution.md`, `../../shared/units-time-datum-contract.md`, `../../shared/navigation-notice-resolution.md`, `../../shared/operational-requirements.md`, and `../../shared/public-response-boundary.md`.

## Generate

1. Accept the resolved place/water regime/mode/date/method/target context from `regional-pack-resolver`.
2. Determine required vs conditional authority domains using `global-authority-stack.md`.
3. Discover primary/official authorities for each required domain. Resolve national/federal, state/province/region, local/special-area and facility overlays, then classify each consequential source/constraint against the exact option as `REQUIRED | CONDITIONAL | NOT_APPLICABLE | UNRESOLVED`.
4. For boat/route plans include `BOATING_SAFETY` requirements and current `NAVIGATION_NOTICES` / temporary route restrictions. Resolve route/overlay intersection rather than treating nearby notices as applicable. For shore/land access resolve applicable access/tenure constraints instead.
5. Resolve target taxon when common-name ambiguity can change legal applicability.
6. Normalize timezone/units/datums before comparing dates, thresholds, tide/water levels or spatial restrictions.
7. Build source references with scope, checked-at/effective dates, freshness/recheck policy, authority class and consequence.
8. Preserve conflicts/unavailable domains and `UNRESOLVED` applicability. Critical legal/closure gaps cannot be replaced by secondary fishing sites or model memory.
9. Emit `GENERATED_PROVISIONAL` pack + authority coverage report + per-option applicability results + readiness + invalidation conditions.
10. Do not edit the distributed plugin source at runtime.

## Reuse

Reuse an existing generated pack only after verifying scope match and refreshing every material source whose freshness window has expired or whose effective period may have changed.

## User-facing boundary

Do not mention skill readers, package files, internal routing or generation machinery unless the user asks about implementation. Surface only relevant source coverage, uncertainty and plan consequence.
