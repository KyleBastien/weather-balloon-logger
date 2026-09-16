# Proposal: devplan-weather-balloon-logger

## Why

Stage 8 requires a hardware development plan that turns the existing schematic, layout draft, constraints, and qualification holds into a safe and repeatable prototype bring-up and ordering sequence without implying fabrication readiness.

## What Changes

- Create `docs/DEVPLAN.md` with ordered unpowered, current-limited power, host/OpenLog, LED/UART, RF, and cutdown bring-up steps.
- Define named test locations using existing refdes and net names, including what to meter first and explicit pass/stop criteria.
- Add a constraint-linked risk register covering pack voltage/UVLO, the 2 mA idle limit, OpenLog 3V3 load, cutdown default-off/leakage/thermal performance, RF impedance/keepout/SMA orientation, cold operation, and draft footprint/MPN qualification.
- Add a staged prototype order plan that verifies footprints and MPNs before PCB fabrication, separates low-risk bench quantities from hazardous cutdown testing, and retains the current fabrication/procurement hold until qualifications pass.
- Update `docs/CHANGELOG.md` and `docs/DECISIONS.md` with the Stage 8 documentation decision and one-line rationale.
