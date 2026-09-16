# Proposal: layout-draft-weather-balloon-logger

## Why

Create the first physical PCB draft from the completed stage-4 schematic, preserving the power, RF, leakage, pin-assignment, and mechanical constraints while clearly identifying work that still requires human RF/power/mechanical review.

## What Changes

- Replace the placeholder 20 × 30 mm outline with a practical first-draft carrier outline and import/place all 15 schematic footprints at explicit coordinates.
- Put external connectors on board edges: downward-mating APRS/WSPR SMA jacks together on the payload-facing edge, battery/switch and nichrome connectors on separate edges, and host headers where their short local paths are practical.
- Place C1/C2 immediately beside the OpenLog 3V3/GND pins; place Q1/R2/R3 as a compact cutdown gate cluster beside J5; place R1/D1 as a compact UART activity cluster.
- Add and honor explicit ≥5 mm component/copper keepout geometry around each SMA dielectric, with J5 and battery metal excluded from those zones; keep J6-to-J3/J4 RF stubs short.
- Reserve clearly documented connector-adjacent ESD placement zones. No ESD component exists in the authoritative schematic/BOM, so this layout stage will not invent electrically unsynchronized devices; LAYOUT.md will mark ESD selection/capture as required specialist follow-up.
- Route the short critical RF stubs, OpenLog decoupling, cutdown gate network, and high-current PACK_SW/CUTDOWN_DRAIN/GND paths with appropriate first-draft widths; leave noncritical signal connectivity as ratsnest.
- Create LAYOUT.md including a `## Draft quality` section that explicitly separates acceptable draft work from items requiring human or specialist rework.
- Update docs/CHANGELOG.md and docs/DECISIONS.md with the layout-stage rationale and known limitations.
