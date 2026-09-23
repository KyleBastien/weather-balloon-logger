# Physical fit-check order list

Prepared 2026-09-22 for the LightHABTracker carrier. The machine-readable version is `outputs/fit-check-order-list.xlsx`. Quantities under **Order** include practical spares.

## Buy now

| Category | Ref/use | Exact part | Need | Order | Source | Note |
| --- | --- | --- | ---: | ---: | --- | --- |
| Host module | Host | LightHABTracker 1.0 | 1 | 1 | [QRP Labs](https://shop.qrp-labs.com/aprs/LightHABTracker) | Measure before carrier fabrication. Includes the 3×AA holder. |
| Logger | A1 | SparkFun `DEV-13955` | 1 | 1 | [SparkFun](https://www.sparkfun.com/sparkfun-openlog-with-headers.html) | Buy the with-headers version. |
| Capacitor | C1 | KEMET `C322C475K5R5TA` | 1 | 3 | DigiKey | 4.7 µF radial THT. |
| Capacitor | C2 | KEMET `C315C104K5R5TA` | 1 | 5 | DigiKey | 100 nF radial THT. |
| LED | D1 | Kingbright `WP710A10SGC` | 1 | 2 | DigiKey | 3 mm green THT. |
| Connector | J5 | JST `S2B-XH-A(LF)(SN)` | 1 | 2 | DigiKey | Side-entry, two-position THT. |
| Resistor | R1, R4 | Yageo `MFR-25FBF52-1K` | 2 | 10 | DigiKey | 1 kΩ axial THT. |
| Resistor | R2 | Yageo `MFR-25FBF52-100K` | 1 | 5 | DigiKey | 100 kΩ axial THT pull-up. |
| J5 mate | Harness | JST `XHP-2` | 1 | 2 | DigiKey | Housing. |
| J5 leads | Harness | JST `ASXHSXH22K152` | 2 | 2 | DigiKey | 22 AWG pre-crimp leads; permanently mark polarity/function. |
| Cells | Flight/test | Energizer `L91` | 3 | 6 | Authorized retailer | Two matched 3-cell sets. |
| Storage | OpenLog | microSDHC ≤32 GB, FAT32 | 1 | 2 | Reputable retailer | One spare. |
| Fit tool | Mounting | M2/M2.5 nylon hardware assortment | 4 positions | 1 kit | Local supplier | Exact diameter/height waits for measurement. |

## Hold until the purchased LightHAB is measured

| Item | Reason | Closure |
| --- | --- | --- |
| J2 1×9 signal interface | Electrical order is known; mechanical location, pitch, and installed orientation are not authoritative. | Measure the actual row and select the exact direct-solder part. |
| J3 OUT1/GND interface | Pad geometry and output capability are unverified. | Measure it and qualify OUT1 with an inert load. |
| Bare carrier PCB | The provisional geometry is intentionally marked no-fabrication. | Update CAD from measurements and pass the 1:1 fit check. |
| APRS/WSPR antennas and cables | Bands, payload geometry, routing, and match are not released. | Select and test against the finished payload. |
| Nichrome and crimp sleeves | Resistance/current and joint sizes depend on verified OUT1 capability. | Qualify an inert load first, then cold-test the exact burn assembly. |
| Final mounting hardware | Hole diameter, stack height, underside components, holder, USB, and SMA envelopes are unknown. | Measure the complete tracker assembly. |

Do not buy the removed LightAPRS-era switch, carrier SMA connectors, RF pins, battery connector/holder, PCF8574, MOSFET driver, MOSFET, Pololu logger regulator, or their associated passives. They are not present in the LightHAB carrier.
