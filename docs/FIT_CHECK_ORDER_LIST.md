# Physical fit-check order list

Prepared 2026-09-20 for one complete Weather Balloon Logger carrier. This is
the purchasing companion to `outputs/BOM.csv`: it includes the populated PCB
parts, the LightAPRS module, mating cable hardware, power source, and fit-check
consumables. Quantities in **Order** include practical prototype spares.

## Buy now

| Category | Ref / use | Exact manufacturer part | Need | Order | Suggested source | Notes |
|---|---|---:|---:|---:|---|---|
| Module | A1 OpenLog | SparkFun `DEV-13955` | 1 | 1 | [SparkFun](https://www.sparkfun.com/sparkfun-openlog-with-headers.html) | Buy the **with headers** version. |
| Module | A2 5 V regulator | `Pololu item 2123` (S7V8F5) | 1 | 1 | [Pololu](https://www.pololu.com/product/2123) | Straight header is included; solder it directly. |
| Module | LightAPRS host | LightAPRS-W 2.0 (+WSPR) | 1 | 1 | [QRP Labs](https://www.qrp-labs.com/lightaprsw2.html) | This is the exact 2.0 WSPR-capable board whose geometry is represented by J2/J6/J7/H1-H4. |
| Capacitor | C1, C5 | KEMET `C322C475K5R5TA` | 2 | 4 | [DigiKey search](https://www.digikey.com/en/products/result?keywords=C322C475K5R5TA) | 4.7 uF radial, through-hole. |
| Capacitor | C2-C4 | KEMET `C315C104K5R5TA` | 3 | 10 | [DigiKey search](https://www.digikey.com/en/products/result?keywords=C315C104K5R5TA) | 0.1 uF radial, through-hole. |
| LED | D1 | Kingbright `WP710A10SGC` | 1 | 2 | [DigiKey search](https://www.digikey.com/en/products/result?keywords=WP710A10SGC) | 3 mm green, through-hole. |
| PCB connector | J1 battery input | JST `S2B-PH-K-S(LF)(SN)` | 1 | 2 | [DigiKey search](https://www.digikey.com/en/products/result?keywords=S2B-PH-K-S%28LF%29%28SN%29) | Side-entry PH, 2 positions. |
| Module header | J2 LightAPRS edge | Wurth `61301111121` | 1 | 2 | [DigiKey search](https://www.digikey.com/en/products/result?keywords=61301111121) | 1x11, 2.54 mm, straight through-hole. |
| RF connector | J3, J4 | Amphenol RF `132134` | 2 | 2 | [DigiKey search](https://www.digikey.com/en/products/result?keywords=132134) | Standard SMA female jack, **not RP-SMA**. |
| PCB connector | J5 cutdown output | JST `S2B-XH-A(LF)(SN)` | 1 | 2 | [DigiKey search](https://www.digikey.com/en/products/result?keywords=S2B-XH-A%28LF%29%28SN%29) | Side-entry XH, 2 positions. |
| RF/module pin | J6, J7 | Wurth `61300111121` | 2 | 5 | [DigiKey search](https://www.digikey.com/en/products/result?keywords=61300111121) | Single-position, 2.54 mm, straight through-hole. |
| MOSFET | Q1 | Infineon `IRLZ44NPBF` | 1 | 2 | [DigiKey search](https://www.digikey.com/en/products/result?keywords=IRLZ44NPBF) | TO-220, through-hole. |
| Resistor | R1, R4 | Yageo `MFR-25FBF52-1K` | 2 | 10 | [DigiKey](https://www.digikey.com/en/products/detail/yageo/MFR-25FBF52-1K/13011) | 1 kohm, 1%, 1/4 W axial. |
| Resistor | R2 | Yageo `MFR-25FBF52-100R` | 1 | 5 | [DigiKey search](https://www.digikey.com/en/products/result?keywords=MFR-25FBF52-100R) | 100 ohm, 1%, 1/4 W axial. |
| Resistor | R3 | Yageo `MFR-25FBF52-1M` | 1 | 5 | [DigiKey search](https://www.digikey.com/en/products/result?keywords=MFR-25FBF52-1M) | 1 Mohm, 1%, 1/4 W axial. Exact part was temporarily out of stock at DigiKey on 2026-09-20; do not substitute without checking body dimensions. |
| Switch | SW1 | C&K `7101SYZQE` | 1 | 1 | [DigiKey](https://www.digikey.com/en/products/detail/c-k/SWITCH-7101SYZQE/25966) | Exact solder-lug variant used for the custom footprint. Do not buy SYWQE. |
| IC | U1 | NXP `PCF8574N` | 1 | 2 | [DigiKey search](https://www.digikey.com/en/products/result?keywords=PCF8574N) | PDIP-16, through-hole. |
| IC | U2 | Microchip `TC4422AVPA` | 1 | 2 | [DigiKey search](https://www.digikey.com/en/products/result?keywords=TC4422AVPA) | PDIP-8, through-hole. |
| Battery harness | 3xAA holder | MPD `BH3AAW` | 1 | 1 | [DigiKey](https://www.digikey.com/en/products/detail/mpd-memory-protection-devices/BH3AAW/32050) | Off-board holder with 6-inch 24 AWG leads. Confirm pulse heating during qualification. |
| Battery harness | J1 mate | JST `PHR-2` | 1 | 2 | [DigiKey](https://www.digikey.com/en/products/detail/jst-sales-america-inc/PHR-2/608607) | Housing only; contacts/leads are separate. |
| Battery harness | J1 pre-crimp leads | JST `ASPHSPH24K152` | 2 conductors | 2 | [DigiKey search](https://www.digikey.com/en/products/result?keywords=ASPHSPH24K152) | 24 AWG, 6-inch, socket-to-socket. Cut each in half and splice to the holder; mark polarity permanently. |
| Cutdown harness | J5 mate | JST `XHP-2` | 1 | 2 | [DigiKey search](https://www.digikey.com/en/products/result?keywords=XHP-2) | Housing only; contacts/leads are separate. |
| Cutdown harness | J5 pre-crimp leads | JST `ASXHSXH22K152` | 2 conductors | 2 | [DigiKey](https://www.digikey.com/en/products/detail/jst-sales-america-inc/ASXHSXH22K152/6684931) | 22 AWG, 6-inch, socket-to-socket. Cut each in half; permanently identify PACK+ and FET-. |
| Power | AA cells | Energizer `L91` Ultimate Lithium | 3 | 6 | [Manufacturer datasheet](https://data.energizer.com/pdfs/l91.pdf) | Three cells in series only. Six gives one flight set and one test set. Never mix age/state. |
| Storage | OpenLog media | 32 GB or smaller microSDHC, FAT32 | 1 | 2 | [OpenLog requirements](https://www.sparkfun.com/sparkfun-openlog-with-headers.html) | Use a reputable card; one spare is worthwhile. |
| Mechanical fit tool | LightAPRS spacing | M2 nylon standoff/screw/nut assortment | 4 positions | 1 kit | Local supplier | Fit-check tool only. Final spacer length waits for the physical module stack-up. |
| Assembly consumable | Wire splices | Adhesive-lined heat-shrink sized for 22-24 AWG | 4 joints | 1 pack | Local supplier | Covers soldered copper-to-copper splices; it is not the nichrome joint. |

## Do not order yet

| Item | Why it is held | Close the hold by |
|---|---|---|
| Bare PCB fabrication | The exact-parts 1:1 fit check is deliberately before fabrication. | Lay every buy-now board part and the LightAPRS module on `outputs/renders/board-fit-check-1to1.pdf`; verify the print scale, body/courtyard fit, pin entry, module hole centers, connector access, and cable bend volume. Then update the PCB and regenerate fabrication outputs if anything differs. |
| APRS antenna/cable | Connector mating and 144-146 MHz operation are known, but payload cable length, antenna geometry, and mounting are not released. | Pick the payload/enclosure layout, cable length, antenna, and strain relief; verify 50-ohm SMA male mating and VHF VSWR. |
| WSPR antenna/cable and low-pass filter | The WSPR band is firmware/configuration dependent and LightAPRS-W 2.0 has no onboard HF low-pass filter. | Select the authorized band, design/select its filter and antenna, then verify harmonics and match. |
| Nichrome wire | Gauge and active length determine resistance and current; selecting a spool now would imply an unverified cutdown design. | Bench-characterize at 3.0-5.4 V and cold; meet the <=2 A, <=30 s design limit with margin. |
| Nichrome termination sleeves | Nichrome is not reliably joined with ordinary solder. Sleeve size depends on final nichrome and copper wire diameters. | After wire selection, use compatible mechanical crimp sleeves and prove pull strength/contact heating. |
| Final M2 spacers | The module-hole coordinates and actual component clearance still require physical confirmation. | Measure the purchased LightAPRS module against the carrier drawing and choose exact spacer length/material. |

## Assembly and fit-check notes

- Use the exact MPNs above for the fit check; a pin-compatible substitute can still
  have the wrong body, lead pitch, or connector envelope.
- `ASPHSPH24K152` and `ASXHSXH22K152` avoid buying proprietary production crimp
  tooling for a one-off prototype. Cut a socket-to-socket lead at its midpoint to
  obtain two terminated pigtails.
- J1 is at the JST-PH family's 2 A edge. The finished battery harness must pass the
  documented pulse-heating, polarity, retention, and cold tests before flight.
- The full board-level engineering BOM remains in `docs/BOM.md`; the machine BOM is
  `outputs/BOM.csv`.

## Source checks

Supplier availability changes. The order links and exact MPNs were checked on
2026-09-20. SparkFun listed `DEV-13955` in stock; QRP Labs listed the LightAPRS-W
2.0 at USD 140; DigiKey listed the exact C&K switch, Amphenol SMA connector,
JST housings/pre-crimp leads, MPD holder, and most discrete parts. Recheck stock,
authorized-distributor status, and price at checkout.
