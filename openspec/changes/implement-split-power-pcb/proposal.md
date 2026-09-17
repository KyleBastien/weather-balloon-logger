# Proposal: implement-split-power-pcb

> Marker: AUTO (autonomous mode; auto-approved, reviewable after the fact)

## Why

The schematic already captures the approved fixed-3s split-power architecture, but the PCB still lacks A2/R4 and retains stale 3V3/direct-UART OpenLog routing. This bounded pass makes the PCB, schematic, BOM, and authoritative layout documents agree while preserving the fixed mechanical and RF design.

## What Changes

- Add A2 with exact `WeatherBalloon:Pololu_S7V8F5_Carrier` footprint, top-side/direct-soldered, in the open left-side power area outside the LightAPRS body and RF reservations.
- Add R4 close to A1.5 and implement `UART_TX` → R4 → `OPENLOG_RXI`.
- Replace only stale A1/C1/C2 3V3 copper with `LOGGER_5V`; connect A2 SHDN/VIN to `PACK_SW`, GND to GND, and VOUT to `LOGGER_5V`.
- Preserve every existing footprint position, all unrelated routing, direct `PACK_SW` feeds to J2.1 and J5.1, the six exact LightAPRS exclusions, and the existing outline unless proven impossible.
- Update `docs/LAYOUT.md`, `docs/FOOTPRINT_AUDIT.md`, `docs/DECISIONS.md`, `docs/CHANGELOG.md`, and this change record; update PINOUT/BOM only if implementation reveals an actual discrepancy.
