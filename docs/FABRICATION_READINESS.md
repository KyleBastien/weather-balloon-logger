# Fabrication readiness checklist

Date: 2026-09-16

## Current disposition

**HOLD — do not upload the current `outputs/gerbers/` directory to a board
manufacturer yet.**

The design is electrically connected, uses only through-hole populated parts,
and currently passes ERC, DRC, Copperhead drift, and schematic-legibility
checks. The tracked drawings are useful review artifacts, but they are not a
released manufacturing package. The items below are the remaining evidence
needed to order an engineering prototype and then qualify a flight revision.

All carrier-mounted parts remain soldered through the PCB. LightAPRS, OpenLog,
and the Pololu regulator use direct-soldered headers; they are not sockets.

## Minimum remaining checklist

Only these four gates still block an **engineering prototype** order. The
detailed sections below define their evidence and the later flight tests.

1. [ ] Perform the 1:1 exact-parts fit check, especially the LightAPRS contact
   and mounting-hole geometry and the 1.0 mm carrier holes for the selected
   Würth headers.
2. [ ] Choose a fabricator and stackup (minimum 1 oz outer copper), then finish
   the two 50-ohm RF launches, return vias, and enforceable keepouts.
3. [ ] Check the complete payload mock-up and record the off-board battery,
   mating connector, crimp, wire, spacer, fastener, antenna, and nichrome
   specifications.
4. [ ] Incorporate those results, regenerate a fabricator-specific Gerber ZIP,
   and independently inspect it before placing a bare-board prototype order.

## Gate A — before ordering bare engineering prototype PCBs

Every required box in this section must be checked and linked to its evidence.

### 1. Reconcile the exact parts and BOM — required

- [x] Select the three LightAPRS interface parts: Würth `61301111121` for J2
  and `61300111121` for J6/J7.
- [ ] Record the off-board mating housings, crimp contacts, battery holder, and
  harness wire specifications.
- [x] Confirm PCB-part pin numbering, polarity, mating gender, current rating, operating
  temperature, lifecycle, and availability from current manufacturer data.
- [x] Add controlled MPN fields to all 23 populated schematic symbols and make
  `outputs/BOM.csv` reproducible with `scripts/export_bom.ps1`.
- [x] Replace the obsolete SMD-era BOM with the current THT selection and
  resolve R4 to the same `MFR-25FBF52-1K` axial part used for R1. The generated
  BOM has no blank or `UNVERIFIED` MPN fields.
- [x] Select SparkFun `DEV-13955`, the current OpenLog variant supplied with
  pre-soldered headers, for A1's direct-solder installation.
- [ ] Record approved alternates explicitly. Do not substitute a mechanically
  similar connector, switch, module, or transistor without rechecking its
  footprint and pinout.

Evidence: signed BOM review, datasheets for the ordered suffixes, and a BOM
diff against the schematic.

### 2. Perform a physical 1:1 fit check — required

- [x] Generate `outputs/renders/board-fit-check-1to1.pdf` at true 1:1 scale
  with hole/slot shapes and board outline visible.
- [ ] Print it at 100% / Actual Size, confirm the 80.0 x 78.5 mm outline with a
  ruler, and annotate the physical checks below.
- [ ] Place every exact purchased part over its footprint and insert leads into
  a drilled paper/card mock-up where practical.
- [ ] Confirm the custom 7101SYZQE solder lugs enter the 2.30 x 1.10 mm plated
  slots without forcing them. Datasheet review already confirms the nominal
  lug dimensions, 4.70 mm pitch, and pin 2 common.
- [ ] Confirm OpenLog body size, six-pin order, microSD access, and top-side
  orientation.
- [ ] Confirm Pololu S7V8F5 body, four-pin order, straight-header orientation,
  and top-side clearance.
- [ ] Confirm JST-PH and JST-XH mating direction, cable exit, strain relief, and
  polarity.
- [ ] Confirm IRLZ44NPBF G/D/S order, DIP notches, LED polarity, resistor lead
  pitch, capacitor lead pitch, and SMA orientation.

Evidence: annotated 1:1 print and photographs with the exact parts fitted.

### 3. Close the LightAPRS mechanical interface — required

- [ ] Measure the actual LightAPRS-W 2.0 board and compare it with the
  32.77 x 54.80 mm reserved body.
- [ ] Verify the J2 eleven-pin row position and physical alignment. Official
  imagery already confirms pitch, pin-1 end, electrical order, and face-up
  orientation.
- [ ] Verify the physical J6 VHF and J7 HF contact locations. Official imagery
  already confirms that they are not electrically reversed.
- [ ] Measure all four mounting-hole centers and diameters. Update H1-H4 if the
  actual module differs from the approximate CAD transcription.
- [ ] Check USB access, underside components, solder-joint access, spacer
  height, and the six narrowly scoped H3/J7 and H4/J6 DRC exclusions.

Evidence: dimensioned measurements or an authoritative vendor drawing plus a
photographed mechanical mock-up.

### 4. Finish the RF design for the selected fabricator — required

- [ ] Choose the fabricator, layer stackup, finished copper weight, dielectric
  thickness/material, board thickness, finish, and controlled-impedance policy.
- [ ] Recalculate both 50 ohm launches using that released stackup. The current
  0.5 mm traces are connectivity geometry, not proof of 50 ohms.
- [ ] Update trace geometry as required, add/finalize the ground-return via
  strategy, and convert the drawn SMA envelopes into enforceable keepout/rule
  areas.
- [ ] Verify at least 5 mm RF/mechanical clearance, battery-metal separation,
  cable bend volume, and the two downward-facing SMA penetrations.
- [ ] Decide whether ESD protection is intentionally omitted or fully capture
  selected devices in the schematic, BOM, and layout. A reserved drawing alone
  is not a fitted protection circuit.

Evidence: impedance calculation or fabricator field-solver result, selected
stackup, updated PCB rules, and RF/mechanical review signoff.

### 5. Close the cutdown current-path calculation — PCB analysis complete

- [x] Calculate the actual PCB traces and IRLZ44NPBF maximum RDS(on) at the
  4.5 V guaranteed test point for 2 A over 30 s.
- [x] Require at least 1 oz finished outer copper. Calculated PCB copper plus
  Q1 is 62.75 milliohm, 125.5 mV drop, and 251 mW at 2 A.
- [x] Compare nameplate current ratings: switch 5 A, JST-XH 3 A, and JST-PH
  2 A. The JST-PH connection is the limiting, zero-nameplate-margin item.
- [ ] After prototype assembly, measure the complete path including contacts,
  crimps, battery holder, harness, solder joints, and nichrome at the worst
  justified cold condition.

Evidence: `docs/CUTDOWN_CALC.md`; later prototype test record for the elements
that do not exist in CAD.

### 6. Complete the payload mechanical review — required

- [ ] Place the board STEP model in a payload/enclosure mock-up with the actual
  LightAPRS, OpenLog, regulator, battery holder, switches, cables, antennas,
  spacers, fasteners, and nichrome harness.
- [ ] Verify board outline, mounting, edge clearance, connector access,
  microSD removal, switch operation, cable bend radii, and readable silkscreen.
- [ ] Decide whether any carrier mounting holes, tooling holes, fiducials, or
  dedicated test points are required. Document an explicit decision for each;
  do not add them automatically if the hand-assembled prototype does not need
  them.

Evidence: reviewed 3D assembly or dimensioned physical mock-up.

### 7. Run the final design-release review — required

- [ ] Incorporate every change from items 1-6 into schematic, PCB, project
  libraries, intent, BOM, and documentation.
- [x] Review schematic-to-footprint pin mapping, net classes, hole/slot sizes,
  annular rings, solder-mask clearances, edge clearances, text, polarity marks,
  and the exact scope of every DRC exclusion.
- [x] Confirm the board still has zero SMD pads and that every populated part is
  intended for through-hole hand soldering.
- [x] Run ERC, DRC, Copperhead drift, constraints, and legibility checks with no
  unexplained failures.
- [ ] Have a second human perform a fabrication review if possible.

Evidence: clean reports, reviewed diff, and a tagged/committed release revision.

### 8. Build a clean manufacturer upload package — required

- [ ] Regenerate all outputs only after the released source files are committed.
- [ ] Create a separate release ZIP containing only the layers the chosen board
  house requests: front/back copper, front/back solder mask, front silkscreen,
  board outline, plated/non-plated drill data, and the Gerber job file when
  supported.
- [ ] Do not blindly upload the whole tracked `outputs/gerbers/` review folder.
  It also contains courtyard, fabrication, adhesive, paste, margin, and user
  drawing layers that normally do not belong in a bare-board order.
- [ ] Open the final ZIP in an independent Gerber viewer. Verify outline,
  dimensions, layer alignment, plated slots for SW1, NPTH mounting holes,
  drill count, no clipped artwork, no copper outside the outline, and readable
  front silkscreen.
- [ ] Record the order settings: two layers, material/Tg, thickness, copper
  weight, surface finish, solder-mask color, silkscreen color, minimum slot
  capability, impedance instructions, quantity, and any electrical-test option.
- [ ] Order **bare PCBs only** unless a separate assembly package has been
  intentionally prepared. This design is through-hole and intended for home
  assembly; the existing JLCPCB BOM is not an assembly release.

Evidence: archived ZIP, viewer screenshots, fabrication notes, and order-setting
record tied to the source commit.

## Gate B — engineering prototype order

When all Gate A items pass, order a small engineering lot, recommended five
bare boards:

1. power-path and unpowered continuity bring-up;
2. LightAPRS/OpenLog integration;
3. RF characterization;
4. destructive cutdown and environmental testing;
5. untouched control/spare.

These are qualification boards, not flight articles. Populate them in stages
so a common footprint or polarity error is found before the whole lot is built.

## Gate C — tests after prototype fabrication, before a flight-board order

Follow `docs/DEVPLAN.md` and `firmware/DEVPLAN.md`. At minimum, record:

- [ ] incoming bare-board dimensional, slot, drill, continuity, and visual
  inspection;
- [ ] unpowered continuity, isolation, connector polarity, and switch tests;
- [ ] 3.0-5.4 V fixed-3S LightAPRS startup and continuous-GPS operation;
- [ ] OpenLog UART integrity and reliable file writes from `LOGGER_5V`;
- [ ] OpenLog idle <=7 mA, write <=25 mA, regulator Iq <0.2 mA, total
  board-added idle <=8 mA, and active/write peak <=30 mA;
- [ ] reset, boot, brownout, and firmware tests proving the cutdown output stays
  off until explicitly armed;
- [ ] dummy-load testing to 2 A for 30 s with measured connector drop, Q1 VDS,
  copper temperature, and safe shutoff;
- [ ] complete cutdown-off leakage <=50 uA and LED-off leakage <=1 uA over the
  required voltage and temperature range;
- [ ] VNA measurements of APRS and WSPR launch return loss, insertion loss,
  isolation, and resonance using qualified 50 ohm loads;
- [ ] controlled nichrome separation at cold/end-of-discharge conditions;
- [ ] environmental operation and cold start over the justified flight range;
- [ ] a four-hour mission rehearsal with continuous GPS, representative radio
  duty cycle, logging, and a safely controlled cutdown event;
- [ ] measured demand <=800 mAh, mean pack current <=200 mA, and at least
  1600 mAh usable 3S L91 capacity under the actual cold/load profile.

Failures require a design revision and a repeat of the affected Gate A review.
Only after Gate C passes should a later revision be designated as a flight
candidate and sent for the flight-board fabrication order.

## Release record

Complete this block for each fabrication release:

| Field | Value |
| --- | --- |
| Source commit/tag | |
| Fabricator and stackup revision | |
| Approved BOM revision | |
| Gerber ZIP filename and SHA-256 | |
| Independent viewer review | |
| ERC/DRC/drift/constraints result | |
| Mechanical/1:1 review evidence | |
| RF calculation reference | |
| Cutdown calculation reference | |
| Reviewer and date | |
| Disposition | HOLD / ENGINEERING PROTOTYPE / FLIGHT CANDIDATE |
