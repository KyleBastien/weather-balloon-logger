# Proposal: part-selection-weather-balloon-logger

## Why

Create a stage-4-capturable fixed BOM whose values, footprints, MPN qualification holds, installed KiCad symbols, and real package pins satisfy the documented electrical, leakage, mechanical, and host-strapping constraints.

## What Changes

- Recreate `docs/BOM.md` using exactly `| Refdes | Value | Footprint | MPN | Rationale |`, with one row per refdes and component-only Value fields.
- Retain only parts backed by installed KiCad symbols and authoritative pin data; document the connector representation of off-board modules.
- Mark every MPN UNVERIFIED and state datasheet-verifiable footprint, pinout, voltage/current, temperature, leakage or quiescent-current acceptance limits.
- Record the part-selection rationale and append the completed stage to the changelog.
