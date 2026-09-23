# Tasks

- [x] Inspect the current intent and exact schematic s-expressions.
- [x] Surgically remove J1/A2 and the VBATT/LOGGER_5V connectivity from intent and schematic.
- [x] Reconnect the five specified supply pins to 3V3 without changing other nets or component choices.
- [x] Update docs/BOM.md, docs/SPEC.md, docs/SUBSYSTEMS.md, docs/PINOUT.md, and the affected constraint records with one-line rationales and the bench-validation hold.
- [x] Remove J1/A2 from the PCB and route direct 3V3 to A1/C1/C2 without disturbing UART, LED, cutdown, logo, or module keepouts.
- [x] Synchronize BOM/order/readiness/audit records and regenerate all tracked review and manufacturing outputs.
- [x] Verify ERC, DRC, zero unconnected pads, zero SMD pads, schematic legibility, drift, constraints, workbook rendering, and the fabrication-source audit.
- [x] Confirm firmware is unchanged and retain the explicit no-fabrication hold for provisional LightHAB mechanics and 3V3 capacity.
