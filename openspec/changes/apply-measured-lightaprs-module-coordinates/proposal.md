# Proposal: apply-measured-lightaprs-module-coordinates

> Marker: AUTO (autonomous mode; auto-approved, reviewable after the fact)

## Why

The PCB must match the measured FACE-UP LightAPRS-W 2.0 coordinate transcription in docs/SUBSYSTEMS.md section 6 while preserving module, RF, and SMA clearances.

## What Changes

- Move H1-H4 to the measured 28.18 x 38.16 mm rectangle using approximately 2.2 mm M2 holes.
- Align J2 at approximately x=154.9, rotation 270 degrees, with 2.548 mm pitch and its 11 pads spanning approximately y=121.7 to 147.2.
- Position J7/HF at the module bottom-left and J6/VHF at the bottom-right, clear of H3/H4, preserving RF_WSPR and RF_APRS mappings.
- Adjust affected routing only as required; keep all other components outside the 32.77 x 54.80 mm module zone and preserve both >=5 mm SMA keepouts.
- Update docs/LAYOUT.md and record the coordinate-placement rationale without removing existing fabrication holds.
