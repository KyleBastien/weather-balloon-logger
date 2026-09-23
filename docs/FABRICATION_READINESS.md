# Fabrication readiness

Date: 2026-09-22

## Current disposition

**HOLD — DO NOT FABRICATE.**

The LightHAB carrier is electrically complete and clean: ERC, DRC, intent drift, and constraints pass; the PCB has zero unconnected items and zero SMD pads. The remaining blocker is mechanical truth. QRP Labs publishes the LightHABTracker overall size (56 × 75 mm), but the exact connector pad positions, mounting-hole coordinates/diameters, battery-holder stack height, USB clearance, and SMA clearance are not available in an authoritative dimensioned drawing.

The current board intentionally carries provisional J2/J3 and H1-H4 geometry plus a prominent `UNVERIFIED LIGHTHAB FIT - DO NOT FABRICATE` silkscreen warning. Generated Gerbers are review artifacts only.

## Minimum work before an engineering PCB order

- [ ] Buy the exact LightHABTracker 1.0 and the remaining buy-now parts in `FIT_CHECK_ORDER_LIST.md`.
- [ ] Measure the tracker with calipers: full outline, all four mounting holes, J2 nine-pin signal row, J3 OUT1/GND, component-side orientation, and pad/hole sizes.
- [ ] Measure maximum component height on both faces, installed 3×AA holder height, USB plug envelope, both SMA connector/cable envelopes, and required soldering access.
- [ ] Bench-confirm that J2.3 remains near 3.3 V during OpenLog startup and sustained writes, including radio transmit bursts and cold/end-of-discharge conditions.
- [ ] Obtain a vendor rating or safely measure LightHAB OUT1 voltage/current behavior with a fused inert load; do not connect nichrome yet.
- [ ] Update the PCB generator, footprint geometry, interface MPNs, BOM, and mechanical keepouts from those measurements.
- [ ] Regenerate the 1:1 fit-check PDF and physically place every exact part. Confirm 90.0 × 80.0 mm printed scale, lead entry, body clearances, solder access, USB/SMA access, and battery fit.
- [ ] Remove the no-fabrication warning only after the measurement record and physical fit check pass.
- [ ] Re-run ERC, DRC, Copperhead drift/constraints, through-hole audit, and independent Gerber review.
- [ ] Create a fabricator-specific ZIP containing only copper, mask, front silk, outline, and drill/job data; record board thickness, copper weight, finish, mask/silk colors, and electrical-test selection.

## Firmware gate

- [ ] Integrate the logger scaffold into official LightHABTracker source commit `797b78d120b0e844f60798b88dfa3735f27e89da` or deliberately document a newer reviewed baseline.
- [ ] Reconfirm A1/PB08 and A2/PB09 are unused, compile the exact target, and retain the build log/hash.
- [ ] Scope A2 through reset, bootloader, brownout, and update; the active-low LED must remain off until intentionally pulsed.
- [ ] Confirm OpenLog UART settings, current, real file writes, and fault behavior without disrupting GPS/APRS/WSPR or vendor pyro logic.

## Prototype qualification before any flight revision

- [ ] Verify 3S Energizer L91 operation, cold start, and four-hour energy margin with continuous GPS and representative radio/logging duty.
- [ ] Verify the direct LightHAB 3V3/OpenLog rail over the battery and temperature range; measure rail voltage, idle current, and write current.
- [ ] Test OUT1 only with inert dummy loads until its limits and safety behavior are established.
- [ ] Select nichrome gauge/length and mechanical crimp sleeves from the verified output envelope; qualify separation at cold/end-of-discharge conditions.
- [ ] Perform antenna/cable selection, match/harmonic checks, environmental testing, reset/brownout fault injection, and a complete four-hour mission rehearsal.

An engineering lot should remain small (five bare boards is sufficient): bring-up, logger integration, RF/payload fit, destructive/environmental test, and an untouched spare. Prototype success does not automatically make that revision a flight article.

## Release record

| Field | Value |
| --- | --- |
| Source commit/tag | |
| LightHAB measurement record | |
| Approved BOM revision | |
| Fabricator/stackup | |
| Gerber ZIP and SHA-256 | |
| ERC/DRC/drift/constraints | |
| 1:1 fit evidence | |
| Firmware build/hash | |
| Reviewer/date | |
| Disposition | HOLD / ENGINEERING PROTOTYPE / FLIGHT CANDIDATE |
