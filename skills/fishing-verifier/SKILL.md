---
name: fishing-verifier
description: Verify current fishing rules, licences/permits, closures, protected-area overlays, access, navigation notices, applicable operational requirements and source freshness anywhere in the world using the resolved regional authority pack.
---

# Fishing Verifier

Read `../../shared/global-authority-stack.md`, `../../shared/authority-applicability.md`, `../../shared/operational-requirements.md`, `../../shared/navigation-notice-resolution.md`, `../../shared/species-taxonomy-resolution.md`, `../../shared/units-time-datum-contract.md` and `../../shared/public-response-boundary.md`.

1. Obtain the applicable curated/generated regional pack from `regional-pack-resolver`; if absent/inadequate, trigger `regional-pack-generator` before consequential verification.
2. Establish the concrete option scope, then verify every authority domain required by that bounded plan. Do not assume one national source controls all layers.
3. Resolve special-area/local/facility overlays and temporary closures/notices, then prove whether each one intersects/applies to the candidate area or route. `Source discovered` is not `constraint applies`, and `source discovered` is not `route clear`.
4. For boating plans, resolve applicable safety/equipment requirements separately from the user's actual compliance state and check material current navigation notices/restrictions.
5. For exact tide/water-level-dependent access, require compatible station/timezone/datum/source evidence under the resolved source contract. Third-party values cannot silently become authoritative.
6. Where target common-name ambiguity could change rules, resolve species/taxon first or withhold species-specific keeper/method advice.
7. Choose weather/marine/inland forecast authority from the actual fishing area, water regime and mode, not merely the user's origin. A marine forecast must not become a required readiness dependency for an inland-only option unless the option actually enters the marine/tidal scope it governs.
8. Do not treat a webcam/community report as official status, protected-area geometry as fishing-productivity evidence, or a source being readable as permission to republish/cache it.

Return for each critical dependency:
- authority domain;
- source/provider and authority scope;
- applicability (`REQUIRED | CONDITIONAL | NOT_APPLICABLE | UNRESOLVED`);
- spatial/temporal/water-regime/mode-subject relation where material;
- evidence class;
- verification state;
- checked-at/effective period/freshness;
- applicable requirement/constraint;
- user-compliance state where relevant;
- consequence for admission/readiness.

Do not expose internal skill/package/provider mechanics in ordinary fishing answers.
