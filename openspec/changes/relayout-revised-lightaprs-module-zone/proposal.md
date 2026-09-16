# Proposal: relayout-revised-lightaprs-module-zone

> Marker: AUTO (autonomous mode; auto-approved, reviewable after the fact)

## Why

The current PCB is explicitly obsolete relative to the revised schematic and lacks the verified 11-pin host header, separate VHF/HF contacts, I2C LED expander, and collision-free 32 x 55 mm LightAPRS-W mounting reservation.

## What Changes

- Re-layout the PCB against the revised schematic, preserving exact refdes and net names.
- Reserve a documented 32 x 55 mm LightAPRS-W 2.0 module-mount zone.
- Place J2, J6, and J7 inside the zone for direct module mating; add corner standoff mounting holes pending exact mechanical verification.
- Place J1, SW1, A1, U1, C3, J3, J4, Q1, D1, R1, R2, R3, C1, and C2 outside the module body projection.
- Re-route power, UART, I2C, LED, cutdown, ground, and separate RF nets while maintaining the two >=5 mm SMA dielectric keepouts.
- Update docs/LAYOUT.md, docs/CHANGELOG.md, and docs/DECISIONS.md with coordinates, rationale, verification status, and remaining footprint/RF/mechanical qualification holds.
