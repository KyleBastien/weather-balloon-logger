# Proposal: convert-eight-logic-passives-to-tht

> Marker: AUTO (autonomous mode; auto-approved, reviewable after the fact)

## Why

Use the user-selected exact through-hole parts for the eight existing logic/passive references while preserving their established electrical behavior and leaving the already-routed PCB unchanged until a separate bounded conversion pass.

## What Changes

- Update schematic.intent.json and weather-balloon-logger.kicad_sch for R1–R3, C1–C3, D1, and U1 only, preserving all existing nets and pin functions.
- Set R1/R2/R3 to MFR-25FBF52-1K / -100R / -1M with the specified DIN0207 axial THT footprint.
- Set C1 to C322C475K5R5TA with WeatherBalloon:KEMET_C322C475K5R5TA; set C2/C3 to C315C104K5R5TA with WeatherBalloon:KEMET_C315C104K5R5TA.
- Set D1 to WP710A10SGC with LED_THT:LED_D3.0mm.
- Replace U1’s schematic symbol with Interface_Expansion:PCF8574P, value/MPN PCF8574N, and Package_DIP:DIP-16_W7.62mm, retaining identical pins, address straps, I2C nets, LED output, and intentional no-connects.
- Update docs/BOM.md, docs/FOOTPRINT_AUDIT.md, and only directly necessary current docs with one-line rationales and an explicit statement that PCB conversion is pending, not complete.
- Do not edit the PCB, footprint library, outputs, firmware, Q1, or add parts.
