# Proposal: firmware-weather-balloon-logger

## Why

Stage 7 requires a reviewable firmware starting point for the ATSAMD21G18 host that implements the documented two-GPIO allocation and demonstrates one safe logging path without weakening hardware constraints.

## What Changes

- Create `firmware/` with an ATSAMD21G18-oriented HAL scaffold.
- Generate `firmware/include/pins.h` from the authoritative assignments in `docs/PINOUT.md`: A1/PB08 SERCOM4 UART_TX and A0 CUTDOWN_CTRL.
- Add UART/OpenLog and cutdown driver interfaces/stubs, keeping cutdown default OFF during initialization.
- Add one working happy path that initializes hardware safely and sends a sample record to OpenLog while leaving cutdown inactive.
- Add build metadata and `firmware/DEVPLAN.md`; build with the vendor toolchain if available, otherwise state exactly `not compiled here`.
- Update `docs/DECISIONS.md` and `docs/CHANGELOG.md` with concise rationales and verification status.
