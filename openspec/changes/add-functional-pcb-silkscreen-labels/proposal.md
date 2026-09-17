# Proposal: add-functional-pcb-silkscreen-labels

> Marker: AUTO (autonomous mode; auto-approved, reviewable after the fact)

## Why

Clear assembly and field-use labels reduce polarity, connector, RF-port, module, and cutdown wiring mistakes without changing the verified electrical or mechanical design.

## What Changes

- Add the requested human-readable functional and polarity labels on F.SilkS using compact 1.0–1.2 mm text and 0.15–0.2 mm strokes.
- Preserve every existing reference designator and the existing JAVAS Logger label.
- Place labels clear of pad solder-mask openings, courtyards, component bodies, the LightAPRS mating area, board edges, and existing legend; rotate edge text where useful.
- Add small F.SilkS identification outlines only if they materially improve clarity and remain collision-free.
- Add a short labeling-convention note to docs/LAYOUT.md.
- Do not alter the schematic, nets, footprints, pads, copper, vias, outline, keepouts, component placement, or constraints.
