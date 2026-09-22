# Specification — Weather Balloon Logger carrier

This carrier adapts a LightHABTracker 1.0 to a SparkFun OpenLog, an activity LED, and a removable nichrome cutdown lead. The LightHABTracker remains the only flight computer and supplies GPS, APRS/WSPR radios, a 3×AA battery holder, two SMA connectors, and two pyro channels.

## 1. Architecture

| Item | Requirement | Status |
| --- | --- | --- |
| Host | LightHABTracker 1.0, ATSAMD21G18 | Selected |
| Flight duration | At least 4 h with GPS and flight firmware continuously available | Required; cold-load test pending |
| Battery | Three Energizer L91 AA cells in the tracker holder | Selected |
| Logger | SparkFun OpenLog DEV-13955, one-way UART receive | Selected |
| Logger supply | Pololu S7V8F5 fixed 5 V buck-boost | Selected |
| Cutdown | LightHAB onboard OUT1 pyro channel passed directly to J5 | Selected; electrical rating unverified |
| Carrier assembly | All populated carrier parts directly soldered through-hole; no SMD pads | Required |

The tracker is approximately 56 × 75 mm and 36 g without batteries or antennas according to the vendor. Exact hole centers, drills, header pitch and coordinates, maximum battery-holder height, and connector/switch geometry are not published and must be measured on a purchased unit before fabrication.

## 2. Power

LightHAB accepts 2.7–16 V and carries its own 3×AA holder. The carrier does not contain a second battery holder or master switch. J1 receives LightHAB `VBATT` and `GND`; `VBATT` feeds both VIN and SHDN on A2. This design assumes the photographed LightHAB switch disconnects or controls J1 VBATT. That behavior is **UNVERIFIED**. If J1 remains live with the tracker switched off, this topology must be revised before fabrication.

A2 produces `LOGGER_5V` only for OpenLog A1 and its local C1/C2 bypass. The tracker 3V3 rail powers only the low-current activity LED path. Common ground joins J1, J2, A1, A2, J3, and J5.

| Parameter | Requirement |
| --- | --- |
| Mission energy | Demonstrate ≥4 h at the real cold-temperature and RF duty profile |
| OpenLog idle/write | Qualify ≤7 mA idle and ≤25 mA writing |
| S7V8F5 input | 2.7–11.8 V; no reverse-polarity protection |
| S7V8F5 quiescent | <0.2 mA enabled |
| LED reset state | Off; R2=100 kΩ pulls active-low `LED_N` to 3V3 |
| Switch-off state | Measure J1 VBATT and carrier current with the LightHAB switch off |

## 3. Interfaces

### J2 — LightHAB extended pins

J2 is a directly soldered 1×9 through-hole interface in this order:

| Pin | LightHAB signal | Carrier use |
| --- | --- | --- |
| 1 | A1 / PB08 | `UART_TX` through R4 to OpenLog RXI |
| 2 | A2 / PB09 | Active-low `LED_N` |
| 3 | 3V3 | LED supply and R2 pull-up |
| 4 | GND | Common return |
| 5 | SCL | Intentional no-connect |
| 6 | SDA | Intentional no-connect |
| 7 | SCK | Intentional no-connect |
| 8 | MISO | Intentional no-connect |
| 9 | MOSI | Intentional no-connect |

A1/PB08 and A2/PB09 appear unused in the reviewed upstream firmware at commit `797b78d120b0e844f60798b88dfa3735f27e89da`, but integration must be rebased and retested against the exact firmware shipped on the purchased tracker.

### OpenLog and activity LED

OpenLog is receive-only: J2.1 → R4 1 kΩ → A1 RXI. A1 TXO is intentionally unused. A2 supplies fixed 5 V to A1 VCC. The LED path is 3V3 → R1 1 kΩ → D1 → `LED_N`; firmware drives J2.2 low during activity. R2 keeps it off while the pin is high-impedance at reset. Activity indicates firmware intent to log, not confirmed SD media completion.

### Cutdown

J3 receives LightHAB OUT1/GND and connects directly to the same pins on J5, a horizontal JST-XH connector. The carrier adds no MOSFET, gate driver, or high-current power path. OUT1 polarity, switching topology, pulse duration, current capability, default state, and fault behavior are **UNVERIFIED**. Do not connect nichrome until those properties and the complete harness are bench-tested with a current-limited supply and inert load.

### Antennas

Both antenna connections remain entirely on the LightHABTracker. The carrier contains no SMA connector and no RF trace. The PCB must keep mechanical clearance below and around both onboard SMA connectors and their cable bend volumes.

## 4. Firmware allocation

- A1/PB08: SERCOM4 UART TX to OpenLog.
- A2/PB09: active-low activity LED; write HIGH before configuring OUTPUT to avoid a reset flash.
- LightHAB D4/D5 and the vendor pyro implementation remain owned by upstream firmware. OUT1 is selected for cutdown.
- SCL, SDA, SCK, MISO, and MOSI are not used by the carrier.
- The local firmware is an integration/qualification scaffold, not a replacement for the complete LightHAB flight firmware.

## 5. Mechanical and environment

The carrier outline is 90 × 80 mm. Reserve a provisional 56 × 75 mm LightHAB zone on the right side with the LightHAB component face outward and its battery holder between module and carrier. Use provisional 18–20 mm board-to-board clearance. Place carrier parts on the left wing and keep the OpenLog microSD card accessible. Align the LightHAB USB connector and two SMA connectors with board edges and preserve plug/cable access.

All LightHAB mounting holes and mating interface pads in this revision are photo-derived placeholders and must be labeled **UNVERIFIED — DO NOT FABRICATE**. Final placement requires a purchased module or an official dimensioned drawing.

Qualification temperature remains −40 °C to +40 °C unless the mission profile establishes a wider range. Cold-soak the complete powered stack, batteries, logger, SD card, connectors, and cutdown harness.

## 6. Release gates

Before a fit-test PCB:

1. Measure the LightHAB outline, four hole centers and drills, 1×9 pitch/coordinates/drills, J1/J3 pad coordinates/drills, holder height, and maximum component height.
2. Confirm mounting orientation and USB/SMA/cable access.
3. Confirm whether the onboard switch controls J1 VBATT.
4. Confirm OUT1/GND polarity, voltage, current limit, switching topology, default state, and supported pulse duration.
5. Reconcile those measurements into the footprint, reroute, and regenerate 1:1 plots.

Before fabrication, additionally complete DRC/ERC, footprint-vs-purchased-part checks, cold/power tests, pyro firing tests, firmware integration tests, and a physical 1:1 paper fit check. Until those gates pass, generated fabrication files are engineering previews only.
