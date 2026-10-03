---
name: regional-pack-resolver
description: Resolve the applicable regional authority context for a fishing request anywhere in the world. Use before consequential planning/verifying to select an adequate curated pack or trigger a generated provisional pack without assuming one-country authority structure.
---

# Regional Pack Resolver

Read `../../shared/global-authority-stack.md`, `../../shared/authority-applicability.md`, `../../shared/jurisdiction-pack-contract.md`, `../../shared/regional-pack-readiness.md`, `../../shared/public-response-boundary.md` and `../../shared/units-time-datum-contract.md`.

1. Resolve place, water regime, fishing mode, relevant date/window, method, target species/taxon precision and the concrete option/access/route scope required for the decision.
2. Identify whether a shipped curated regional pack matches the actual plan area and has sufficient readiness.
3. If a curated pack is adequate, return its pack ref/readiness and material authority domains.
4. If no adequate curated pack exists, route to `regional-pack-generator`; do not fall back to a random generic web answer.
5. Preserve overlapping authority layers. Country borders alone do not determine fisheries, protected-area, navigation or access authority. Apply authority observations against the actual option scope; a nearby authority/source is not automatically applicable.
6. If location/jurisdiction is too ambiguous to identify material legal authority, keep it unresolved and downgrade/block the dependent decision.
7. Do not expose internal pack/skill mechanics in ordinary user-facing fishing answers.
