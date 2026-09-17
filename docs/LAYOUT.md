# Revised layout — Weather Balloon Logger harness

The coordinate-level PCB draft is synchronized to the verified FACE-UP LightAPRS-W 2.0 geometry: J2 is the 11-position module interface on the matching right-hand long edge in carrier top view, J7/HF is bottom-left, J6/VHF is bottom-right, U1/C3 implement the I2C LED path, D1 is on `LED_N`, and cutdown uses A2/PB09 on `CUTDOWN_CTRL`. The board outline is now 80 mm × 78.5 mm, from (100,91.5) to (180,170) mm in KiCad coordinates; only the top edge moved, by 8.5 mm, for the exact OpenLog carrier. Rationale: the top extension fully contains A1's official module courtyard and leaves its microSD end accessible without disturbing the fixed LightAPRS interface or bottom RF layout.

The exact 32.77 × 54.80 mm LightAPRS-W 2.0 body reservation occupies (123.615,101) to (156.385,155.8), with the 54.80 mm long axis vertical. Only direct-mating contacts J2, J6, J7 and four approximate 2.2 mm M2 standoff holes are inside this zone. The measured transcription places H1–H4 at (125.9,115.35), (154.1,115.35), (125.9,153.52), and (154.1,153.52), forming a 28.20 mm measured-X by 38.17 mm measured-Y rectangle (nominal drawing transcription 28.18 × 38.16 mm; coordinate rounding accounts for the 0.02/0.01 mm difference). The stock J2 footprint is stored at 0° because its library-local pad row is vertical; its pads remain at x=154.9 spanning y=121.72–147.20. The former 270° value described the differently drawn placeholder's local axes, not a physical rotation of the connector. J7/HF and J6/VHF remain at the bottom-left and bottom-right respectively, shifted outward and downward to (123.7,155.0) and (156.3,155.0) to clear H3/H4 while preserving the measured corner intent. Every other electrical component is outside the body projection. All target-map substitutions are complete and the PCB contains no `CopperheadDraft_*` footprints. The LightAPRS coordinates still require confirmation against the vendor drawing and a physical module before fabrication, and the existing `outputs/` package remains stale until all fabrication holds are closed.

The front silkscreen includes the horizontal, right-reading board label `JAVAS Logger` centered at (110,96) mm with 1.8 mm text height and 0.30 mm stroke. It was moved to the open upper-left area so the A2 module body, solder joints, and hand-assembly access remain unobstructed while the label stays outside the LightAPRS and RF reservations.

## Placement

| Refdes | Position (mm) | Rotation | Placement rationale |
| --- | ---: | ---: | --- |
| J1 | (103,108) | 90° | Real side-entry JST-PH footprint remains at the left edge; its rotated full courtyard is inside the outline and its mating opening is edge-accessible. |
| SW1 | (114,108) | 0° | Exact 7101SYZQE direct-solder slot footprint shifted right for J1 courtyard clearance; top-side toggle actuation remains unobstructed and SW1 still breaks pack positive. |
| A2 | (106,121) | 270° | Exact Pololu S7V8F5 top-side direct-solder carrier in the left power area. Its full body/courtyard clears SW1, J1, J5, R2, the LightAPRS body, and both RF reservations; VIN/SHDN face the nearby switched-pack trunk. |
| J2 | (154.9,121.72) | 0° | Stock footprint library orientation; its vertical 11-pad row at 2.548 mm pitch spans y=121.72–147.20 and matches the FACE-UP module without mirroring. The old placeholder required 270° because its local axes differed. |
| A1 | (171,110) | 0° | Exact top-side solder-down OpenLog carrier shifted 9 mm right so its full body/courtyard is outside the fixed LightAPRS zone; its microSD end faces the newly extended top edge for direct home-assembly access. |
| C2 | (164,114) | 0° | OpenLog high-frequency bypass retained close below A1's 3V3/GND header pins; only its local connection is reconciled. |
| C1 | (168,114) | 0° | OpenLog bulk bypass retained close below A1's supply pins and inside the unchanged right-side logic corridor. |
| R4 | (166.62,118) | 180° | Leaded 1/4 W axial through-hole UART back-power limiter on 7.62 mm pitch. It clears A1/C1/C2/U1 and the fixed LightAPRS body zone while remaining close to A1 RXI. |
| U1 | (166,128) | 0° | PCF8574T is outside the module zone on the right-side logic corridor. |
| C3 | (172,124) | 0° | Local U1 decoupling beside VDD/GND. |
| R1 | (162,137) | 0° | LED limiter outside the module zone beside U1/D1. |
| D1 | (166,137) | 180° | Visible active-low LED beside U1 P0, isolated from UART_TX. |
| J5 | (103,141) | 90° | Real side-entry JST-XH footprint remains at the left edge; its rotated full courtyard is inside the outline, its mating opening is edge-accessible, and it stays outside both RF envelopes. |
| R2 | (116,135) | 0° | Gate series resistor in the left-side cutdown cluster. |
| Q1 | (116,141) | 0° | FET remains close to J5 to minimize the high-current drain neck. |
| R3 | (116,147) | 0° | Intentional default-off pulldown remains adjacent to Q1. |
| J7 | (123.7,155.0) | 0° | HF/WSPR contact at the FACE-UP module's bottom-left edge, shifted outward and downward from the approximate measured center to clear H3 by the DRC hole-clearance rule. |
| J6 | (156.3,155.0) | 0° | VHF/APRS contact at the FACE-UP module's bottom-right edge, shifted outward and downward from the approximate measured center to clear H4 by the DRC hole-clearance rule. |
| J4 | (112,162) | 0° | Exact `SMA_Amphenol_132134_Vertical` WSPR footprint remains fixed at the bottom-left edge; pad 1 is the RF_WSPR center and all four pad-2 shield tabs are GND. |
| J3 | (168,162) | 0° | Exact `SMA_Amphenol_132134_Vertical` APRS footprint remains fixed at the bottom-right edge; pad 1 is the RF_APRS center and all four pad-2 shield tabs are GND. |
| H1/H2 | (125.9,115.35) / (154.1,115.35) | — | Approximate 2.2 mm upper M2 holes from the measured coordinate transcription. |
| H3/H4 | (125.9,153.52) / (154.1,153.52) | — | Approximate 2.2 mm lower M2 holes; placed span is 28.20 × 38.17 mm after coordinate rounding versus the nominal 28.18 × 38.16 mm transcription. |

The on-board WSPR clearance envelope is drawn from (102,152) to (122,170) around left-side J4, and the APRS envelope is drawn from (158,152) to (178,170) around right-side J3. Each preserves the existing ≥5 mm RF/mechanical reservation; the required lower clearance continues beyond the board edge, where no PCB copper or parts exist. Only the intended SMA, RF trace, and shield-ground copper occupy each envelope. Battery, OpenLog, expander, LED, and nichrome hardware remain outside both. Each exact SMA has center pad 1 and four through-hole shield pads numbered 2. The four shields are joined symmetrically on B.Cu by 1.0 mm local U-shaped copper, then tied at the connector centerline to the existing 1.0 mm bottom GND trunk; the obsolete placeholder ground stubs were removed. Reserved ESD areas remain drawings only because no protection device is captured in the schematic or BOM. Rationale: the symmetric short shield fanout gives every tab a direct first-pass return connection while retaining both fixed connector positions and the full reservation.

## Routing rules used

- PACK_IN, the main PACK_SW path, and CUTDOWN_DRAIN use 1.5 mm copper except the 0.6 mm Q1 drain neck. Rationale: retain first-draft margin for the assumed 2 A, 30 s cutdown pulse while acknowledging the SOT-23 bottleneck.
- Ground uses a 1.0 mm B.Cu perimeter/bottom trunk with 0.4–1.0 mm local branches. At J3 and J4, 1.0 mm symmetric B.Cu U-fanouts join all four through-hole shield tabs and connect at the footprint centerline to that bottom trunk. Rationale: keep returns continuous, eliminate the placeholder dangling stubs, and give both first-pass RF launches short balanced shield connections.
- 3V3 uses 0.5 mm on the host trunk and 0.4 mm local branches; the short U1-to-C3 connection changes layer through local vias to clear SCL. OpenLog is no longer on this rail.
- A2 VIN/SHDN use a short 0.8 mm B.Cu branch from the existing `PACK_SW` trunk; A2 GND uses 0.6 mm B.Cu to J1 ground. `LOGGER_5V` uses 0.5 mm F.Cu along the board top to A1/C1/C2, outside the LightAPRS body reservation. The cutdown feed remains independently connected directly to `PACK_SW`.
- UART_TX, OPENLOG_RXI, I2C_SCL, I2C_SDA, LED_A, LED_N, CUTDOWN_CTRL, and CUTDOWN_GATE use 0.3 mm. The leaded through-hole R4 separates UART_TX from OPENLOG_RXI beside A1; local GND and SCL B.Cu paths detour around its drilled pads while preserving clearance.
- RF_WSPR uses a separate 0.5 mm first-draft trace from bottom-left J7/HF to J4 pad 1; RF_APRS runs from bottom-right J6/VHF to J3 pad 1. Each trace now approaches its center pad along the connector centerline between the two upper shield tabs, with DRC clearance to every pad-2 shield. Rationale: preserve the electrical mappings and remove the real-footprint shorts without moving either connector. The 0.5 mm width is not a 50 Ω qualification.
- Every schematic-connected net is routed and the revised board has no ratsnest or DRC violation. Copper under the module zone is limited to required mating-contact fanout and shared routing; no non-mating component body is placed there.

## Draft quality

The revised coordinate study is internally consistent and DRC-clean:

- All 20 schematic refdes are present with exact revised net names; A2/R4 and `LOGGER_5V`/`OPENLOG_RXI` are routed, J2 has 11 contacts, J6/J7 are separate, and U1/C3 plus `I2C_SCL`, `I2C_SDA`, and `LED_N` are routed.
- The exact 32.77 × 54.80 mm FACE-UP module zone is explicit. J2/J6/J7 and H1–H4 are inside; J1, SW1, A1, U1, C3, J3, J4, J5, Q1, D1, R1–R3, and C1/C2 are outside.
- The HF/WSPR branch leaves bottom-left J7 toward left-side J4, while VHF/APRS leaves bottom-right J6 toward right-side J3; unrelated parts do not enter either ≥5 mm SMA envelope.
- OpenLog bypassing, U1 bypassing, active-low LED control, reset-default-off cutdown hardware, power, ground, UART, I2C, and both RF paths are routed with no DRC violations.

A human or specialist must still close these fabrication holds:

- Verify the physical LightAPRS-W board against the 32 × 55 mm reservation, J2 orientation/order, J6/J7 corner locations, USB access, underside component heights, and all four approximate standoff coordinates. The hole pattern is not published and is not claimed exact.
- Verify every exact footprint and connector orientation on a 1:1 print with the purchased parts and mating hardware; the CAD substitutions are complete, but physical fit is not yet qualified.
- Convert both drawn SMA envelopes into enforceable rule areas, calculate the center-trace geometry from the released stackup, design and verify the final return-via strategy, and validate both launches with VNA measurements. The DRC-clean 0.5 mm traces and through-hole-tab B.Cu fanouts are first-pass connectivity geometry only and are not a 50 Ω qualification.
- Verify downward SMA mating, enclosure penetration, cable bend radius, battery-metal separation, and connector access with a 3D/mechanical mock-up.
- Recalculate and test the complete 2 A for 30 s cutdown path using released copper, connectors, AO3400A maximum RDS(on), SOA, and thermal data.
- Qualify the implemented A2/R4 split-power path: LightAPRS RAW/J2.1 and J5.1 remain direct `PACK_SW`; verify OpenLog ≤7 mA idle and ≤25 mA write, regulator Iq <0.2 mA, board-added ≤8 mA idle and ≤30 mA active peak, U1 ≤100 µA, reverse-polarity handling, UART integrity through R4, and cold operation.
- Capture and qualify any ESD/protection parts before placement; reserved drawings do not authorize unbudgeted components.
- Add production mounting/tooling, fiducials, test points, polarity/RF labels, enclosure clearances, and full fabrication review. Regenerate `outputs/` only after those holds are resolved.
