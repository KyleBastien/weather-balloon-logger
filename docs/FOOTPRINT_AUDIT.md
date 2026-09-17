# Real-footprint audit

Date: 2026-09-16

This audit records the completed staged Copperhead placement and routing work.
The PCB now contains the full target set of real library/project footprints and
no draft footprint placeholders; the remaining holds are qualification tasks,
not footprint-substitution work.

## Assembly constraint

Every board-mounted part is intentionally soldered for home assembly. Do not
replace the LightAPRS, OpenLog, or A2 regulator carrier holes with female
sockets or other plug-in module connectors. Their header pins enter from the
top and are soldered to the carrier. J1/J5/J3/J4/SW1 are likewise soldered PCB
parts; only their external cable or RF mates are removable.

## Corrections found

- C&K `7101SYZQE` uses `Z` solder-lug terminals. The project intentionally
  solders those lugs directly into plated slots for home assembly. C&K does not
  publish this as a formal PCB land pattern, so the project footprint adapts the
  published 2.03 x 0.76 mm lug geometry to 2.30 x 1.10 mm insertion slots.
- C&K `7101SYWQE` uses long wire-wrap terminals, so it is not the intended PCB
  version either.
- SparkFun's official OpenLog drawing gives a 0.600 x 0.750 inch
  (15.24 x 19.05 mm) board. The previous 23 x 14 mm assumption was incorrect.
- The OpenLog must use the project carrier footprint below; a generic 1x06
  header footprint does not reserve the module body and cannot detect clashes.

## Copperhead target map

Courtyard measurements are from KiCad 10.0.6 library geometry or the verified
project-local geometry. They are the minimum placement envelopes before any
extra RF, cable, service, or enclosure clearance.

| Refs | Target footprint | Courtyard / envelope | Status and placement constraint |
| --- | --- | ---: | --- |
| J1 | `Connector_JST:JST_PH_S2B-PH-K_1x02_P2.00mm_Horizontal` | 6.90 x 8.60 mm | Stock KiCad footprint. Place at the board edge for the battery-holder cable; verify plug polarity before power-up. |
| SW1 | `WeatherBalloon:SW_CK_7101SYZQE` | 7.86 x 13.70 mm | Project-local direct-solder adaptation from C&K pages F-4/F-9: three 2.30 x 1.10 mm plated slots on 4.70 mm centers for the nominal 2.03 x 0.76 mm lugs. Matching STEP model attached. Pin 2 is common. |
| J2 | `Connector_PinHeader_2.54mm:PinHeader_1x11_P2.54mm_Vertical` | 3.54 x 28.94 mm | Stock footprint for the LightAPRS installed header. Preserve the vendor module envelope and verify on the physical module before fabrication. |
| A1 | `WeatherBalloon:SparkFun_OpenLog_DEV-13712_Carrier` | 16.24 x 20.05 mm | Project-local full-module footprint. Top-side module, header soldered downward into the carrier; pin 1 BLK through pin 6 GRN matches the schematic. |
| A2 | `WeatherBalloon:Pololu_S7V8F5_Carrier` | 12.43 x 17.51 mm | Implemented project-local full-module footprint for Pololu S7V8F5 item 2123 at (106,121), 270°. Top-side direct-solder installation; official 11.43 x 16.51 mm body, four 1.0 mm drills for official 1.02 mm holes, 2.54 mm pitch, centered row 1.27 mm from the edge, and pads 4 VOUT, 3 GND, 2 VIN, 1 SHDN. |
| C1, C5 | `WeatherBalloon:KEMET_C322C475K5R5TA` | 6.08 x 5.07 mm | Exact project footprint for the KEMET 4.7 µF, 50 V X7R radial part: 5.08 mm pitch, 0.8 mm drills, 1.6 mm pads. |
| C2-C4 | `WeatherBalloon:KEMET_C315C104K5R5TA` | 4.81 x 3.54 mm | Exact project footprint for the KEMET 100 nF, 50 V X7R radial part: 2.54 mm pitch, 0.8 mm drills, 1.6 mm pads. |
| U1 | `Package_DIP:DIP-16_W7.62mm` | 9.82 x 20.91 mm | Stock KiCad DIP-16 footprint matching TI PCF8574N. |
| U2 | `Package_DIP:DIP-8_W7.62mm` | 9.82 x 10.75 mm | Stock KiCad DIP-8 footprint matching Microchip TC4422AVPA. |
| D1 | `LED_THT:LED_D3.0mm` | 4.93 x 4.51 mm | Stock KiCad 3 mm leaded LED footprint matching Kingbright WP710A10SGC. |
| R1-R3 | `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal` | 9.81 x 3.09 mm each | Stock KiCad axial footprint matching the selected Yageo MFR-25 parts. |
| R4 | `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal` | 9.72 x 3.00 mm courtyard | Stock KiCad 1/4 W axial through-hole footprint with two 0.8 mm drilled holes on 7.62 mm pitch. It is installed through the board and soldered from the underside; no SMD-only R4 pads remain. |
| J5 | `Connector_JST:JST_XH_S2B-XH-A_1x02_P2.50mm_Horizontal` | 8.40 x 12.51 mm | Stock KiCad footprint; 3 A family provides margin over the 2 A cutdown pulse. Place at edge with wire-service clearance. |
| Q1 | `Package_TO_SOT_THT:TO-220-3_Vertical` | 10.59 x 4.99 mm | Stock KiCad TO-220 footprint matching Infineon IRLZ44NPBF; pin order is G/D/S. |
| J6, J7 | `Connector_PinHeader_2.54mm:PinHeader_1x01_P2.54mm_Vertical` | 3.54 x 3.54 mm each | Stock footprint for the LightAPRS VHF/HF contacts. Preserve the measured module-corner locations. |
| J3, J4 | `Connector_Coaxial:SMA_Amphenol_132134_Vertical` | 8.34 x 8.34 mm each | Exact stock KiCad footprints fixed at J3 (168,162) and J4 (112,162), rotation 0°. Pad 1 is the RF center; four through-hole pads numbered 2 are the GND shield tabs. Retain the existing RF/mechanical and cable reservations beyond the component courtyard and verify downward mating in the mechanical mock-up. |
| H1-H4 | `MountingHole:MountingHole_2.2mm_M2` | 4.90 mm diameter | Stock non-plated hole. Verify the physical LightAPRS hole diameter and center locations before fabrication. |

## Module and non-courtyard envelopes

- LightAPRS-W 2.0 body: 32.77 x 54.80 mm.
- LightAPRS mounting-hole center rectangle: nominal 28.18 x 38.16 mm; the
  current coordinate transcription is 28.20 x 38.17 mm because of rounding.
- OpenLog body: 15.24 x 19.05 mm; included in A1's custom courtyard.
- Pololu S7V8F5 A2 body: 11.43 x 16.51 mm; included in its 12.43 x 17.51 mm custom courtyard. Its 1x4 row is centered on the 11.43 mm edge, 1.27 mm from that edge, and uses 1.0 mm drills for the official 1.02 mm holes.
- SMA clearance: keep the existing additional 5 mm RF/mechanical envelope and
  downward cable volume. The 8.34 mm KiCad courtyard alone is insufficient.
- J1 and J5 require off-board cable exit and bend volume outside their listed
  courtyards.

Because the LightAPRS electrical contacts and its four mounting holes are
separate references, represent the 32.77 x 54.80 mm body as an explicit board
rule/mechanical area instead of a component courtyard. Permit only J2, J6, J7,
and H1-H4 inside that area.

## Pass 1 real-geometry repair and scoped exclusions

The pass-1 library imports keep H3/J7 and H4/J6 at the fixed, measured LightAPRS-W vendor-module coordinates. Their actual NPTH and PTH copper/hole features do not overlap, but the stock `MountingHole_2.2mm_M2` circular courtyard intersects the stock `PinHeader_1x01_P2.54mm_Vertical` rectangular courtyard at each pair. The project therefore excludes only the six exact UUID-paired `courtyards_overlap`, `npth_inside_courtyard`, and `pth_inside_courtyard` findings for H3/J7 and H4/J6. No DRC class or severity is disabled globally; copper, hole, clearance, connectivity, and every unrelated courtyard finding remain enforced. Rationale: moving either member would violate the measured module interface, while broad suppression would conceal unrelated assembly errors.

Pass 1 also keeps every footprint position and orientation fixed while repairing the local Q1 gate/ground routing, clearing the two vias adjacent to U1 pads 4 and 15, hiding the colliding C1 reference, and moving only the two J6 silkscreen strokes clipped by H4 from F.SilkS to F.Fab. `scripts/update_board_footprints.py` remains the reproducible source for the imported library geometry.

## Power-connector pass — final placement

- J1 `Connector_JST:JST_PH_S2B-PH-K_1x02_P2.00mm_Horizontal` is at (103, 108) mm, rotation 90°. Its rotated full real courtyard is inside the 100 mm left board edge, and the side-entry mating opening remains accessible from that edge for the battery-holder cable and hand assembly.
- J5 `Connector_JST:JST_XH_S2B-XH-A_1x02_P2.50mm_Horizontal` is at (103, 141) mm, rotation 90°. Its rotated larger real courtyard is fully on-board, its side-entry opening remains accessible from the left edge, and it clears fixed Q1/R2 plus the RF reservation.
- SW1 `WeatherBalloon:SW_CK_7101SYZQE` is at (114, 108) mm, rotation 0°. Its exact three 2.30 x 1.10 mm plated slots and library identity are unchanged; pad 2 remains PACK_IN common, pad 1 remains PACK_SW, and pad 3 remains intentionally unconnected. The top-side toggle and solder lugs remain unobstructed for hand assembly.
- The final conversion rerouted local power, logic, and cutdown copper for the leaded parts. The Q1 drain path is now 1.5 mm to the TO-220 pad; the six exact H3/J7 and H4/J6 vendor-module DRC exclusions remain unchanged.

Rationale: J1 and J5 already fit when their rotated courtyards are evaluated correctly; only SW1 moves 2 mm right, which is the minimum placement change that separates the real J1/SW1 courtyards without changing the outline or disturbing another footprint.

## OpenLog mechanical pass — final placement

- A1 `WeatherBalloon:SparkFun_OpenLog_DEV-13712_Carrier` is at (171,110) mm, rotation 0°, top-side and direct-soldered. Its official 15.24 × 19.05 mm body and 16.24 × 20.05 mm courtyard lie outside the fixed LightAPRS body zone. The BLK-through-GRN pad order and pad geometry are unchanged; pads 2/3/5 are now GND/LOGGER_5V/OPENLOG_RXI and pins 1/4/6 remain intentionally unconnected.
- C2 is at (173,121) mm and C1 at (173,115) mm. Both leaded bypass capacitors remain close to A1 on `LOGGER_5V`; verify leakage within the approved current budgets.
- The outline is (100,91.5)–(180,170) mm, 80 × 78.5 mm. Only the top edge moved, by 8.5 mm; A1's microSD end faces that edge so the card and solder-down header remain accessible for home assembly.
- A2 is at (106,121), rotation 270°, and leaded through-hole R4 is at (166.62,118), rotation 180°. A2 pads 1/2 connect directly to `PACK_SW`, pad 3 to GND, and pad 4 to `LOGGER_5V`; R4 separates `UART_TX` from `OPENLOG_RXI`. The fixed LightAPRS interface, direct cutdown feed, bottom RF layout, all unrelated routes, and the six exact H3/J7 and H4/J6 exclusions remain unchanged.

Rationale: moving A1 9 mm right and extending only the top edge is the smallest coherent change that clears the fixed LightAPRS body reservation, contains the real OpenLog courtyard, and provides edge access without disturbing the RF or power layout.

## SMA routing pass — final first-pass fanout

- J3 remains fixed at (168,162), rotation 0°, with J6 `RF_APRS` routed on 0.5 mm F.Cu to center pad 1 along the footprint centerline between the upper shield tabs.
- J4 remains fixed at (112,162), rotation 0°, with J7 `RF_WSPR` routed on 0.5 mm F.Cu to center pad 1 along the footprint centerline between the upper shield tabs.
- On each connector, all four through-hole pad-2 shield tabs are joined by a symmetric 1.0 mm B.Cu U-fanout and tied at the connector centerline to the existing 1.0 mm bottom GND trunk. The two dangling placeholder ground stubs are gone.
- All footprints, orientations, board edges, RF/mechanical reservation drawings, unrelated copper, and the six exact H3/J7 and H4/J6 exclusions remain unchanged.

Rationale: centerline entry clears the real shield holes while the short symmetric shield fanout provides complete first-pass return connectivity with the minimum bounded routing change. This does not release the RF geometry for fabrication: trace width/spacing and the final return-via strategy still require released-stackup calculation, and both launches require VNA validation.

## Completed substitution state and remaining fabrication holds

All substitutions are complete: the board contains 23 populated electrical footprints plus four NPTH mounting holes, no `CopperheadDraft_*` names, and zero SMD pads. All populated parts use plated through-hole pads. J2's stock footprint is stored at 0° because its library-local pad row is vertical.

The final all-through-hole placement is C1 (173,115), C2 (173,121), C3 (173,132), C4 (107.7,133.3), C5 (103,115.5), U1 (161,121.5), U2 (114,133), D1 (173,145), Q1 (115.7,149), R1 (160,145), R2 (103,148), and R3 (114,144), in millimetres. Normal KiCad DRC reports zero violations and zero unconnected pads.

The design is not fabrication-ready until the physical LightAPRS module, hole pattern, header alignment, exact purchased MPNs, and all connector orientations pass a 1:1 print and mechanical mock-up. The released stackup must be used to calculate the two 50 Ω launches, finalize the return-via strategy, and support VNA validation. The 2 A/30 s cutdown path still requires copper, connector, MOSFET SOA, and thermal qualification. Enclosure, cable, microSD, switch, and SMA access must be checked in the payload assembly. Run final ERC, DRC, courtyard, 3D/mechanical, and fabrication review and regenerate `outputs/` only after those holds are closed.
