# Bill of materials — Weather Balloon Logger harness

This is the complete carrier-PCB selection, re-audited on 2026-09-16. Every
populated refdes now has an exact manufacturer part number in the schematic and
generated BOM. That resolves the CAD/BOM identity, but procurement remains on
hold until the exact purchased parts pass the documented 1:1 fit, mating-part,
temperature, availability, and electrical qualification checks. The fixed
table has exactly one row per individual refdes; each Value cell contains only
the component value, and descriptive prose stays in Rationale.

## KiCad capture contract

Fresh `search_symbols` checks against the installed KiCad 10 libraries found no named `LightAPRS-W 2.0` or `OpenLog` symbol. The off-board LightAPRS-W host is therefore represented by its verified eleven-position carrier interface J2 using installed `Connector_Generic:Conn_01x11`; A1 OpenLog remains its real six-pin header using installed `Connector_Generic:Conn_01x06`. The module's opposite-corner VHF and HF contacts are represented separately by installed single-contact symbols J6 and J7 (`Connector_Generic:Conn_01x01`), with VHF→APRS SMA J3 and HF→WSPR SMA J4. Installed `Interface_Expansion:PCF8574P` is U1; its authoritative pins are A0/A1/A2=1/2/3, P0–P3=4–7, GND=8, P4–P7=9–12, INT=13, SCL=14, SDA=15, and VDD=16. J2 pin 3 A1/PB08 is one-way SERCOM4 UART_TX, pin 4 A2/PB09 drives the non-inverting U2 gate driver, and pins 7–8 carry the shared I2C bus to U1. U1 P0 sinks the write LED active-low; P1–P7 remain intentional no-connects for future status LEDs.

Installed-symbol pin contracts freshly confirmed on this machine:

- J1 and J5: `Connector_Generic:Conn_01x02`, package pins 1–2.
- J2: `Connector_Generic:Conn_01x11`, package pins 1–11 in verified RAW, GND, A1/PB08, A2/PB09, 3V3, GND, SCL, SDA, SCK, MISO, MOSI order.
- J6 and J7: `Connector_Generic:Conn_01x01`, package pin 1; J6 = VHF/APRS and J7 = HF/WSPR.
- A1: `Connector_Generic:Conn_01x06`, package pins 1–6.
- U1: `Interface_Expansion:PCF8574P`, package pins 1–16; address pins 1–3 low select 0x20, P0 pin 4 drives the active-low write LED, pins 5–7 and 9–12 are reserved outputs, pin 13 INT is unused, pins 14–15 are SCL/SDA, pin 16 is VDD, and pin 8 is GND.
- U2: `Driver_FET:TC4422`, package pins 1/8 VDD, 2 IN, 3 NC, 4/5 GND, and 6/7 OUT.
- J3 and J4: `Connector:Conn_Coaxial`, pin 1 center and pin 2 shield.
- SW1: `Switch:SW_SPDT`, package pins 1–3; one throw is intentionally unused to obtain ON/OFF action.
- Q1: `Transistor_FET:IRLZ44N`, pin 1 G, pin 2 D, pin 3 S.
- D1: `Device:LED`, pin 1 K and pin 2 A.
- A2: `Connector_Generic:Conn_01x04`, package pin 1 SHDN, pin 2 VIN, pin 3 GND, and pin 4 VOUT.
- R1–R4: `Device:R`, package pins 1–2. C1–C5: `Device:C`, package pins 1–2.

## Fixed BOM

| Refdes | Value | Footprint | MPN | Rationale |
| --- | --- | --- | --- | --- |
| J1 | Conn_01x02 | Connector_JST:JST_PH_S2B-PH-K_1x02_P2.00mm_Horizontal | S2B-PH-K-S(LF)(SN) | Switched-pack input matching the selected JST-PH battery-holder plug. The PH family is at the 2 A cutdown-current limit, so verify the exact housing/contact pair, crimp quality, polarity, pulse heating, retention, and −40 °C operation. |
| SW1 | SPDT | WeatherBalloon:SW_CK_7101SYZQE | 7101SYZQE | Mechanical master switch in pack positive, hand-soldered directly into plated slots. The `Z` lugs are nominally 2.03 × 0.76 mm; the project adaptation uses 2.30 × 1.10 mm slots on the published 4.70 mm SPDT terminal pitch. C&K rates Q-contact material at 5 A at 28 VDC. Pin 2 is common; one throw is intentionally no-connect. |
| A2 | Pololu S7V8F5 | WeatherBalloon:Pololu_S7V8F5_Carrier | Pololu item 2123 | Dedicated fixed 5 V buck-boost module for OpenLog only, mounted top-side and direct-soldered through its included straight header. Pin 1 SHDN and pin 2 VIN connect to `PACK_SW`, pin 3 to GND, and pin 4 VOUT creates `LOGGER_5V`. Input is 2.7–11.8 V and quiescent current must remain <0.2 mA. The module has no reverse-polarity protection; its temperature rating is unverified and requires cold qualification. |
| J2 | Conn_01x11 | Connector_PinHeader_2.54mm:PinHeader_1x11_P2.54mm_Vertical | 61301111121 | Würth WR-PHD eleven-position, single-row, straight 2.54 mm THT male header for the LightAPRS-W 2.0 edge interface. Official LightAPRS imagery verifies the physical order: 1 RAW→PACK_SW, 2 GND, 3 A1/PB08→UART_TX, 4 A2/PB09→CUTDOWN_CTRL, 5 3V3, 6 GND, 7 SCL→I2C_SCL, 8 SDA→I2C_SDA, 9 SCK, 10 MISO, 11 MOSI. SPI pins are physically present but intentional carrier no-connects. Verify the 1.0 mm carrier drill against the purchased header and module before release. |
| A1 | OpenLog | WeatherBalloon:SparkFun_OpenLog_DEV-13712_Carrier | DEV-13955 | SparkFun OpenLog with factory pre-soldered headers, mounted top-side with its straight header soldered directly into the carrier. SparkFun lists DEV-13955 as the header-equipped version of the DEV-13712 serial OpenLog. The custom carrier footprint includes the official 15.24 × 19.05 mm module body, with pin 1 = BLK, pin 2 = GND, pin 3 = VCC on approved `LOGGER_5V`, pin 4 = TXO, pin 5 = RXI, and pin 6 = GRN. Qualification limits: idle ≤7 mA and write ≤25 mA across required conditions. Source: https://www.sparkfun.com/sparkfun-openlog-with-headers.html |
| J3 | SMA | Connector_Coaxial:SMA_Amphenol_132134_Vertical | 132134 | APRS 50 Ω vertical SMA jack placed on the PCB bottom so the mate points downward. Retain the additional RF/mechanical and cable keepouts beyond the stock 8.34 × 8.34 mm courtyard. |
| J4 | SMA | Connector_Coaxial:SMA_Amphenol_132134_Vertical | 132134 | WSPR 50 Ω vertical SMA jack placed on the PCB bottom so the mate points downward. Retain the additional RF/mechanical and cable keepouts beyond the stock 8.34 × 8.34 mm courtyard. |
| J6 | VHF | Connector_PinHeader_2.54mm:PinHeader_1x01_P2.54mm_Vertical | 61300111121 | Würth WR-PHD single-position, straight 2.54 mm THT male header for the LightAPRS VHF corner contact to RF_APRS and J3 center. The active part is rated 3 A and −40 °C to +105 °C. Verify the current 1.0 mm carrier drill against Würth's nominal 1.10 mm recommended hole and the physical module before release. Source: https://www.we-online.com/components/products/datasheet/61300111121.pdf |
| J7 | HF | Connector_PinHeader_2.54mm:PinHeader_1x01_P2.54mm_Vertical | 61300111121 | Same Würth single-position straight THT header as J6, used for the separate LightAPRS HF corner contact to RF_WSPR and J4 center. Official LightAPRS imagery confirms HF at bottom-left and VHF at bottom-right in face-up view. Verify physical fit before release. |
| J5 | Conn_01x02 | Connector_JST:JST_XH_S2B-XH-A_1x02_P2.50mm_Horizontal | S2B-XH-A(LF)(SN) | Nichrome output connector with more current margin than JST-PH. Place outside both SMA keepouts and verify the exact housing/contact pair, retention, 2 A for 30 s pulse heating, cable bend volume, and −40 °C operation. |
| Q1 | IRLZ44NPBF | Package_TO_SOT_THT:TO-220-3_Vertical | IRLZ44NPBF | Active Infineon 55 V TO-220 low-side cutdown FET. U2 drives its gate from fixed 5 V because its guaranteed maximum 35 mΩ RDS(on) point is VGS=4.5 V; do not drive it directly from the 3.3 V host. Verify 2 A for 30 s SOA and thermal rise on released copper. |
| U2 | TC4422AVPA | Package_DIP:DIP-8_W7.62mm | TC4422AVPA | Active Microchip non-inverting PDIP-8 MOSFET driver. LOGGER_5V powers pins 1/8, CUTDOWN_CTRL drives pin 2, pin 3 is NC, pins 4/5 are GND, and tied outputs 6/7 drive R2. VIH is compatible with 3.3 V logic (2.4 V requirement), supply range is 4.5–18 V, and input-low supply current is at most 0.2 mA. |
| D1 | WP710A10SGC | LED_THT:LED_D3.0mm | WP710A10SGC | Kingbright 3 mm green leaded write-activity LED wired 3V3 → R1 → D1 anode, with D1 cathode on U1 P0 (`LED_N`). P0 high after reset leaves it off. Verify polarity on the 1:1 print. |
| R1 | 1k | Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal | MFR-25FBF52-1K | Yageo 1%, 1/4 W leaded metal-film LED current limiter; 6.3 x 2.4 mm nominal body on 7.62 mm pitch. |
| R4 | 1k | Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal | MFR-25FBF52-1K | Same Yageo 1%, 1/4 W leaded metal-film part as R1, inserted through two 0.8 mm drilled holes on 7.62 mm pitch and soldered from the underside; no 0603 assembly. It limits possible UART back-power during regulator startup or brownout. Verify UART signal integrity before release. |
| R2 | 100R | Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal | MFR-25FBF52-100R | Yageo 1%, 1/4 W leaded metal-film series resistor between U2 outputs and Q1 gate. |
| R3 | 1M | Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal | MFR-25FBF52-1M | Yageo 1%, 1/4 W leaded metal-film gate pulldown; keeps Q1 off if U2 is unpowered or disconnected. |
| C1 | 4.7uF | WeatherBalloon:KEMET_C322C475K5R5TA | C322C475K5R5TA | 50 V X7R radial ceramic OpenLog bulk bypass, 5.08 mm pitch, −55 to +125 °C. |
| C2 | 100nF | WeatherBalloon:KEMET_C315C104K5R5TA | C315C104K5R5TA | 50 V X7R radial ceramic OpenLog high-frequency bypass, 2.54 mm pitch, −55 to +125 °C. |
| U1 | PCF8574N | Package_DIP:DIP-16_W7.62mm | PCF8574N | Active TI PDIP-16 I2C expander on 3V3. A0/A1/A2 are low for address 0x20; P0 is the active-low LED sink; P1–P7 and INT remain intentional no-connects. Maximum standby current remains limited to 100 µA. |
| C3 | 100nF | WeatherBalloon:KEMET_C315C104K5R5TA | C315C104K5R5TA | 50 V X7R radial ceramic local U1 bypass, 2.54 mm pitch, −55 to +125 °C. |
| C4 | 100nF | WeatherBalloon:KEMET_C315C104K5R5TA | C315C104K5R5TA | Local high-frequency LOGGER_5V bypass at U2, installed adjacent to its VDD/GND pins. |
| C5 | 4.7uF | WeatherBalloon:KEMET_C322C475K5R5TA | C322C475K5R5TA | Local bulk LOGGER_5V bypass at U2, paired with C4 per the driver test circuit guidance. |

## Budget and intentional-absence notes

- The flight pack is exactly three series Energizer L91 cells, 3.0–5.4 V; 4s is no longer permitted. J1 accepts the pack and SW1 creates `PACK_SW`. LightAPRS RAW/J2.1 and cutdown J5.1 remain directly on `PACK_SW` and must never be routed through the logger regulator.
- With SW1 OFF, pack positive is physically open and the PCB target is 0 µA except real switch/connector insulation leakage.
- With SW1 ON and cutdown OFF, Q1 remains off through R3, D1 is commanded off, and U2 adds at most 0.2 mA with its input low. The approved split-power limits remain OpenLog idle ≤7 mA, S7V8F5 Iq <0.2 mA, U1 standby ≤0.1 mA, board-added idle ≤8 mA, and board-added active/write peak ≤30 mA.
- Q1 target dissipation at 2 A is bounded using the guaranteed maximum RDS(on) at VGS=4.5 V, not threshold voltage. Copper area, transient thermal impedance, and 30 s safe operating area remain layout qualification items.
- No relay, second MCU, carrier RTC, USB bridge, charger, or separate 5 V flight source is populated; each absence is intentional under SPEC.md.
- The verified LightAPRS-W 2.0 physical header uses J2 pin 3 A1/PB08 for one-way SERCOM4 UART_TX and J2 pin 4 A2/PB09 for `CUTDOWN_CTRL` into U2. J2 pins 7–8 share the exposed I2C bus with U1; no duplicate pull-ups are populated until the module's effective pull-up resistance is verified. U1 P0 sinks D1 active-low, leaving P1–P7 reserved.
