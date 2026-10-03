# Plan readiness and verification presentation

Every consequential fishing plan must expose a readiness state before the detailed itinerary.

## States
- `READY_TO_USE`: all critical dependencies required for this plan are verified/current enough under their source contracts and all hard constraints pass. This does **not** mean the trip is safe.
- `PROVISIONAL`: the plan is structurally viable, but one or more material non-blocking dependencies are unverified, conflicting or approximate. Identify exactly what needs recheck.
- `RESEARCH_ONLY`: useful for comparing ideas or prospective areas, but current conditions/access/legal dependencies are not verified sufficiently for operational use.
- `BLOCKED`: a hard constraint fails or a critical dependency needed to construct an admissible plan is unavailable/conflicting.

## Verification summary
For each critical dependency report, where available:
- source ID/provider,
- subject (weather, warning, tide, access, rule, etc.),
- status: `VERIFIED_CURRENT | VERIFIED_AS_OF | STALE | CONFLICTING | UNAVAILABLE | NOT_REQUIRED`,
- `checked_at`,
- freshness/expiry note,
- consequence for the plan.

Never let a concise itinerary hide a `CONFLICTING` or `UNAVAILABLE` critical dependency.


## Presentation invariant

For a consequential complete plan, readiness appears before the detailed itinerary and is followed by a verification summary. Contract existence is not enough: if the user-visible answer omits readiness or hides an unresolved critical dependency, the response is non-conforming.
