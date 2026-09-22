# Generated review outputs

These files reflect the LightHABTracker carrier source at the current commit. They are **review artifacts, not a fabrication release** because the tracker interface and mounting geometry are provisional.

## Drawings

- `board.svg`: standard top board plot.
- `renders/weather-balloon-logger.svg`: schematic plot.
- `renders/board-full-color.svg`: colored top view including copper, through-hole pads, silkscreen, outline, and the provisional LightHAB envelope/keepouts.
- `renders/board-green-top.png`: flat green-board contrast render with no 3D component models.
- `renders/board-fit-check-1to1.pdf`: true-scale fit sheet. Print at 100% / Actual Size and verify the 90.0 × 80.0 mm outline before use.
- `board.step`: board geometry export; component-model completeness is not required for this fit stage.

The front silkscreen includes the coffee artwork and the required `UNVERIFIED LIGHTHAB FIT - DO NOT FABRICATE` warning.

## BOM and order list

- `BOM.csv` is generated from schematic MPN fields and contains 12 populated through-hole references.
- `jlcpcb-bom.csv` is a convenient grouped reference only; this project is intended for hand assembly and is not an assembly-service release.
- `fit-check-order-list.xlsx` separates safe buy-now items from held interfaces/fabrication. The three PNG files are visual checks of every worksheet.

## Gerbers

`gerbers/` is an engineering review export that also contains empty paste and back-silkscreen plots. Do not upload it wholesale. After the measured fit gate passes, create and independently inspect a fabricator-specific ZIP containing only the requested copper, mask, front silk, outline, drill, and job files.

See `../docs/FABRICATION_READINESS.md` for the remaining gates.
