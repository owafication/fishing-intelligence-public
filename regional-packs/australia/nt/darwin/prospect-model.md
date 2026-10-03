# Darwin Prospect Intelligence model

## Initial feature types
- `TERRAIN_BREAK`: grid-derived local relief/gradient search area.
- `ISOLATED_RELIEF`: isolated rise/depression candidate from qualified grid evidence.
- `CHANNEL_EDGE`: supported by bathymetry or visible low-tide channel geometry.
- `INTERTIDAL_DRAIN`: visible/qualified drainage feature; temporal imagery context retained.
- `ARTIFICIAL_STRUCTURE_HALO`: generated search area around an `OFFICIAL_LOCATION`; never replaces the official coordinate record.

## What this prospect model does not claim
- fish presence,
- catch probability,
- precise current direction/speed from terrain alone,
- navigational depth/clearance,
- live tiled AusSeabed ingestion,
- automatic interpretation of every NT low-tide image without visual evidence available in the host.

## Darwin inputs
Regional bathymetry/terrain datasets and low-tide imagery can support broad terrain and intertidal-structure reasoning when the underlying source is available for inspection. Official artificial-reef records can seed official structure locations.
