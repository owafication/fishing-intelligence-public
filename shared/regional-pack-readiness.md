# Regional pack readiness

Regional depth is separate from global core capability.

Pack source context:
- `CURATED`: distributed/reviewed regional source/adaptor material;
- `GENERATED_PROVISIONAL`: runtime authority/source bundle generated on demand and not self-promoted into shipped source.

Readiness:
- `REFERENCE_READY`: current authority/reference resolution is available, but complete operational planning dependencies are not established;
- `PLANNING_READY`: required legal/access/environment/operational authority domains for the bounded plan are implemented or verified;
- `PROSPECT_READY`: planning plus adequate spatial/prospect evidence is available;
- `INSUFFICIENT`: one or more critical domains cannot be resolved strongly enough for the requested task.

Shipped deep packs currently include:
- `AU-NT-DARWIN`: `PROSPECT_READY`;
- `AU-SA-ADELAIDE-GSV`: `PLANNING_READY`.

Other locations are not treated as unsupported merely because no shipped pack exists. Route them through `regional-pack-resolver`; generate `GENERATED_PROVISIONAL` packs when current host reference access can resolve the required authority stack. Never imply equal local/prospect depth globally.
