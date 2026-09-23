# Development and qualification plan

## Current design

The carrier mounts a LightHABTracker 1.0, powers an OpenLog directly from LightHAB J2.3 3V3, provides an active-low write-attempt LED, and passes LightHAB OUT1/GND directly to J5. The tracker retains its onboard 3×AA holder, dual SMA connectors, radios, GPS, and pyro control. The carrier adds no RF path, logger regulator, or pyro driver.

## Next bounded revision: measured mechanical fit

1. Purchase and photograph the exact LightHABTracker.
2. Record all dimensions listed in `FABRICATION_READINESS.md` with a caliper and annotated photos.
3. Confirm J2.3 3V3 capacity and OUT1 electrical behavior on a protected bench setup.
4. Replace provisional J2/J3 and H1-H4 geometry in `scripts/rebuild_lighthab_board.py`; select exact interface MPNs.
5. Rebuild the PCB, preserve the 90 × 80 mm outline unless measurements demand a documented change, and check USB/SMA/battery envelopes.
6. Print the 1:1 fit sheet and perform the exact-parts physical overlay.
7. Regenerate all sources, BOM/order list, renders, and review outputs. Remove the warning only when evidence closes the fit gate.

## Electrical bring-up

1. With LightHAB and OpenLog disconnected, inspect soldering and verify no shorts between 3V3, OUT1, and GND.
2. Current-limit the bench supply and confirm 3.3 V at A1 VCC before installing OpenLog.
3. Confirm the rail stays in tolerance during OpenLog startup and sustained writes, including representative radio activity; confirm R4 limits unwanted UART back-power current.
4. Confirm D1 is off at reset and active only when A2/PB09 is driven low.
5. Test J5 using an inert load and the vendor firmware's OUT1 controls. The carrier does not increase the output rating.

## Flight qualification

Follow `firmware/DEVPLAN.md` for software integration. Qualify the exact 3S L91 set, logger current, radio duty, antennas, thermal/vacuum behavior, cutdown assembly, and four-hour mission profile. Preserve raw measurements and stop on unexplained resets, heating, rail droop, radio degradation, or unexpected pyro activation.
