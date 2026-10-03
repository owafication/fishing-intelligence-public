# Prospect source selection

## Coverage/discovery
Coverage indexes answer “what datasets may exist here?” only. Do not treat their polygons as depth grids or infer cell size when the coverage metadata says it is unavailable.

## Grid/DEM
A dataset with explicit resolution may support terrain analysis at that scale. Record the exact dataset identity, not merely “AusSeabed”.

## Intertidal imagery
Low-tide imagery may support identification of visible rock bars, drains, sandbars and reef edges. The feature observation is bounded to the capture conditions/date and remains non-navigational.

## Official structures
Artificial reefs and other published structures remain `OFFICIAL_LOCATION`. Generate a separate `ARTIFICIAL_STRUCTURE_HALO` only when the user needs a broader fishing search area, and label the halo as hypothesis-bearing.

## Legal overlays
Area closures/protection boundaries are exclusion constraints, not fishing-prospect evidence. Verify current legal effect before operational planning.
