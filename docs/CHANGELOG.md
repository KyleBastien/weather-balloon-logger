# Design changelog

Append-only, newest first. One entry per committed copperhead run.

## 2026-09-16 — create pipeline stage: devplan

- Change: devplan-weather-balloon-logger
- Files: docs/DEVPLAN.md, docs/CHANGELOG.md, docs\DECISIONS.md
- Verification: ERC clean, DRC clean

## 2026-09-16 — create pipeline stage: devplan

- Change: devplan-weather-balloon-logger
- Files: docs/DEVPLAN.md, docs/CHANGELOG.md, docs/DECISIONS.md
- Verification: hardware bring-up, probe-location, risk, and prototype-order plan added; ERC, DRC, drift, and schematic legibility checks run in this stage

## 2026-09-16 — create pipeline stage: firmware

- Change: firmware-weather-balloon-logger
- Files: firmware/tools/generate_pins.py, firmware/include/pins.h, firmware/include/cutdown.h, firmware/include/openlog.h, firmware/include/telemetry.h, firmware/src/cutdown.cpp, firmware/src/openlog.cpp, firmware/src/telemetry_stub.cpp, firmware/WeatherBalloonLogger.ino, firmware/README.md, firmware/DEVPLAN.md, docs/CHANGELOG.md, docs\DECISIONS.md, openspec/changes/firmware-weather-balloon-logger/tasks.md
- Verification: ERC clean, DRC clean

## 2026-09-16 — create pipeline stage: firmware

- Change: firmware-weather-balloon-logger
- Files: firmware/, docs/CHANGELOG.md, docs/DECISIONS.md, .copperhead/constraints.json
- Verification: pins generated from docs/PINOUT.md; safe one-record happy path added; C++11 compatibility/readback checks clean; firmware not compiled here because no exact board package/compiler/build action is exposed; ERC clean; DRC clean; drift clean; schematic legibility 0 errors with one low-utilization advisory

## 2026-09-16 — create pipeline stage: outputs

- Change: outputs-weather-balloon-logger
- Files: outputs/, outputs/BOM.csv, outputs/README.md, docs\DECISIONS.md, docs/CHANGELOG.md
- Verification: ERC clean, DRC clean

## 2026-09-16 — create pipeline stage: outputs

- Change: outputs-weather-balloon-logger
- Files: outputs/ Gerbers and drill, outputs/outline.dxf, outputs/board.step, outputs/board.svg, outputs/schematic.svg, outputs/BOM.csv, outputs/README.md, docs/CHANGELOG.md, docs/DECISIONS.md
- Verification: every requested export succeeded; ERC clean; DRC clean; drift clean; schematic legibility 0 errors with one low-utilization advisory; output package remains explicitly blocked from fabrication and procurement because CopperheadDraft footprints and all MPNs are UNVERIFIED

## 2026-09-16 — create pipeline stage: layout-draft

- Change: layout-draft-weather-balloon-logger
- Files: docs\DECISIONS.md
- Verification: ERC clean, DRC clean

## 2026-09-16 — create pipeline stage: layout-draft

- Change: layout-draft-weather-balloon-logger
- Files: docs\DECISIONS.md
- Verification: ERC clean, DRC clean

## 2026-09-16 — create pipeline stage: layout-draft

- Change: layout-draft-weather-balloon-logger
- Files: weather-balloon-logger.kicad_pcb, LAYOUT.md, docs/CHANGELOG.md, docs\DECISIONS.md
- Verification: ERC clean, DRC clean

## 2026-09-16 — create pipeline stage: layout-draft

- Change: layout-draft-weather-balloon-logger
- Files: weather-balloon-logger.kicad_pcb, LAYOUT.md, docs/CHANGELOG.md, docs/DECISIONS.md
- Verification: 80 × 70 mm coordinate-level board draft; all 15 refdes placed; critical power, ground, RF, decoupling, UART/LED, and cutdown nets routed; dual SMA clearance envelopes and ESD reservation areas documented; DRC clean; board SVG exported; board-local draft land patterns explicitly require verified-footprint replacement before fabrication

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
