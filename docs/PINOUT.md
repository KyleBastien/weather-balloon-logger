# Pinout — Weather Balloon Logger harness

Authoritative LightHABTracker 1.0 carrier assignment. J2 is the official known nine-position order A1, A2, 3V3, GND, SCL, SDA, SCK, MISO, MOSI. A1/PB08 is one-way OpenLog UART TX; A2/PB09 is active-low LED_N. The PCB implements this mapping with provisional connector and mounting geometry pending measurement of the purchased tracker.

## Host interface J2

| Refdes | Pin | Net | Host mapping / rationale |
| --- | --- | --- | --- |
| J2 | 1 | UART_TX | A1/PB08 one-way host TX through R4 to OpenLog RXI. |
| J2 | 2 | LED_N | A2/PB09 active-low LED sink; R2 pulls it to 3V3 so reset/high-impedance defaults D1 off. |
| J2 | 3 | 3V3 | LightHAB regulated 3.3 V for the LED anode path and R2 pull-up. |
| J2 | 4 | GND | Common signal and power return. |
| J2 | 5 | NC | Physical SCL contact intentionally unused on this carrier. |
| J2 | 6 | NC | Physical SDA contact intentionally unused on this carrier. |
| J2 | 7 | NC | Physical SCK contact intentionally unused on this carrier. |
| J2 | 8 | NC | Physical MISO contact intentionally unused on this carrier. |
| J2 | 9 | NC | Physical MOSI contact intentionally unused on this carrier. |

The A1/PB08 and A2/PB09 assignments follow the requested LightHAB interface contract. R2 is the intentional hardware reset-default-off path for the active-low LED; the former PCF8574 and cutdown-driver reset behavior no longer applies.

## Complete schematic pin/net table

| Refdes | Pin | Net | Function / intentional absence |
| --- | --- | --- | --- |
| J1 | 1 | VBATT | LightHAB VBATT feed to A2; onboard-switch control of this rail is unverified. |
| J1 | 2 | GND | LightHAB power return. |
| A2 | 1 | VBATT | SHDN tied to LightHAB VBATT under the unverified onboard-switch assumption. |
| A2 | 2 | VBATT | S7V8F5 VIN from LightHAB VBATT. |
| A2 | 3 | GND | Regulator return. |
| A2 | 4 | LOGGER_5V | Fixed 5 V output for OpenLog. |
| J2 | 1 | UART_TX | A1/PB08 host TX to R4. |
| J2 | 2 | LED_N | A2/PB09 active-low LED cathode/sink node. |
| J2 | 3 | 3V3 | LightHAB regulated 3.3 V. |
| J2 | 4 | GND | Common return. |
| J2 | 5 | NC | Physical SCL contact intentionally unused. |
| J2 | 6 | NC | Physical SDA contact intentionally unused. |
| J2 | 7 | NC | Physical SCK contact intentionally unused. |
| J2 | 8 | NC | Physical MISO contact intentionally unused. |
| J2 | 9 | NC | Physical MOSI contact intentionally unused. |
| A1 | 1 | NC | BLK orientation pin intentionally unused. |
| A1 | 2 | GND | OpenLog ground. |
| A1 | 3 | LOGGER_5V | OpenLog VCC from S7V8F5. |
| A1 | 4 | NC | TXO intentionally unused. |
| A1 | 5 | OPENLOG_RXI | RXI receives host bytes through R4. |
| A1 | 6 | NC | GRN orientation pin intentionally unused. |
| C1 | 1 | LOGGER_5V | OpenLog bulk bypass. |
| C1 | 2 | GND | Bypass return. |
| C2 | 1 | LOGGER_5V | OpenLog high-frequency bypass. |
| C2 | 2 | GND | Bypass return. |
| R4 | 1 | UART_TX | Host side of UART back-power limiter. |
| R4 | 2 | OPENLOG_RXI | OpenLog receive side. |
| R1 | 1 | 3V3 | LED current-limiter supply. |
| R1 | 2 | LED_A | D1 anode feed. |
| D1 | 1 | LED_N | Cathode driven active-low by J2.2. |
| D1 | 2 | LED_A | Anode from R1. |
| R2 | 1 | 3V3 | Reset-default-off pull-up supply. |
| R2 | 2 | LED_N | 100 kΩ pull-up keeps D1 off while J2.2 is high-impedance. |
| J3 | 1 | OUT1 | LightHAB pyro output passed directly to J5.1; rating unverified. |
| J3 | 2 | GND | LightHAB pyro return passed directly to J5.2. |
| J5 | 1 | OUT1 | Direct LightHAB OUT1 cutdown output. |
| J5 | 2 | GND | Direct LightHAB pyro return. |

## Intentional absences

- No host RX path: OpenLog TXO remains unused.
- No I2C expander: U1 and C3 are intentionally removed because LightHAB A2/PB09 drives the LED directly.
- No carrier pyro driver: U2, Q1, R3, C4, and C5 are intentionally removed because LightHAB OUT1/GND passes directly to J5; its switching and current rating remain unverified.
- No carrier RF connectors or nets are present; the LightHAB onboard SMA connectors remain accessible inside the documented mechanical keepouts.
- SCL, SDA, SCK, MISO, and MOSI remain physically present on J2.5–J2.9 and are intentional no-connects.
- The schematic and PCB are synchronized electrically; the LightHAB mounting/connector geometry remains explicitly provisional and blocks fabrication.
