# Proposal: final-pcb-mechanical-legend-cleanup

> Marker: AUTO (autonomous mode; auto-approved, reviewable after the fact)

## Why

Clear the remaining mechanical courtyard, PTH-inside-courtyard, and front-silkscreen DRC findings while preserving the clean electrical topology, fixed board outline, RF routing, pads, fabrication geometry, and zero-unconnected state.

## What Changes

- Move only C4 and C5 enough to eliminate their J5 courtyard overlaps and PTH-inside-courtyard findings, rerouting only their LOGGER_5V and GND connections.
- Adjust only F.SilkS geometry in both project KEMET footprint library files and synchronize the embedded C1-C5 board footprint silk so it clears each footprint's own pad solder-mask openings.
- Reposition or hide only reference text and local silk strokes responsible for the listed U1/R4, J5/C4/C5, U2/R3/Q1, and A2/U2 collisions.
- Do not alter the schematic, intent, BOM, scripts, board outline, RF routes, functional topology, pads, courtyards, fabrication/fab geometry, or commit history.
