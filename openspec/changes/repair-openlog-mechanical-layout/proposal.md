# Proposal: repair-openlog-mechanical-layout

> Marker: AUTO (autonomous mode; auto-approved, reviewable after the fact)

## Why

The exact solder-down OpenLog carrier footprint now exposes a real courtyard extending beyond the draft outline, plus stale A1-related copper and edge-silkscreen findings. A bounded placement, outline, and local reroute pass is required while preserving the fixed LightAPRS and RF layout.

## What Changes

- Keep A1 as `WeatherBalloon:SparkFun_OpenLog_DEV-13712_Carrier`, top-side and direct-soldered, with unchanged pads, pin order, and nets.
- Move/rotate only A1, C1, and C2 to form an accessible OpenLog cluster outside the fixed LightAPRS body zone.
- Extend only the top and/or right board edges by the minimum amount needed for A1 courtyard containment and practical microSD/header assembly access.
- Remove stale A1/C1/C2 route ends and reroute only their GND, 3V3, and UART_TX copper, except any unavoidable local trunk extension.
- Preserve every other footprint and route, the fixed J2/J6/J7/H1-H4 geometry, all SMA/bottom-RF constraints, and the six exact vendor-module DRC exclusions.
- Update `docs/LAYOUT.md`, `docs/FOOTPRINT_AUDIT.md`, `docs/DECISIONS.md`, and `docs/CHANGELOG.md` with final geometry and one-line rationales.
