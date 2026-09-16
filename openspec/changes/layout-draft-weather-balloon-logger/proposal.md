# Proposal: layout-draft-weather-balloon-logger

## Why

Complete and recover Stage 5 as a verifiable coordinate-level KiCad board draft, preserving the existing valid work where possible and explicitly disclosing every non-fabrication-ready element.

## What Changes

- Verify and surgically correct the existing rule-driven PCB placement, edge connectors, decoupling proximity, RF/cutdown separation, keepouts, and routed critical nets.
- Keep noncritical connectivity as ratsnest where appropriate; require every existing routed net to pass DRC.
- Ensure LAYOUT.md contains a complete `## Draft quality` section stating exactly what is acceptable and what a human or specialist tool must redo.
- Export and verify the exact PCB SVG artifact.
- Update the design memory/changelog and register the exact PCB, LAYOUT.md, and PCB SVG artifact paths before finish.
