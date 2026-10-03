# Fishing prospect record

Generated spatial prospects should include:
- ID, privacy and status;
- `origin_type = GENERATED_PROSPECT`;
- prospect type;
- geometry appropriate to source precision;
- CRS and source resolution;
- source vertical datum/meaning where relevant;
- `navigation_suitable` (default false);
- structure/fishing evidence references;
- target species/family when applicable;
- environmental assumptions;
- hypothesis state: `GENERATED | TESTED | SUPPORTED | WEAKENED | REJECTED`;
- precision statement;
- applicable legal/exclusion verification state.

An official location and a generated fishing search area around it are distinct.
