# Weather Balloon Logger carrier brief

Build a hand-solderable through-hole carrier around the QRP Labs LightHABTracker 1.0. LightHAB remains the GPS/APRS/WSPR host, supplies its own 3×AA battery holder and antenna connectors, and owns the two pyro outputs.

The carrier shall:

- mount the tracker once its exact geometry is measured;
- power a SparkFun OpenLog with headers from LightHAB VBATT through a dedicated Pololu S7V8F5 fixed 5 V regulator;
- send telemetry from A1/PB08 to OpenLog RXI through a 1 kΩ series resistor;
- use A2/PB09 as an active-low write-attempt LED with a hardware 100 kΩ reset-default-off pull-up;
- pass LightHAB OUT1/GND directly to a soldered JST-XH cutdown connector;
- contain only through-hole soldered parts, with no SMD pads or carrier RF routing;
- preserve access/keepouts for LightHAB USB, SMA connectors, battery holder, and solder joints;
- remain explicitly blocked from fabrication until the purchased tracker is measured and passes a 1:1 exact-parts fit check.

The carrier does not provide sockets, a second battery holder, a second power switch, an I²C expander, an external pyro MOSFET/driver, or carrier SMA connectors.
