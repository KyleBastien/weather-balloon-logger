# Proposal: refresh-verified-design-exports

> Marker: AUTO (autonomous mode; auto-approved, reviewable after the fact)

## Why

The verified source design and synchronized documentation are current, but all deterministic manufacturing, mechanical, BOM, and SVG artifacts must be regenerated from that exact state and accepted only after every verification gate is clean.

## What Changes

- Regenerate `.copperhead/renders/board.svg` and `.copperhead/renders/weather-balloon-logger.svg` from the unchanged PCB/schematic.
- Refresh `weather-balloon-logger.svg`, `outputs/board.svg`, `outputs/renders/weather-balloon-logger.svg`, Gerbers, drill files, STEP, outline DXF, and BOM artifacts using deterministic export tools.
- Preserve the current schematic, PCB, intent, libraries, constraints, firmware, BOM source, design documentation, topology, footprints, and zero-SMD all-through-hole implementation.
- Include already-synchronized documentation changes with the refreshed exports in one commit only after clean verification.
