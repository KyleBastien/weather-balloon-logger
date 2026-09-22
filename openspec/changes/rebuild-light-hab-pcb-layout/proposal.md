# Proposal: rebuild-light-hab-pcb-layout

> Marker: AUTO (autonomous mode; auto-approved, reviewable after the fact)

## Why

The committed LightHAB schematic has replaced the former LightAPRS carrier topology, while the PCB and mechanical documentation still describe obsolete parts, RF routing, power switching, and module geometry. A bounded PCB-only rebuild is required to synchronize physical implementation without changing the approved electrical topology.

## What Changes

- Rebuild `weather-balloon-logger.kicad_pcb` around the committed 12-reference schematic using only directly soldered through-hole footprints and no SMD pads.
- Set the exact 90 x 80 mm outline at (100,90)–(190,170), reserve the provisional LightHAB body zone at x=134..190, y=95..170, and place all carrier electronics in the left wing with OpenLog microSD access.
- Remove obsolete LightAPRS-era placement/routing and retain only A1, A2, C1, C2, D1, R1, R2, R4, J1, J2, J3, and J5, with J2 1x9, J1/J3 1x2, J5 horizontal JST-XH, and existing verified THT footprints elsewhere.
- Add four provisional 3.2 mm NPTH LightHAB mounting holes, provisional J1/J2/J3 mating locations, mechanical-only bottom SMA and right-edge USB clearances, 18–20 mm stack-clearance documentation, and prominent `UNVERIFIED LIGHTHAB FIT - DO NOT FABRICATE` warnings on F.SilkS and User.Comments.
- Preserve the coffee-balloon F.SilkS artwork only if readable and unobstructed; update functional labels and polarity/pin-1 markings.
- Route every committed schematic net with reasonable power widths, zero unconnected items, and no topology changes.
- Update `docs/LAYOUT.md` and `docs/FOOTPRINT_AUDIT.md` to distinguish verified carrier footprints from photo-derived provisional LightHAB geometry; record decisions and changelog for this bounded pass.
