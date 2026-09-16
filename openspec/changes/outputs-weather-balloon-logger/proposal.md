# Proposal: outputs-weather-balloon-logger

## Why

Create the requested Stage 6 manufacturing/output bundle while preserving the documented fabrication and procurement qualification holds.

## What Changes

- Create `outputs/` containing JLC-profile Gerber layers and drill files.
- Export the board outline as DXF and STEP.
- Export schematic and PCB SVG renders and place copies in the output package.
- Generate `outputs/BOM.csv` from `docs/BOM.md`, consolidated by identical MPN with `refdes`, `MPN`, and `qty`; retain the documented UNVERIFIED status rather than implying procurement approval.
- Update `docs/CHANGELOG.md` and `docs/DECISIONS.md` with the exact exports, verification result, and the intentional non-fabrication-ready/non-procurement-ready qualification hold.
