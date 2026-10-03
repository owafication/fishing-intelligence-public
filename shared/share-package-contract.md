# Share package contract

A `SharePackage` is a derived exported view of selected Fishing Intelligence records. It does not change accepted privacy.

Supported structured audience transformations: `PRIVATE | NAMED_PEOPLE | TRUSTED_GROUP | APPROXIMATE | PUBLIC`. Without shared auth/ACL, `NAMED_PEOPLE` and `TRUSTED_GROUP` describe intended audience only; no durable recipient access control is claimed.

Location sharing defaults PRIVATE. `APPROXIMATE` structured exports may coarsen/replace geometry and must not include exact coordinates in the structured output.

**Binary/media attachment scrubbing is not implemented in the core plugin.** Do not claim a photo, GPX attachment, screenshot or arbitrary binary is privacy-safe merely because the visible record was coarsened. Include such material only after an actually available transformation removes hidden exact location/EXIF/metadata and the result is verified.

Revoking a package locally cannot revoke copies already exported elsewhere.

## Public-release privacy reminder
Public examples/fixtures must remain synthetic. Never include connected-store IDs, private marks, personal trip coordinates, provider receipts or user fishing history in a public package.
