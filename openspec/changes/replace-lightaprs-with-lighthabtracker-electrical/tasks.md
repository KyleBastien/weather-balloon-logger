# Tasks

- [x] Inspect current intent, schematic symbols/nets, and authoritative installed symbol pins.
- [x] Validate this bounded electrical-only proposal before editing.
- [x] Surgically update intent and schematic with exact refdes, pin order, nets, footprints, and intentional no-connects.
- [x] Update authoritative electrical documentation and constraints; record one-line rationale for each non-trivial decision and each intentional removal.
- [x] Verify all retained/new symbols against installed KiCad libraries.
- [x] Run ERC and repair every violation.
- [x] Run schematic legibility and reconcile every error-severity finding.
- [x] Run drift/intent consistency checks and resolve stale electrical references in the scoped docs.
- [x] Finish only when the bounded schematic pass is clean, while explicitly leaving PCB/layout/output synchronization for the later pass requested by the user.
