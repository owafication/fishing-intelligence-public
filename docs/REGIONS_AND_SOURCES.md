# Regions and sources

Fishing Intelligence has a global core with uneven regional depth.

## Global default

For any location, the resolver first looks for an adequate curated regional pack. If none exists and current reference access is available, it builds a temporary regional source set from applicable official authorities.

## Shipped regional depth

- `AU-NT-DARWIN` — `PROSPECT_READY`
- `AU-SA-ADELAIDE-GSV` — `PLANNING_READY`
- other bundled Australian jurisdiction references — `REFERENCE_READY`

These packs contain routing/source links and planning context. Current weather forecasts and tide predictions are retrieved from external sources when needed rather than stored in the package.

`REFERENCE_READY` means current authority can be resolved for reference questions. `PLANNING_READY` means the required authority domains can be checked for a bounded plan. `PROSPECT_READY` additionally has adequate spatial/prospect evidence. `INSUFFICIENT` means a critical dependency cannot be resolved.
