# Plan input matrix

Before generating fishing options, resolve each input into `KNOWN | USER_LIMIT | UNKNOWN | NOT_REQUIRED`.

## Required dimensions
- calendar window and explicit timezone;
- origin plus origin precision: `EXACT | SUBURB | REGION | UNKNOWN`;
- fishing mode;
- target intent: exact species, species family, general opportunity, or unspecified;
- hard time constraints such as latest return;
- vessel facts actually supplied;
- usable fuel/range when a candidate depends on it;
- user operating limits when supplied;
- critical environmental/access/legal dependencies and their verification state.

## Precision rules
A regional origin can support approximate road-access comparison but not a minute-precise departure time. Unknown vessel range cannot be back-filled from engine horsepower or hull length. Unknown target intent is not an invitation to silently choose a favourite species.

## Target-unspecified behavior
When the user simply wants to fish, build materially different opportunity families that survive admission. Opportunity families depend on the actual water and mode (for example estuary/creek, reef/demersal, pelagic/offshore, lake/river, surf/rock/shore). A family whose critical access, vessel/range, authority or conditions requirements are unresolved may be withheld rather than presented as operational.
