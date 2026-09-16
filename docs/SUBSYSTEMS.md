# Subsystems — Weather Balloon Logger harness

Carrier PCB only. Firmware, GPS, and radios live on LightAPRS-W 2.0. This document freezes the block diagram and per-subsystem budgets before schematic. No GPIO is assigned until the LightAPRS-W 2.0 / ESP32 strapping table is checked (`docs/PINOUT.md` does not exist yet; that absence is intentional).

## Prose block diagram

Energizer L91 AA cells in a **3s baseline** holder (4s only if host VIN/UVLO cannot run to 3s EOD 3.0 V) feed pack+ through a mechanical switch **SW1 that breaks pack positive**. Switched pack+ goes to LightAPRS-W 2.0 **VIN**. The tracker’s regulated **3V3** fans out on this board to OpenLog VCC, the write-activity LED (GPIO → 1 kΩ → LED → GND), and the cutdown MOSFET gate (GPIO → gate, **intentional pulldown** to GND so nichrome cannot false-fire on reset). Cutdown is a **low-side** FET: nichrome 2-pin jack between switched pack+ and FET drain; source to GND. Host UART TX (and optional RX) go to OpenLog RX/TX with common GND. Two **50 Ω SMA jacks** on this board, mates pointing **downward**, take APRS and WSPR RF from the tracker’s bottom **VHF** (APRS) and **HF** (WSPR) pins via a 2-pin host RF header **J6** (VHF→SMA_APRS J3, HF→SMA_WSPR J4) (short RF path; **≥ 5 mm** keepout from SMA dielectric; no battery metal in the near field). No second MCU, no carrier RTC, no USB-serial bridge, no L91 charger, no 5 V USB as a flight source.

```text
L91 3s (4s iff UVLO) --pack+--> SW1 --VIN--> LightAPRS-W 2.0 --3V3--> OpenLog, LED, FET gate
                                      GND common
Host UART TX/RX <------------------> OpenLog RX/TX
Host GPIO (unassigned) ------------> LED + series R; FET gate + pulldown
Pack+ --nichrome jack--> FET drain; FET source --> GND
LightAPRS-W VHF/HF pins --(J6 RF hdr)--> SMA_APRS (VHF,J3) + SMA_WSPR (HF,J4) (downward, 50 Ω)
```

## 1. Power

| Item | Value | Why |
| --- | --- | --- |
| Chemistry | L91 AA Li-FeS2 | SPEC §2.1; alkaline forbidden (cold); LiPo 1S forbidden |
| Topology | 3s baseline, 4s only for VIN/UVLO | Series does not add mAh; 3s meets ≥1600 mAh usable vs 800 mAh flight load |
| Pack voltage | 3s 3.0–5.4 V; 4s 4.0–7.2 V | Fresh ≤1.8 V/cell, EOD ≥1.0 V/cell; combined bound 3.0–7.2 V |
| Host VIN | ASSUMED 3.5–12 V class | **Unconfirmed** from LightAPRS-W 2.0 docs; if 3s EOD 3.0 V is below UVLO, use 4s — do not add cells for amp-hours |
| Mean pack current | ≤ 200 mA over 4 h | GPS on + ESP32 + OpenLog + APRS/WSPR TX duty; peaks do not relax the mean |
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

LightAPRS-W 2.0 (QRP Labs, ESP32) is the **only** MCU. It hosts all flight firmware, GPS, APRS, and WSPR. This PCB is a harness: power, connectors, OpenLog + write LED, cutdown switch, dual SMA.

- **RTC on this carrier:** not required; host RTC/GPS time is sufficient. Absence is intentional.
- **Strapping:** check LightAPRS-W 2.0 / ESP32 strapping table **before any harness GPIO** (boot, log UART, cutdown, LED). Forbidden: pins that hold download mode or disable flash at reset; cutdown on a pin that glitches high at boot.
- **UART:** OpenLog must use a free UART or documented TX pin; do not steal the GPS UART.
- **No PINOUT this stage:** no GPIO assigned until that table is read.

## 3. Connectivity

### 3.1 UART SD logger

SparkFun OpenLog (ATmega328, headers). Host TX → OpenLog RX; host RX optional for commands; GND common. UART is 3.3 V; no 5 V shifter. Absence of a USB-serial bridge on this PCB is intentional — programming the ESP32 stays on LightAPRS-W 2.0.

OpenLog idle current counts toward **board-added ≤ 2 mA**. If 3V3 LDO current share cannot cover OpenLog, stop and revisit the 3V3 tie rather than silently moving OpenLog to raw pack (especially 4s fresh 7.2 V).

### 3.2 Antennas

Two SMA jacks, 50 Ω, mates facing **downward** through the payload. One SMA **APRS** (typically 2 m), one SMA **WSPR** (HF as built on LightAPRS-W 2.0). Keep RF path short. Board keepout **≥ 5 mm** from SMA dielectric; no battery metal in the near-field of the jacks. Nichrome connector stays out of that keepout.

The tracker feeds RF from its two bottom-edge pins — **VHF** (APRS) and **HF** (WSPR) — into a 2-pin host RF header **J6** on this board: J6 pin 1 (VHF) → SMA_APRS **J3** center, J6 pin 2 (HF) → SMA_WSPR **J4** center; both SMA shields return to board GND. Keep each RF run short and inside the ≥ 5 mm keepout.

## 4. UI (operator)

- **SW1:** mechanical pack on/off; breaks pack+. Required by brief.
- **Write LED:** on **this** board (not only OpenLog module LEDs). 3.3 V GPIO → series **1 kΩ** (ASSUMED) → LED → GND; If **≤ 3 mA**. Flashes only on SD write (firmware or OpenLog write-activity line; if no dedicated pin, host GPIO toggled in the same code path as the log write). Do not hang the LED on unregulated pack. OFF leakage ≤ 1 µA.

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

## 7. Intentional absences

| Missing block | Why the absence is intentional |
| --- | --- |
| Second MCU | Firmware lives on LightAPRS-W 2.0 |
| Carrier RTC | Host RTC/GPS time is enough |
| USB-serial bridge | OpenLog is the logger; ESP32 programming stays on the tracker |
| L91 charger | Primary cells |
| 5 V USB as flight source | Pack is the flight source; switch-off budget is 0 µA on pack+ |
| IRLZ44N / 3.3 V relay | Vgs/Iq not proven; pick a FET specified on at 2.5–3.3 V Vgs later |
| GPIO assignments / PINOUT.md | Strapping table not yet applied |
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
| `power.board_added_idle_mA` | max 2 | OpenLog idle + LED off + FET off |
| `power.cutdown_off_leakage_uA` | max 50 | FET selection |
| `power.led_off_leakage_uA` | max 1 | LED circuit |
| `power.gpio_logic_V` | 3.3 | No pack-driven gates/LEDs |
| `openlog.vcc_V` | 3.3–12 | Tie 3V3 unless LDO share exceeded |
| `antenna.connector` | SMA 50 Ω ×2 downward | Two jacks |
| `antenna.keepout_mm` | min 5 | SMA vs pack metal / nichrome |
| `cutdown.load_current_A` | max 2 burst | FET and traces |
| `cutdown.vgs_fully_on_V` | fully on at 3.3 V Vgs | IRLZ44N not auto-approved |
| `power.strap_leakage_uA` | max 50 | No GPIO until strap table |
