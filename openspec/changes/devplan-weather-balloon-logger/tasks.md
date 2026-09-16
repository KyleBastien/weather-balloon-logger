# Tasks

- [ ] Read any existing hardware and firmware development-plan material and preserve their distinct scopes.
- [ ] Write `docs/DEVPLAN.md` with prerequisites, instruments, ordered bring-up, test locations, first-meter checks, stop conditions, risk register, and prototype order gates.
- [ ] Use exact schematic net names and refdes; do not invent uncaptured test-point components.
- [ ] Keep every CopperheadDraft footprint and BOM MPN explicitly UNVERIFIED and block fabrication/procurement until the relevant acceptance checks pass.
- [ ] Append the Stage 8 entry to `docs/CHANGELOG.md` and record the development-plan decision in `docs/DECISIONS.md`.
- [ ] Run ERC, DRC, drift, and schematic legibility checks to confirm documentation work did not desynchronize or disturb the design.
- [ ] Finish only after all verification obligations pass.
