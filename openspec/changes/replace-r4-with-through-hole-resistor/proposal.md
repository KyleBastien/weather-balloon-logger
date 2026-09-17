# Proposal: replace-r4-with-through-hole-resistor

## Why

R4 must be a leaded part installed through drilled board holes rather than a surface-mount-only 0603 resistor so it is straightforward to hand assemble.

## What Changes

- Replace only R4 with the stock KiCad horizontal DIN0207 1/4 W axial footprint on 7.62 mm pitch.
- Keep its electrical value at 1 kΩ and preserve `UART_TX` to `OPENLOG_RXI` isolation.
- Reposition and locally reroute only what the larger through-hole body and pads require.
- Preserve all other footprints, the board outline, LightAPRS interface, power architecture, cutdown, and RF routing.
