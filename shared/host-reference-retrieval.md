# Host reference retrieval procedure

When the host provides web/search/browsing capability, Fishing Intelligence may use it to verify registered external sources without claiming that the plugin owns a production data adapter.

## Procedure
1. Resolve the regional Source Contract Registry entry before retrieval when one exists.
2. Retrieve the authoritative/reference source through the host's available public-web capability.
3. Record source ID/provider, subject, retrieved/checked-at time and the facts actually needed for the decision.
4. Evaluate freshness against the source contract where defined.
5. Normalize only the decision-relevant facts; do not silently keep restricted page content.
6. Return a verification state and dependency consequence.
7. Preserve conflicting values as `CONFLICTING`; do not average or select the convenient one.
8. If the host lacks web access, return `UNAVAILABLE` or `NOT_VERIFIED` and degrade readiness accordingly.

## Boundaries
- Host reference retrieval is not evidence that a commercial API/feed exists.
- Region-specific restricted/licensed material must follow the applicable regional source contract; host readability does not create redistribution or commercial-feed rights.
- Search-engine snippets alone are insufficient for a consequential verification claim when the source page can be checked.
- A current web citation does not make a generated prospect suitable for navigation.
