# Units, timezone and datum contract

Global planning requires explicit normalization rather than implicit conversion.

For consequential values preserve:
- source value/unit;
- normalized comparison value/unit when conversion is needed;
- local timezone and date;
- coordinate reference/datum when spatial precision matters;
- tide/water-level datum/station when comparing heights or access thresholds;
- conversion method and uncertainty when material.

Rules:
- Never compare heights from incompatible/unknown datums as if directly equivalent.
- Never shift a tide/closure/forecast event between dates without resolving local timezone.
- User-preferred display units do not change source source context.
- Unknown datum/timezone stays unknown and may downgrade or block the dependent decision.
