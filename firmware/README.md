# Weather Balloon Logger firmware scaffold

This Stage-7 scaffold targets the LightAPRS-W 2.0 ATSAMD21G18 with the Arduino SAMD core plus the vendor CMSIS device registers already shipped by that core. It is an integration seed, not flight-ready firmware.

`docs/PINOUT.md` is the single source of truth. Regenerate `include/pins.h` from the repository root with:

```text
python firmware/tools/generate_pins.py
```

The generator fails closed unless J2 pin 3 remains `UART_TX` on A1/PB08 and J2 pin 4 remains `CUTDOWN_CTRL` on A2/PB09. It claims no GPS UART, SPI, RESET, or SWD pin; J2 SCL/SDA are reserved for the PCF8574T LED expander.

## Happy path

`WeatherBalloonLogger.ino` first drives cutdown OFF on A2/PB09, initializes a polling TX-only SERCOM4 UART on PB08/PAD0, then sends a CSV heading and one deterministic safe telemetry row to OpenLog. OpenLog TXO is unused. The revised board LED is on PCF8574T P0 at 0x20; this scaffold does not yet implement the I2C LED transaction and must not claim visible write indication until that firmware is added and tested.

## Boundaries

- `cutdown` provides the default-off hardware driver boundary. Production arming, maximum-on-time, one-shot, altitude validation, and fault policy are deliberately not invented here.
- `openlog` provides TX-only UART output without taking the occupied GPS UART.
- `telemetry_stub` marks the integration seam for the existing LightAPRS GPS/radio application.
- No code in this scaffold fires the nichrome output.

See `DEVPLAN.md` for build status and required qualification work.
