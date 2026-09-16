# Firmware development plan

## Status

The selected firmware environment is the Arduino SAMD core for ATSAMD21G18, using its vendor CMSIS device definitions for polling SERCOM4 TX. No Arduino board package, LightAPRS-W board variant, compiler, or firmware-build action is exposed in this Copperhead run, so this scaffold was **not compiled here**. Do not interpret source review as a passing build.

## Pin-source contract

`docs/PINOUT.md` is authoritative. `tools/generate_pins.py` generates `include/pins.h` and stops if the required J2 assignments change. J2.4 A2/PB09 is CUTDOWN_CTRL; J2.3 A1/PB08 is SERCOM4/PAD0 UART_TX. No RX pin is configured. Shared J2.7/J2.8 SCL/SDA are reserved for the PCF8574T LED expander; occupied GPS, radio, SPI, RESET, and SWD pins remain untouched.

## UART qualification default

The scaffold uses 9600 baud because it is a conservative OpenLog configuration default, not because the installed module has been verified. Before flight, confirm the actual OpenLog configuration and either retain 9600 or update the documented constant, regenerate `pins.h`, and test the complete logger path. UART is 8-N-1, polling, TX-only. The activity LED is no longer tied to UART; firmware must command PCF8574T P0 low/high around the intended indication, and the LED still cannot prove SD media commit.

## Happy-path acceptance

1. On reset, verify Q1 gate remains low through startup; `cutdown::init_safe()` must remain the first application-level call.
2. Build against the exact LightAPRS-W 2.0 Arduino SAMD board variant and confirm PB08 function-D maps to SERCOM4/PAD0 without colliding with upstream firmware.
3. Connect a qualified 3.3 V OpenLog and confirm the header plus one `0,0,0,SAFE` row appear on the card.
4. Add and test the PCF8574T transaction: initialize address 0x20 with all outputs high, drive P0 low/high around the desired write indication, and confirm D1 is dark after reset and at idle.
5. Verify GPS, APRS, WSPR, I2C, and SPI functions remain operational.

## Before flight

- Add an upstream build target, startup/linker configuration, warnings-as-errors, and CI build using the exact LightAPRS-W board package.
- Replace the telemetry stub with real GPS/flight records and add bounded scheduling plus write-error observability.
- Add cutdown arming interlocks, altitude/time validation, a hard maximum-on timer no greater than 30 s, one-shot latching, reset/brownout tests, and explicit ground-test mode.
- Bench-test at 3.0–7.2 V pack conditions and the intended temperature range while preserving the 200 mA mean-flight and board leakage budgets.
- Confirm OpenLog maximum idle current is no greater than 1.85 mA, PCF8574T maximum idle current is no greater than 100 µA, remaining leakage is no greater than 50 µA, and the host 3V3 regulator has sufficient peak-current margin.
