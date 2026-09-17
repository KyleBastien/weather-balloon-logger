# Project-local KiCad library

`WeatherBalloon.pretty` is registered by the repository's `fp-lib-table` as
the `WeatherBalloon` footprint library.

## C&K 7101 switch

`WeatherBalloon:SW_CK_7101SYZQE` adapts the exact `Z` solder-lug part for
direct hand soldering into the carrier. The C&K drawing specifies each lug as
2.03 x 0.76 mm and the SPDT terminal row at 4.70 mm pitch. The footprint uses
2.30 x 1.10 mm plated slots to provide practical insertion clearance, with
3.80 x 2.60 mm copper pads and the 6.86 x 12.70 mm body outline.

C&K does not publish this as a formal PCB land pattern: it is a documented
project adaptation of the published lug geometry. The matching downloaded
`7101SYZQE.stp` model is stored under `3dmodels` and linked to the footprint.

## SparkFun OpenLog

`WeatherBalloon:SparkFun_OpenLog_DEV-13712_Carrier` models a top-side OpenLog
module soldered into the carrier through its installed six-pin header. Unlike a
generic header footprint, its courtyard covers the full 15.24 x 19.05 mm module
body from SparkFun's official dimensional drawing. Pin 1 is BLK and pin 6 is GRN,
matching the existing schematic numbering.

## Pololu S7V8F5 logger regulator

`WeatherBalloon:Pololu_S7V8F5_Carrier` models Pololu item 2123 mounted top-side
and direct-soldered through its included straight 1x4 header. The footprint
reserves the official 11.43 x 16.51 mm module body and uses four 1.0 mm drills
for the official 1.02 mm holes. The 2.54 mm-pitch row is centered across the
11.43 mm edge and lies 1.27 mm from that edge. With the body extending upward
from the row in top view, pads read left-to-right as 4 VOUT, 3 GND, 2 VIN, and
1 SHDN. Future schematic/PCB implementation reserves refdes A2 for this module.
