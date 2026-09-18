# Stage 6 output package

Generated from the current Weather Balloon Logger KiCad design.

## Render files

- `board.svg` is the standard Copperhead PCB plot.
- `renders/weather-balloon-logger.svg` is the schematic render.
- `renders/board-full-color.svg` is a board-fitted top view showing front copper in red, back copper in blue, production front silkscreen, plated holes, and the board outline. Engineering-only User-layer notes are deliberately omitted so assembly labels remain readable.
- The production front-silkscreen outputs include the 7.50 x 11.25 mm
  coffee-cup/weather-balloon `G1` artwork in the unobstructed lower-center area.
- `renders/board-fit-check-1to1.pdf` is a black-and-white, true-scale top
  fabrication/silkscreen print with actual pad and slot shapes. Print it at
  **100% / Actual Size** (never “Fit”) and verify the 80.0 x 78.5 mm board
  outline with a ruler before using it for the exact-parts fit check.

## Qualification hold

The PCB now uses real library or documented project footprints and contains no SMD pads. Do not release it for fabrication until the documented 1:1 physical-fit, LightAPRS mating-geometry, RF-impedance, cutdown thermal/SOA, environmental, leakage, and sourcing checks are closed.

Follow `../docs/FABRICATION_READINESS.md` for the authoritative release gates.
Do not upload the entire `gerbers/` directory: it is a complete review export
and includes engineering layers that normally do not belong in a manufacturer
upload. Build and independently inspect a fabricator-specific ZIP after the
release gates close.

`BOM.csv` is generated from the schematic's controlled MPN fields by
`../scripts/export_bom.ps1` and reflects all 23 populated through-hole refdes.
All rows now have exact MPNs, but the BOM is not a procurement release until
the physical-fit and mating-part checks in the readiness checklist pass.
`jlcpcb-bom.csv` is intentionally not an assembly release because this board is
intended for home through-hole assembly.
