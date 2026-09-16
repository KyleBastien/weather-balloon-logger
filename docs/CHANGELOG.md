# Design changelog

Append-only, newest first. One entry per committed copperhead run.

## 2026-09-16 — create pipeline stage: schematic

- Change: schematic-weather-balloon-logger
- Files: schematic.intent.json, weather-balloon-logger.kicad_sch, docs/BOM.md, docs/SPEC.md, docs/SUBSYSTEMS.md, docs/PINOUT.md, docs/CHANGELOG.md, docs\DECISIONS.md
- Verification: ERC clean

## 2026-09-15 — create pipeline stage: schematic

- Change: schematic-weather-balloon-logger
- Files: schematic.intent.json, weather-balloon-logger.kicad_sch, docs/PINOUT.md, docs/BOM.md, docs/SPEC.md, docs/SUBSYSTEMS.md, docs/CHANGELOG.md, docs/DECISIONS.md, .copperhead/constraints.json
- Verification: deterministic draft with 15 BOM parts and six subsystem groups; all BOM symbol pins confirmed; ERC clean; legibility 0 errors with one low-utilization advisory; BOM/PINOUT drift clean; generated copperhead_power rail helpers reconciled as engine-local symbols

## 2026-09-15 — create pipeline stage: part-selection

- Change: recover-part-selection-weather-balloon-logger
- Files: docs/BOM.md, docs/CHANGELOG.md, docs\DECISIONS.md
- Verification: ERC not required

## 2026-09-15 — recover pipeline stage: part-selection

- Change: recover-part-selection-weather-balloon-logger
- Files: docs/BOM.md, docs/CHANGELOG.md, docs/DECISIONS.md
- Verification: complete BOM reread; fresh installed-symbol searches and authoritative pin checks; power-budget audit; check_drift after readback

## 2026-09-15 — create pipeline stage: part-selection

- Change: part-selection-weather-balloon-logger
- Files: docs/BOM.md, docs/CHANGELOG.md, docs\DECISIONS.md
- Verification: ERC not required

## 2026-09-15 — recover pipeline stage: part-selection

- Change: part-selection-weather-balloon-logger
- Files: docs/BOM.md, docs/CHANGELOG.md, docs/DECISIONS.md
- Verification: exact five-column/one-refdes BOM read back; named-module absence and all selected installed symbols/pins tool-verified; constraint revisits resolved; check_drift run before finish

## 2026-09-15 — create pipeline stage: part-selection

- Change: part-selection-weather-balloon-logger
- Files: docs/BOM.md, docs/CHANGELOG.md, docs\DECISIONS.md
- Verification: ERC not required

## 2026-09-15 — create pipeline stage: part-selection

- Change: part-selection-weather-balloon-logger
- Files: docs/BOM.md, docs/CHANGELOG.md, docs/DECISIONS.md
- Verification: installed KiCad symbols searched and authoritative pins checked; BOM-to-schematic drift checked before finish

## 2026-09-15 — create pipeline stage: architecture

- Change: architecture-weather-balloon-logger
- Files: docs/SUBSYSTEMS.md, docs/CHANGELOG.md, docs\DECISIONS.md
- Verification: ERC not required

## 2026-09-15 — create pipeline stage: architecture

- Change: architecture-weather-balloon-logger
- Files: docs/SUBSYSTEMS.md, docs/CHANGELOG.md, docs/DECISIONS.md
- Verification: ERC not required (no schematic this stage)

## 2026-09-15 — create pipeline stage: spec-seed

- Change: seed-weather-balloon-logger-spec
- Files: docs/SPEC.md, docs\DECISIONS.md
- Verification: ERC not required
