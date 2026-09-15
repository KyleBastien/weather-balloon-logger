# Proposal: recover-part-selection-weather-balloon-logger

## Why

Complete the interrupted stage-3 part-selection artifact with a capturable, power-budget-aware fixed BOM and explicit installed KiCad symbol/pin evidence.

## What Changes

- Rewrite `docs/BOM.md` as a complete artifact using exactly `| Refdes | Value | Footprint | MPN | Rationale |`.
- Keep one row per individual refdes and component-only Value fields; move all descriptive prose to Rationale.
- Mark every selected MPN UNVERIFIED and state datasheet-verifiable electrical, leakage/quiescent, environmental, footprint, and availability acceptance checks.
- Record installed KiCad symbol availability and authoritative package-pin contracts for every IC, module representation, connector, switch, transistor, LED, resistor, and capacitor.
- Preserve unresolved host GPIO assignments until the LightAPRS-W/ESP32 strapping and occupied-pin tables are checked.
- Update `docs/CHANGELOG.md` and `docs/DECISIONS.md` with the completed recovery and its rationale.
