# Experiment engine

The Experiment Engine defines a `PROPOSED` fishing experiment plan intended to reduce uncertainty in a personal hypothesis. It is a contract-supported reasoning workflow, not a separate durable experiment master.

Inputs: current hypothesis, competing explanations, accepted attempts/effort, context dimensions, hard constraints and available windows. Prefer tests that vary one material uncertain dimension while holding other feasible dimensions reasonably comparable. Avoid selecting only the historically successful condition.

Outputs: `question`, `comparison_needed`, `target_context`, `control_context` when feasible, required observations, stopping/effort target, confounders and what result would support/weaken the hypothesis.

If the user accepts the experiment for execution, create/modify an ordinary FishingTrip through normal planning/admission and version rules. An experiment suggestion is not a causal conclusion.
