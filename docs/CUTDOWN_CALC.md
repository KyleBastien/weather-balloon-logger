# Cutdown current-path calculation

Date: 2026-09-16

This is the pre-fabrication calculation for the nominal 2 A, 30 s cutdown
pulse. It closes the PCB copper-sizing question; it does not replace the
prototype test of the complete battery, connectors, harness, and nichrome.

## Released assumptions

- Two-layer FR-4 with **at least 1 oz (35 um) finished outer copper**.
- 2.0 A continuous current for 30 s during the cutdown event.
- Copper resistivity: 1.724e-8 ohm-m at 20 degrees C.
- IRLZ44NPBF maximum RDS(on): 35 milliohm at VGS = 4.5 V.
- The board resistance below is intentionally calculated from trace centerline
  length and nominal width only. Pads add copper area, so excluding them is
  conservative for the bare-board conductor.

## PCB conductor calculation

Resistance is calculated as `R = rho * length / (width * thickness)`.

| Path | Geometry | Resistance | Drop at 2 A | Loss at 2 A |
| --- | ---: | ---: | ---: | ---: |
| J1 to SW1 (`PACK_IN`) | 11.00 mm at 1.50 mm | 3.61 mohm | 7.2 mV | 14 mW |
| SW1 to J5 (`PACK_SW`) | 13.59 mm at 1.50 mm plus 23.95 mm at 1.00 mm | 16.26 mohm | 32.5 mV | 65 mW |
| J5 to Q1 (`CUTDOWN_DRAIN`) | 23.98 mm at 1.50 mm | 7.88 mohm | 15.8 mV | 32 mW |
| **PCB copper total** | | **27.75 mohm** | **55.5 mV** | **111 mW** |

The board copper dissipates approximately 3.33 J over 30 s. At 0.5 oz the
calculated copper resistance and loss would double, so this design requires at
least 1 oz outer copper unless the calculation is repeated after a layout or
stackup change.

## MOSFET and calculated board total

At the datasheet maximum 35 milliohm, Q1 contributes no more than 70 mV and
140 mW at 2 A, or 4.2 J over 30 s. The calculated PCB-copper-plus-Q1 total is
therefore 62.75 milliohm, 125.5 mV drop, 251 mW, and 7.53 J over the pulse.
This is low electrical stress for the TO-220 device, but actual Q1 VDS and
temperature must still be measured on the assembled prototype at the coldest
driver/battery condition.

## Component margin and remaining test

- C&K 7101SYZQE Q contacts are rated 5 A at 28 VDC, above the 2 A pulse.
- The JST-XH output family is rated 3 A, above the 2 A pulse.
- The JST-PH pack connection is rated 2 A and therefore has no nameplate
  current margin. Exact mating housing, contacts, crimp, wire gauge, and cold
  contact resistance must be qualified together.
- Connector contact resistance, battery-holder resistance, harness resistance,
  solder-joint resistance, and nichrome resistance are outside the PCB files
  and cannot be closed by CAD analysis.

Before flight release, run a 2 A, 30 s dummy-load test on an assembled
engineering prototype. Record voltage drop across J1, SW1, J5, Q1, and the
complete harness, plus peak temperatures at both connectors, the narrow PCB
traces, solder joints, and Q1. Repeat at the worst justified cold battery and
ambient condition. Any connector heating or excessive voltage loss requires a
connector/harness or copper revision.

## Sources

- Infineon IRLZ44N datasheet:
  https://www.infineon.com/assets/row/public/documents/24/49/infineon-irlz44n-datasheet-en.pdf
- C&K 7000-series switch datasheet: local controlled copy
  `C:\Users\Kyle Bastien\Downloads\CKCI-S-A0001796810-1.pdf`
- JST PH and XH manufacturer catalogs:
  https://www.jst-mfg.com/product/index.php?series=199 and
  https://www.jst-mfg.com/product/index.php?series=277

