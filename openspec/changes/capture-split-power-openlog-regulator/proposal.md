# Proposal: capture-split-power-openlog-regulator

> Marker: AUTO (autonomous mode; auto-approved, reviewable after the fact)

## Why

Implement the already approved fixed-3s split-power architecture in the schematic: retain direct PACK_SW feeds for LightAPRS and cutdown, power OpenLog from the dedicated S7V8F5 LOGGER_5V rail, and limit UART back-power during regulator startup or brownout.

## What Changes

- Add A2 using `Connector_Generic:Conn_01x04` and `WeatherBalloon:Pololu_S7V8F5_Carrier`, with pins 1 SHDN, 2 VIN, 3 GND, and 4 VOUT.
- Connect A2.1/A2.2 to `PACK_SW`, A2.3 to `GND`, and A2.4 to new `LOGGER_5V`; preserve J2.1 and J5.1 directly on `PACK_SW`.
- Move A1.3, C1.1, and C2.1 from `3V3` to `LOGGER_5V`, retaining their ground connections.
- Add R4 = 1k, 0603, between J2.3 `UART_TX` and new `OPENLOG_RXI` at A1.5 to limit startup/brownout back-power.
- Preserve A1 pins 1/4/6 and all other existing intentional no-connects and interfaces.
- Update `schematic.intent.json`, the KiCad schematic, BOM, pinout/current-architecture documentation, changelog/decisions, and this change's OpenSpec tasks consistently.
- Record the unchanged PCB as intentionally pending a later A2 placement and LOGGER_5V/OPENLOG_RXI routing pass; do not edit PCB, footprint library, constraints, firmware, outputs, or historical proposals.
