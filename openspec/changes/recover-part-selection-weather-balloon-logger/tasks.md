# Tasks

- [ ] Search installed symbols for every active/module/connector part and confirm each selected lib_id with `symbol_pins`.
- [ ] Rewrite the complete BOM with the exact five-column header, one row per refdes, value-only Value cells, and UNVERIFIED MPN acceptance checks.
- [ ] Re-read the entire BOM and audit format, completeness, symbol/pin evidence, and all quiescent/leakage/current budgets.
- [ ] Record the recovery in the changelog and document non-trivial selection/intentional-absence decisions.
- [ ] Run `check_drift` only after the full-file audit and resolve every applicable finding before finish.
