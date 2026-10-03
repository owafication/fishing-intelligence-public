# Generated regional pack

When no adequate curated regional pack exists, Fishing Intelligence may build a temporary regional reference set from current official sources.

`pack_class = GENERATED_PROVISIONAL`

A generated pack records the place/mode/date scope, applicable authority layers, source links, coverage, option-specific applicability, currentness, units/timezone/datum handling, unresolved conflicts and readiness.

Rules:
1. Search primary/official authorities first.
2. Resolve overlapping jurisdiction and special-area layers.
3. A discovered source is not automatically applicable to the exact route/mode/species/time.
4. Resolve species identity where rules depend on it.
5. Normalize units, timezone and datum before comparing thresholds or tide/water-level information.
6. For boating plans, resolve boating requirements and navigation notices when applicable.
7. Preserve unavailable/conflicting dependencies.
8. Store links/references rather than copied source pages or live datasets.
9. Generated packs remain temporary; the runtime does not edit the distributed plugin source.
