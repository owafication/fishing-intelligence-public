# Architecture

Fishing Intelligence is a portable skills plugin. No dedicated backend or persistent storage is required.

## Main flow

1. Resolve the fishing place, mode, target and time window.
2. Resolve the applicable jurisdiction and authority layers.
3. Use a curated regional source pack when available; otherwise build a temporary regional reference set from current official sources.
4. Apply rules, access constraints, weather/tide dependencies, boating requirements and navigation notices only when they apply to the proposed option.
5. Admit feasible options before comparing fishing quality.
6. Return readiness, unknowns, verification, itinerary and recheck conditions.

## Source handling

External facts remain external. Regional packs contain links and source-routing information, not frozen copies of current weather, tide tables or regulatory pages.

## Portable behavior

The plugin works from the package plus conversation context. Host-provided web, file and image capabilities can improve current verification or accept user inputs, but they are not required infrastructure owned by Fishing Intelligence.
