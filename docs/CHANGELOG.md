# Design changelog

Append-only, newest first. One entry per committed copperhead run.

## 2026-09-17 — Export-only refresh from the current verified design. Do not modify schematic or PCB sources. Regenerate all existing output artifacts, including .copperhead/renders/board.svg, .copperhead/renders/weather-balloon-logger.svg, outputs/board.svg, outputs/renders/board-full-color.svg, outputs/renders/weather-balloon-logger.svg, all Gerbers and drill files in outputs/gerbers, outputs/board.step, the outline DXF, and BOM artifacts. Preserve the current verified through-hole design and readable silkscreen exactly.

- Change: refresh-all-verified-design-exports
- Files: outputs/
- Verification: ERC clean, DRC clean

## 2026-09-17 — Export-only refresh from the current verified design. Do not modify schematic, PCB, intent, libraries, constraints, firmware, BOM, or design docs. Regenerate .copperhead/renders/board.svg and weather-balloon-logger.svg plus outputs/board.svg, outputs/renders/weather-balloon-logger.svg, Gerbers, drill, STEP, outline DXF, and BOM artifacts from the current committed PCB/schematic state using deterministic export tools. Preserve the current zero-SMD all-through-hole design. Run ERC, DRC, drift, legibility, and constraints. Commit the already-synchronized documentation changes together with refreshed exports only if all checks are clean.

- Change: refresh-verified-design-exports
- Files: outputs/, weather-balloon-logger.svg
- Verification: ERC clean, DRC clean

## 2026-09-17 — Final PCB mechanical/legend cleanup. Current electrical DRC is clean with zero unconnected pads. Do not change schematic, intent, BOM, scripts, outline, RF routes, or functional topology. Fix the remaining 30 DRC findings only: move C4 and C5 to eliminate both J5 courtyard overlaps and three PTH-inside-courtyard errors, rerouting only their LOGGER_5V/GND connections while preserving electrical cleanliness; adjust F.SilkS geometry in both project KEMET footprint library files and their embedded C1-C5 board footprints so silk does not cross their own pad solder-mask openings; reposition or hide only reference text and local silk strokes causing the listed U1/R4, J5/C4/C5, U2/R3/Q1, and A2/U2 silk collisions. Preserve fabrication/fab/courtyard dimensions and all pads. Finish with normal KiCad DRC zero violations and zero unconnected items. Do not commit.

- Change: final-pcb-mechanical-legend-cleanup
- Files: library/WeatherBalloon.pretty/KEMET_C315C104K5R5TA.kicad_mod, library/WeatherBalloon.pretty/KEMET_C322C475K5R5TA.kicad_mod, weather-balloon-logger.kicad_pcb, docs\DECISIONS.md, docs/PINOUT.md
- Verification: ERC clean, DRC clean

## 2026-09-17 — Export-only refresh from the current committed design. Do not modify the schematic, PCB, schematic.intent.json, footprint libraries, constraints, firmware, BOM, or design documentation. Regenerate the current PCB SVG in .copperhead/renders and refresh outputs/board.svg using Copperhead's export_svg/export_outputs tools; bundled deterministic export artifacts may be refreshed as required by export_outputs. Preserve all existing fabrication qualification holds. Then run ERC, DRC, drift, schematic legibility, and constraint/spec validation. Finish only if the exports reflect the current weather-balloon-logger.kicad_pcb and checks are clean. Do not make layout or electrical changes.

- Change: refresh-current-pcb-exports
- Files: outputs/
- Verification: ERC clean, DRC clean

## 2026-09-17 — Replace R4 with leaded through-hole part

- Replaced R4's 0603 land pattern with `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal`.
- R4 now uses two 0.8 mm drilled holes, mounts horizontally at (166.62,118), and is soldered from the underside.
- Rerouted only local UART, GND, and I2C copper needed for the through-hole leads.
- Verification: normal KiCad DRC has zero violations and zero unconnected items; Copperhead ERC, DRC, drift, and constraints are clean.

## 2026-09-17 — Implement split-power PCB

- Placed direct-solder A2 at (106,121), 270°, and R4 at (159.8,113.3), 90°, without moving any existing footprint or changing the outline.
- Routed A2 VIN/SHDN directly from `PACK_SW`, GND to the pack return, and fixed `LOGGER_5V` to A1/C1/C2; the cutdown and LightAPRS feeds remain direct `PACK_SW` branches.
- Replaced the direct UART trace with `UART_TX` → R4 → `OPENLOG_RXI` and moved the board label to (110,96) for module access.
- Verification: normal KiCad DRC has zero violations and zero unconnected items; Copperhead ERC, DRC, drift, and constraints are clean.

## 2026-09-17 — Capture split-power schematic

- Added A2 Pololu S7V8F5 with SHDN/VIN on `PACK_SW`, GND common, and VOUT on new `LOGGER_5V`.
- Moved A1/C1/C2 from `3V3` to `LOGGER_5V` in the captured schematic.
- Added R4 1 kΩ between `UART_TX` and new `OPENLOG_RXI` to limit startup/brownout back-power.
- Preserved direct `PACK_SW` feeds to LightAPRS J2.1 and cutdown J5.1; PCB placement and routing remain the next bounded pass.
- Verification: Copperhead ERC, DRC, drift, and constraints clean; schematic legibility has zero errors and one unchanged low-utilization advisory.

## 2026-09-17 — Resume and complete the already proposed bounded add-pololu-s7v8f5-carrier-footprint pass. The exact new project-local footprint file WeatherBalloon:Pololu_S7V8F5_Carrier has now been created because the previous Copperhead run could not create a new KiCad file. Audit it against the validated OpenSpec proposal and official data: top-side direct-solder, 11.43 x 16.51 mm body, 1.02 mm official holes represented by 1.0 mm drills, 2.54 mm pitch, row centered and 1.27 mm from edge, top-view left-to-right pads 4 VOUT, 3 GND, 2 VIN, 1 SHDN. Make only necessary corrections to that footprint. Update library/README.md, docs/BOM.md, docs/FOOTPRINT_AUDIT.md, and this run's OpenSpec tasks to reserve A2 and correct C1/C2 future LOGGER_5V/current-limit prose. Do not modify schematic, PCB, schematic.intent.json, constraints, outputs, firmware, or historical proposals. Run ERC, DRC, drift, and commit this bounded footprint pass only if clean.

- Change: add-pololu-s7v8f5-carrier-footprint
- Files: library/README.md, docs/BOM.md, docs/FOOTPRINT_AUDIT.md, openspec/changes/add-pololu-s7v8f5-carrier-footprint/tasks.md
- Verification: ERC clean, DRC clean

## 2026-09-17 — Documentation and constraints pass only for the approved split-power architecture. Fixed battery is exactly 3 series Energizer L91 cells, 3.0-5.4 V. LightAPRS-W 2.0 RAW/J2.1 remains directly on switched PACK_SW so its GPS stays powered continuously for at least four hours. Cutdown J5.1 remains directly on PACK_SW and must never be routed through a regulator. Add Pololu S7V8F5 item 2123 as the selected dedicated fixed 5 V buck-boost module for OpenLog only: VIN and SHDN on PACK_SW, GND on GND, VOUT creates LOGGER_5V, and OpenLog A1 VCC moves from LightAPRS 3V3 to LOGGER_5V. Record input 2.7-11.8 V, fixed 5 V, <0.2 mA quiescent, 0.1-inch four-pin interface, direct-solder straight header, no reverse-polarity protection, and module temperature rating unverified requiring cold qualification. Update only current authoritative documentation, constraints, BOM, decisions/changelog, and this run's OpenSpec files; do not edit schematic, PCB, footprint libraries, outputs, firmware, or old historical proposals. Supersede stale 4S, 3V3-powered OpenLog, and 2 mA/1.85 mA limits in current docs. Use realistic limits of OpenLog idle <=7 mA, write <=25 mA, regulator Iq <=0.2 mA, board-added idle <=8 mA, and board-added active/write peak <=30 mA. Preserve existing PCF8574 and safety leakage limits. Keep the four-hour demand <=800 mAh and require >=1600 mAh usable capacity under actual cold/load profile. Run Copperhead checks and commit this bounded documentation pass only if consistent.

- Change: document-split-power-openlog-regulator
- Files: docs/SPEC.md, docs/SUBSYSTEMS.md, docs/BOM.md, docs/PINOUT.md, docs/DEVPLAN.md, docs/LAYOUT.md, docs/FOOTPRINT_AUDIT.md, docs/CHANGELOG.md, docs\DECISIONS.md, openspec/changes/document-split-power-openlog-regulator/tasks.md
- Verification: ERC clean, DRC clean

## 2026-09-16 — Document approved split-power OpenLog architecture

- Change: document-split-power-openlog-regulator
- Files: current authoritative docs, .copperhead/constraints.json, this run's OpenSpec files, docs/DECISIONS.md, docs/CHANGELOG.md
- Verification: documentation-only pass; fixed exactly 3s L91 at 3.0–5.4 V, preserved direct PACK_SW feeds to LightAPRS RAW/J2.1 and cutdown J5.1, selected Pololu S7V8F5 item 2123 for OpenLog-only LOGGER_5V, and superseded stale logger current budgets; schematic/PCB implementation intentionally deferred

## 2026-09-16 — SMA footprint/routing pass only. J3 and J4 now contain the exact KiCad footprints Connector_Coaxial:SMA_Amphenol_132134_Vertical, each with center pad 1 and four through-hole shield pads numbered 2. Their current positions are J3 (168,162) for RF_APRS and J4 (112,162) for RF_WSPR and must remain fixed; the footprints fit the outline and existing RF reservation.\n\nRepair only this real-footprint fallout:\n- Keep all footprints, orientations, and board edges fixed.\n- Preserve J6 RF_APRS to J3 center pad 1 and J7 RF_WSPR to J4 center pad 1.\n- Reroute only RF_APRS, RF_WSPR, and local GND so neither center conductor crosses or violates clearance to any shield pad.\n- Connect all four pad-2 shield tabs on each SMA solidly to GND using short symmetric local copper and/or nearby ground vias/trunk connections appropriate for a first-pass RF launch.\n- Remove dangling placeholder ground stubs.\n- Preserve the existing >=5 mm RF/mechanical reservation drawings and keep unrelated copper/components out.\n- Do not claim final 50-ohm qualification: document that trace geometry and return-via strategy still require released stackup calculation and VNA validation.\n- Preserve all six exact LightAPRS mechanical-interface exclusions; add no global DRC suppression.\n- Update docs/LAYOUT.md and docs/FOOTPRINT_AUDIT.md with the actual SMA pad/fanout result and remaining RF fabrication hold.\n- Run normal kicad-cli DRC and Copperhead checks. Commit this pass only with zero normal DRC violations and zero unconnected items.

- Change: repair-sma-footprint-routing
- Files: weather-balloon-logger.kicad_pcb, docs/LAYOUT.md, docs/FOOTPRINT_AUDIT.md, docs/CHANGELOG.md, docs\DECISIONS.md
- Verification: ERC clean, DRC clean

## 2026-09-16 — Repair exact SMA launch routing

- Change: repair-sma-footprint-routing
- Files: weather-balloon-logger.kicad_pcb, docs/LAYOUT.md, docs/FOOTPRINT_AUDIT.md, docs/CHANGELOG.md, docs/DECISIONS.md
- Verification: exact fixed J3/J4 footprints retain J6→J3.1 RF_APRS and J7→J4.1 RF_WSPR; all eight pad-2 shield tabs connect through symmetric local B.Cu fanouts to the bottom GND trunk; normal DRC clean with zero violations and zero unconnected items; 50 Ω stackup calculation, final return-via design, and VNA validation remain fabrication holds

## 2026-09-16 — OpenLog mechanical pass only. A1 now contains the exact project footprint WeatherBalloon:SparkFun_OpenLog_DEV-13712_Carrier with the official 15.24 x 19.05 mm module body/courtyard and solder-down header. The real body currently extends above the draft board outline, and only two stale routes plus two A1 edge-silk findings remain.\n\nMake the smallest coherent OpenLog layout change:\n- Keep the exact A1 footprint identity, pad geometry, top-side installation, and direct-solder assembly.\n- Keep the LightAPRS module interface J2/J6/J7/H1-H4 and its 32.77 x 54.80 mm reserved body coordinates fixed.\n- Keep all footprints fixed except A1, C1, and C2. You may move/rotate only those three to create a practical OpenLog cluster outside the LightAPRS body zone.\n- Enlarge the board outline only as much as needed to fully contain A1's courtyard and allow practical access to the OpenLog microSD card and header for home assembly. Prefer extending the top/right edges rather than disturbing the fixed module and bottom RF layout.\n- Keep A1 pin order BLK through GRN and preserve nets: pad 2 GND, pad 3 3V3, pad 5 UART_TX; unused module pins remain intentionally unconnected as captured.\n- Reroute only A1/C1/C2-related GND, 3V3, and UART_TX copper. Remove stale route ends and keep bypass capacitors reasonably close to A1's supply pins.\n- Keep every other footprint and route unchanged except an unavoidable ground/power trunk extension.\n- Preserve the six exact documented LightAPRS interface exclusions and do not add global DRC suppression.\n- Resolve all DRC/connectivity/silkscreen/edge findings and update docs/LAYOUT.md and docs/FOOTPRINT_AUDIT.md with the final outline and A1/C1/C2 coordinates plus access rationale.\n- Run normal kicad-cli DRC and Copperhead checks. Commit only with zero normal DRC violations and zero unconnected items.

- Change: repair-openlog-mechanical-layout
- Files: docs/LAYOUT.md, docs/FOOTPRINT_AUDIT.md, docs\DECISIONS.md, weather-balloon-logger.kicad_pcb, docs/CHANGELOG.md
- Verification: ERC clean, DRC clean

## 2026-09-16 — Repair exact OpenLog mechanical layout

- Change: repair-openlog-mechanical-layout
- Files: weather-balloon-logger.kicad_pcb, docs/LAYOUT.md, docs/FOOTPRINT_AUDIT.md, docs/CHANGELOG.md, docs/DECISIONS.md
- Verification: normal DRC clean with zero violations and zero unconnected items; ERC clean; drift clean; schematic legibility has zero errors and one unchanged low-utilization advisory; A1 is at (171,110), C1/C2 remain at (168,114)/(164,114), and only the top outline edge extends to y=91.5 mm

## 2026-09-16 — Power connector pass only. J1, J5, and SW1 now contain their exact real footprints: Connector_JST:JST_PH_S2B-PH-K_1x02_P2.00mm_Horizontal, Connector_JST:JST_XH_S2B-XH-A_1x02_P2.50mm_Horizontal, and WeatherBalloon:SW_CK_7101SYZQE. SW1 is the requested C&K 7101SYZQE with direct-solder plated slots; keep its library identity and pad geometry.\n\nRepair this batch in the smallest manufacturable change:\n- Keep the board outline and every footprint except J1, J5, and SW1 fixed.\n- You may move and rotate only J1, J5, and SW1 so their real bodies/courtyards do not overlap, remain fully inside the board, and their mating/actuation directions remain accessible from board edges for hand assembly.\n- Preserve net intent: SW1 pad 2 is PACK_IN common, pad 1 is switched PACK_SW, and pad 3 is intentionally no-connect. Never connect pad 3.\n- Reroute only PACK_IN, PACK_SW, GND, and CUTDOWN_OUT as locally necessary; remove stale track segments beneath the real switch/connector bodies.\n- Maintain existing current-capable track widths for the battery and cutdown paths.\n- Resolve all new courtyard, edge, silkscreen, solder-mask, short, and connectivity findings without global DRC suppression. Reference-text or nonfunctional silk may move/hide.\n- Preserve the six already documented and exact vendor-module exclusions in weather-balloon-logger.kicad_pro.\n- Update docs/FOOTPRINT_AUDIT.md with final J1/J5/SW1 locations/orientations and hand-assembly accessibility.\n- Run kicad-cli DRC and Copperhead checks. Commit this bounded pass only if normal DRC has zero violations and zero unconnected items.

- Change: repair-power-connector-footprints
- Files: weather-balloon-logger.kicad_pcb, docs/LAYOUT.md, docs/FOOTPRINT_AUDIT.md, docs/CHANGELOG.md, docs\DECISIONS.md
- Verification: ERC clean, DRC clean

## 2026-09-16 — Repair real power connector placement

- Change: repair-power-connector-footprints
- Files: weather-balloon-logger.kicad_pcb, docs/FOOTPRINT_AUDIT.md, docs/LAYOUT.md, docs/CHANGELOG.md, docs/DECISIONS.md
- Verification: normal DRC clean with zero violations and zero unconnected items; ERC clean; drift clean; J1/J5 remain at their edge-accessible real-footprint positions, only SW1 moves to (114,108), local PACK_IN/PACK_SW/GND/CUTDOWN_DRAIN copper is repaired, pad 3 remains unconnected, and all six vendor-module exclusions are preserved

## 2026-09-16 — Add front-silkscreen (F.SilkS) board label text reading 'JAVAS Logger' in a clear, readable area that does not overlap any component, pad, trace, mounting hole (H1-H4), the 32.77 x 54.80 mm module zone, or the >=5 mm SMA keepouts. Use a standard silkscreen text height of about 1.5-2 mm, horizontal and right-reading (upright). A good open area is the left-center of the board. Update docs/LAYOUT.md to note the label, then re-run DRC and keep it clean.

- Change: add-javas-logger-silkscreen-label
- Files: weather-balloon-logger.kicad_pcb, docs/LAYOUT.md, docs/CHANGELOG.md, docs\DECISIONS.md
- Verification: ERC clean, DRC clean

## 2026-09-16 — Add front-silkscreen `JAVAS Logger` board label

- Change: add-javas-logger-silkscreen-label
- Files: weather-balloon-logger.kicad_pcb, docs/LAYOUT.md, docs/CHANGELOG.md, docs/DECISIONS.md
- Verification: label centered at (114.5, 118.0) mm on F.SilkS with 1.8 mm upright text; DRC and drift re-run

## 2026-09-16 — Apply the measured LightAPRS-W 2.0 coordinates from docs/SUBSYSTEMS.md section 6 (Measured coordinate transcription) to the board. (1) Place the four module standoff holes as ~M2 (2.2 mm) holes at H1 (125.9,115.35), H2 (154.1,115.35), H3 (125.9,153.52), H4 (154.1,153.52), forming a 28.18 x 38.16 mm rectangle. (2) Keep J2 (11-pin, 2.548 mm pitch, 270 deg) along the right edge at about x=154.9, centered vertically over the rectangular body, spanning about y=121.7 to 147.2. (3) Keep J7 HF at the module bottom-left and J6 VHF at the module bottom-right, positioned clear of the H3/H4 standoff holes. (4) Keep every other component outside the 32.77 x 54.80 mm module zone and honor the >=5 mm SMA keepouts. Update docs/LAYOUT.md and re-run DRC; iterate placement and routing until DRC is clean.

- Change: apply-measured-lightaprs-module-coordinates
- Files: weather-balloon-logger.kicad_pcb, docs/LAYOUT.md, docs\DECISIONS.md
- Verification: ERC clean, DRC clean

## 2026-09-16 — Correct the module-mount layout to the exact verified LightAPRS-W 2.0 geometry and FACE-UP orientation in docs/SUBSYSTEMS.md section 6. (1) Resize the module-mount zone to exactly 32.77 x 54.80 mm with the long axis vertical. (2) The module mounts FACE UP, so carrier pads must match the module top view with NO left-right mirror: place J2 (11-pin header) on the zone edge that matches the module's header edge, and place the RF corner contacts as HF bottom-left = J7 and VHF bottom-right = J6, which reverses the previous mirrored placement. (3) Keep RF nets VHF/J6 -> J3 (RF_APRS) and HF/J7 -> J4 (RF_WSPR); the two SMA jacks are edge-mounted facing down, so move J3 toward the VHF/right side and J4 toward the HF/left side for short launches. (4) Place four approximate M2 standoff holes on the dimensioned pattern with about a 42.73 mm outer horizontal span. (5) Keep J1, SW1, A1, U1, C3, Q1 and all passives outside the module zone and honor the >=5 mm SMA keepouts. Update docs/LAYOUT.md and the board, then re-run DRC.

- Change: correct-face-up-lightaprs-module-layout
- Files: weather-balloon-logger.kicad_pcb, docs/LAYOUT.md, docs\DECISIONS.md
- Verification: ERC clean, DRC clean

## 2026-09-16 — Re-lay-out the board for the revised schematic and reserve a 32 x 55 mm LightAPRS-W 2.0 module-mount zone per docs/SUBSYSTEMS.md section 6. Place the mating headers J2 (11-pin host interface), J6 (VHF) and J7 (HF) INSIDE that zone, positioned to align with the module's 2.54 mm edge header and its bottom opposite-corner HF/VHF pins so the module plugs directly onto them; add corner standoff mounting holes in the zone. Place all OTHER components (J1 pack input, SW1, A1 OpenLog, U1 PCF8574T + C3, J3/J4 SMA jacks, Q1 cutdown plus D1/R1/R2/R3/C1/C2) OUTSIDE the module footprint so they cannot collide with the module body, honoring the >=5 mm SMA keepouts. Update docs/LAYOUT.md and the board, then re-run DRC.

- Change: relayout-revised-lightaprs-module-zone
- Files: weather-balloon-logger.kicad_pcb, docs/LAYOUT.md, docs/SUBSYSTEMS.md, docs/CHANGELOG.md, docs\DECISIONS.md
- Verification: ERC clean, DRC clean

## 2026-09-16 — Re-layout revised LightAPRS module zone

- Change: relayout-revised-lightaprs-module-zone
- Files: weather-balloon-logger.kicad_pcb, docs/LAYOUT.md, docs/SUBSYSTEMS.md, docs/CHANGELOG.md, docs/DECISIONS.md, .copperhead/constraints.json
- Verification: revised 18-refdes board synchronized to the schematic; 32 × 55 mm module zone with J2/J6/J7 and four approximate standoff holes; all other components outside; separate SMA envelopes retained; DRC clean; fabrication remains blocked on exact module geometry, footprints, RF, thermal, and part qualification

## 2026-09-16 — Revise the host interface and add an I2C LED expander to match the verified LightAPRS-W 2.0 module (docs/SUBSYSTEMS.md section 6). Final pin plan: A1/PB08 = OpenLog UART TX one-way (host TX to OpenLog RXI, no host RX); A2/PB09 = cutdown gate on a direct GPIO (keep R2 series gate resistor and R3 gate pulldown for default-off at power-up); write LED and future GPS-status LEDs on a PCF8574 I2C GPIO expander. (1) Change J2 to the module's 11-position 2.54mm edge header using an installed 11-pin connector symbol Connector_Generic:Conn_01x11, pin order RAW, GND, A1(PB08), A2(PB09), 3V3, GND, SCL, SDA, SCK, MISO, MOSI; wire PACK_SW switched pack+ to RAW, board 3V3 rail from 3V3, GND to the GND pins, A1 to OpenLog RXI, A2 to the cutdown gate network. (2) Add a PCF8574 I2C GPIO expander using an installed KiCad symbol powered from 3V3/GND with a 100nF decoupling cap, address pins strapped for 0x20, SDA/SCL on the module's exposed I2C bus; drive write LED D1 active-low from output P0 (expander output to D1 cathode, D1 anode to 3V3 via R1); leave P1..P7 available for future GPS-satellite-status LEDs as no-connect. (3) Move the cutdown gate source from A0 to A2/PB09, keeping the intentional pulldown so it is default-off. (4) Represent RF as two single contacts HF and VHF at the module opposite bottom corners: VHF to J3 (RF_APRS), HF to J4 (RF_WSPR); replace the 2-pin J6 with the two corner contacts. (5) Update docs/PINOUT.md, docs/BOM.md, docs/SUBSYSTEMS.md and the schematic; keep 3.3V logic and all leakage/idle budgets. Run ERC.

- Change: revise-lightaprs-host-and-i2c-led-expander
- Files: schematic.intent.json, docs/BOM.md, docs/PINOUT.md, docs/SUBSYSTEMS.md, weather-balloon-logger.kicad_sch, docs/SPEC.md, firmware/tools/generate_pins.py, firmware/include/pins.h, firmware/include/cutdown.h, firmware/README.md, firmware/DEVPLAN.md, docs/DEVPLAN.md, docs/LAYOUT.md, docs/CHANGELOG.md, docs\DECISIONS.md
- Verification: ERC clean, DRC clean

## 2026-09-16 — revise verified LightAPRS interface and LED expansion

- Change: revise-lightaprs-host-and-i2c-led-expander
- Files: schematic.intent.json, weather-balloon-logger.kicad_sch, docs/BOM.md, docs/PINOUT.md, docs/SPEC.md, docs/SUBSYSTEMS.md, docs/DEVPLAN.md, docs/LAYOUT.md, firmware pin-contract docs/files, .copperhead/constraints.json, docs/DECISIONS.md
- Verification: ERC clean; drift clean; schematic legibility 0 errors with one low-utilization advisory; DRC clean on the unchanged but explicitly obsolete PCB; installed functional symbols and PCF8574T pins verified; engine-local copperhead_power helpers remain intentionally exempt; existing PCB/outputs remain blocked pending layout synchronization

## 2026-09-16 — create pipeline stage: devplan

- Change: devplan-weather-balloon-logger
- Files: docs/DEVPLAN.md, docs/CHANGELOG.md, docs\DECISIONS.md
- Verification: ERC clean, DRC clean

## 2026-09-16 — create pipeline stage: devplan

- Change: devplan-weather-balloon-logger
- Files: docs/DEVPLAN.md, docs/CHANGELOG.md, docs/DECISIONS.md
- Verification: hardware bring-up, probe-location, risk, and prototype-order plan added; ERC, DRC, drift, and schematic legibility checks run in this stage

## 2026-09-16 — create pipeline stage: firmware

- Change: firmware-weather-balloon-logger
- Files: firmware/tools/generate_pins.py, firmware/include/pins.h, firmware/include/cutdown.h, firmware/include/openlog.h, firmware/include/telemetry.h, firmware/src/cutdown.cpp, firmware/src/openlog.cpp, firmware/src/telemetry_stub.cpp, firmware/WeatherBalloonLogger.ino, firmware/README.md, firmware/DEVPLAN.md, docs/CHANGELOG.md, docs\DECISIONS.md, openspec/changes/firmware-weather-balloon-logger/tasks.md
- Verification: ERC clean, DRC clean

## 2026-09-16 — create pipeline stage: firmware

- Change: firmware-weather-balloon-logger
- Files: firmware/, docs/CHANGELOG.md, docs/DECISIONS.md, .copperhead/constraints.json
- Verification: pins generated from docs/PINOUT.md; safe one-record happy path added; C++11 compatibility/readback checks clean; firmware not compiled here because no exact board package/compiler/build action is exposed; ERC clean; DRC clean; drift clean; schematic legibility 0 errors with one low-utilization advisory

## 2026-09-16 — create pipeline stage: outputs

- Change: outputs-weather-balloon-logger
- Files: outputs/, outputs/BOM.csv, outputs/README.md, docs\DECISIONS.md, docs/CHANGELOG.md
- Verification: ERC clean, DRC clean

## 2026-09-16 — create pipeline stage: outputs

- Change: outputs-weather-balloon-logger
- Files: outputs/ Gerbers and drill, outputs/outline.dxf, outputs/board.step, outputs/board.svg, outputs/schematic.svg, outputs/BOM.csv, outputs/README.md, docs/CHANGELOG.md, docs/DECISIONS.md
- Verification: every requested export succeeded; ERC clean; DRC clean; drift clean; schematic legibility 0 errors with one low-utilization advisory; output package remains explicitly blocked from fabrication and procurement because CopperheadDraft footprints and all MPNs are UNVERIFIED

## 2026-09-16 — create pipeline stage: layout-draft

- Change: layout-draft-weather-balloon-logger
- Files: docs\DECISIONS.md
- Verification: ERC clean, DRC clean

## 2026-09-16 — create pipeline stage: layout-draft

- Change: layout-draft-weather-balloon-logger
- Files: docs\DECISIONS.md
- Verification: ERC clean, DRC clean

## 2026-09-16 — create pipeline stage: layout-draft

- Change: layout-draft-weather-balloon-logger
- Files: weather-balloon-logger.kicad_pcb, LAYOUT.md, docs/CHANGELOG.md, docs\DECISIONS.md
- Verification: ERC clean, DRC clean

## 2026-09-16 — create pipeline stage: layout-draft

- Change: layout-draft-weather-balloon-logger
- Files: weather-balloon-logger.kicad_pcb, LAYOUT.md, docs/CHANGELOG.md, docs/DECISIONS.md
- Verification: 80 × 70 mm coordinate-level board draft; all 15 refdes placed; critical power, ground, RF, decoupling, UART/LED, and cutdown nets routed; dual SMA clearance envelopes and ESD reservation areas documented; DRC clean; board SVG exported; board-local draft land patterns explicitly require verified-footprint replacement before fabrication

## 2026-09-16 — create pipeline stage: schematic

- Change: schematic-weather-balloon-logger
- Files: schematic.intent.json, weather-balloon-logger.kicad_sch, docs/BOM.md, docs/SPEC.md, docs/SUBSYSTEMS.md, docs/PINOUT.md, docs/CHANGELOG.md, docs\DECISIONS.md
- Verification: ERC clean

## 2026-09-15 — create pipeline stage: schematic

- Change: schematic-weather-balloon-logger
- Files: schematic.intent.json, weather-balloon-logger.kicad_sch, docs/PINOUT.md, docs/BOM.md, docs/SPEC.md, docs/SUBSYSTEMS.md, docs/CHANGELOG.md, docs/DECISIONS.md, .copperhead/constraints.json
- Verification: deterministic draft with 15 BOM parts and six subsystem groups; all BOM symbol pins confirmed; ERC clean; legibility 0 errors with one low-utilization advisory; BOM/PINOUT drift clean; generated copperhead_power rail helpers reconciled as engine-local symbols

## 2026-09-15 — create pipeline stage: part-selection

- Change: recover-part-selection-weather-balloon-logger
- Files: docs/BOM.md, docs/CHANGELOG.md, docs\DECISIONS.md
- Verification: ERC not required

## 2026-09-15 — recover pipeline stage: part-selection

- Change: recover-part-selection-weather-balloon-logger
- Files: docs/BOM.md, docs/CHANGELOG.md, docs/DECISIONS.md
- Verification: complete BOM reread; fresh installed-symbol searches and authoritative pin checks; power-budget audit; check_drift after readback

## 2026-09-15 — create pipeline stage: part-selection

- Change: part-selection-weather-balloon-logger
- Files: docs/BOM.md, docs/CHANGELOG.md, docs\DECISIONS.md
- Verification: ERC not required

## 2026-09-15 — recover pipeline stage: part-selection

- Change: part-selection-weather-balloon-logger
- Files: docs/BOM.md, docs/CHANGELOG.md, docs/DECISIONS.md
- Verification: exact five-column/one-refdes BOM read back; named-module absence and all selected installed symbols/pins tool-verified; constraint revisits resolved; check_drift run before finish

## 2026-09-15 — create pipeline stage: part-selection

- Change: part-selection-weather-balloon-logger
- Files: docs/BOM.md, docs/CHANGELOG.md, docs\DECISIONS.md
- Verification: ERC not required

## 2026-09-15 — create pipeline stage: part-selection

- Change: part-selection-weather-balloon-logger
- Files: docs/BOM.md, docs/CHANGELOG.md, docs/DECISIONS.md
- Verification: installed KiCad symbols searched and authoritative pins checked; BOM-to-schematic drift checked before finish

## 2026-09-15 — create pipeline stage: architecture

- Change: architecture-weather-balloon-logger
- Files: docs/SUBSYSTEMS.md, docs/CHANGELOG.md, docs\DECISIONS.md
- Verification: ERC not required

## 2026-09-15 — create pipeline stage: architecture

- Change: architecture-weather-balloon-logger
- Files: docs/SUBSYSTEMS.md, docs/CHANGELOG.md, docs/DECISIONS.md
- Verification: ERC not required (no schematic this stage)

## 2026-09-15 — create pipeline stage: spec-seed

- Change: seed-weather-balloon-logger-spec
- Files: docs/SPEC.md, docs\DECISIONS.md
- Verification: ERC not required
# 2026-09-21 — provisional LightHAB PCB rebuild

- Replaced the obsolete LightAPRS layout with the 12-reference LightHAB electrical design.
- Added a 90 × 80 mm outline, provisional 56 × 75 mm module zone, four provisional 3.2 mm NPTH holes, onboard SMA/USB mechanical keepouts, functional silkscreen labels, and a prominent no-fabrication warning.
- Preserved the coffee-balloon front-silkscreen artwork and moved all populated carrier parts to the left wing.
- Verification: KiCad ERC clean; DRC clean; zero unconnected items; zero SMD pads; Copperhead drift/constraints/legibility checks clean except the existing A4 paper-size advisory.
