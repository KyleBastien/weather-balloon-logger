# Proposal: document-split-power-openlog-regulator

> Marker: AUTO (autonomous mode; auto-approved, reviewable after the fact)

## Why

The approved architecture fixes the flight pack at exactly three series L91 cells and separates the OpenLog supply from the LightAPRS 3V3 rail using a dedicated Pololu S7V8F5 fixed-5-V module. Current authoritative documentation and constraints still describe optional 4S operation, 3V3-powered OpenLog, and obsolete 2 mA/1.85 mA budgets, so they must be superseded without changing hardware design files in this bounded pass.

## What Changes

- Fix the battery architecture at exactly 3 series Energizer L91 cells, 3.0–5.4 V, while preserving direct switched PACK_SW feeds to LightAPRS RAW/J2.1 and cutdown J5.1.
- Add Pololu S7V8F5 item 2123 as the selected OpenLog-only fixed 5 V buck-boost module: VIN and SHDN to PACK_SW, GND to GND, VOUT to LOGGER_5V, and A1 VCC documented on LOGGER_5V.
- Record its 2.7–11.8 V input, fixed 5 V output, <0.2 mA quiescent current, 0.1-inch four-pin direct-solder straight-header interface, lack of reverse-polarity protection, and unverified temperature rating requiring cold qualification.
- Supersede current 4S, 3V3-powered OpenLog, 2 mA board-idle, and 1.85 mA OpenLog-idle statements with OpenLog idle ≤7 mA, write ≤25 mA, regulator Iq ≤0.2 mA, board-added idle ≤8 mA, and board-added active/write peak ≤30 mA.
- Preserve the PCF8574 allocation, safety leakage limits, four-hour demand ≤800 mAh, and required usable capacity ≥1600 mAh under the actual cold/load profile.
- Update only current authoritative docs, .copperhead/constraints.json, BOM, decisions/changelog, and this change’s OpenSpec files; do not edit schematic, PCB, footprint libraries, outputs, firmware, or old historical proposals.
