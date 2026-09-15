# Bill of materials — Weather Balloon Logger harness

This is the stage-3 selection for the carrier PCB. Every manufacturer part number is **UNVERIFIED** until checked against the current manufacturer datasheet, ordering record, land pattern, temperature range, and availability. The rationale column states the exact acceptance checks; no UNVERIFIED item may be released to procurement merely because its name appears here.

## KiCad capture contract

Only symbols installed in KiCad 10 on this machine are used. `LightAPRS-W 2.0` and `OpenLog` do not exist as named installed symbols. The off-board LightAPRS-W host is therefore represented by its seven-wire carrier interface J2 using `Connector_Generic:Conn_01x07`; A1 OpenLog is represented by its real six-pin header using `Connector_Generic:Conn_01x06`. This is intentional and avoids an invented module symbol. Host GPIO functions and J2 pin allocation remain unassigned until the LightAPRS-W 2.0 / ESP32 strapping and occupied-pin tables are checked in stage 4.

Installed-symbol pin contracts confirmed for capture:

- J1 and J5: `Connector_Generic:Conn_01x02`, package pins 1–2.
- J2: `Connector_Generic:Conn_01x07`, package pins 1–7.
- A1: `Connector_Generic:Conn_01x06`, package pins 1–6.
- J3 and J4: `Connector:Conn_Coaxial`, pin 1 center and pin 2 shield.
- SW1: `Switch:SW_SPDT`, package pins 1–3; one throw is intentionally unused to obtain ON/OFF action.
- Q1: `Transistor_FET:AO3400A`, pin 1 G, pin 2 S, pin 3 D.
- D1: `Device:LED`, pin 1 K and pin 2 A.
- R1–R3: `Device:R`, package pins 1–2. C1–C2: `Device:C`, package pins 1–2.

## Fixed BOM

| Refdes | Value | Footprint | MPN | Rationale |
| --- | --- | --- | --- | --- |
| J1 | Conn_01x02 | Connector_Molex:Molex_Micro-Fit_3.0_43650-0200_1x02_P3.00mm_Horizontal | UNVERIFIED — 43650-0200 | Switched-pack input connector; verify exact land pattern, mating family, contact rating at least 2 A DC at 7.2 V, contact resistance, retention, and −40 °C operation. Passive connector adds no quiescent current; verify insulation leakage is negligible relative to 50 µA budgets. |
| SW1 | SPDT | Button_Switch_THT:SW_CK_7101MD9CQE | UNVERIFIED — 7101MD9CQE | Mechanical master switch in pack positive; common and one throw implement ON/OFF and the other throw is intentionally no-connect. Verify the ordered suffix, three terminal numbers, footprint, maintained action, at least 2 A DC rating at 7.2 V, contact resistance, and −40 °C operation. Open switch provides the required ideal 0 µA except physical insulation leakage. |
| J2 | Conn_01x07 | Connector_PinHeader_2.54mm:PinHeader_1x07_P2.54mm_Vertical | UNVERIFIED — 61300711121 | Seven-wire interface to the off-board LightAPRS-W 2.0 for switched VIN, GND, 3V3, UART TX/RX, write LED GPIO, and cutdown GPIO. Verify footprint, pin numbering, retention, at least 1 A per powered contact, and −40 °C operation; do not assign GPIOs until the host strapping/occupied-pin table is checked. Passive header has no Iq and must have negligible insulation leakage. |
| A1 | OpenLog | Connector_PinSocket_2.54mm:PinSocket_1x06_P2.54mm_Vertical | UNVERIFIED — DEV-13712 | Required SparkFun OpenLog module, captured as its six-pin installed connector symbol because no named OpenLog symbol is installed. Power from 3V3, UART at 3.3 V. Qualification hold: verify exact header order, 3.3 V operation, −40 °C suitability, and maximum idle current no greater than 1.95 mA so A1 plus all board leakage remains within the 2 mA board-added limit; a 2 mA typical-only claim is not sufficient. Active write current must also keep mean pack current at or below 200 mA. |
| J3 | SMA | Connector_Coaxial:SMA_Amphenol_132289 | UNVERIFIED — 132289 | APRS 50 Ω SMA jack, mounted so the mate points downward. Verify jack gender, vertical orientation, footprint, RF band performance, and −40 °C operation. Passive connector draws no current; keep at least 5 mm board keepout from dielectric and battery metal. |
| J4 | SMA | Connector_Coaxial:SMA_Amphenol_132289 | UNVERIFIED — 132289 | WSPR 50 Ω SMA jack, mounted so the mate points downward. Verify jack gender, vertical orientation, footprint, HF performance, and −40 °C operation. Passive connector draws no current; keep at least 5 mm board keepout from dielectric and battery metal. |
| J5 | Conn_01x02 | Connector_Molex:Molex_Micro-Fit_3.0_43650-0200_1x02_P3.00mm_Horizontal | UNVERIFIED — 43650-0200 | Nichrome output connector, placed outside both SMA keepouts. Verify land pattern, mating family, retention, at least 2 A DC for 30 s, contact heating, and −40 °C operation. Passive connector adds no Iq and must have negligible insulation leakage. |
| Q1 | AO3400A | Package_TO_SOT_SMD:SOT-23 | UNVERIFIED — AO3400A | Low-side cutdown FET with installed exact symbol and real G/S/D pins 1/2/3. Verify authentic manufacturer source, VDS at least 30 V, maximum RDS(on) specified at VGS = 2.5 V or lower, safe operating area and junction rise for 2 A for 30 s at 3.3 V gate drive, IDSS no greater than 1 µA at 7.2 V over −40 °C to +40 °C, and IGSS no greater than 0.1 µA. This is selected instead of IRLZ44N because 3.3 V enhancement is specified. |
| D1 | Green LED | LED_SMD:LED_0603_1608Metric | UNVERIFIED — LTST-C190KGKT | Write-activity indicator driven only during an SD write through R1. Verify polarity, footprint, visibility at about 1–2 mA, reverse leakage no greater than 1 µA, and −40 °C operation. GPIO-low OFF state creates no forward-current path and must meet the 1 µA LED-off limit. |
| R1 | 1k | Resistor_SMD:R_0603_1608Metric | UNVERIFIED — RC0603FR-071KL | LED current limiter; at 3.3 V it keeps current below 3 mA for any plausible green LED forward voltage. Verify 1%, at least 0.1 W, pulse rating, footprint, and −40 °C operation. It draws zero current when D1 is off. |
| R2 | 100R | Resistor_SMD:R_0603_1608Metric | UNVERIFIED — RC0603FR-07100RL | Series gate resistor limits GPIO edge current and ringing without creating DC idle draw. Verify 1%, at least 0.1 W, footprint, and −40 °C operation. |
| R3 | 1M | Resistor_SMD:R_0603_1608Metric | UNVERIFIED — RC0603FR-071ML | Intentional Q1 gate pulldown prevents reset-time nichrome firing. It draws 0 µA while the gate is low and 3.3 µA only while cutdown is commanded, below the 50 µA strap-leakage ceiling; verify 1%, voltage rating, footprint, and −40 °C operation. |
| C1 | 4.7uF | Capacitor_SMD:C_0603_1608Metric | UNVERIFIED — GRM188R60J475KE19D | Local OpenLog 3V3 bulk bypass. Verify X5R or better, at least 6.3 V rating, effective capacitance after DC bias, footprint, insulation resistance/leakage contribution compatible with the 2 mA idle budget, and −40 °C operation. |
| C2 | 100nF | Capacitor_SMD:C_0603_1608Metric | UNVERIFIED — GRM188R71H104KA93D | High-frequency OpenLog 3V3 bypass. Verify X7R, at least 16 V rating, footprint, insulation resistance/leakage contribution compatible with the 2 mA idle budget, and −40 °C operation. |

## Budget and intentional-absence notes

- The carrier uses the specified off-board 3s L91 holder, with 4s permitted only if confirmed LightAPRS-W VIN/UVLO data requires it; the holder and cells are not PCB population rows. J1 accepts the switched pack.
- With SW1 OFF, pack positive is physically open and the PCB target is 0 µA except real switch/connector insulation leakage.
- With SW1 ON and cutdown OFF, Q1 target drain leakage is at most 1 µA, gate leakage at most 0.1 µA, D1 has no forward path, R2/R3 have no DC path from 3V3, and passive insulation leakage must be negligible. A1 therefore must demonstrate a maximum idle current no greater than 1.95 mA across the required conditions; otherwise this selection violates `power.board_added_idle_mA` and must be replaced or the architecture explicitly revisited.
- Q1 target dissipation at 2 A is bounded using the verified maximum RDS(on) at 2.5–3.3 V, not threshold voltage. Copper area, transient thermal impedance, and 30 s safe operating area remain layout qualification items.
- No IRLZ44N, relay, second MCU, carrier RTC, USB bridge, charger, or 5 V flight source is populated; each absence is intentional under SPEC.md.
- No GPIO MPN or pin is implied by J2. Stage 4 must check LightAPRS-W/ESP32 strapping and existing GPS/radio/flash use before assigning UART, LED, or cutdown signals.
