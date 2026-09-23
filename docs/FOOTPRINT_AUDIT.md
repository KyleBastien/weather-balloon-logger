# Through-hole footprint audit

Date: 2026-09-22

## Result

The PCB contains 10 populated electrical references, four NPTH mounting holes, and one padless silkscreen-art footprint. Automated inspection reports 35 pads (31 plated through-hole and four NPTH) and **zero SMD pads**. KiCad reports zero footprint errors, zero DRC violations, and zero unconnected items.

Every populated carrier component is intended for direct through-hole soldering. There are no surface-mount lands, castellated pseudo-pads, test-pad-only connections, or carrier SMA pads.

## Electrical footprints

| Refs | Footprint | Status |
| --- | --- | --- |
| A1 | `WeatherBalloon:SparkFun_OpenLog_DEV-13712_Carrier` | Verified against SparkFun 15.24 × 19.05 mm module drawing; confirm purchased header orientation |
| C1 | `WeatherBalloon:KEMET_C322C475K5R5TA` | Project THT footprint for selected radial 4.7 µF part |
| C2 | `WeatherBalloon:KEMET_C315C104K5R5TA` | Project THT footprint for selected radial 100 nF part |
| R1, R2, R4 | `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal` | Stock leaded axial footprint |
| D1 | `LED_THT:LED_D3.0mm` | Stock 3 mm leaded LED footprint |
| J5 | `Connector_JST:JST_XH_S2B-XH-A_1x02_P2.50mm_Horizontal` | Stock horizontal THT JST-XH; verify housing/contact/polarity |
| J2 | `Connector_PinHeader_2.54mm:PinHeader_1x09_P2.54mm_Vertical` | **Provisional:** electrical pin count/order known; physical pitch/position/drill unverified |
| J3 | `Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical` | **Provisional placeholder:** LightHAB pad pitch/position/drill unverified |

## Mechanical and artwork footprints

| Refs | Footprint | Status |
| --- | --- | --- |
| H1–H4 | `MountingHole:MountingHole_3.2mm_M3` | **Provisional:** 3.2 mm NPTH and all centers require measurement |
| G1 | `WeatherBalloon:CoffeeBalloon_7.5x11.25mm` | Padless front-silkscreen artwork; OUT1 and GND traces route outside its full envelope |

## Removed obsolete footprints

The following LightAPRS-era parts are absent from the board: SW1, U1, U2, Q1, C3, C4, C5, R3, J4, J6, and J7. J1 and A2 were subsequently removed when the logger supply moved to direct LightHAB 3V3. The carrier has no RF connectors, I2C expander, discrete cutdown driver, VBATT interface, or logger regulator.

## Fit-test hold

Do not fabricate this revision. The selected generic J2/J3 footprints and H1–H4 are deliberately visible placeholders, not claims that LightHAB uses 2.54 mm headers or 3.2 mm mounting holes. Replace them after measuring the purchased tracker, then perform a 1:1 paper fit with the actual module, headers/pins, standoffs, USB cable, SMA mates, batteries, OpenLog, JST cable, and enclosure.
