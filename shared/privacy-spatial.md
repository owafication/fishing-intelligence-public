# Privacy and spatial precision

## Privacy levels
`PRIVATE | NAMED_PEOPLE | TRUSTED_GROUP | APPROXIMATE | PUBLIC`

Private by default for fishing locations and derived knowledge that can reveal them.

Derived records inherit the most restrictive relevant privacy state unless the user explicitly authorises a change.

Protect not only coordinates but also:
- EXIF-bearing photos,
- GPX/KML tracks,
- trip exports,
- screenshots,
- patterns that reveal a secret location,
- aggregated outputs that allow re-identification of a private mark.

## Spatial precision
A fishing prospect is a search area, not a navigation instruction.

Every spatial output should preserve:
- CRS,
- source resolution,
- estimated positional accuracy where known,
- output precision,
- `navigation_suitable` flag.

Default `navigation_suitable = false` for generated prospects.

Do not convert coarse bathymetry into falsely precise coordinates. Prefer polygons/approximate areas where source resolution supports only an area.

## Geometry
Support point, line, polygon, corridor and approximate-area semantics. Avoid forcing every fishing object into a point.
