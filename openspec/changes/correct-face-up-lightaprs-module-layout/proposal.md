# Proposal: correct-face-up-lightaprs-module-layout

> Marker: AUTO (autonomous mode; auto-approved, reviewable after the fact)

## Why

The current PCB layout uses the superseded mirrored 32 × 55 mm LightAPRS-W placement. The verified module is 32.77 × 54.80 mm and mounts face up, requiring top-view pad geometry without left-right mirroring, corrected HF/VHF corner placement, and corresponding SMA relocation while preserving the existing electrical mapping and keepouts.

## What Changes

- Resize the LightAPRS-W module reservation to exactly 32.77 × 54.80 mm with its long axis vertical.
- Reposition J2 on the verified matching module-header edge using the FACE-UP top-view geometry with no left-right mirror.
- Put J7/HF at the module bottom-left and J6/VHF at the bottom-right while retaining J7→J4/RF_WSPR and J6→J3/RF_APRS.
- Move J4 toward the left/HF side and J3 toward the right/VHF side for short downward-facing SMA launches.
- Reposition four approximate M2 standoff holes to the dimensioned pattern, including about 42.73 mm outer horizontal span.
- Keep every non-mating electrical component outside the exact module zone and preserve at least 5 mm SMA dielectric keepouts.
- Update docs/LAYOUT.md and the board documentation/decision trail consistently.
