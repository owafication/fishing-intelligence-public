# Replan freshness and telemetry

Dynamic replanning must distinguish **event time** from **retrieval time**.

Examples:
- a weather forecast refreshed now may be current;
- a user-reported location from 90 minutes ago may not support a precise distance-to-ramp calculation;
- fuel reported before several long runs may not support a current range calculation.

Every consequential current-state field should therefore carry `observed_at` and source/source context.

When source age exceeds the tolerance needed for the decision:
- refresh if a verified source/telemetry capability exists;
- otherwise degrade the affected conclusion to `PROVISIONAL`, `WITHHELD` or `BLOCKED`.

Do not pretend that chat itself provides continuous GPS, fuel, sounder, engine or weather telemetry.
