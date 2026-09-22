# Bill of materials — Weather Balloon Logger harness

This is the complete carrier-PCB selection, re-audited on 2026-09-21. Exact
LightHAB mating parts remain intentionally TBD because the vendor has not
published sufficient pad and hole dimensions. Procurement and fabrication stay
on hold until purchased parts pass the documented fit, mating-part,
temperature, and electrical qualification checks.

## KiCad capture contract

No named LightHABTracker 1.0 or OpenLog symbol is available in the installed KiCad libraries, so the off-board modules are represented by installed generic connector symbols. J2 uses `Connector_Generic:Conn_01x09` in official known order A1, A2, 3V3, GND, SCL, SDA, SCK, MISO, MOSI. J1 and J3 use `Connector_Generic:Conn_01x02` for the LightHAB VBATT/GND and OUT1/GND interfaces. A1 remains the six-pin OpenLog connector and A2 remains the four-pin Pololu carrier. J2.1 A1/PB08 is UART_TX through R4; J2.2 A2/PB09 is active-low LED_N with R2=100 kΩ to 3V3 for reset-default-off. J2.5–J2.9 are intentional no-connects. LightHAB VBATT switching and OUT1 pyro current capability are explicitly unverified.

Installed-symbol pin contracts freshly confirmed on this machine:

- J1, J3, and J5: `Connector_Generic:Conn_01x02`, package pins 1–2.
- J2: `Connector_Generic:Conn_01x09`, package pins 1–9 in A1, A2, 3V3, GND, SCL, SDA, SCK, MISO, MOSI order.
- A1: `Connector_Generic:Conn_01x06`, package pins 1–6.
- D1: `Device:LED`, pin 1 K and pin 2 A.
- A2: `Connector_Generic:Conn_01x04`, package pin 1 SHDN, pin 2 VIN, pin 3 GND, and pin 4 VOUT.
- R1, R2, and R4: `Device:R`, package pins 1–2. C1 and C2: `Device:C`, package pins 1–2.

## Fixed BOM

| Refdes | Value | Footprint | MPN | Rationale |
| --- | --- | --- | --- | --- |
| J1 | LightHAB VBATT/GND | Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical | TBD-LightHAB-VBATT | Direct-solder through-hole two-pin LightHABTracker VBATT/GND power interface. VBATT feeds A2 VIN and SHDN only; the assumption that the LightHAB onboard switch controls this rail is explicitly unverified and must be bench-confirmed before release. |
| A2 | Pololu S7V8F5 | WeatherBalloon:Pololu_S7V8F5_Carrier | Pololu item 2123 | Dedicated fixed 5 V buck-boost module for OpenLog only, mounted top-side and direct-soldered through its included straight header. Pin 1 SHDN and pin 2 VIN connect to LightHAB `VBATT`, pin 3 to GND, and pin 4 VOUT creates `LOGGER_5V`. Input is 2.7–11.8 V and quiescent current must remain <0.2 mA. The module has no reverse-polarity protection; its temperature rating is unverified and requires cold qualification. |
| J2 | LightHABTracker 1.0 | Connector_PinHeader_2.54mm:PinHeader_1x09_P2.54mm_Vertical | TBD-LightHAB-1x9 | Direct-solder through-hole 1x9 LightHABTracker interface in official known order A1, A2, 3V3, GND, SCL, SDA, SCK, MISO, MOSI. Pin 1 is UART_TX; pin 2 is active-low LED_N; pins 5–9 are physically present and intentionally unconnected on this carrier. Mechanical fit and exact purchased header remain for the later PCB pass. |
| A1 | OpenLog | WeatherBalloon:SparkFun_OpenLog_DEV-13712_Carrier | DEV-13955 | SparkFun OpenLog with factory pre-soldered headers, mounted top-side with its straight header soldered directly into the carrier. SparkFun lists DEV-13955 as the header-equipped version of the DEV-13712 serial OpenLog. The custom carrier footprint includes the official 15.24 × 19.05 mm module body, with pin 1 = BLK, pin 2 = GND, pin 3 = VCC on approved `LOGGER_5V`, pin 4 = TXO, pin 5 = RXI, and pin 6 = GRN. Qualification limits: idle ≤7 mA and write ≤25 mA across required conditions. Source: https://www.sparkfun.com/sparkfun-openlog-with-headers.html |
| J3 | LightHAB OUT1/GND | Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical | TBD-LightHAB-OUT1 | Direct-solder through-hole two-pin LightHABTracker OUT1/GND pyro interface. It passes straight through to J5 with no carrier driver; LightHAB OUT1 polarity, switching behavior, and pyro current rating remain explicitly unverified. |
| J5 | Cutdown output | Connector_JST:JST_XH_S2B-XH-A_1x02_P2.50mm_Horizontal | S2B-XH-A(LF)(SN) | Retained direct-solder JST-XH cutdown output. Pin 1 receives LightHAB OUT1 directly from J3.1 and pin 2 is GND from J3.2; the carrier adds no pyro switch or current capability, and the LightHAB rating is unverified. |
| D1 | WP710A10SGC | LED_THT:LED_D3.0mm | WP710A10SGC | Kingbright 3 mm green leaded write-activity LED wired 3V3 → R1 → D1 anode, with D1 cathode on LightHAB A2/PB09 (`LED_N`). R2 holds the node high/off at reset. Verify polarity on the 1:1 print. |
| R1 | 1k | Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal | MFR-25FBF52-1K | Yageo 1%, 1/4 W leaded metal-film LED current limiter; 6.3 x 2.4 mm nominal body on 7.62 mm pitch. |
| R4 | 1k | Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal | MFR-25FBF52-1K | Same Yageo 1%, 1/4 W leaded metal-film part as R1, inserted through two 0.8 mm drilled holes on 7.62 mm pitch and soldered from the underside; no 0603 assembly. It limits possible UART back-power during regulator startup or brownout. Verify UART signal integrity before release. |
| R2 | 100k | Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal | MFR-25FBF52-100K | Yageo 1%, 1/4 W leaded metal-film pull-up from LED_N to 3V3. It keeps the active-low LED off while LightHAB A2/PB09 is high-impedance during reset. |
| C1 | 4.7uF | WeatherBalloon:KEMET_C322C475K5R5TA | C322C475K5R5TA | 50 V X7R radial ceramic OpenLog bulk bypass, 5.08 mm pitch, −55 to +125 °C. |
| C2 | 100nF | WeatherBalloon:KEMET_C315C104K5R5TA | C315C104K5R5TA | 50 V X7R radial ceramic OpenLog high-frequency bypass, 2.54 mm pitch, −55 to +125 °C. |

## Budget and intentional-absence notes

- The flight pack is exactly three Energizer L91 cells in the LightHAB holder. No carrier pack or switch is populated.
- J1 VBATT feeds only A2 VIN/SHDN. Whether the LightHAB onboard switch controls this node is unverified and is a release gate.
- J3 OUT1/GND passes directly to J5. The carrier does not add cutdown current capacity; LightHAB OUT1 ratings and behavior are release gates.
- OpenLog idle ≤7 mA, OpenLog write ≤25 mA, and S7V8F5 quiescent current <0.2 mA remain qualification targets.
- No relay, second MCU, carrier RTC, USB bridge, charger, carrier RF connector, I2C expander, or discrete cutdown driver is populated; each absence is intentional under SPEC.md.
