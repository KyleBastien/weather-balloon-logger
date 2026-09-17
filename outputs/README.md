# Stage 6 output package

Generated from the current Weather Balloon Logger KiCad design.

## Render files

- `board.svg` is the standard Copperhead PCB plot.
- `renders/weather-balloon-logger.svg` is the schematic render.
- `renders/board-full-color.svg` is a board-fitted top view showing front copper in red, back copper in blue, production front silkscreen, plated holes, and the board outline. Engineering-only User-layer notes are deliberately omitted so assembly labels remain readable.

## Qualification hold

The PCB now uses real library or documented project footprints and contains no SMD pads. Do not release it for fabrication until the documented 1:1 physical-fit, LightAPRS mating-geometry, RF-impedance, cutdown thermal/SOA, environmental, leakage, and sourcing checks are closed.

BOM.csv consolidates identical MPNs and retains the UNVERIFIED marker in the MPN field.
