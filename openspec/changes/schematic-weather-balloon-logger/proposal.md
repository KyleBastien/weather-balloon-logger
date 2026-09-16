# Proposal: schematic-weather-balloon-logger

## Why

Capture the approved weather-balloon carrier architecture as a deterministic KiCad schematic while preserving the fixed BOM, verified symbol pin contracts, power/leakage budgets, host occupied-pin rules, and intentional absences.

## What Changes

- Create schematic.intent.json with every fixed-BOM refdes, canonical installed lib_id, exact BOM value and footprint, subsystem group, named net, and deliberate no-connect.
- Draft weather-balloon-logger.kicad_sch from the validated intent rather than hand-authoring geometry.
- Assign the exposed LightAPRS-W interface pins consistently: switched VIN, GND, 3V3, SERCOM UART, write LED control, and default-off cutdown control, without reusing documented occupied host pins.
- Create docs/PINOUT.md matching the schematic assignments and close the reopened GPIO-logic and strap-leakage revisits.
- Record schematic-stage decisions and verification in docs/DECISIONS.md and docs/CHANGELOG.md.
