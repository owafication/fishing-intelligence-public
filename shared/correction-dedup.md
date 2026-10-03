# Correction and deduplication semantics

## Corrections
When a user corrects an accepted record, preserve the stable record ID, advance version monotonically, record the correction reason/source, and retain the prior version in history. Example: correcting 08:03 to 08:30 is version 2 of the catch, not a second catch.

## Invalid observations
Use `INVALID` when evidence establishes that an accepted record should no longer participate in analysis. Do not erase history merely to improve statistics. Privacy-erasure requests are a separate authorised storage operation and must follow provider capabilities.

## Duplicates
- Deterministic source context identity: may classify duplicate.
- Heuristic similarity: flag for review only.
- Never auto-collapse two user-entered catches solely because time/location/species are close.

## Concurrency
A mutation supplied with stale `expectedRevision` must fail rather than overwriting a newer correction.
