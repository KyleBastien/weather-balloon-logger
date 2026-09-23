# Subsystems — Weather Balloon Logger carrier

The LightHABTracker 1.0 is the flight computer, GPS, radio system, battery carrier, logger power source, and pyro controller. This PCB is a passive through-hole carrier.

## Block diagram

```text
LightHAB 3×AA holder / onboard power
        +-- J2.3 3V3 --> OpenLog VCC + C1/C2 bypass
        +-- A1/PB08 --> 1 kΩ --> OpenLog RXI
        +-- A2/PB09 --> active-low activity LED
        +-- OUT1/GND --> J3 --> J5 JST-XH --> cutdown harness
        +-- onboard VHF/UHF radios --> onboard SMA connectors
```

LightHAB 3V3 current capacity and J3 OUT1 electrical capability are assumptions requiring bench validation.

## 1. Power

LightHAB J2.3 3V3 directly supplies OpenLog and its bypass capacitors. SparkFun supports a 3.3 V OpenLog supply; LightHAB rail capacity at startup/write current remains a bench-test gate.

## 2. Host / MCU

- J2: 1×9 extended-pin row ordered A1, A2, 3V3, GND, SCL, SDA, SCK, MISO, MOSI.
- J3: two-pin OUT1/GND pyro handoff to the carrier cutdown connector.
- A1 and A2 are the only extension GPIO used by the carrier.
- I2C and SPI contacts remain physically present and intentional no-connects.

The old LightAPRS 11-pin interface, separate VHF/HF contacts, carrier SMA connectors, carrier master switch, PCF8574 expander, and discrete cutdown driver are removed.

## 3.1 UART SD logger

LightHAB J2.3 directly powers OpenLog A1 VCC. C1 4.7 µF and C2 100 nF bypass the 3V3 rail at OpenLog. OpenLog remains a direct-solder module with through-hole headers.

LightHAB A1/PB08 provides one-way SERCOM4 TX. R4 1 kΩ limits possible back-power into A1 RXI during rail sequencing. OpenLog TXO, BLK, and GRN are intentionally unused.

## 4. UI (operator)

The tracker 3V3 rail drives R1 1 kΩ and D1. LightHAB A2/PB09 sinks `LED_N` when the LED should illuminate. R2 100 kΩ pulls `LED_N` high at reset so the LED defaults off. Firmware must set the output latch HIGH before configuring the pin as OUTPUT.

The PCF8574 and its decoupling capacitor are no longer present.

## 5. Cutdown

LightHAB OUT1/GND arrives at J3 and passes directly to J5, a horizontal JST-XH output. The carrier does not condition, amplify, switch, or fuse this path. Vendor documentation confirms two onboard pyro channels but does not publish sufficient electrical ratings for release. Bench characterization is mandatory before nichrome use.

The former TC4422, IRLZ44N, gate resistors, and bypass capacitors are removed. LightHAB firmware owns pyro default-off behavior and firing duration.

## 6. RF and mechanics

The carrier has no RF circuit. Both SMA connectors are part of LightHAB. The carrier only reserves physical keepouts for the SMA bodies, mating connectors, coax bends, USB access, battery holder, and module components.

The provisional layout mounts LightHAB on the right side, component face outward, with the battery holder between boards. Carrier electronics occupy the left wing. Photo-derived holes and pad positions are placeholders marked **UNVERIFIED — DO NOT FABRICATE** until measured on purchased hardware.

## 7. Intentional absences

| Block | Reason |
| --- | --- |
| Second MCU, GPS, radios | Integrated on LightHAB |
| Carrier battery holder/switch | LightHAB includes them |
| Carrier logger regulator | OpenLog accepts 3.3 V; LightHAB J2.3 supplies it directly |
| Carrier SMA and RF traces | LightHAB includes two SMA connectors |
| I2C LED expander | A2/PB09 directly drives one low-current LED |
| Carrier MOSFET/driver | LightHAB OUT1 is selected, pending rating verification |
| Host RX path | OpenLog is receive-only |
| Charger | Three primary L91 cells are used |
