# Replan admission

Re-admit **remaining** steps using the ordinary hard-constraint order:
legal -> access -> time -> vessel/range -> user operating limits -> critical data.

Each future step receives:
- prior status from current trip version;
- new status `RETAINED | REMOVED | ADDED | WITHHELD`;
- `AdmissionResult`;
- reason/evidence refs.

Rules:
1. A new hard failure removes the option.
2. A required but unknown dependency withholds the option.
3. Completed attempts are not re-admitted because they are history.
4. Do not restore an option solely because fishing elsewhere was blank.
5. Catch/blank outcomes may affect preferences/evidence, but cannot override a failed legal/access/time/range constraint.
6. Re-evaluate return feasibility after every sequence change.
7. If the return deadline cannot be met by any verified remaining sequence, result is `REPLAN_REQUIRED` with no operational continuation plan until an admissible sequence exists.
