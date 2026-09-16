# Proposal: add-javas-logger-silkscreen-label

> Marker: AUTO (autonomous mode; auto-approved, reviewable after the fact)

## Why

Provide the requested readable board identification while preserving all component, copper, mounting-hole, module-zone, and SMA-clearance constraints.

## What Changes

- Add horizontal, right-reading `JAVAS Logger` text on F.SilkS at about 1.8 mm height in a verified-clear left-center location.
- Document the label coordinates, size, orientation, and clearance rationale in `docs/LAYOUT.md`.
- Re-run PCB DRC and keep it clean.
