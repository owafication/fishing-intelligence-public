# Global regional-pack generation

## Why it exists

Fishing regulation and operational authority is layered differently around the world. Some places split marine/freshwater or state/federal authority; some use fishing areas or special reserves; navigation, boating-safety, weather, tide and access authorities may be separate again. The plugin therefore resolves an authority stack instead of hard-coding one country's model.

## Runtime generation

When no adequate curated pack exists:

`request -> regional-pack-resolver -> authority stack -> regional-pack-generator -> GENERATED_PROVISIONAL pack -> verifier/admission -> planner`

A generated pack contains current source contracts and a coverage matrix for the authority domains that matter to the specific mode. It is bounded to place/water/mode/date/method/species context and has explicit invalidation/freshness rules.

## Reuse and promotion

Generated packs may be cached in the plugin's optional durable store, but material sources are rechecked before reuse. Repeated successful operation may produce a `RegionalPackCandidate` for developer review. Runtime generation never edits shipped source and never declares itself curated.

## Standalone behavior

The plugin remains standalone. It does not require a proprietary Fishing Intelligence backend. Generation uses host-visible web/reference capability when available. Without current reference access, the plugin can still work from user-supplied evidence and shipped packs, but current legal/access planning may become `RESEARCH_ONLY` or `BLOCKED` rather than being guessed.

## Per-option authority applicability

Source discovery is not enough. Every consequential authority observation is evaluated against the exact candidate option using `REQUIRED | CONDITIONAL | NOT_APPLICABLE | UNRESOLVED`. Spatial restrictions additionally preserve whether the planned route/area intersects the controlled geometry. A nearby marine forecast, protected area or navigation notice therefore cannot lower readiness merely because it was discovered. Material unresolved applicability remains conservative.
