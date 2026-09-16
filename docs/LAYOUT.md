# Revised layout — Weather Balloon Logger harness

The coordinate-level PCB draft is synchronized to the revised schematic: J2 is the 11-position LightAPRS-W interface, J6 and J7 are separate VHF/HF contacts, U1/C3 implement the I2C LED path, D1 is on `LED_N`, and cutdown uses A2/PB09 on `CUTDOWN_CTRL`. The board outline remains 80 mm × 70 mm, from (100,100) to (180,170) mm in KiCad coordinates.

A 32 × 55 mm LightAPRS-W 2.0 body reservation occupies (124,101) to (156,156). Only the direct-mating contacts J2, J6, J7 and four approximate M2 standoff holes are inside this zone. Every other electrical component is outside the body projection. The hole pattern, header-to-module alignment, component-height clearance, and module orientation still require confirmation against a physical LightAPRS-W board before fabrication. All `CopperheadDraft_*` land patterns remain non-fabrication-ready placeholders, and the existing `outputs/` package is stale until explicitly regenerated after footprint qualification.

## Placement

| Refdes | Position (mm) | Rotation | Placement rationale |
| --- | ---: | ---: | --- |
| J1 | (103,108) | 90° | Pack input remains on the left edge, outside the module and RF zones. |
| SW1 | (112,108) | 0° | Adjacent to J1; PACK_IN stays short and SW1 still breaks pack positive. |
| J2 | (125.5,112) | 270° | Inside the module zone along its left long edge; 11 pads at 2.54 mm pitch directly mate the verified host row. |
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
| J6 | (126,154) | 0° | VHF/APRS single contact inside the module's lower-left corner. |
| J7 | (154,154) | 0° | HF/WSPR single contact inside the module's lower-right corner. |
| J3 | (112,162) | 0° | APRS SMA on the downward-facing bottom-left edge, directly outward from J6. |
| J4 | (168,162) | 0° | WSPR SMA on the downward-facing bottom-right edge, directly outward from J7. |
| H1/H2 | (128.5,105) / (151.5,105) | — | Approximate top M2 standoff reservations inside the module zone. |
| H3/H4 | (128.5,150) / (151.5,150) | — | Approximate bottom M2 standoff reservations, separated from J6/J7. |

The on-board APRS clearance envelope is drawn from (102,152) to (122,170); the WSPR envelope is drawn from (158,152) to (178,170). Each reserves 5 mm laterally and above the 10 mm-diameter draft SMA body; the required lower clearance continues beyond the board edge, where no PCB copper or parts exist. Only the intended SMA, RF trace, and shield-ground copper occupy each envelope. Battery, OpenLog, expander, LED, and nichrome hardware remain outside both. Reserved ESD areas remain drawings only because no protection device is captured in the schematic or BOM.

## Routing rules used

- PACK_IN, the main PACK_SW path, and CUTDOWN_DRAIN use 1.5 mm copper except the 0.6 mm Q1 drain neck. Rationale: retain first-draft margin for the assumed 2 A, 30 s cutdown pulse while acknowledging the SOT-23 bottleneck.
- Ground uses a 1.0 mm B.Cu perimeter/bottom trunk with 0.4–1.0 mm local branches. Rationale: keep returns continuous while clearing the direct-mating header and revised signal corridors.
- 3V3 uses 0.5 mm on the host trunk and 0.4 mm local branches; the short U1-to-C3 connection changes layer through local vias to clear SCL. Rationale: keep both OpenLog and U1 bypass connections short without copper collisions.
- UART_TX, I2C_SCL, I2C_SDA, LED_A, LED_N, CUTDOWN_CTRL, and CUTDOWN_GATE use 0.3 mm. SCL and SDA use controlled layer changes where necessary to reach U1 without crossing address straps or supply copper.
- RF_APRS and RF_WSPR use separate 0.5 mm first-draft traces directly outward from J6/J7 to J3/J4. Rationale: preserve physical channel separation and short launches pending a real 50 Ω stackup calculation.
- Every schematic-connected net is routed and the revised board has no ratsnest or DRC violation. Copper under the module zone is limited to required mating-contact fanout and shared routing; no non-mating component body is placed there.

## Draft quality

The revised coordinate study is internally consistent and DRC-clean:

- All 18 schematic refdes are present with exact revised net names; J2 has 11 contacts, J6/J7 are separate, and U1/C3 plus `I2C_SCL`, `I2C_SDA`, and `LED_N` are routed.
- The 32 × 55 mm module zone is explicit. J2/J6/J7 and H1–H4 are inside; J1, SW1, A1, U1, C3, J3, J4, J5, Q1, D1, R1–R3, and C1/C2 are outside.
- The APRS and WSPR branches leave opposite module corners toward separate bottom-edge SMA envelopes; unrelated parts do not enter those envelopes.
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
