# Developer guide

## Principles

1. Keep the plugin portable: do not introduce a required Fishing Intelligence backend or persistent store.
2. Keep current external facts as links/references; do not freeze mutable weather, tide, closure or access values into deterministic tests.
3. Preserve unknowns rather than inventing capability, depth, legal status or current conditions.
4. Generated fishing areas are not navigation instructions.
5. Keep private-location examples synthetic.

## Adding a region

Add a regional pack only for stable routing/context. Link to official sources for mutable facts. If a new region does not justify a curated pack, rely on the on-demand regional resolver/generator instead.

## Tests

Run `python scripts/validate.py` after changes. Add deterministic fixtures for stable behavior, not current forecast/tide values.
