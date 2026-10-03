# Validation

The public portable package includes a deterministic validator at `scripts/validate.py`.

It checks:

- manifest/version alignment;
- portable-only runtime declaration;
- Apache-2.0 public licence markers;
- JSON integrity;
- skill/shared-file references;
- absence of private/development artefacts and removed architecture terms;
- external-source link hygiene;
- deterministic planning, prospect, regional and authority-applicability fixtures.

Run the validator locally before publishing a modified archive.
