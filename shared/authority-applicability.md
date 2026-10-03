# Authority applicability contract

Authority discovery and authority applicability are separate decisions.

A current official source can be valid evidence yet still be irrelevant to a particular fishing option. Every consequential authority observation, restriction or requirement must therefore be evaluated **against the concrete option scope** before it can affect admission or readiness.

## Option scope

Resolve the smallest practical option envelope before applying authority evidence:
- fishing/launch/access area and intended route or shore-access footprint;
- water regime (for example inland, tidal river/estuary, coastal/marine, offshore, lake/reservoir);
- fishing mode and vessel/party class where material;
- target species/taxon and method/gear where material;
- planned date/time/effective period;
- access facility or land/tenure context where material.

Unknown scope stays unknown. Do not invent route geometry, vessel class, taxon identity or access boundaries merely to make a source appear applicable.

## Applicability states

Each authority observation/constraint receives exactly one:

`REQUIRED | CONDITIONAL | NOT_APPLICABLE | UNRESOLVED`

- `REQUIRED` — the source/constraint is within the option scope and materially governs admission, legal operation, access or a required environmental dependency.
- `CONDITIONAL` — it governs only if a stated trigger is taken, such as entering a secondary route, switching method, retaining a species, using a different launch, crossing into another authority area or changing water category.
- `NOT_APPLICABLE` — evidence establishes that the source/constraint is outside the option's geography, water regime, mode, subject, vessel/party class or effective period.
- `UNRESOLVED` — applicability cannot yet be determined strongly enough.

`NOT_APPLICABLE` does not lower readiness **only when the scope mismatch is supported by sufficient evidence**. `CONDITIONAL` does not lower readiness while its trigger is explicitly known not to be active, but the trigger and required recheck must remain visible. If the trigger state itself is unknown, applicability is effectively `UNRESOLVED` for the dependent decision. A material `UNRESOLVED` legal/safety/navigation/access applicability can withhold or block the affected option.

## Scope dimensions

Where material, record why the applicability state was reached:
- `spatial_relation = INTERSECTS | DOES_NOT_INTERSECT | UNRESOLVED | NOT_SPATIAL`;
- `temporal_relation = ACTIVE | INACTIVE | UNRESOLVED | NOT_TEMPORAL`;
- `water_regime_relation = APPLIES | DOES_NOT_APPLY | UNRESOLVED`;
- `mode_subject_relation = APPLIES | DOES_NOT_APPLY | UNRESOLVED`.

A nearby protected area, marine forecast district, notice-to-mariners polygon or local rule is not automatically applicable merely because it appeared in search results.

## Spatial restrictions

For `AREA_CLOSURES_PROTECTED`, `NAVIGATION_NOTICES`, `ACCESS` and other spatial restrictions, determine whether the planned option/route intersects the controlled area. If exact geometry is unavailable, use the strongest authoritative named-area/route evidence available and preserve `UNRESOLVED` when intersection cannot be established.

Never convert `source discovered` into `route cleared`. `DOES_NOT_INTERSECT` may be used only when authoritative geometry or sufficiently precise named-area/route evidence supports that conclusion. Otherwise use `UNRESOLVED`. `UNRESOLVED` means the dependent route cannot be treated as notice/closure-clear.

## Weather and water authority

Forecast/source selection must match the actual option's location **and water regime**. A marine forecast can be useful context for a nearby inland option, but it is not a required readiness dependency unless the admitted option includes marine/tidal operation covered by that product. Likewise, an inland forecast must not substitute for a required marine forecast.

## Readiness

Readiness is calculated only from evidence whose applicability is `REQUIRED`, plus triggered `CONDITIONAL` dependencies. Non-applicable evidence remains source context/context, not a blocker. Material `UNRESOLVED` applicability is treated according to the consequence of possibly applying: legal/safety/navigation/access uncertainty may withhold or block the affected option; non-critical contextual uncertainty may keep the plan provisional.
