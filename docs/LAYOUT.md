# Revised layout — Weather Balloon Logger harness

The coordinate-level PCB draft is synchronized to the verified FACE-UP LightAPRS-W 2.0 geometry: J2 is the 11-position module interface on the matching right-hand long edge in carrier top view, J7/HF is bottom-left, J6/VHF is bottom-right, U1/C3 implement the I2C LED path, D1 is on `LED_N`, and cutdown uses A2/PB09 on `CUTDOWN_CTRL`. The board outline remains 80 mm × 70 mm, from (100,100) to (180,170) mm in KiCad coordinates. Rationale: a face-up module must reproduce the vendor top view directly, without a left-right mirror.

The exact 32.77 × 54.80 mm LightAPRS-W 2.0 body reservation occupies (123.615,101) to (156.385,155.8), with the 54.80 mm long axis vertical. Only direct-mating contacts J2, J6, J7 and four approximate M2 standoff holes are inside this zone. The vendor drawing's approximately 42.73 mm outer hole span lies along its long horizontal drawing axis; rotating the module to the required long-axis-vertical carrier orientation makes that a 42.73 mm PCB-vertical span, from y=106.535 to y=149.265. Every other electrical component is outside the body projection. Exact hole offsets, header-to-module alignment, component-height clearance, and USB access still require confirmation against the vendor drawing and a physical LightAPRS-W board before fabrication. All `CopperheadDraft_*` land patterns remain non-fabrication-ready placeholders, and the existing `outputs/` package is stale until explicitly regenerated after footprint qualification.

## Placement

| Refdes | Position (mm) | Rotation | Placement rationale |
| --- | ---: | ---: | --- |
| J1 | (103,108) | 90° | Pack input remains on the left edge, outside the module and RF zones. |
| SW1 | (112,108) | 0° | Adjacent to J1; PACK_IN stays short and SW1 still breaks pack positive. |
| J2 | (154.885,112) | 270° | Inside the FACE-UP module zone along its matching right long edge; 11 pads at 2.54 mm pitch reproduce the verified top-view host row without mirroring. |
| A1 | (162,110) | 0° | OpenLog is outside the module's right edge with short UART and 3V3 access. |
| C2 | (164,114) | 0° | OpenLog high-frequency bypass immediately below A1. |
| C1 | (168,114) | 0° | OpenLog bulk bypass immediately below A1. |
| U1 | (166,128) | 0° | PCF8574T is outside the module zone on the right-side logic corridor. |
| C3 | (172,124) | 0° | Local U1 decoupling beside VDD/GND. |
| R1 | (162,137) | 0° | LED limiter outside the module zone beside U1/D1. |
| D1 | (166,137) | 180° | Visible active-low LED beside U1 P0, isolated from UART_TX. |
| J5 | (103,141) | 90° | Nichrome connector remains on the left edge and outside both RF envelopes. |
| R2 | (116,135) | 0° | Gate series resistor in the left-side cutdown cluster. |
| Q1 | (116,141) | 0° | FET remains close to J5 to minimize the high-current drain neck. |
| R3 | (116,147) | 0° | Intentional default-off pulldown remains adjacent to Q1. |
| J7 | (125.615,154) | 0° | HF/WSPR single contact at the FACE-UP module's bottom-left corner. |
| J6 | (154.385,154) | 0° | VHF/APRS single contact at the FACE-UP module's bottom-right corner. |
| J4 | (112,162) | 0° | WSPR SMA on the downward-facing bottom-left edge, directly outward from J7/HF. |
| J3 | (168,162) | 0° | APRS SMA on the downward-facing bottom-right edge, directly outward from J6/VHF. |
| H1/H2 | (128.5,106.535) / (151.5,106.535) | — | Approximate upper M2 standoff reservations inside the exact module zone. |
| H3/H4 | (128.5,149.265) / (151.5,149.265) | — | Approximate lower M2 reservations; the upper-to-lower span is 42.73 mm after rotating the vendor drawing to the carrier's vertical long axis. |

The on-board WSPR clearance envelope is drawn from (102,152) to (122,170) around left-side J4, and the APRS envelope is drawn from (158,152) to (178,170) around right-side J3. Each reserves at least 5 mm laterally and above the 10 mm-diameter draft SMA body; the required lower clearance continues beyond the board edge, where no PCB copper or parts exist. Only the intended SMA, RF trace, and shield-ground copper occupy each envelope. Battery, OpenLog, expander, LED, and nichrome hardware remain outside both. Reserved ESD areas remain drawings only because no protection device is captured in the schematic or BOM. Rationale: placing each downward-facing SMA outward from its corrected FACE-UP RF corner avoids crossed, long launches.

## Routing rules used

- PACK_IN, the main PACK_SW path, and CUTDOWN_DRAIN use 1.5 mm copper except the 0.6 mm Q1 drain neck. Rationale: retain first-draft margin for the assumed 2 A, 30 s cutdown pulse while acknowledging the SOT-23 bottleneck.
- Ground uses a 1.0 mm B.Cu perimeter/bottom trunk with 0.4–1.0 mm local branches. Rationale: keep returns continuous while clearing the direct-mating header and revised signal corridors.
- 3V3 uses 0.5 mm on the host trunk and 0.4 mm local branches; the short U1-to-C3 connection changes layer through local vias to clear SCL. Rationale: keep both OpenLog and U1 bypass connections short without copper collisions.
- UART_TX, I2C_SCL, I2C_SDA, LED_A, LED_N, CUTDOWN_CTRL, and CUTDOWN_GATE use 0.3 mm. SCL and SDA use controlled layer changes where necessary to reach U1 without crossing address straps or supply copper.
- RF_WSPR uses a separate 0.5 mm first-draft trace from bottom-left J7/HF to left-side J4; RF_APRS runs from bottom-right J6/VHF to right-side J3. Rationale: preserve the electrical mappings while making both FACE-UP launches short and uncrossed pending a real 50 Ω stackup calculation.
- Every schematic-connected net is routed and the revised board has no ratsnest or DRC violation. Copper under the module zone is limited to required mating-contact fanout and shared routing; no non-mating component body is placed there.

## Draft quality

The revised coordinate study is internally consistent and DRC-clean:

- All 18 schematic refdes are present with exact revised net names; J2 has 11 contacts, J6/J7 are separate, and U1/C3 plus `I2C_SCL`, `I2C_SDA`, and `LED_N` are routed.
- The exact 32.77 × 54.80 mm FACE-UP module zone is explicit. J2/J6/J7 and H1–H4 are inside; J1, SW1, A1, U1, C3, J3, J4, J5, Q1, D1, R1–R3, and C1/C2 are outside.
- The HF/WSPR branch leaves bottom-left J7 toward left-side J4, while VHF/APRS leaves bottom-right J6 toward right-side J3; unrelated parts do not enter either ≥5 mm SMA envelope.
- OpenLog bypassing, U1 bypassing, active-low LED control, reset-default-off cutdown hardware, power, ground, UART, I2C, and both RF paths are routed with no DRC violations.

A human or specialist must still close these fabrication holds:

- Verify the physical LightAPRS-W board against the 32 × 55 mm reservation, J2 orientation/order, J6/J7 corner locations, USB access, underside component heights, and all four approximate standoff coordinates. The hole pattern is not published and is not claimed exact.
- Replace every `CopperheadDraft_*` land pattern with the exact verified manufacturer/library footprint and repeat placement, mechanical review, ERC, and DRC.
- Convert both drawn SMA envelopes into enforceable rule areas after exact connector geometry is known; calculate 50 Ω launches from the released stackup and add the required return-via strategy. The 0.5 mm RF widths are drafting widths only.
- Verify downward SMA mating, enclosure penetration, cable bend radius, battery-metal separation, and connector access with a 3D/mechanical mock-up.
- Recalculate and test the complete 2 A for 30 s cutdown path using released copper, connectors, AO3400A maximum RDS(on), SOA, and thermal data.
- Verify OpenLog maximum idle current ≤1.85 mA, U1 maximum idle current ≤100 µA, the LightAPRS 3V3 regulator margin, and all leakage budgets over temperature.
- Capture and qualify any ESD/protection parts before placement; reserved drawings do not authorize unbudgeted components.
- Add production mounting/tooling, fiducials, test points, polarity/RF labels, enclosure clearances, and full fabrication review. Regenerate `outputs/` only after those holds are resolved.
