# Proposal: migrate-openlog-to-lighthab-3v3

> Marker: AUTO (autonomous mode; auto-approved, reviewable after the fact)

## Why

The user accepts direct OpenLog power from LightHAB J2.3 3V3, eliminating the separate VBATT-fed Pololu regulator path and its obsolete fixed-5V claims while retaining a bench-validation gate for the unverified host-rail capacity.

## What Changes

- Remove J1, A2, VBATT, and LOGGER_5V from schematic intent and schematic capture.
- Connect A1.3, C1.1, C2.1, R1.1, and R2.1 to the existing J2.3 3V3 net.
- Preserve UART, active-low LED, J3/J5 OUT1, GND, intentional no-connects, and through-hole choices.
- Update BOM, specification, subsystem, pinout, and affected constraint entries to describe direct LightHAB 3V3 power.
- Record SparkFun OpenLog VCC as 3.3–12 V, recommended 3.3–5 V, with about 20–23 mA active-write current; retain LightHAB 3V3 capacity as an accepted assumption requiring bench validation.
- Remove J1/A2 from the PCB, route J2.3 directly to A1/C1/C2, update the 3V3 silkscreen label, and regenerate all review/manufacturing outputs.
- Synchronize the BOM, fit-check order workbook, readiness checklist, footprint audit, and deterministic build/export scripts; leave firmware and historical change records intact except for new append-only entries.
