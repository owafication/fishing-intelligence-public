# Trip admission engine

Admission happens before fishing-quality comparison.

For every candidate option produce an `AdmissionResult` with:
- legal: PASS | FAIL | UNKNOWN;
- access: PASS | FAIL | UNKNOWN;
- time: PASS | FAIL | UNKNOWN;
- vessel_range: PASS | FAIL | UNKNOWN | NOT_REQUIRED;
- user_limits: PASS | FAIL | UNKNOWN | NOT_REQUIRED;
- critical_data: PASS | FAIL | UNKNOWN;
- result: ADMITTED | REJECTED | WITHHELD;
- reasons and evidence refs.

Rules:
1. A known hard-constraint failure -> `REJECTED`.
2. A missing dependency that is necessary to determine a hard constraint -> `WITHHELD` or overall `BLOCKED`, not optimistic admission.
3. A non-critical unknown may allow admission but normally reduces readiness to `PROVISIONAL`.
4. Do not use a fishing-quality preference to override a failed access/legal/time/range constraint.
5. Tide-dependent ramp admission requires a sufficiently verified tide prediction aligned to the ramp threshold's datum/context; unresolved conflicting tide values cannot produce `VERIFIED_CURRENT` access admission.
