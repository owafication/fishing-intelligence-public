# Species identification input

## Purpose
Allow image/vision-assisted species identification to accelerate recording without making Fishing Intelligence a mandatory computer-vision product or silently promoting a model guess to fact.

## Identification states
`UNIDENTIFIED | PROPOSED_IDENTIFICATION | USER_CONFIRMED | AUTHORITY_CONFIRMED | CONFLICTING`.

A host vision model or specialist may produce a proposed species with source/model identity and, when available, confidence/evidence notes. The proposal is not a accepted confirmed species until accepted under the recording workflow.

## Length/size
Image-derived length is accepted only when the method has a defensible scale/calibration. Otherwise record `UNAVAILABLE` or an explicitly approximate estimate; never fabricate measurement precision from an uncalibrated photo.

## Offline/import
Historic photo identification is an import/enrichment operation. Original photo time/location metadata is source evidence only when actually present and must preserve privacy/EXIF handling rules.

## Dependency
Core planning, recording and learning remain available when no image/vision capability exists.
