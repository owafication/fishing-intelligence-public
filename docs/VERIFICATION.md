# Verification and uncertainty

Fishing Intelligence separates three user-visible questions:

- **Evidence class:** what kind of support is this? `AUTHORITATIVE | OBSERVED | SUPPORTED | HYPOTHESIS`
- **Verification state:** how current/confirmed is it? `VERIFIED_CURRENT | VERIFIED_AS_OF | STALE | CONFLICTING | UNAVAILABLE | NOT_REQUIRED`
- **Applicability:** does it govern this exact option? `REQUIRED | CONDITIONAL | NOT_APPLICABLE | UNRESOLVED`

Unknown stays unknown. Tide prediction is not observed water level or site-specific current. A forecast is not an observation. A nearby restriction is not automatically applicable to a route.
