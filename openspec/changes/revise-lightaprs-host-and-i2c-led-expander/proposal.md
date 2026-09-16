# Proposal: revise-lightaprs-host-and-i2c-led-expander

> Marker: AUTO (autonomous mode; auto-approved, reviewable after the fact)

## Why

The current 7-pin host abstraction, A0 cutdown assignment, UART-sunk LED, and two-pin RF header do not match the verified LightAPRS-W 2.0 physical interface. The revision must use the verified 11-position edge-header order, exposed A1/PB08 and A2/PB09 functions, discrete HF/VHF corner contacts, and an I2C LED expander while retaining default-off cutdown and all current budgets.

## What Changes

- Replace J2 with Connector_Generic:Conn_01x11 and map RAW, dual GND, A1/PB08 UART TX, A2/PB09 cutdown, 3V3, SCL, SDA, SCK, MISO, and MOSI in verified physical order.
- Add a PCF8574 on 3V3/GND with 100 nF decoupling, A0/A1/A2 address pins strapped low for address 0x20, SDA/SCL on the exposed host I2C bus, P0 driving D1 cathode active-low, and P1-P7 intentionally no-connect for future LEDs.
- Move CUTDOWN_CTRL from host A0 to A2/PB09 while preserving R2 and the intentional R3 reset-time pulldown.
- Replace J6 with two single-contact module RF endpoints, VHF to RF_APRS/J3 and HF to RF_WSPR/J4.
- Update schematic and all affected BOM, pinout, subsystem, specification, layout/development, constraint, decision, changelog, and firmware pin references so no stale A0/J6/UART-LED assumptions remain.
- Keep the PCF8574 plus OpenLog and all passive leakage within the existing 2 mA board-added idle budget; retain 3.3 V logic and existing OFF-leakage limits.
