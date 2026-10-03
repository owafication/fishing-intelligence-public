# Import staging contract

Imported fishing history is untrusted/candidate data until interpreted.

## States
`CANDIDATE | ACCEPTED | REJECTED | DUPLICATE | CONFLICTING`.
Only `ACCEPTED` candidates may create/update accepted fishing records.

## Source context keys
Prefer deterministic source identity such as external record ID, file hash + row/item index, photo hash, GPX feature ID or another source-stable key. Preserve original source type and import batch.

## No silent promotion
Parsing success does not prove semantic correctness. Ambiguous species, timestamps, coordinates, units or record meaning remain candidate warnings until resolved.

## Duplicate handling
A deterministic source context match can classify `DUPLICATE`. Similar place/time/species is only a heuristic flag and must return `REVIEW_REQUIRED`; do not auto-merge because multiple fish or attempts can legitimately be similar.
