# Layout — provisional LightHAB carrier

The current PCB is a mechanically provisional, electrically complete LightHABTracker 1.0 carrier. It is suitable for reviewing architecture and ordering the already-verified carrier parts, but it is explicitly **not suitable for fabrication** until the purchased LightHAB is measured.

## Board and module zones

- Carrier outline: exactly 90 × 80 mm, from (100,90) to (190,170) mm.
- Provisional LightHAB envelope: 56 × 75 mm, from (134,95) to (190,170) mm.
- Mounting: LightHAB components face outward; the onboard 3×AA holder sits between the LightHAB and this carrier.
- Provisional board-to-board clearance: 18–20 mm.
- Carrier electronics: entirely in the left wing, outside the LightHAB body zone.
- OpenLog: top-left, with the microSD edge exposed toward the board top.
- LightHAB onboard SMA clearance: two mechanical-only bottom-edge reservations.
- LightHAB USB clearance: mechanical-only reservation at the right edge.

The module envelope, connector locations, and holes are photo-derived placeholders. Front silkscreen and User.Comments both state `UNVERIFIED LIGHTHAB FIT - DO NOT FABRICATE`.

## Placement

| Ref | Position / orientation | Purpose and status |
| --- | --- | --- |
| A1 | (116.5,110), 0° | Verified OpenLog module footprint; microSD accessible at top edge |
| R4 | (128,106), 180° | THT UART series resistor |
| A2 | (103,140), 0° | Verified Pololu S7V8F5 module footprint |
| C1 | (116,132), 0° | THT 4.7 µF logger bypass |
| C2 | (116,138), 0° | THT 100 nF logger bypass |
| R1 | (110,116), 0° | THT LED current resistor |
| D1 | (122.7,116), 180° | THT activity LED |
| R2 | (110,120), 0° | THT 100 kΩ LED reset pull-up |
| J5 | (108.5,158), 180° | Horizontal JST-XH cutdown output |
| J2 | (136.5,109), 0° | Provisional LightHAB 1×9 extended-pin interface |
| J1 | (144,142), 0° | Provisional LightHAB VBATT/GND interface |
| J3 | (144,155), 0° | Provisional LightHAB OUT1/GND interface |
| H1–H4 | (138,99), (186,99), (138,166), (186,166) | Provisional 3.2 mm NPTH module holes |
| G1 | (126,163), 0° | Front-silkscreen coffee-balloon artwork |

All populated electrical parts are direct-solder through-hole footprints. The four mounting holes are NPTH. G1 is artwork and has no pads.

## Routing

- Nine schematic nets are fully routed with zero unconnected pads.
- `GND` uses 0.8 mm B.Cu branches and a right-side return trunk.
- `VBATT`, `LOGGER_5V`, and direct `OUT1` use 0.5–0.8 mm F.Cu.
- UART and LED signals use 0.35 mm F.Cu.
- No carrier RF trace exists; both RF paths remain on LightHAB.
- The module zone contains only required mating-interface fanout and ground routing; no carrier component body is placed beneath it.

KiCad 10 reports zero DRC violations and zero unconnected items. The clean DRC proves internal CAD consistency, not LightHAB fit or pyro capability.

## Silkscreen and assembly readability

Front silkscreen labels identify OpenLog/microSD access, logger 5 V, activity, cutdown polarity, the extended-pin interface, VBATT/GND, OUT1/GND, and the no-fabrication warning. The warning sits above the module zone and remains visible with the module installed. The coffee-balloon artwork remains unobstructed in the lower-left wing.

Engineering annotations on User.Comments show the provisional LightHAB body, stack direction/clearance, SMA keepouts, and USB keepout. They are not copper or electrical pads.

## Required measurement update

Before a fit-test PCB, replace every provisional coordinate with measurements from the purchased LightHAB or an official dimensioned drawing:

1. Board outline and corner radii.
2. Four mounting-hole centers and finished hole diameters.
3. J2 pin pitch, row position, hole/drill size, and pin-1 orientation.
4. J1 VBATT/GND and J3 OUT1/GND pad centers, drills, and polarity.
5. Battery-holder and maximum underside component height.
6. USB connector body and mating-cable envelope.
7. Both SMA body, nut, mating-connector, antenna/coax, and bend envelopes.
8. Onboard switch body/actuator envelope and its relationship to VBATT.

After measurement, rerun the deterministic layout build, move only the provisional module interfaces/mechanics as required, reroute, regenerate a 1:1 PDF, and repeat ERC/DRC/no-SMD/visual checks.
