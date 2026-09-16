# Proposal: repair-real-footprint-fallout-pass-1

> Marker: AUTO (autonomous mode; auto-approved, reviewable after the fact)

## Why

The reproducibly imported real KiCad footprint geometry exposes localized routing, clearance, courtyard, and silkscreen conflicts. This bounded pass must restore zero unsuppressed DRC/connectivity errors without moving the fixed LightAPRS interface or weakening unrelated rules.

## What Changes

- Surgically reroute only the Q1 CUTDOWN_GATE/GND neighborhood and the minimum nearby tracks/vias needed to clear U1 pads 4 and 15.
- Add only object-scoped exclusions for the intentional H3/J7 and H4/J6 vendor-interface courtyard and inside-courtyard findings.
- Resolve the A1/C1 reference-silkscreen overlap and J6 silk-over-hole findings using reference-text visibility/placement or nonfunctional silk edits, without moving footprints.
- Document the vendor-coordinate courtyard rationale in docs/FOOTPRINT_AUDIT.md and record the bounded repair in design history.
- Preserve the board outline, all footprint names/geometry/positions/orientations, and scripts/update_board_footprints.py unchanged.
