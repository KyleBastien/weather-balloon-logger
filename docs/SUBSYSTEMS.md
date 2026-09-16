# Subsystems — Weather Balloon Logger harness

Carrier PCB only. Firmware, GPS, and radios live on LightAPRS-W 2.0. This document freezes the block diagram and per-subsystem budgets. Stage 4 checked the LightAPRS-W 2.0 (ATSAMD21G18) occupied-pin map and records the final two-GPIO allocation in `docs/PINOUT.md`.

## Prose block diagram

Energizer L91 AA cells in a **3s baseline** holder (4s only if host VIN/UVLO cannot run to 3s EOD 3.0 V) feed pack+ through a mechanical switch **SW1 that breaks pack positive**. Switched pack+ goes to LightAPRS-W 2.0 **RAW** on J2.1. The tracker’s regulated **3V3** powers OpenLog, U1 PCF8574T, and the write-activity path 3V3 → 1 kΩ → LED → U1 P0; P0 is active-low and powers up high/off. A2/PB09 drives the cutdown MOSFET gate through R2 with an **intentional pulldown** to GND so nichrome cannot false-fire on reset. A1/PB08 provides one-way SERCOM4 UART TX to OpenLog RXI; OpenLog TXO is intentionally unused. J2.7/J2.8 expose the shared SCL/SDA bus to U1 at address 0x20; P1–P7 are reserved no-connect outputs for future GPS-status LEDs. Two **50 Ω SMA jacks** take RF from separate opposite-corner module contacts: J6 VHF→J3 APRS and J7 HF→J4 WSPR. No second MCU, carrier RTC, USB-serial bridge, L91 charger, or 5 V flight source is added.

```text
L91 3s (4s iff UVLO) --pack+--> SW1 --VIN--> LightAPRS-W 2.0 --3V3--> OpenLog + LED anode path
                                      GND common
Host A1/PB08 SERCOM4 TX -----------> OpenLog RXI (one-way)
Host A2/PB09 -----------------------> FET gate + pulldown
Host SCL/SDA -----------------------> PCF8574T @ 0x20; P0 sinks write LED, P1–P7 reserved
Pack+ --nichrome jack--> FET drain; FET source --> GND
LightAPRS-W VHF J6 / HF J7 --------> SMA_APRS J3 / SMA_WSPR J4 (downward, 50 Ω)
```

## 1. Power

| Item | Value | Why |
| --- | --- | --- |
| Chemistry | L91 AA Li-FeS2 | SPEC §2.1; alkaline forbidden (cold); LiPo 1S forbidden |
| Topology | 3s baseline, 4s only for VIN/UVLO | Series does not add mAh; 3s meets ≥1600 mAh usable vs 800 mAh flight load |
| Pack voltage | 3s 3.0–5.4 V; 4s 4.0–7.2 V | Fresh ≤1.8 V/cell, EOD ≥1.0 V/cell; combined bound 3.0–7.2 V |
| Host VIN | ASSUMED 3.5–12 V class | **Unconfirmed** from LightAPRS-W 2.0 docs; if 3s EOD 3.0 V is below UVLO, use 4s — do not add cells for amp-hours |
| Mean pack current | ≤ 200 mA over 4 h | GPS on + ATSAMD21G18 + OpenLog + APRS/WSPR TX duty; peaks do not relax the mean |
| Flight energy | 800 mAh @ 4 h; usable pack ≥ 1600 mAh after ASSUMED 50% cold derate | 2× margin; 3s L91 meets capacity |
| Switch OFF | **0 µA** (ideal) except holder/switch leakage | SW1 **must break pack+**; any always-on divider on pack+ is a budget bug |
| Board-added idle | ≤ **2 mA** beyond LightAPRS-W 2.0 | Switch ON, cutdown OFF, LED off, OpenLog idle |
| Cutdown OFF leakage | ≤ **50 µA** at max pack V | FET Idss / relay off |
| LED OFF leakage | ≤ **1 µA** | No bleed path that looks like a glow |
| Strap leakage | ≤ **50 µA** total extra | Pull-ups/downs on host GPIOs |
| Logic rail | **3.3 V** from tracker 3V3, not raw pack | GPIO, LED, FET gate |
| OpenLog VCC | Module 3.3–12 V; **tie to 3V3** unless 3V3 LDO current share is exceeded | Do not feed OpenLog from unregulated 4s (~7.2 V fresh) |

A part that fits voltage/package but blows Iq is a bug. No paralleling cells without per-string fusing (not in brief; not assumed).

## 2. Host / MCU

LightAPRS-W 2.0 (QRP Labs, **ATSAMD21G18** / ARM Cortex-M0, 3.3 V) is the **only** MCU. It hosts all flight firmware, GPS, APRS, and WSPR. This PCB is a harness: power, connectors, OpenLog + write LED, cutdown switch, dual SMA.

- **RTC on this carrier:** not required; host RTC/GPS time is sufficient. Absence is intentional.
- **Boot / strapping (ATSAMD21G18):** the SAMD21 boots from internal flash with **no ESP32-style GPIO boot straps**; its bootloader is entered by a double-tap on RESET, and SWDIO/SWCLK/RESET are programming pins not broken out to the extension header. The governing constraint is therefore the *occupied-pin* map below plus keeping cutdown default-off (gate pulldown), not ESP32 strap avoidance.
- **Verified host pin map** (from LightAPRS-W-2.0 firmware source + qrp-labs.com). Occupied — do NOT reuse: `D0/D1` GPS UART (Serial1), `D3` VHF PTT, `D4` Si4463 SDN, `D7` GPS power, `D8` Si4463 nSEL (SPI CS), `D9` Si4463 nIRQ, `A3` Si5351 power, `A4` TCXO power, `A5` battery sense; `SDA/SCL` I2C bus (BMP180 + Si5351); `MOSI/MISO/SCK` SPI bus (Si4463). The verified 11-position header exposes **A1/PB08** and **A2/PB09** as the two dedicated carrier GPIOs plus the shared I2C/SPI buses. A1 is UART_TX, A2 is cutdown, I2C is shared with U1, and carrier SPI is unused.
- **UART for OpenLog:** A1/PB08 remains one-way SERCOM4 TX to OpenLog RXI. OpenLog TXO is intentionally unused; the occupied GPS UART remains untouched.
- **Cutdown GPIO:** the verified header exposes A2/PB09, which now drives CUTDOWN_CTRL directly through R2; R3 remains the mandatory hardware default-off path. A0 is no longer claimed.
- **LED expansion:** shared SCL/SDA drive U1 PCF8574T at 0x20. P0 sinks D1 active-low; P1–P7 are reserved for future GPS-status LEDs and INT is unused. This avoids loading UART_TX and preserves direct GPIO cutdown control.

## 3. Connectivity

### 3.1 UART SD logger

SparkFun OpenLog (ATmega328, headers). Host A1/PB08 SERCOM4 TX → OpenLog RXI; OpenLog TXO is intentionally no-connect; GND common. UART is 3.3 V; no 5 V shifter. Absence of a USB-serial bridge on this PCB is intentional — programming the ATSAMD21G18 stays on LightAPRS-W 2.0 (native USB).

OpenLog idle current counts toward **board-added ≤ 2 mA** and is now limited to a verified maximum of 1.85 mA so U1 may use at most 0.10 mA and all other idle leakage may use at most 0.05 mA. If 3V3 LDO current share cannot cover OpenLog plus U1, stop and revisit the architecture rather than silently moving either load to raw pack.

### 3.2 Antennas

Two SMA jacks, 50 Ω, mates facing **downward** through the payload. One SMA **APRS** (typically 2 m), one SMA **WSPR** (HF as built on LightAPRS-W 2.0). Keep RF path short. Board keepout **≥ 5 mm** from SMA dielectric; no battery metal in the near-field of the jacks. Nichrome connector stays out of that keepout.

The tracker feeds RF from two physically separate opposite-corner contacts: single-contact **J6 VHF** → SMA_APRS **J3** center and single-contact **J7 HF** → SMA_WSPR **J4** center; both SMA shields return to board GND. Keep each RF run short and inside the ≥ 5 mm keepout; the contacts must not be collapsed into a two-pin header.

## 4. UI (operator)

- **SW1:** mechanical pack on/off; breaks pack+. Required by brief.
- **Write LED:** on **this** board. 3V3 → series **1 kΩ** → D1 → U1 P0; firmware drives P0 low for activity and high/off otherwise. PCF8574T ports power up high, so reset defaults the LED off. This is an activity proxy, not proof of physical SD commit. P1–P7 remain reserved for future GPS-status LEDs. OFF leakage ≤ 1 µA; U1 maximum idle current must be ≤100 µA.

No other user LEDs this stage (extra Iq).

## 5. Cutdown

Nichrome burn wire severs payload-from-balloon cord at max altitude. Load **ASSUMED ≤ 2 A** burst for ≤ 30 s; FET and traces must carry this.

- **Switch:** low-side **logic-level MOSFET** fully enhanced at **3.3 V Vgs**. Gate pulldown is **intentional** (a missing pulldown looks like a mistake; a floating gate can false-fire nichrome). Default-off on host reset/strap default is required.
- **IRLZ44N:** Rds(on) is specified at **5 V Vgs**; at 3.3 V it may not be fully on. **Not committed.** Do not silently use it. A 3.3 V opto relay module is also **not committed** (coil Iq + vibration vs a specified logic-level FET).
- **High-side nichrome:** out of spec unless an explicit later decision.
- **Connector:** 2-pin nichrome, away from SMA keepout.
- OFF leakage ≤ 50 µA at max pack voltage.

## 6. Mechanical / environment

SMA perpendicular to board, mates pointing down. Temperature **ASSUMED −40 °C to +40 °C**; L91 chosen because alkaline fails cold. Mass/outline unspecified (fit under typical HAB foam). Conformal coat / enclosure out of scope. Battery holder is off-board (3AA class, or 4AA if voltage requires it); keep pack metal out of SMA near-field.

**LightAPRS-W 2.0 module mounting (verified from qrp-labs.com + repo pinout image).** The module is **32 mm × 55 mm** (portrait, plus a small antenna tab at the top edge), ~4.6 g, SMD on both sides. To mount it on this carrier, reserve a **32 × 55 mm module keepout** with standoff/component-height clearance and keep the SMA jacks (J3/J4), pack input (J1), switch (SW1), OpenLog (A1), and cutdown (Q1) out of that footprint. The 80 × 70 mm PCB now contains a coordinate-level 32 × 55 mm reservation from (124,101) to (156,156), with J2 on the long edge, J6/J7 at opposite bottom corners, and four approximate M2 standoff holes inside; all other components are outside. Exact connector alignment, underside clearance, orientation, and hole coordinates remain UNVERIFIED against the physical module, so this is not a fabrication release.

Verified module connector geometry (for header placement / mating):
- **Interface header:** a single **2.54 mm-pitch row along one long edge**, 11 positions in order: `RAW(VBAT)`, `GND`, `A1/AIN2 (PB08)`, `A2/AIN3 (PB09)`, `3V3`, `GND`, `SCL (PA23)`, `SDA (PA22)`, `SCK (PB11)`, `MISO (PA12)`, `MOSI (PB10)`. This carries VIN (RAW), 3V3, GND, the free UART pins (PB08/PB09 = SERCOM4), and the shared I2C/SPI buses.
- **RF pins:** `HF` (WSPR) at one bottom corner and `VHF` (APRS) at the other bottom corner, with an `HF GND` pad near the top-left. These are separate schematic contacts: J6 VHF→J3 APRS and J7 HF→J4 WSPR.
- **USB micro-B** on the opposite long edge (keep accessible if in-field reflash is wanted).
- **Mounting holes:** exact pattern not officially published; at least one hole near top-center. Reserve corner standoff holes (≈M2) pending confirmation from the physical board.

The schematic/BOM now match the verified model: one 11-position J2 edge header plus separate J6 VHF and J7 HF corner contacts. All three footprints remain UNVERIFIED until aligned to the physical module and its keepout.

## 7. Intentional absences

| Missing block | Why the absence is intentional |
| --- | --- |
| Second MCU | Firmware lives on LightAPRS-W 2.0 |
| Carrier RTC | Host RTC/GPS time is enough |
| USB-serial bridge | OpenLog is the logger; ATSAMD21G18 programming stays on the tracker |
| L91 charger | Primary cells |
| 5 V USB as flight source | Pack is the flight source; switch-off budget is 0 µA on pack+ |
| IRLZ44N / 3.3 V relay | Vgs/Iq not proven; pick a FET specified on at 2.5–3.3 V Vgs later |
| Host RX / extra direct LED GPIO | OpenLog is one-way; A1/PB08 is UART_TX, A2/PB09 is cutdown, and shared I2C plus U1 supplies LED outputs without another dedicated GPIO |
| On-board GPS, APRS PA | Those are the LightAPRS-W 2.0 module |
| High-side cutdown | Not decided |
| Cell paralleling | Not in brief; not assumed |

## 8. Constraint map

| Key | Bound | Where it bites architecture |
| --- | --- | --- |
| `flight.duration_h` | min 4 | Continuous GPS + radios; no in-flight deep-sleep budget |
| `power.pack_chemistry` | L91 AA Li-FeS2 | Holder and pack net only |
| `power.series_cells` | min 3, max 4 | 3s unless UVLO forces 4s |
| `power.pack_voltage_V` | 3.0–7.2 V | VIN, FET Vds, OpenLog must not sit on raw 4s if 3V3 exists |
| `power.mean_flight_current_mA` | max 200 | Mean energy; TX peaks allowed |
| `power.flight_energy_mAh` | min 1600 usable | Do not upsize cell count for mAh |
| `power.switch_off_current_uA` | max 0 | SW1 breaks pack+ |
| `power.board_added_idle_mA` | max 2 | OpenLog ≤1.85 mA + U1 ≤0.10 mA + other leakage ≤0.05 mA |
| `power.openlog_idle_mA` | max 1.85 | Tightened after adding U1 |
| `power.led_expander_idle_uA` | max 100 | PCF8574T selection and qualification |
| `power.cutdown_off_leakage_uA` | max 50 | FET selection |
| `power.led_off_leakage_uA` | max 1 | LED circuit |
| `power.gpio_logic_V` | 3.3 | No pack-driven gates/LEDs |
| `openlog.vcc_V` | 3.3–12 | Tie 3V3 unless LDO share exceeded |
| `antenna.connector` | SMA 50 Ω ×2 downward | Two jacks |
| `antenna.keepout_mm` | min 5 | SMA vs pack metal / nichrome |
| `cutdown.load_current_A` | max 2 burst | FET and traces |
| `cutdown.vgs_fully_on_V` | fully on at 3.3 V Vgs | IRLZ44N not auto-approved |
| `power.strap_leakage_uA` | max 50 | No GPIO until strap table |
