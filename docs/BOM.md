# Bill of materials — Weather Balloon Logger harness

This is the complete carrier-PCB selection, re-audited on 2026-09-22. Exact
LightHAB mating parts remain intentionally TBD because the vendor has not
published sufficient pad and hole dimensions. Procurement and fabrication stay
on hold until purchased parts pass the documented fit, mating-part,
temperature, and electrical qualification checks.

## KiCad capture contract

No named LightHABTracker 1.0 or OpenLog symbol is available in the installed KiCad libraries, so the off-board modules are represented by installed generic connector symbols. J2 uses `Connector_Generic:Conn_01x09` in official known order A1, A2, 3V3, GND, SCL, SDA, SCK, MISO, MOSI. J3 uses `Connector_Generic:Conn_01x02` for the LightHAB OUT1/GND interface, and A1 remains the six-pin OpenLog connector. J2.1 A1/PB08 is UART_TX through R4; J2.2 A2/PB09 is active-low LED_N with R2=100 kΩ to 3V3 for reset-default-off; J2.3 directly powers OpenLog and C1/C2. J2.5–J2.9 are intentional no-connects. LightHAB 3V3 capacity is an accepted assumption requiring bench validation, and OUT1 pyro current capability remains explicitly unverified.

Installed-symbol pin contracts freshly confirmed on this machine:

- J3 and J5: `Connector_Generic:Conn_01x02`, package pins 1–2.
- J2: `Connector_Generic:Conn_01x09`, package pins 1–9 in A1, A2, 3V3, GND, SCL, SDA, SCK, MISO, MOSI order.
- A1: `Connector_Generic:Conn_01x06`, package pins 1–6.
- D1: `Device:LED`, pin 1 K and pin 2 A.
- R1, R2, and R4: `Device:R`, package pins 1–2. C1 and C2: `Device:C`, package pins 1–2.

## Fixed BOM

| Refdes | Value | Footprint | MPN | Rationale |
| --- | --- | --- | --- | --- |
| J2 | LightHABTracker 1.0 | Connector_PinHeader_2.54mm:PinHeader_1x09_P2.54mm_Vertical | TBD-LightHAB-1x9 | Provisional direct-solder through-hole 1x9 interface in official known order A1, A2, 3V3, GND, SCL, SDA, SCK, MISO, MOSI. Pin 1 is UART_TX; pin 2 is active-low LED_N; pins 5–9 are intentionally unconnected. Measure the purchased tracker and select the exact interface MPN before fabrication. |
| A1 | OpenLog | WeatherBalloon:SparkFun_OpenLog_DEV-13712_Carrier | DEV-13955 | SparkFun OpenLog with factory pre-soldered headers, mounted top-side with its straight header soldered directly into the carrier. Pin 1 = BLK, pin 2 = GND, pin 3 = VCC directly on LightHAB `3V3`, pin 4 = TXO, pin 5 = RXI, and pin 6 = GRN. SparkFun specifies 3.3–12 V VCC, recommends 3.3–5 V, and lists approximately 20–23 mA active writing current. LightHAB rail capacity requires bench validation. Source: https://learn.sparkfun.com/tutorials/openlog-hookup-guide/all |
| J3 | LightHAB OUT1/GND | Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical | TBD-LightHAB-OUT1 | Direct-solder through-hole two-pin LightHABTracker OUT1/GND pyro interface. It passes straight through to J5 with no carrier driver; LightHAB OUT1 polarity, switching behavior, and pyro current rating remain explicitly unverified. |
| J5 | Cutdown output | Connector_JST:JST_XH_S2B-XH-A_1x02_P2.50mm_Horizontal | S2B-XH-A(LF)(SN) | Retained direct-solder JST-XH cutdown output. Pin 1 receives LightHAB OUT1 directly from J3.1 and pin 2 is GND from J3.2; the carrier adds no pyro switch or current capability, and the LightHAB rating is unverified. |
| D1 | WP710A10SGC | LED_THT:LED_D3.0mm | WP710A10SGC | Kingbright 3 mm green leaded write-activity LED wired 3V3 → R1 → D1 anode, with D1 cathode on LightHAB A2/PB09 (`LED_N`). R2 holds the node high/off at reset. Verify polarity on the 1:1 print. |
| R1 | 1k | Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal | MFR-25FBF52-1K | Yageo 1%, 1/4 W leaded metal-film LED current limiter; 6.3 x 2.4 mm nominal body on 7.62 mm pitch. |
| R4 | 1k | Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal | MFR-25FBF52-1K | Same Yageo 1%, 1/4 W leaded metal-film part as R1, inserted through two 0.8 mm drilled holes on 7.62 mm pitch and soldered from the underside; no 0603 assembly. It limits possible UART back-power during rail sequencing or brownout. Verify UART signal integrity before release. |
| R2 | 100k | Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal | MFR-25FBF52-100K | Yageo 1%, 1/4 W leaded metal-film pull-up from LED_N to 3V3. It keeps the active-low LED off while LightHAB A2/PB09 is high-impedance during reset. |
| C1 | 4.7uF | WeatherBalloon:KEMET_C322C475K5R5TA | C322C475K5R5TA | 50 V X7R radial ceramic OpenLog bulk bypass, 5.08 mm pitch, −55 to +125 °C. |
| C2 | 100nF | WeatherBalloon:KEMET_C315C104K5R5TA | C315C104K5R5TA | 50 V X7R radial ceramic OpenLog high-frequency bypass, 2.54 mm pitch, −55 to +125 °C. |

## Budget and intentional-absence notes

- The flight pack is exactly three Energizer L91 cells in the LightHAB holder. No carrier pack or switch is populated.
- J3 OUT1/GND passes directly to J5. The carrier does not add cutdown current capacity; LightHAB OUT1 ratings and behavior are release gates.
- OpenLog idle ≤7 mA and write ≤25 mA remain qualification targets. Confirm LightHAB 3V3 stays in tolerance during card inrush and writes.
- No relay, second MCU, carrier RTC, USB bridge, charger, carrier RF connector, I2C expander, or discrete cutdown driver is populated; each absence is intentional under SPEC.md.
