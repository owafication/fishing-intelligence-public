# Fishing mode contract

Supported modes: `TRAILER_BOAT | KAYAK | SHORE | ROCK | BEACH | OFFSHORE | RIVER | LAKE`.

Each mode injects access, rule/licence, equipment/method, environmental and geometry constraints into **one planner kernel**; it does not create a separate planner.

Examples: ROCK may add declared-area legal requirements; LAKE/RIVER may require inland licences or stocked/reservoir permits; TRAILER_BOAT adds ramp/retrieval and vessel/range; KAYAK uses kayak access rather than requiring a boat ramp; SHORE/BEACH must not infer access over private/restricted land.
