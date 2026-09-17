# Pinout — Weather Balloon Logger harness

Authoritative LightAPRS-W 2.0 carrier assignment. J2 matches the verified 11-position 2.54 mm module edge header. A1/PB08 is one-way OpenLog UART TX; A2/PB09 is the direct cutdown GPIO; the exposed I2C bus drives a PCF8574T at address 0x20 for the write LED and future GPS-status LEDs. Logic remains 3.3 V, while the approved OpenLog VCC target is dedicated fixed `LOGGER_5V` from a Pololu S7V8F5 item 2123. This documentation-only pass intentionally leaves schematic and PCB implementation for a later hardware change.

## Host interface J2

| Refdes | Pin | Net | Host mapping / rationale |
| --- | --- | --- | --- |
| J2 | 1 | PACK_SW | RAW/VBAT input from switched pack positive; SW1 physically opens this rail when OFF. |
| J2 | 2 | GND | First module ground. |
| J2 | 3 | UART_TX | A1/PB08, SERCOM4/PAD0 TX to OpenLog RXI; no host RX is assigned. |
| J2 | 4 | CUTDOWN_CTRL | A2/PB09 direct GPIO through R2 to Q1 gate; R3 guarantees reset-time default-off. |
| J2 | 5 | 3V3 | Regulated module rail powering OpenLog, U1, and the LED anode path. |
| J2 | 6 | GND | Second module ground. |
| J2 | 7 | I2C_SCL | Exposed SCL/PA23 shared with the module's existing I2C devices; no duplicate carrier pull-up is populated pending measured bus resistance. |
| J2 | 8 | I2C_SDA | Exposed SDA/PA22 shared with the module's existing I2C devices; connects to U1 SDA. |
| J2 | 9 | NC | Physical SCK/PB11 contact is present but intentionally unused by this carrier. |
| J2 | 10 | NC | Physical MISO/PA12 contact is present but intentionally unused by this carrier. |
| J2 | 11 | NC | Physical MOSI/PB10 contact is present but intentionally unused by this carrier. |

PB08 and PB09 have no ESP32-style boot-strap role on ATSAMD21G18. R3 is the only static cutdown GPIO path: 0 µA when cutdown is low and 3.3 µA only while commanded. U1 address pins A0/A1/A2 are strapped low for 0x20; its quasi-bidirectional ports power up high, so P0 leaves D1 off until firmware explicitly drives it low.

## Complete schematic pin/net table

| Refdes | Pin | Net | Function / intentional absence |
| --- | --- | --- | --- |
| J1 | 1 | PACK_IN | Unswitched L91 pack positive input. |
| J1 | 2 | GND | Pack return. |
| SW1 | 1 | PACK_SW | Selected ON throw. |
| SW1 | 2 | PACK_IN | Switch common. |
| SW1 | 3 | NC | Intentional unused throw implements ON/OFF. |
| J2 | 1 | PACK_SW | RAW/VBAT input. |
| J2 | 2 | GND | Module ground. |
| J2 | 3 | UART_TX | A1/PB08 SERCOM4 TX. |
| J2 | 4 | CUTDOWN_CTRL | A2/PB09 direct cutdown command. |
| J2 | 5 | 3V3 | Module regulated output. |
| J2 | 6 | GND | Module ground. |
| J2 | 7 | I2C_SCL | Shared host I2C clock. |
| J2 | 8 | I2C_SDA | Shared host I2C data. |
| J2 | 9 | NC | SCK contact intentionally unused. |
| J2 | 10 | NC | MISO contact intentionally unused. |
| J2 | 11 | NC | MOSI contact intentionally unused. |
| A1 | 1 | NC | BLK/FTDI orientation pin intentionally unused. |
| A1 | 2 | GND | OpenLog ground. |
| A1 | 3 | 3V3 | Current captured schematic net only; superseded by the approved `LOGGER_5V` target from S7V8F5 fixed 5 V output. Schematic and PCB implementation are intentionally deferred beyond this documentation-only pass. |
| A1 | 4 | NC | TXO intentionally unused; logger is receive-only. |
| A1 | 5 | UART_TX | RXI receives host log bytes. |
| A1 | 6 | NC | GRN/FTDI orientation pin intentionally unused. |
| C1 | 1 | 3V3 | OpenLog bulk bypass. |
| C1 | 2 | GND | Bypass return. |
| C2 | 1 | 3V3 | OpenLog high-frequency bypass. |
| C2 | 2 | GND | Bypass return. |
| U1 | 1 | GND | A0 address strap low. |
| U1 | 2 | GND | A1 address strap low. |
| U1 | 3 | GND | A2 address strap low; address is 0x20. |
| U1 | 4 | LED_N | P0 active-low write LED sink. |
| U1 | 5 | NC | P1 reserved for future GPS-status LED. |
| U1 | 6 | NC | P2 reserved for future GPS-status LED. |
| U1 | 7 | NC | P3 reserved for future GPS-status LED. |
| U1 | 8 | GND | Expander ground. |
| U1 | 9 | NC | P4 reserved for future GPS-status LED. |
| U1 | 10 | NC | P5 reserved for future GPS-status LED. |
| U1 | 11 | NC | P6 reserved for future GPS-status LED. |
| U1 | 12 | NC | P7 reserved for future GPS-status LED. |
| U1 | 13 | NC | INT intentionally unused. |
| U1 | 14 | I2C_SCL | Shared I2C clock. |
| U1 | 15 | I2C_SDA | Shared I2C data. |
| U1 | 16 | 3V3 | Expander VDD. |
| C3 | 1 | 3V3 | U1 local decoupling. |
| C3 | 2 | GND | U1 decoupling return. |
| R1 | 1 | 3V3 | LED current-limiter supply. |
| R1 | 2 | LED_A | D1 anode feed. |
| D1 | 1 | LED_N | Cathode; U1 P0 active-low sink. |
| D1 | 2 | LED_A | Anode from R1. |
| R2 | 1 | CUTDOWN_CTRL | A2/PB09 series gate input. |
| R2 | 2 | CUTDOWN_GATE | Q1 gate node. |
| R3 | 1 | CUTDOWN_GATE | Intentional default-off pulldown. |
| R3 | 2 | GND | Pulldown return. |
| Q1 | 1 | CUTDOWN_GATE | Gate. |
| Q1 | 2 | GND | Source. |
| Q1 | 3 | CUTDOWN_DRAIN | Drain to nichrome low side. |
| J5 | 1 | PACK_SW | Nichrome high side. |
| J5 | 2 | CUTDOWN_DRAIN | Nichrome switched low side. |
| J6 | 1 | RF_APRS | Single LightAPRS VHF corner contact. |
| J7 | 1 | RF_WSPR | Single LightAPRS HF corner contact. |
| J3 | 1 | RF_APRS | APRS SMA center. |
| J3 | 2 | GND | APRS SMA shield. |
| J4 | 1 | RF_WSPR | WSPR SMA center. |
| J4 | 2 | GND | WSPR SMA shield. |

## Intentional absences

- No host RX path: OpenLog TXO remains unused.
- No UART-sunk LED: D1 is isolated from UART_TX and is controlled by U1 P0.
- P1–P7 are reserved but intentionally no-connect until future GPS-status LEDs are specified and budgeted.
- U1 INT is unused; firmware may poll or write the expander without consuming another host pin.
- No added I2C pull-ups are populated until the existing LightAPRS-W bus pull-ups and effective resistance are verified.
- SCK, MISO, and MOSI are present on J2 but intentionally unused by this carrier.
