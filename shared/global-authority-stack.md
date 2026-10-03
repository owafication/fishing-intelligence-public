# Global authority stack

Fishing Intelligence resolves applicable authority **by place, water regime, fishing mode, method, target species and date**, not by assuming one country-wide rule source.

## Authority domains

Evaluate the domains that are material to the requested plan:

- `FISHERIES_RULES` — size/bag/possession, seasons, methods/gear, protected species and harvest rules;
- `LICENSING_PERMITS` — licences, permits, endorsements and exemptions;
- `AREA_CLOSURES_PROTECTED` — reserves, sanctuaries, temporary closures, customary/local overlays and special zones;
- `ACCESS` — launch/shore access, opening/status constraints, land-tenure or facility restrictions;
- `BOATING_SAFETY` — applicable equipment/operating requirements for the vessel, water category and mode;
- `NAVIGATION_NOTICES` — temporary works, exclusion/closed-water/no-wake zones, notices to mariners and route restrictions;
- `WEATHER_WARNINGS` — the official forecast/warning authority appropriate to the fishing area;
- `TIDE_WATER_LEVEL` — tide, river/lake level, flow or hydrology authority when consequential;
- `SPECIES_TAXONOMY` — authoritative species/taxon identity when a common name is ambiguous or rule applicability depends on exact identity;
- `BIOSECURITY_HEALTH_ADVISORY` — bait/live-fish transport, invasive-species controls, shellfish/harvest health notices or similar when applicable.

Not every domain is required for every mode. A shore session may not require boating-safety or navigation-notice resolution; a powered-boat route normally does.

## Authority layering

Resolve all applicable layers rather than choosing one convenient page:

`INTERNATIONAL/TRANSBOUNDARY -> NATIONAL/FEDERAL -> STATE/PROVINCE/REGION -> LOCAL/SPECIAL AREA -> FACILITY/ACCESS`

The exact hierarchy varies by jurisdiction. Preserve conflicts instead of choosing by familiarity or search ranking. Prefer primary regulators and current official notices. Secondary sources may support discovery or fishing context but cannot replace a required primary authority without an explicit source contract.

## Coverage and applicability result

Domain coverage and individual-source applicability are separate.

For each material domain, retain the authority/source inventory and then classify each consequential source, notice, overlay, restriction or requirement against the exact option using `authority-applicability.md`.

Each consequential evidence item records:
- applicability: `REQUIRED | CONDITIONAL | NOT_APPLICABLE | UNRESOLVED`;
- authority/source identity and authority scope;
- option scope it was compared against;
- spatial/temporal/water-regime/mode-subject relation where material;
- evidence class;
- verification state;
- checked-at/effective period/freshness;
- conflicts and unresolved overlays;
- consequence for admission/readiness.

Readiness considers only `REQUIRED` items plus triggered `CONDITIONAL` dependencies. A discovered official source that is `NOT_APPLICABLE` does not lower readiness. A material `UNRESOLVED` legal/closure/access/safety/navigation applicability cannot be treated as clear.

A generated regional pack is only as strong as its weakest **applicable** critical dependency. Missing or conflicting legal/closure authority blocks any dependent keeper/method/area decision. Unknown non-critical fishing-context evidence may merely reduce confidence.
