# GPS and field-state source context

GPS use is opt-in and capability-dependent.

A GPS sample records `observed_at`, latitude/longitude, reported horizontal accuracy when available, provider/device source, and privacy. It is `OBSERVED_INSTRUMENT` only when an actual device/location API produced it.

If GPS permission is denied or unavailable, **Replan from here** may still work from a user-supplied place/area, but the position is `USER_REPORTED` with the supplied precision.

Never infer continuous tracking from occasional samples. Never infer fuel from GPS distance alone. Tracks are private by default and remain separate from generated prospect geometry.
