# Vessel and trip capability matrix

Before vessel-dependent admission, separate known facts, user-selected limits and unknown capability inputs.

## Known/unknown presentation
Examples of known vessel facts: hull length/material, propulsion, user-described draft, fuel actually reported, electronics actually reported.
Examples of unknowns that may matter: usable fuel, economy/range, crew, communications, navigation equipment, safety equipment, offshore experience and user-selected wind/swell limits.

Never infer usable range from engine horsepower or hull length alone.
Never infer overall vessel suitability/capability from hull length, engine horsepower or appearance alone. Prefer wording such as `nothing supplied excludes this bounded option` while preserving unresolved range/equipment/operating-limit inputs.
Never infer navigation, communication or legally required safety equipment merely because a vessel appears capable.
A shallow-draft description does not override documented access constraints or navigational hazards.

## Consequence
- If an unknown is irrelevant to the bounded plan, label it non-blocking.
- If it prevents range/access/operational-feasibility admission, readiness is `BLOCKED` or the affected option is withheld.
- For a conservative inner/local option, unknown offshore capability can remain non-blocking while offshore alternatives are withheld.


## Operationalisation invariant

When a supplied vessel fact is consequential, convert it into an explicit admission/operating consequence rather than merely echoing it. A user-reported draft, for example, should qualify shallow-water/ramp/bar candidates when supporting access/depth evidence exists. Do not invent a minimum depth or navigation conclusion from draft alone.
