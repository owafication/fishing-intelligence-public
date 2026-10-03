# Complete fishing-plan response contract

This contract governs the user-visible structure of a consequential pre-trip plan.

## Mandatory order

A complete plan presents:

1. `READINESS`
2. `KNOWN / USER LIMITS / UNKNOWNS`
3. `OPTIONS`
4. `VERIFICATION`
5. `ITINERARY`
6. `RECHECK / ABANDON CONDITIONS`

The detailed itinerary must not precede readiness.

## Readiness

Use exactly one of:

`READY_TO_USE | PROVISIONAL | RESEARCH_ONLY | BLOCKED`

Do not emit a synonym or additional readiness label such as `CONDITIONAL`, `PREFERRED`, `GO`, `CAUTION`, or `NOT READY`. A material non-blocking dependency that is unverified, conflicting or approximate implies `PROVISIONAL`; a critical dependency that prevents an admissible plan implies `BLOCKED`.

Readiness is a planning/verification state, not a safety verdict.

## Known / user limits / unknowns

Separate:
- supplied or verified facts;
- user-selected operating limits;
- material unknowns.

Translate consequential facts into operational effects. Examples:
- a supplied draft can qualify/exclude shallow access or structure when supporting access/depth evidence exists;
- unknown usable fuel/range can withhold long-range options;
- unknown crew/comms/navigation/safety-equipment state remains unknown when relevant.

Do not invent capability from vessel length or horsepower.

## Options

Present 1–3 materially distinct admitted options. Each option exposes:
- objective/target intent;
- mode;
- access/launch choice if relevant;
- evidence class;
- advantages/trade-offs;
- material unknowns;
- any verified applicable access/navigation constraint;
- material travel/towing/access-timing trade-offs when options differ.

A listed/map-visible alternative is not allowed to hide a known material applicable access constraint. Authority evidence is evaluated against the option scope; a nearby rule/notice that does not intersect the option is context, not a blocker.

## Verification

For a consequential complete plan, the user-visible `VERIFICATION` section must expose at minimum these six **separate fields** for every critical dependency:

`Dependency | Source/provider | Evidence class | Verification state | Applicability | Consequence`

A Markdown table is preferred. Equivalent structured fields are acceptable only when each field is explicitly labelled and independently readable. Do not merge fields into a combined `Current evidence`, `State`, or `Evidence / verification` value.

Accepted values are:
- evidence class: `AUTHORITATIVE | OBSERVED | SUPPORTED | HYPOTHESIS`;
- verification state: `VERIFIED_CURRENT | VERIFIED_AS_OF | STALE | CONFLICTING | UNAVAILABLE | NOT_REQUIRED`;
- applicability: `REQUIRED | CONDITIONAL | NOT_APPLICABLE | UNRESOLVED`.

Also report `checked_at`, freshness/effective period and subject/scope when available and material. These may be additional columns or explicit detail attached to the same dependency, but they do not replace the six mandatory fields.

Evidence class, verification state and applicability are independent dimensions. `AUTHORITATIVE` does **not** mean `VERIFIED_CURRENT`; `CONDITIONAL` is an applicability state and is **not** a verification state. Never collapse or substitute these fields.

Exact tide-dependent access cannot be called verified from a source that the regional source contract does not permit for that purpose.

## Evidence language

- `AUTHORITATIVE`: official legal/access/warning state.
- `OBSERVED`: user/instrument observation.
- `SUPPORTED`: credible evidence supporting a system-level fishing proposition.
- `HYPOTHESIS`: prospective/site-specific interpretation not established by the evidence.

Tide height/phase alone does not establish site-specific current speed or direction.

## Geographic source selection

Select environmental/forecast context from the proposed fishing area **and water regime**. A user's origin may be useful for travel planning but does not determine the forecast product. A marine forecast does not become a required readiness dependency for an inland-only option merely because it is nearby.

## Recheck / abandon

Identify what would invalidate, withhold or require re-verification of the plan, including material forecast/warning, access, tide, legal, range, time or user-limit changes.
