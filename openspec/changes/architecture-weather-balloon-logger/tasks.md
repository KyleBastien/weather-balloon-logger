# Tasks

- [ ] Write docs/SUBSYSTEMS.md with prose diagram and one section per subsystem, citing SPEC § and constraint keys.
- [ ] State 3s vs 4s voltage-only upsizing; host VIN ASSUMED 3.5–12 V still unconfirmed.
- [ ] State cutdown: low-side logic-level FET + intentional gate pulldown; IRLZ44N and 3.3 V relay not committed.
- [ ] State OpenLog on 3V3 unless LDO current-share exceeded; write LED on 3.3 V GPIO not pack.
- [ ] Record architecture decisions/constraints; check_drift after docs; finish when docs match SPEC.
