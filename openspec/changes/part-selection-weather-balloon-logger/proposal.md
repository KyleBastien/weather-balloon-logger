# Proposal: part-selection-weather-balloon-logger

## Why

Select a complete, stage-4-capturable BOM while preserving the L91 pack, leakage, 3.3 V gate-drive, ESP32 strapping, RF keepout, and 2 A cutdown constraints.

## What Changes

- Create docs/BOM.md using exactly `| Refdes | Value | Footprint | MPN | Rationale |`, with one row per refdes and component-only Value fields.
- Select only parts representable by symbols installed on this machine, verifying authoritative package pin numbers before commitment.
- Mark every introduced MPN UNVERIFIED and put datasheet-verifiable electrical, leakage/quiescent, package, and rating checks in Rationale.
- Update docs/CHANGELOG.md and record the non-trivial part-selection decisions without assigning host GPIOs before the LightAPRS-W/ESP32 pin table is available.
- Run drift checking before completion.
