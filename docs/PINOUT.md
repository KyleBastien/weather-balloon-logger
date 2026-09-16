# Pinout — Weather Balloon Logger harness

Stage-4 authoritative pin and net assignment. The LightAPRS-W 2.0 occupied-pin map leaves only A0 and A1 as confirmed free dedicated GPIOs. J2 therefore uses A1/PB08 for one-way SERCOM4 UART_TX and A0 for cutdown. The write LED is 3V3-fed and sunk by UART_TX; no A2 breakout or occupied I2C/SPI/GPS/radio pin is assumed. All logic is 3.3 V.

## Host interface J2

| Refdes | Pin | Net | Host mapping / rationale |
| --- | --- | --- | --- |
| J2 | 1 | PACK_SW | Switched pack positive to LightAPRS-W VIN; SW1 physically opens this rail when OFF. |
| J2 | 2 | GND | Common return. |
| J2 | 3 | 3V3 | Regulated 3.3 V from the tracker; powers OpenLog and the LED anode path. |
| J2 | 4 | UART_TX | LightAPRS A1/PB08, firmware SERCOM4 TX; drives OpenLog RXI and sinks D1 on low bits. |
| J2 | 5 | NC | Intentional: no host RX; OpenLog TXO is unused to conserve the confirmed two-pin GPIO budget. |
| J2 | 6 | NC | Intentional spare; no unverified A2 breakout or occupied shared-bus pin is assumed. |
| J2 | 7 | CUTDOWN_CTRL | LightAPRS A0 output through R2 to Q1 gate; R3 guarantees reset-time default-off. |

A0 and A1/PB08 have no ESP32-style boot-strap role on ATSAMD21G18. The only added static GPIO path is R3 to GND: 0 µA when cutdown is low and 3.3 µA only while commanded, below the 50 µA strap-leakage ceiling. UART_TX idles high, leaving D1 unbiased and meeting the 1 µA LED-off target subject to the selected LED leakage qualification.

## Complete schematic pin/net table

| Refdes | Pin | Net | Function / intentional absence |
| --- | --- | --- | --- |
| J1 | 1 | PACK_IN | Unswitched L91 pack positive input. |
| J1 | 2 | GND | Pack return. |
| SW1 | 1 | PACK_SW | Selected ON throw. |
| SW1 | 2 | PACK_IN | Switch common. |
| SW1 | 3 | NC | Intentional unused throw implements ON/OFF. |
| J2 | 1 | PACK_SW | Host VIN. |
| J2 | 2 | GND | Host ground. |
| J2 | 3 | 3V3 | Host regulated output. |
| J2 | 4 | UART_TX | A1/PB08 SERCOM4 TX and LED sink. |
| J2 | 5 | NC | Intentional host-RX omission. |
| J2 | 6 | NC | Intentional spare. |
| J2 | 7 | CUTDOWN_CTRL | A0 cutdown command. |
| A1 | 1 | NC | BLK/FTDI orientation pin intentionally unused. |
| A1 | 2 | GND | OpenLog ground. |
| A1 | 3 | 3V3 | OpenLog VCC. |
| A1 | 4 | NC | TXO intentionally unused; logger is receive-only. |
| A1 | 5 | UART_TX | RXI receives host log bytes. |
| A1 | 6 | NC | GRN/FTDI orientation pin intentionally unused. |
| C1 | 1 | 3V3 | OpenLog bulk bypass. |
| C1 | 2 | GND | Bypass return. |
| C2 | 1 | 3V3 | OpenLog high-frequency bypass. |
| C2 | 2 | GND | Bypass return. |
| R1 | 1 | 3V3 | LED current-limiter supply. |
| R1 | 2 | LED_A | D1 anode feed. |
| D1 | 1 | UART_TX | Cathode; active-low UART activity sink. |
| D1 | 2 | LED_A | Anode from R1. |
| R2 | 1 | CUTDOWN_CTRL | Series gate input. |
| R2 | 2 | CUTDOWN_GATE | Q1 gate node. |
| R3 | 1 | CUTDOWN_GATE | Intentional default-off pulldown. |
| R3 | 2 | GND | Pulldown return. |
| Q1 | 1 | CUTDOWN_GATE | Gate. |
| Q1 | 2 | GND | Source. |
| Q1 | 3 | CUTDOWN_DRAIN | Drain to nichrome low side. |
| J5 | 1 | PACK_SW | Nichrome high side. |
| J5 | 2 | CUTDOWN_DRAIN | Nichrome switched low side. |
| J6 | 1 | RF_APRS | LightAPRS VHF output. |
| J6 | 2 | RF_WSPR | LightAPRS HF output. |
| J3 | 1 | RF_APRS | APRS SMA center. |
| J3 | 2 | GND | APRS SMA shield. |
| J4 | 1 | RF_WSPR | WSPR SMA center. |
| J4 | 2 | GND | WSPR SMA shield. |

## Intentional absences

- No host RX path: OpenLog TXO is not needed for flight logging, and omitting it preserves the cutdown output within the confirmed GPIO budget.
- No dedicated LED GPIO: UART_TX low bits provide the visible log-transmit indication while UART idle-high guarantees OFF.
- No A2 assumption and no reuse of GPS UART, I2C, SPI, radio, power-control, battery-sense, RESET, or SWD pins.
- No pull-up is added to either host GPIO; R3 is the required cutdown pulldown and does not create idle leakage when A0 is low.
