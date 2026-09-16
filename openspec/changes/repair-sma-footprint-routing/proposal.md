# Proposal: repair-sma-footprint-routing

> Marker: AUTO (autonomous mode; auto-approved, reviewable after the fact)

## Why

The exact four-shield-tab SMA footprints expose clearance and connectivity fallout from the former placeholder geometry. The RF centers and every shield tab must be routed correctly without disturbing fixed mechanical placement or claiming unverified impedance performance.

## What Changes

- Reroute only RF_APRS from J6 to J3.1 and RF_WSPR from J7 to J4.1 so center conductors clear all J3/J4 shield pads.
- Repair only local GND around J3/J4, tying all four pad-2 shield tabs per connector into short symmetric ground fanout and the existing ground return; remove obsolete dangling placeholder stubs.
- Keep every footprint, orientation, board edge, RF reservation drawing, unrelated route, and the six exact LightAPRS mechanical exclusions unchanged.
- Update docs/LAYOUT.md and docs/FOOTPRINT_AUDIT.md with the actual fanout and the continuing stackup/VNA fabrication hold.
- Record the bounded routing decision and append the run changelog entry.
