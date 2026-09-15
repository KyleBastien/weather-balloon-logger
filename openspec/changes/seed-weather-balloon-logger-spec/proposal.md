# Proposal: seed-weather-balloon-logger-spec

## Why

Stage 1 spec-seed: capture the Weather Balloon Logger as a requirements document with explicit electrical/mechanical budgets so later schematic work cannot silently violate power, voltage, pin, or antenna constraints.

## What Changes

- Write docs/SPEC.md describing the device, interfaces, power budget, voltage ranges, cutdown, antennas, and ASSUMED defaults for anything the brief does not state.
- Record every stated budget with record_constraint (energy, flight duration, pack voltage, logic level, SMA orientation, cutdown drive).
- Do not create schematic/board symbols or BOM yet.
- Skip openspec/ unless that directory already exists.
