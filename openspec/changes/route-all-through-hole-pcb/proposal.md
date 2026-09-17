# Proposal: route-all-through-hole-pcb

> Marker: AUTO (autonomous mode; auto-approved, reviewable after the fact)

## Why

The PCB has been converted to all-through-hole components but still contains stale copper and vias from former SMD locations, leaving the moved and newly added circuitry needing a clean, connected, DRC-compliant routing pass.

## What Changes

- Modify only `weather-balloon-logger.kicad_pcb`.
- Remove stale copper and vias associated with former SMD locations for U1, C1-C3, R1-R3, D1, and Q1.
- Route the moved through-hole U1, C1-C3, R1-R3, D1, and Q1 plus new U2, C4, and C5 using the existing net names.
- Preserve the LightAPRS zone, H1-H4, J2/J6/J7, A1/A2, J1/J3-J5/SW1, RF paths, and board outline; permit only a small local placement adjustment if routing cannot otherwise satisfy DRC.
- Maintain minimum widths: CUTDOWN_DRAIN 1.5 mm, PACK_SW 0.8 mm, LOGGER_5V 0.5 mm, 3V3 0.4 mm, and signals 0.25 mm.
- Keep Q1 close to J5 and preserve the split-power and default-off cutdown architecture.
- Do not modify schematic, intent, BOM, libraries, documentation, scripts, outputs, firmware, or commit history.
