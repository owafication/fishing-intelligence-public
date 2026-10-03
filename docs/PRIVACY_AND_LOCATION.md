# Privacy and location

Fishing locations and information that can reveal them are private by default.

## Privacy levels

`PRIVATE | NAMED_PEOPLE | TRUSTED_GROUP | APPROXIMATE | PUBLIC`

Derived outputs should not become more public than the information they depend on unless the user explicitly requests broader disclosure.

## Location leakage

Coordinates are not the only risk. Tracks, screenshots, EXIF-bearing photos, exported metadata and combinations of facts can reveal a private mark.

## Generated prospects

Generated prospects preserve source precision and default to `navigation_suitable=false`. Coarse data should produce approximate areas rather than false exact waypoints.

## Sharing limitation

Once information has been copied or exported to another person or system, Fishing Intelligence cannot revoke that external copy.
