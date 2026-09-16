# Hardware development plan — Weather Balloon Logger harness

## Status and release gates

This is the Stage 8 hardware bring-up and prototype-order plan. `firmware/DEVPLAN.md` remains the separate firmware qualification plan. The current PCB is a coordinate-level layout study, not a fabrication release: every `CopperheadDraft_*` land pattern and every BOM manufacturer part number is **UNVERIFIED**. Do not order production parts or fabricate the exported board until the exact ordered parts, footprints, temperature ranges, leakage/current limits, RF geometry, and mechanical clearances have been verified, the PCB has been updated, and ERC/DRC have been rerun.

The locations below are accessible component pads or connector pins, not populated test-point refdes. Probe only with power removed unless a step explicitly calls for live measurement. Keep the nichrome wire disconnected until the final controlled cutdown test.

## Required equipment and safe setup

- Current-limited bench supply covering 3.0–7.2 V, two DMMs with µA/mA/A ranges, oscilloscope, logic analyzer or 3.3 V UART decoder, and a temperature probe or thermal camera.
- Fused nonflammable dummy load for cutdown tests, then a guarded fire-resistant nichrome fixture outdoors or in a suitable enclosure. Keep personnel, cord, batteries, and antennas away from the hot wire.
- Verified 50 Ω cables, terminations, and a VNA or RF specialist setup for J6-to-J3/J4 qualification. Never transmit APRS/WSPR into an open connector or an unqualified load.
- ESD-safe bench, magnification, 1:1 footprint print, exact mating connectors, exact LightAPRS-W 2.0 and OpenLog modules, and the manufacturer datasheets for every ordered suffix.
- A written test log recording board serial, installed MPNs, instrument IDs, ambient temperature, supply voltage/current limit, measured values, and pass/fail disposition.

## Probe-location map

| Quantity | First-choice probe locations | Expected meaning |
| --- | --- | --- |
| Pack input | J1.1 `PACK_IN` to J1.2 `GND` | Unswitched pack voltage. |
| Switched pack | SW1.1 or J2.1/J5.1 `PACK_SW` to `GND` | Zero with SW1 OFF; approximately `PACK_IN` with SW1 ON. |
| Ground continuity | J1.2, J2.2, A1.2, Q1.2, J3.2, J4.2 | Common return; verify before live tests. |
| Host 3.3 V | J2.3, A1.3, C1.1, C2.1, or R1.1 `3V3` to `GND` | Regulated host rail, never raw pack. |
| Logger UART | J2.4 or A1.5 `UART_TX` to `GND` | 3.3 V idle-high, 9600 baud scaffold default pending installed OpenLog confirmation. |
| LED anode | R1.2 or D1.2 `LED_A` to `GND` | Current-limited LED feed; pulses during low UART bits. |
| Cutdown command | J2.7 or R2.1 `CUTDOWN_CTRL` to `GND` | Must be low before other application initialization. |
| FET gate | R2.2, R3.1, or Q1.1 `CUTDOWN_GATE` to Q1.2 `GND` | Held low by R3 at reset; about 3.3 V only when armed/firing. |
| FET drain | Q1.3 or J5.2 `CUTDOWN_DRAIN` to `GND` | Load low side; near ground only when Q1 is commanded on. |
| APRS RF path | J6.1 to J3.1 `RF_APRS`; J3.2 shield | Continuity/RF path only; no DC connection to the center conductor is expected elsewhere. |
| WSPR RF path | J6.2 to J4.1 `RF_WSPR`; J4.2 shield | Continuity/RF path only; no DC connection to the center conductor is expected elsewhere. |

## Bring-up sequence

Stop at the first failed limit, unexpected heating, unstable rail, excess current, smoke, odor, or intermittent connection. Record the failure and correct the design before continuing. Do not defeat a current limit merely to make a failing board start.

### 1. Pre-power document and assembly audit

1. Match each received MPN and suffix to `docs/BOM.md`; verify pin numbering, exact land pattern, voltage/current rating, −40 °C suitability, leakage/Iq limits, and lifecycle/availability. Reject substitutions that have not been requalified.
2. Replace all `CopperheadDraft_*` footprints with verified manufacturer/library footprints. Confirm connector mating direction, SW1 terminal numbering, AO3400A G/S/D pins, LED polarity, OpenLog header order, and downward SMA mating orientation on a 1:1 print and mechanical mock-up.
3. Convert the drawn SMA envelopes into enforceable rule areas, calculate 50 Ω launches from the actual stackup, add the required return-via strategy, and re-evaluate the ≥5 mm dielectric/battery-metal keepout.
4. Recalculate the complete 2 A for 30 s cutdown path using actual copper weight, trace/pour/via geometry, connector resistance, Q1 maximum RDS(on) at 2.5–3.3 V, transient thermal impedance, and safe operating area.
5. Run ERC, DRC, BOM/pin drift checks, and fabrication review on the revised design. This is the fabrication-order gate.

### 2. What to meter first — unpowered board

1. Inspect solder joints, bridges, polarity, connector orientation, and debris under magnification. Leave LightAPRS-W, OpenLog, antennas, and nichrome disconnected.
2. Meter continuity among all listed `GND` locations. A missing ground connection is an immediate stop.
3. With SW1 OFF, verify J1.1 `PACK_IN` is open from J2.1/J5.1 `PACK_SW`. With SW1 ON, verify low resistance from `PACK_IN` to `PACK_SW`; exercise the switch and reject intermittent contacts.
4. Measure resistance from `PACK_IN`, `PACK_SW`, `3V3`, `CUTDOWN_DRAIN`, `CUTDOWN_GATE`, `RF_APRS`, and `RF_WSPR` to `GND`. Investigate any unexpected short before applying power. Capacitors may cause a momentary charging indication on `3V3`.
5. Verify R3 measures approximately 1 MΩ from `CUTDOWN_GATE` to `GND`, R2 approximately 100 Ω from `CUTDOWN_CTRL` to `CUTDOWN_GATE`, and the LED path has the expected diode polarity through R1.
6. Check RF center-to-center continuity from J6.1 to J3.1 and J6.2 to J4.1, shield-to-ground continuity, isolation between APRS/WSPR centers, and no center-to-shield short.

### 3. Bare carrier power-path test

1. Keep J2, A1, J5 load, and both RF outputs disconnected. Set SW1 OFF and connect a current-limited supply to J1 at a conservative 3.0 V. Confirm no measurable load current beyond instrument uncertainty and physical insulation leakage; SW1 must break pack positive.
2. Confirm `PACK_SW` is 0 V with SW1 OFF. Toggle SW1 ON and confirm `PACK_SW` follows `PACK_IN` without abnormal current or contact drop. Repeat across 3.0–5.4 V. Test 7.2 V only after every installed part on the switched path is verified for the allowed 4s case.
3. Return SW1 OFF before connecting or removing any module.

### 4. Host-only power and 3V3 qualification

1. Connect only the verified LightAPRS-W interface at J2; leave OpenLog and nichrome disconnected and disable RF transmission or attach qualified 50 Ω loads. Start at a known-safe host input voltage, using the host datasheet/current profile to set a protective limit above verified inrush.
2. Power on and meter `PACK_SW` first, then J2.3 `3V3`. Stop if raw pack appears on `3V3`, if the rail is outside the verified host tolerance, or if the supply current is unexplained.
3. Verify host startup, GPS, APRS, WSPR, I2C, and SPI remain functional. Confirm A0/A1 assignments do not collide with occupied pins.
4. Determine the real LightAPRS-W VIN/UVLO behavior from 5.4 V down toward 3.0 V under representative load. Use 3s only if operation through the required end-of-discharge range is demonstrated; otherwise use the allowed 4s pack. Do not add series cells for amp-hours.
5. Measure host-only current at defined modes to establish the baseline used for the board-added-current subtraction and the ≤200 mA mean-flight budget.

### 5. Default-off cutdown control before installing a load

1. Probe `CUTDOWN_CTRL` and `CUTDOWN_GATE` during power application, reset, bootloader entry, brownout, firmware restart, and power removal. Both must remain low until an explicit armed command; `cutdown::init_safe()` must be the first application-level action. Any positive glitch is an immediate stop.
2. Confirm Q1 remains off with the host disconnected and while its GPIO is high impedance. R3 is intentional and must not be omitted.
3. Command cutdown only in a bench test mode. Verify approximately 3.3 V at `CUTDOWN_CTRL`, the expected small drop across R2, and approximately 3.3 V at `CUTDOWN_GATE`. Verify the commanded R3 current is about 3.3 µA and is zero when the gate is low.
4. Remove the command and verify the gate returns promptly to 0 V. Do not proceed until reset-time and firmware default-off behavior passes repeatedly.

### 6. OpenLog power-budget and UART test

1. Verify the installed OpenLog configuration and voltage requirements independently. Confirm its maximum idle current is no greater than 1.95 mA over required voltage and temperature; a typical-only 2 mA claim fails the present ≤2 mA board-added limit.
2. Connect A1 with power off. Power on and meter `3V3` at A1.3 first; confirm the LightAPRS 3V3 regulator supports OpenLog startup/write peaks without droop, reset, or overheating. Do not move A1 to raw pack to hide a regulator-margin failure.
3. Measure carrier-plus-OpenLog idle current relative to the host-only baseline with D1 off and Q1 off. It must be ≤2 mA beyond the LightAPRS module. Separately confirm Q1/off-path leakage ≤50 µA at the maximum qualified pack voltage.
4. Decode `UART_TX`: idle must be high, logic levels must be 3.3 V compatible, and the baud/configuration must match the installed OpenLog. The scaffold default is 9600 baud, 8-N-1, not a verified flight setting.
5. Transmit a uniquely numbered record. Verify D1 flashes during low UART bits and is dark at idle; LED-off leakage must be ≤1 µA. Remove the SD card safely and confirm the exact record is present. The LED is only a transmit proxy, not proof of media commit.
6. Repeat logging while GPS and both radio functions operate into qualified loads, watching for rail droop, UART corruption, resets, and current-budget violations.

### 7. RF and mechanical qualification

1. With power off, repeat RF continuity/isolation checks after assembly. Inspect launch soldering and verify SMA mates point downward through the payload without cable, enclosure, or battery interference.
2. Using the actual stackup and qualified 50 Ω equipment, measure each J6-to-SMA path for return loss, insertion loss, channel isolation, and unintended resonance across the applicable APRS and WSPR bands. A DRC-clean 0.5 mm draft trace is not a 50 Ω proof.
3. Verify the ≥5 mm SMA dielectric keepouts, return-current path/via fence, reserved protection strategy, cable bend radius, and absence of battery metal or nichrome hardware in the near field.
4. Perform conducted/radiated system checks only with suitable loads/antennas and regulatory controls; confirm simultaneous subsystem operation does not corrupt GPS or logging.

### 8. Cutdown dummy-load test

1. Use a fused nonflammable dummy load, not nichrome. Keep RF disabled or correctly terminated. Begin below full load and increase only while monitoring supply current, Q1 VDS, connector drop, trace/via drop, and temperature.
2. At the qualified worst-case pack voltage and up to the assumed 2 A load, verify Q1 is fully enhanced from the measured 3.3 V gate drive. Use maximum RDS(on), safe-operating-area, and thermal limits rather than threshold voltage.
3. Exercise the hard firmware maximum-on timer, one-shot/interlock behavior, resets, brownouts, and removal of the command. No firing or restart may leave Q1 on, and every activation must end within 30 s.
4. Measure OFF leakage through the complete cutdown path at the maximum pack voltage and required temperature extremes; it must be ≤50 µA. Inspect connectors, solder joints, copper, and Q1 after repeated pulses.

### 9. Controlled nichrome and environmental test

1. Only after the dummy-load test passes, fit the intended nichrome geometry in a guarded fire-resistant fixture with a sacrificial representative cord. Use the real connector/harness and a fused supply.
2. Demonstrate clean separation at worst-case pack/end-of-discharge and cold conditions without exceeding 2 A or 30 s. Record current, voltage, time-to-cut, Q1 VDS, and temperatures. Repeat enough times to establish margin; a single successful burn is not qualification.
3. Repeat power, logging, reset/brownout, RF, leakage, and cutdown checks across the intended −40 °C to +40 °C environment or a justified test envelope. Recalculate the 4 h energy budget from measured mode durations and currents; mean pack current must remain ≤200 mA and usable capacity margin must remain ≥1600 mAh after the assumed derate.
4. Complete a four-hour end-to-end mission rehearsal with continuous GPS, representative APRS/WSPR duty, OpenLog logging, correct LED activity, and a safely simulated or controlled cutdown event. Confirm file integrity and no unexplained resets.

## Risk register

| Risk | Evidence needed to close it | Stop/mitigation |
| --- | --- | --- |
| Draft footprints or wrong connector pin order | Exact MPN datasheets, 1:1 print, mating-part inspection, updated PCB and DRC | No PCB order while any `CopperheadDraft_*` footprint remains. |
| UNVERIFIED part sourcing or cold rating | Manufacturer-authorized source, exact suffix, lifecycle and −40 °C data | Reject substitutions; keep procurement hold. |
| 3s host brownout near 3.0 V | Measured LightAPRS VIN/UVLO under representative load and cold | Use allowed 4s only if voltage testing requires it; verify 7.2 V maxima. |
| OpenLog exceeds the 2 mA board-added idle budget | Maximum idle-current measurement over voltage/temperature plus host-only subtraction | Stop and replace/re-architect; do not accept a typical-only 2 mA claim. |
| Host 3V3 regulator lacks OpenLog peak margin | Startup/write waveform and regulator thermal/current data | Revisit architecture explicitly; do not silently power OpenLog from raw pack. |
| Cutdown false-fire at reset/brownout | Scope captures at `CUTDOWN_CTRL` and `CUTDOWN_GATE`, repeated fault tests | R3 stays fitted; firmware initializes low first; no nichrome testing until clean. |
| Q1/trace/connector overheats at 2 A for 30 s | Verified RDS(on)/SOA, measured VDS/drop/temperature, actual copper calculation | Widen/pour/multiply vias or change qualified parts and repeat schematic/layout review. |
| Cutdown OFF leakage exceeds 50 µA | Maximum-voltage and temperature measurement of complete path | Reject Q1/contamination/assembly and correct before flight. |
| LED glows or loads UART | Idle-high waveform, ≤1 µA OFF leakage, UART/OpenLog error test | Correct polarity/value/part; LED remains a transmit proxy only. |
| RF path is not 50 Ω or violates keepout | Actual stackup calculation, VNA data, rule areas, mechanical mock-up | Reroute launches/returns; no RF-power test into an unqualified path. |
| Downward SMA or payload mechanics do not fit | 3D/mechanical mock-up with cables, enclosure, battery, and harness | Move/reorient before PCB order; keep battery metal outside near field. |
| Firmware scaffold is unbuilt or baud is wrong | Exact board-package build and installed OpenLog configuration/readback | Follow `firmware/DEVPLAN.md`; no flight on source review alone. |
| Four-hour/cold energy margin is optimistic | Logged mission-profile currents and cold-capacity evidence | Reduce load/duty within mission needs or revisit pack architecture without forbidden chemistry. |
| ESD/protection remains only reserved space | Selected/captured parts with leakage, voltage, capacitance, RF, BOM, and layout verification | Do not populate invented protection; make an explicit design revision. |

## Prototype order plan

1. **Qualification samples only:** obtain small quantities of the exact candidate J1/J5 connector pair, SW1, SMA connectors, Q1, LED, passives, and their mating parts from traceable sources. Obtain the exact LightAPRS-W and OpenLog modules separately. These purchases are for measurement and footprint qualification, not production approval.
2. **Bench fixtures before PCB:** build or buy current-limited/fused cable assemblies, a cutdown dummy load, guarded nichrome jig, 50 Ω RF cables/loads, and a mechanical payload mock-up. Validate module current, header order, switch terminals, connector mating, and OpenLog baud before committing copper.
3. **Release the revised prototype PCB only after gates pass:** replace all draft footprints, implement enforceable RF rules and calculated launches, complete thermal/current-path work, add required mounting/test/label features, reconcile any protection decisions with schematic and BOM, then rerun ERC, DRC, drift, and fabrication review. The existing `outputs/` package must not be sent to fabrication.
4. **Recommended first revised lot:** order a small five-board engineering lot after the release review—one for unpowered/power-path bring-up, one for host/OpenLog integration, one for RF characterization, one for destructive cutdown/environmental testing, and one unmodified control/spare. This allocation prevents a stressed cutdown specimen from becoming the flight article.
5. **Staged population:** populate and pass the power-path board first; then logic/logger; then RF; then the cutdown specimen. Do not kit or assemble the full lot after a common footprint or current-budget failure.
6. **Flight-candidate order:** issue a later revision only after all risks above have objective closure, the four-hour mission rehearsal passes, exact MPNs and alternates are controlled, and the schematic/PCB/BOM/docs are synchronized. Repeat incoming inspection and acceptance testing on every flight candidate.

## Completion record

A prototype stage passes only when its measured results, instrument conditions, exact installed parts, deviations, and corrective actions are recorded. Any waiver to a stated electrical budget or safety limit requires an explicit specification and constraint decision; it must not be hidden in a test note.
