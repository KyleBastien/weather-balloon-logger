# Weather Balloon Logger firmware integration scaffold

This scaffold is the carrier-side patch seed for the LightHABTracker 1.0 ATSAMD21G18 firmware. It is not a standalone, compiled flight image: the final changes must be rebased onto and built with the upstream LightHABTracker source pinned in `DEVPLAN.md`.

`docs/PINOUT.md` is the pin source of truth. Regenerate `include/pins.h` from the repository root with:

```text
python firmware/tools/generate_pins.py
```

The generator fails closed unless J2.1 remains UART TX on A1/PB08 and J2.2 remains the active-low activity LED on A2/PB09.

## Intended behavior

`WeatherBalloonLogger.ino` preloads A2 HIGH before making it an output, initializes a polling TX-only SERCOM4 UART on A1/PB08, then writes a heading and one deterministic record to OpenLog while pulsing the LED low. OpenLog TXO is unused.

LightHAB's upstream firmware—not this carrier scaffold—owns OUT1 cutdown timing, arming, and safety. No carrier code directly commands the pyro output.

## Boundaries

- `openlog` provides the proposed TX-only UART implementation without taking the occupied GPS UART.
- `telemetry_stub` marks the seam where upstream LightHAB telemetry must be supplied.
- The LED pulse reports that bytes were sent; it cannot prove that the microSD card committed them.
- A1/PB08 and A2/PB09 appeared unused in the inspected upstream source, but that must be reconfirmed during the pinned-source integration and build.

See `DEVPLAN.md` for the exact upstream baseline and qualification gates.
