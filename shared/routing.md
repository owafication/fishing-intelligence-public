# Capability selection

## Positive fit
Use Fishing Intelligence for fishing-trip planning, opportunity comparison, target/species strategy, prospect timing, fishing access/regulations, tackle strategy, catch/effort recording, fishing-history analysis, active-trip replanning and fishing-specific travel/guide context.

## Negative space
Do not use it merely because a prompt mentions a boat, weather, travel, food or shopping. It does not provide certified marine navigation, emergency response, general boating navigation, vessel maintenance, ecommerce, travel booking, payments/CRM or general recipe management.

## Primary workflow
Choose one primary skill for each turn: `fishing-planner | fishing-replanner | fishing-recorder | fishing-analyst | fishing-verifier`. Shared contracts provide common rules; they do not create additional state owners.

For out-of-scope tasks, return the bounded fishing context needed by another capable system instead of pretending to perform the external task.
