# Core invariants

1. Preserve user observations and explicit corrections; do not silently rewrite history.
2. Preserve uncertainty and source precision.
3. Separate hard constraints, soft preferences and unknowns.
4. Keep private fishing locations private by default.
5. Coarse spatial data must not become a fake precise waypoint.
6. Keep tide prediction, observed water level and current/flow inference separate.
7. Current legal or keeper guidance requires current authoritative verification.
8. Unknown vessel capability or operating limits remain unknown.
9. Generated prospects are search areas, not navigation instructions.
10. Catch counts without effort/exposure are not sufficient evidence of fishing advantage.
11. Replanning changes the remaining plan; it does not rewrite completed events.
12. The plugin must remain usable without a dedicated Fishing Intelligence service or persistent store.
