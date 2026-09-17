# Proposal: refresh-all-verified-design-exports

> Marker: AUTO (autonomous mode; auto-approved, reviewable after the fact)

## Why

Refresh every existing deliverable from the current verified KiCad sources without changing schematic, PCB, topology, footprints, placement, routing, or readable silkscreen.

## What Changes

- Regenerate `.copperhead/renders/board.svg` and `.copperhead/renders/weather-balloon-logger.svg`.
- Regenerate `outputs/board.svg`, `outputs/renders/board-full-color.svg`, and `outputs/renders/weather-balloon-logger.svg`.
- Regenerate all existing Gerber and drill artifacts under `outputs/gerbers/`.
- Regenerate `outputs/board.step`, the existing outline DXF, and all existing BOM artifacts.
- Do not modify `weather-balloon-logger.kicad_sch`, `weather-balloon-logger.kicad_pcb`, libraries, intent, constraints, firmware, or authoritative design documentation.
- Preserve the verified all-through-hole design and all functional/readable silkscreen exactly.
