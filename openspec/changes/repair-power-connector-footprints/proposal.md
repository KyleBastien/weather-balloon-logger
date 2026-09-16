# Proposal: repair-power-connector-footprints

> Marker: AUTO (autonomous mode; auto-approved, reviewable after the fact)

## Why

The exact real J1, J5, and SW1 footprints now require a localized manufacturability repair so their bodies and courtyards fit inside the existing outline, remain edge-accessible for hand assembly, and preserve the verified switched-pack and cutdown connectivity without disturbing the rest of the layout.

## What Changes

- Keep the board outline and every footprint except J1, J5, and SW1 fixed.
- Move or rotate only J1, J5, and SW1 as minimally needed for real-body/courtyard clearance and edge accessibility.
- Preserve SW1 pad 2 = PACK_IN, pad 1 = PACK_SW, and pad 3 intentionally unconnected.
- Remove stale copper beneath those real bodies and locally reroute only PACK_IN, PACK_SW, GND, and CUTDOWN_OUT using existing current-capable widths.
- Resolve local DRC findings without global suppression while preserving the six exact vendor-module exclusions in the project file.
- Record final locations, orientations, and hand-assembly access in docs/FOOTPRINT_AUDIT.md and append the bounded run records.
