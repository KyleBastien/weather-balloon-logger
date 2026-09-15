# Proposal: architecture-weather-balloon-logger

## Why

Stage 2 architecture must freeze the harness block diagram against SPEC.md budgets before schematic: 3s L91 baseline, switch-break pack+, 3.3 V GPIO, OpenLog on 3V3, dual downward SMA, logic-level cutdown FET with gate pulldown, no second MCU/RTC/charger. A part that meets voltage but blows Iq or strapping is a bug.

## What Changes

- Create docs/SUBSYSTEMS.md: prose block diagram (pack → SW1 pack+ → VIN / 3V3 fan-out → OpenLog, write LED, cutdown gate; dual SMA from LightAPRS-W RF; UART to OpenLog; 2-pin nichrome).
- Sections: Power, Host/MCU (LightAPRS-W 2.0 only), Connectivity (UART + SMA), UI (SW + write LED), Cutdown, Mechanical/keepout, Intentional absences, Constraint map.
- Lock key values: 3s 3.0–5.4 V (4s only if UVLO), mean ≤200 mA / ≥1600 mAh usable, switch OFF 0 µA, board-added idle ≤2 mA, FET off ≤50 µA, LED off ≤1 µA, straps ≤50 µA, OpenLog 3.3 V, LED 1 kΩ ≤3 mA, cutdown ≤2 A burst, FET fully on at 3.3 V Vgs (IRLZ44N not committed), SMA 50 Ω ×2 downward ≥5 mm keepout.
- No PINOUT GPIO assignments until strapping table is checked. No schematic/PCB/BOM part commits this run.
