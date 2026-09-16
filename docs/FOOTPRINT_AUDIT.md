# Real-footprint audit

Date: 2026-09-16

This audit is the input for the next Copperhead placement and routing pass. The
current PCB still contains `CopperheadDraft_*` placeholders; Copperhead has not
been run as part of this audit.

## Assembly constraint

Every board-mounted part is intentionally soldered for home assembly. Do not
replace the LightAPRS or OpenLog carrier holes with female sockets or other
plug-in module connectors. Their already-installed header pins enter from the
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
| C1-C3 | `Capacitor_SMD:C_0603_1608Metric` | 2.96 x 1.46 mm each | Stock KiCad footprint; selected MPNs are 0603. |
| U1 | `Package_SO:SOIC-16_3.9x9.9mm_P1.27mm` | 7.40 x 10.40 mm | Stock KiCad footprint; matches PCF8574T SO16 package. |
| D1 | `LED_SMD:LED_0603_1608Metric` | 2.965 x 1.47 mm | Stock KiCad footprint; matches LTST-C190KGKT 0603 package. |
| R1-R3 | `Resistor_SMD:R_0603_1608Metric` | 2.96 x 1.46 mm each | Stock KiCad footprint. |
| J5 | `Connector_JST:JST_XH_S2B-XH-A_1x02_P2.50mm_Horizontal` | 8.40 x 12.51 mm | Stock KiCad footprint; 3 A family provides margin over the 2 A cutdown pulse. Place at edge with wire-service clearance. |
| Q1 | `Package_TO_SOT_SMD:SOT-23` | 3.86 x 3.40 mm | Stock KiCad footprint; matches AO3400A package. |
| J6, J7 | `Connector_PinHeader_2.54mm:PinHeader_1x01_P2.54mm_Vertical` | 3.54 x 3.54 mm each | Stock footprint for the LightAPRS VHF/HF contacts. Preserve the measured module-corner locations. |
| J3, J4 | `Connector_Coaxial:SMA_Amphenol_132134_Vertical` | 8.34 x 8.34 mm each | Exact stock KiCad footprints fixed at J3 (168,162) and J4 (112,162), rotation 0°. Pad 1 is the RF center; four through-hole pads numbered 2 are the GND shield tabs. Retain the existing RF/mechanical and cable reservations beyond the component courtyard and verify downward mating in the mechanical mock-up. |
| H1-H4 | `MountingHole:MountingHole_2.2mm_M2` | 4.90 mm diameter | Stock non-plated hole. Verify the physical LightAPRS hole diameter and center locations before fabrication. |

## Module and non-courtyard envelopes

- LightAPRS-W 2.0 body: 32.77 x 54.80 mm.
- LightAPRS mounting-hole center rectangle: nominal 28.18 x 38.16 mm; the
  current coordinate transcription is 28.20 x 38.17 mm because of rounding.
- OpenLog body: 15.24 x 19.05 mm; included in A1's custom courtyard.
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
- Only local PACK_IN, PACK_SW, GND, and schematic-named CUTDOWN_DRAIN copper was repaired. Battery and cutdown widths remain 1.0–1.5 mm except the pre-existing 0.6 mm Q1 drain neck. The six exact H3/J7 and H4/J6 vendor-module DRC exclusions remain unchanged.

Rationale: J1 and J5 already fit when their rotated courtyards are evaluated correctly; only SW1 moves 2 mm right, which is the minimum placement change that separates the real J1/SW1 courtyards without changing the outline or disturbing another footprint.

## OpenLog mechanical pass — final placement

- A1 `WeatherBalloon:SparkFun_OpenLog_DEV-13712_Carrier` is at (171,110) mm, rotation 0°, top-side and direct-soldered. Its official 15.24 × 19.05 mm body and 16.24 × 20.05 mm courtyard lie outside the fixed LightAPRS body zone. The BLK-through-GRN pad order and pad geometry are unchanged; pads 2/3/5 remain GND/3V3/UART_TX and pins 1/4/6 remain intentionally unconnected.
- C2 remains at (164,114) mm, rotation 0°, and C1 remains at (168,114) mm, rotation 0°. Both bypass capacitors remain close to A1's supply header while avoiding the module body and the fixed U1 corridor.
- The outline is (100,91.5)–(180,170) mm, 80 × 78.5 mm. Only the top edge moved, by 8.5 mm; A1's microSD end faces that edge so the card and solder-down header remain accessible for home assembly.
- Only the stale A1 GND and UART_TX route ends plus the local A1 3V3/bypass feed were repaired. The fixed LightAPRS interface, bottom RF layout, all unrelated routes, and the six exact H3/J7 and H4/J6 exclusions remain unchanged.

Rationale: moving A1 9 mm right and extending only the top edge is the smallest coherent change that clears the fixed LightAPRS body reservation, contains the real OpenLog courtyard, and provides edge access without disturbing the RF or power layout.

## SMA routing pass — final first-pass fanout

- J3 remains fixed at (168,162), rotation 0°, with J6 `RF_APRS` routed on 0.5 mm F.Cu to center pad 1 along the footprint centerline between the upper shield tabs.
- J4 remains fixed at (112,162), rotation 0°, with J7 `RF_WSPR` routed on 0.5 mm F.Cu to center pad 1 along the footprint centerline between the upper shield tabs.
- On each connector, all four through-hole pad-2 shield tabs are joined by a symmetric 1.0 mm B.Cu U-fanout and tied at the connector centerline to the existing 1.0 mm bottom GND trunk. The two dangling placeholder ground stubs are gone.
- All footprints, orientations, board edges, RF/mechanical reservation drawings, unrelated copper, and the six exact H3/J7 and H4/J6 exclusions remain unchanged.

Rationale: centerline entry clears the real shield holes while the short symmetric shield fanout provides complete first-pass return connectivity with the minimum bounded routing change. This does not release the RF geometry for fabrication: trace width/spacing and the final return-via strategy still require released-stackup calculation, and both launches require VNA validation.

## Required next Copperhead pass

1. Replace every remaining `CopperheadDraft_*` board footprint with the target map above.
2. Retain the qualified A1/C1/C2 cluster and top-edge microSD access unless later enclosure measurements require an explicit mechanical revision.
3. Keep both vertical SMA connectors on the bottom and preserve the extra RF and
   cable keepouts.
4. Re-place and reroute after real courtyard substitution; do not preserve draft
   coordinates when they conflict with the real envelopes.
5. Run ERC, DRC, courtyard-overlap review, 3D/mechanical review, and regenerate
   `outputs/` only after the physical LightAPRS header/hole measurements are
   confirmed.
