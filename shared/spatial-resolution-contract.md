# Spatial resolution contract

## Non-negotiable rules
- Never output generated geometry more precise than the source supports.
- AusSeabed coverage polygons are discovery metadata; if per-survey cell size is unavailable, they cannot justify derived precise prospect geometry.
- A raster/grid prospect must record dataset ID, CRS, horizontal grid resolution, vertical datum/meaning where known and source lineage.
- Generated prospects default to `navigation_suitable=false`.
- Do not use a prospect geometry to recommend a navigation route, minimum water depth or clearance.

## Grid-derived area floor
For the reference implementation, a generated raster prospect must cover at least a 3 x 3 cell neighbourhood (9 cells) unless the source itself documents a discrete structure with better positional support. This is a product anti-false-precision rule, not a biological claim.

For a 30 m grid, the minimum derived raster search footprint is therefore approximately 90 m x 90 m before any additional uncertainty/feature extent is applied.

## Source vs output precision
`output_resolution_m >= source_resolution_m` for raster-derived prospects. Coordinates may be used internally to define an area but should not be formatted with decimal precision that implies accuracy beyond the source.

## Mixed-resolution compilations
A nominal 30 m compilation can incorporate source observations of varying original accuracy and can include interpolation/base-grid replacement. Preserve the compilation's lineage limitations; 30 m cell spacing does not imply 30 m positional or depth accuracy everywhere.
