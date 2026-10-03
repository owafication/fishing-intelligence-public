# Advanced capability boundaries

## Contract-supported now
- host-mediated GPX/KML/CSV/GeoJSON interoperability when the host can actually inspect/create the file;
- guide/charter trip-context reasoning without booking or CRM ownership;
- readiness-aware fishing travel comparison;
- structured privacy-aware share-package construction;
- evidence-driven experiment-plan design;
- optional image-assisted species suggestions when an image-capable host is available.

## Not implemented or not verified
- bundled deterministic GPX/KML/CSV/GeoJSON parser/export runtime;
- direct chartplotter or cloud-device sync;
- binary/photo/attachment metadata scrubber;
- durable multi-user authentication/ACL enforcement;
- bookings, payments or CRM;
- automatic revocation of already-exported files;
- certified navigation;
- continuous background geofencing from the skills-only plugin.

A contract-supported workflow may use host capabilities that are actually present. Missing host capability must degrade only the affected workflow and must never become an implementation claim.
