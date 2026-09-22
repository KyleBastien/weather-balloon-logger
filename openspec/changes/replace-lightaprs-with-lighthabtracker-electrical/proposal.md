# Proposal: replace-lightaprs-with-lighthabtracker-electrical

> Marker: AUTO (autonomous mode; auto-approved, reviewable after the fact)

## Why

The carrier electrical capture must match the requested LightHABTracker 1.0 interfaces while deferring all PCB and mechanical reconciliation. The pass must preserve the existing OpenLog and S7V8F5 logger supply, explicitly mark LightHAB VBATT switching and pyro capability unverified, and avoid retaining obsolete LightAPRS RF, I2C-expander, or MOSFET-driver circuitry.

## What Changes

- Replace the LightAPRS-W 2.0 electrical interface with LightHABTracker 1.0 J2 as a directly soldered through-hole 1x9 connector ordered A1, A2, 3V3, GND, SCL, SDA, SCK, MISO, MOSI.
- Recreate J1 as the two-pin LightHAB VBATT/GND power interface feeding A2 VIN and SHDN, with onboard switching explicitly unverified.
- Recreate J3 as the two-pin LightHAB OUT1/GND pyro interface and pass it directly to retained J5 JST-XH without claiming a verified pyro current rating.
- Retain A1 DEV-13955, A2 S7V8F5, C1/C2, D1, R1, and R4; use J2.1 A1/PB08 for UART_TX through R4 to OPENLOG_RXI.
- Use J2.2 A2/PB09 as active-low LED_N; connect 3V3 through R1 and D1 to LED_N and add through-hole R2=100k from LED_N to 3V3 for reset-default-off behavior.
- Mark J2.5-J2.9 SCL/SDA/SCK/MISO/MOSI as intentional carrier no-connects.
- Remove SW1, U1, U2, Q1, C3, C4, C5, R3, J4, J6, J7 and obsolete PACK_IN/PACK_SW/I2C-expander/cutdown-driver/RF nets from schematic and intent.
- Update schematic.intent.json, weather-balloon-logger.kicad_sch, docs/PINOUT.md, docs/BOM.md, docs/SPEC.md, docs/SUBSYSTEMS.md, constraints/decision/changelog records as required for electrical consistency. Leave weather-balloon-logger.kicad_pcb, mechanical/layout documents, and generated outputs unchanged for a later pass.
- Keep every populated component directly soldered through-hole with no SMD pads.
