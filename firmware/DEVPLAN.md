# LightHABTracker firmware integration plan

## Status and baseline

This repository contains a reviewed integration scaffold, not a compiled LightHAB flight image. Apply it to the official `lightaprs/LightHABTracker-1.0` source at inspected commit `797b78d120b0e844f60798b88dfa3735f27e89da`, then build and test with the project's actual Arduino SAMD board package. Re-check the upstream default branch before deliberately changing that pin.

The inspected source used D4/D5 for the two pyro channels and defaulted OUT1 cutdown duration to 10 seconds. A1/PB08 and A2/PB09 appeared unused, but this is an inspection result—not a guaranteed vendor interface contract.

## Pin contract

`docs/PINOUT.md` is authoritative. `tools/generate_pins.py` generates `include/pins.h` and stops if either required assignment changes:

- J2.1 A1/PB08: polling SERCOM4/PAD0 UART TX to OpenLog through R4.
- J2.2 A2/PB09: active-low activity LED. Write HIGH before `pinMode(..., OUTPUT)`.

No RX path is configured. SCL, SDA, SCK, MISO, and MOSI are not used by the carrier.

## Integration sequence

1. Check out the pinned upstream commit in a separate build tree and record the exact board package/tool versions.
2. Reconfirm A1/PB08 and A2/PB09 are unclaimed across source, variant files, and libraries.
3. Merge the OpenLog initialization and record-writing calls into the existing LightHAB setup/loop without replacing GPS, APRS, WSPR, telemetry, or vendor cutdown logic.
4. Initialize the LED HIGH-before-output before any potentially blocking work. Pulse it LOW only around attempted log writes.
5. Replace `telemetry_stub` with fields already produced by LightHAB. Keep buffers bounded and avoid heap allocation in the flight loop.
6. Build with warnings enabled and retain the complete build log and binary hash.

## Bench acceptance

1. Scope A2 through power-on, bootloader, reset, brownout, and firmware update; it must not glitch low before intended use.
2. Confirm A1/PB08 is SERCOM4/PAD0, idle-high, 3.3 V logic, 9600 baud 8-N-1 unless the installed OpenLog configuration is deliberately changed.
3. Confirm the header and one `0,0,0,READY` test row appear on a FAT32 microSD card. Verify the LED is off at reset/idle and pulses during the attempted write.
4. Repeat with the logger unplugged and its card missing/full/corrupt; GPS, APRS, WSPR, and LightHAB's own pyro logic must remain safe and responsive.
5. Verify both existing LightHAB OUT channels using inert dummy loads only. Do not infer pyro current capability from the carrier's direct pass-through.
6. Run a four-hour mission rehearsal at the intended battery, temperature, radio duty cycle, and logging interval, then validate the complete log.

## Release blockers

- Exact upstream build environment and successful compiled integration.
- Vendor or measured confirmation that A1/PB08 and A2/PB09 are safe to use.
- Installed OpenLog baud/current behavior and cold operation.
- Reset/brownout LED captures and logging fault-injection results.
- Independent validation of LightHAB OUT1 voltage/current capability and safety behavior.
