# Active trip state

Active trip state is a time-stamped planning snapshot, not live telemetry unless an actual live input is present.

Useful fields include trip reference, observed time, current objective, completed attempts and any return deadline. Optional fields include position with source/accuracy, user-reported fuel state, environmental observations and changed access/rule state.

Rules:
- Never infer current position from a planned waypoint.
- A qualitative fuel statement remains qualitative unless the user supplies a usable conversion.
- Current-state age matters to the decision being made.
- Missing species, counts, position or rule applicability remain unknown.
