# Proposal: refresh-current-pcb-exports

> Marker: AUTO (autonomous mode; auto-approved, reviewable after the fact)

## Why

The committed PCB has changed since the prior output package, so its deterministic PCB SVG and bundled exports must be regenerated without altering any design source or relaxing fabrication holds.

## What Changes

- Regenerate the PCB SVG in `.copperhead/renders/` from `weather-balloon-logger.kicad_pcb`.
- Refresh `outputs/board.svg` and only bundled deterministic export artifacts produced by the authorized export workflow.
- Make no layout, electrical, source, documentation, BOM, firmware, library, or constraint changes.
- Preserve every existing fabrication and procurement qualification hold.
