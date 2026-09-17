# Proposal: add-pololu-s7v8f5-carrier-footprint

> Marker: AUTO (autonomous mode; auto-approved, reviewable after the fact)

## Why

The approved split-power architecture needs a verified project-local land pattern for Pololu S7V8F5 item 2123 before later schematic and PCB implementation; this bounded pass records official geometry and top-view pin order without changing live hardware files.

## What Changes

- Audit and, only if necessary, correct `WeatherBalloon:Pololu_S7V8F5_Carrier` for top-side direct solder, the official 11.43 x 16.51 mm body, four 1.0 mm-drill plated pads at 2.54 mm pitch, a centered row 1.27 mm from the edge, and top-view left-to-right pads 4 VOUT, 3 GND, 2 VIN, 1 SHDN.
- Update `library/README.md`, `docs/BOM.md`, and `docs/FOOTPRINT_AUDIT.md` to reserve future refdes A2, assign the exact footprint, and correct C1/C2 future `LOGGER_5V` and approved current-limit prose.
- Update only this change's task checklist.
- Do not modify schematic, PCB, schematic intent, constraints, outputs, firmware, or historical proposals.
