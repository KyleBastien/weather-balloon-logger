# First-draft layout — Weather Balloon Logger harness

Stage 5 records a coordinate-level KiCad PCB draft derived from the authoritative stage-4 schematic. The board outline is 80 mm × 70 mm, from (100,100) to (180,170) mm in KiCad coordinates. All footprint references and electrical net names remain identical to the schematic.

## Placement

| Refdes | Position (mm) | Rotation | Placement rationale |
| --- | ---: | ---: | --- |
| J1 | (103,115) | 90° | Battery input on left edge; separated from both RF envelopes. |
| SW1 | (115,115) | 0° | Adjacent to J1 so PACK_IN is short and the switch still breaks pack positive. |
| J2 | (135,103) | 0° | Host interface on top edge. |
| A1 | (135,120) | 0° | OpenLog immediately below J2 for short 3V3/GND/UART connections. |
| C2 | (142,113.5) | 0° | 100 nF bypass beside the A1 supply pins. |
| C1 | (142,116.5) | 0° | 4.7 µF bulk bypass beside the A1 supply pins. |
| R1 | (150.6,109) | 0° | LED limiter beside D1 and the host UART breakout. |
| D1 | (149,112) | 0° | Visible activity LED in the top-side logic cluster. |
| J5 | (103,142) | 90° | Nichrome connector on left edge, outside both SMA clearance envelopes. |
| R2 | (116,140) | 0° | Gate series resistor near the cutdown power cluster. |
| Q1 | (124,145) | 0° | Cutdown FET kept near J5 to minimize the high-current drain run. |
| R3 | (124,150) | 180° | Gate pulldown next to Q1, arranged to clear the drain neck. |
| J6 | (145,154) | 0° | Host RF header centered between the two antenna branches. |
| J3 | (130,162) | 0° | APRS SMA at the payload-facing bottom edge. |
| J4 | (160,162) | 0° | WSPR SMA at the payload-facing bottom edge. |

The APRS envelope is drawn from (120,152) to (140,170); the WSPR envelope is drawn from (150,152) to (170,170). Each reaches 5 mm beyond the 10 mm-diameter draft SMA body, contains only its connector and intended RF/shield copper, and contains no battery or nichrome hardware. Reserved ESD areas are drawn near J1 and J5, but no ESD device is electrically present because stage 4 contains no ESD symbol or BOM row.

## Routing rules used

- PACK_IN, the main PACK_SW feed, and the main CUTDOWN_DRAIN run use 1.5 mm copper; the drain narrows to 0.6 mm only at Q1's SOT-23 pad. Rationale: maximize first-draft copper for the assumed 2 A, 30 s cutdown pulse while acknowledging the device-pad bottleneck.
- Ground distribution uses 1.0–1.5 mm B.Cu trunks, with local 0.4 mm bypass branches. Rationale: keep the high-current return away from top-side signal crossings.
- PACK_SW uses paired 1.8/0.8 mm vias for two short B.Cu crossings. Rationale: preserve the 1.5 mm power path without crossing PACK_IN or CUTDOWN_DRAIN.
- 3V3 is 0.5 mm on the host/OpenLog trunk and 0.4 mm for local branches. UART_TX, LED_A, CUTDOWN_CTRL, and CUTDOWN_GATE use 0.3 mm.
- RF_APRS and RF_WSPR are 0.5 mm first-draft traces with one 45° approach each from J6 to its SMA. Rationale: keep both stubs short and simple pending an impedance-controlled stackup.
- Every connected net on this small harness was treated as critical enough to route: power/ground, both RF paths, OpenLog power/UART/decoupling, LED activity, and cutdown control/gate/drain. Therefore no ratsnest remains after DRC closure; a later specialist may rip up noncritical logic traces while replacing the draft land patterns.

## Draft quality

Fine for a first-draft placement/routing study:

- The KiCad board parses, renders, and passes `run_drc` with no reported violations after the final routing pass.
- All 15 schematic refdes are placed at explicit coordinates, external connectors are on the top/left/bottom edges, and J5/battery hardware remain outside the two RF clearance envelopes.
- C1/C2 are adjacent to the OpenLog supply pins; R2/R3/Q1 form a local default-off cutdown cluster; R1/D1 form a local UART activity cluster.
- PACK_IN, PACK_SW, CUTDOWN_DRAIN, ground, RF, decoupling, UART, LED, and gate/control nets are electrically continuous and DRC-clean.
- The RF branches are short, symmetric in intent, separated from the power/cutdown cluster, and contain no unrelated component or copper inside the marked 5 mm clearance envelopes.

A human or specialist tool must redo or verify before fabrication:

- Replace every `CopperheadDraft_*` board-local land pattern with the exact verified KiCad/manufacturer footprint, then repeat placement and DRC. The board-local pads are electrically useful placeholders, not procurement-approved land patterns; in particular SW1 and both SMA footprints were not found under the BOM's named library identifiers.
- Convert the two drawn RF clearance envelopes into enforceable KiCad rule areas after the exact SMA dielectric geometry is known. The current geometry is visibly honored but is not an automatic copper/footprint prohibition.
- Re-route J6→J3/J4 using a confirmed PCB stackup and a 50 Ω microstrip or grounded coplanar calculation; add the return-via fence and tune launch geometry with an RF specialist. The present 0.5 mm width is only a DRC-clean drafting width, not an impedance claim.
- Select and capture actual ESD/protection parts in the schematic and BOM before placing them. The current board reserves connector-adjacent space but intentionally does not invent unsynchronized devices. RF protection must satisfy insertion-loss/capacitance needs; power/control protection must meet 7.2 V, leakage, and cutdown-current constraints.
- Verify the physical downward-mating SMA orientation, connector shell clearance, payload wall penetration, cable bend radius, battery-metal separation, and J1/J5 mating access with 3D models or a mechanical mock-up.
- Recalculate the complete 2 A for 30 s cutdown path using verified copper weight, ambient/altitude conditions, connector/contact resistance, SOT-23 thermal data, and AO3400A safe operating area. Widen or pour PACK_SW/GND/CUTDOWN_DRAIN and multiply vias as required.
- Verify OpenLog peak current and LightAPRS 3V3 regulator margin; this layout does not close the existing 1.95 mA maximum-idle-current qualification hold.
- Add mounting holes, panelization/tooling strategy, fiducials, test points, polarity labels, RF labels on production silkscreen, and enclosure clearances. None are implied by this first draft.
- Run full fabrication review after replacing footprints: courtyard, paste/mask, annular ring, drill tolerances, creepage, solderability, assembly access, return-current continuity, thermal reliefs, and manufacturer rules.
