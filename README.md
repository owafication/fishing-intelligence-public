# Fishing Intelligence

Fishing Intelligence is an open-source, portable fishing decision-intelligence plugin. It helps plan trips, compare opportunities, capture what happened, adapt while fishing and learn from personal results.

## Important limitations

Fishing Intelligence is decision support. It is **not** certified navigation, a weather service, a legal authority, emergency-response software or a safety-certification system. Current rules, access restrictions, navigation notices, weather and tide-dependent decisions depend on external sources being available and current. Local source depth varies by region, and the plugin does not guarantee fishing success.

See [Limitations](docs/LIMITATIONS.md) for the full list of non-claims and operational limits.

## What it does

- global fishing-jurisdiction and authority resolution;
- on-demand regional source packs when no curated pack exists;
- trip planning with hard constraints before fishing-quality comparison;
- current rule, licence, closure, access, boating and navigation-notice checks where applicable;
- weather/tide source resolution without bundling live weather or tide data;
- fishing prospect reasoning where suitable spatial evidence exists;
- catch, blank and effort capture inside the active session;
- effort-normalised personal metrics and private-mark analysis;
- active-trip replanning;
- species/taxon checks when legal rules depend on exact identity;
- privacy-aware handling of fishing locations.

## Portable-only

Fishing Intelligence requires no dedicated server and no persistent store. It runs from the plugin package and current conversation context. When the host provides web, file or image tools, the plugin can use them for current references or user-supplied inputs; those tools are optional capabilities, not a separate Fishing Intelligence service.

## Install

The repository is the complete portable plugin package.

1. Clone the repository or download the release ZIP.
2. Keep `plugin.json`, `.codex-plugin/`, `skills/`, `shared/` and the other packaged files in their existing relative locations.
3. Import or install the package in a compatible plugin host. No Fishing Intelligence server, database or account is required.
4. Optional: verify the package before use with:

```bash
python scripts/validate.py
```

If you install Fishing Intelligence from a published plugin directory rather than from source, use that directory's normal install flow; the repository is primarily useful for inspection, development and self-hosted/package-based installation.

## Quick start

Example first use:

- `I have a 5.5 m trailer boat and want to target snapper this weekend. I can fish Saturday or Sunday, want a short run, and I don't know my exact fuel range. Plan the trip and verify the current rules, access, weather and navigation constraints.`

More examples:

- `Plan a trailer-boat fishing trip for this weekend. I want a short run and I don't know my exact fuel range.`
- `Compare these two private marks with a new exploratory area. Use catches, blanks and effort, not just catch totals.`
- `We fished this spot for 45 minutes with no bites, wind has increased and I need to be back at the ramp by 4:30. Replan from here.`
- `Record 3 fish released at this attempt. I will add the lengths later.`

See `docs/QUICKSTART.md` and `docs/CAPABILITIES.md`.

## Regional sources

The repository includes links to official fishing, access, weather, tide and navigation-source families used for live reference. It does **not** bundle current weather forecasts, tide predictions or copied third-party pages. See `docs/REGIONS_AND_SOURCES.md` and `docs/EXTERNAL_SOURCES.md`.

## Validation

Run:

```bash
python scripts/validate.py
```

The public validator checks package structure, manifests, source-link hygiene, documentation references and deterministic planning/region/applicability fixtures.

## Licence

Apache License 2.0. See `LICENSE` and `NOTICE`.
