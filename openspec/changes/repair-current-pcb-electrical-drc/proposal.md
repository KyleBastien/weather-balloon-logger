# Proposal: repair-current-pcb-electrical-drc

> Marker: AUTO (autonomous mode; auto-approved, reviewable after the fact)

## Why

The current board has electrical shorts, clearance violations, track crossings, dangling stubs, and two named connectivity gaps that must be repaired locally while preserving placement, outline, RF routing, and all non-PCB artifacts.

## What Changes

- Edit only `weather-balloon-logger.kicad_pcb`.
- Remove obsolete dangling copper and locally reroute the reported crossings, shorts, and clearance failures using existing net widths.
- Close the reported `I2C_SDA` and `CUTDOWN_DRIVE` B.Cu segment gaps without altering footprint placement or preserved RF routes.
- Leave silkscreen and courtyard warnings unchanged and do not commit.
