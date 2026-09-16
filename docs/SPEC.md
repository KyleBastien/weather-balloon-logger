# Specification — Weather Balloon Logger

Carrier board that integrates a LightAPRS-W 2.0 tracker with flight-pack power, dual SMA antennas, UART SD logging, a write-activity LED, and a nichrome cutdown driver. Firmware lives on the LightAPRS-W 2.0 (ATSAMD21G18 / ARM Cortex-M0). This board is the harness, not a second MCU.

## 1. Device and architecture

| Item | Requirement |
| --- | --- |
| Host | LightAPRS-W 2.0 (QRP Labs), ATSAMD21G18 (ARM Cortex-M0), hosts all flight firmware. Rationale: brief names this as brains. |
| Role of this PCB | Power distribution, connectors, OpenLog + write LED, cutdown switch, downward SMA. No competing MCU. |
| Flight duration | **≥ 4 h** continuous GPS + APRS + WSPR for the whole flight. Source: brief “~4 hour flight”. |
| Logging | SparkFun OpenLog (ATmega328, headers), UART from host, post-flight SD analysis. |
| Cutdown | Nichrome burn wire severs payload-from-balloon cord at max altitude; driven from this board. |
| Operator control | Mechanical pack on/off switch. Rationale: brief requires on/off for the battery array. |

## 2. Power and energy budget

### 2.1 Cells and pack

| Parameter | Value | Status |
| --- | --- | --- |
| Chemistry | Energizer L91 Ultimate Lithium AA (Li-FeS2) | Stated |
| Topology | Series string, **3 cells baseline**, **4 cells allowed** if host VIN or regulator dropout needs it | 3-cell holder is brief intent; “maybe bigger if needed” → 4-cell is the only upsizing path |
| Holder | 3AA case (e.g. Amazon B07M7WYZ32 class) or 4AA if voltage requires it | Stated / ASSUMED size |
| Per-cell voltage | Fresh ≤ **1.8 V**, nominal **1.5 V**, end-of-discharge **≥ 1.0 V** (do not discharge L91 into reversal) | ASSUMED from L91 datasheet class |
| Pack voltage **3s** | **3.0–5.4 V** (EOD–fresh) | ASSUMED |
| Pack voltage **4s** | **4.0–7.2 V** (EOD–fresh) | ASSUMED |
| Host VIN | Must accept the chosen pack range without exceeding LightAPRS-W 2.0 absolute max. **ASSUMED 3.5–12 V** class input on the tracker; **if 3s EOD 3.0 V is below tracker UVLO, use 4s**. | ASSUMED — confirm from LightAPRS-W 2.0 docs before layout |

**Forbidden:** alkaline AA/AAA, LiPo 1S as the flight pack (brief specifies L91), and paralleling cells without per-string fusing (not in brief; not assumed).

### 2.2 Energy (continuous GPS, 4 h)

| Parameter | Value | Status |
| --- | --- | --- |
| GPS mode | Continuous for the entire flight (not 1-Hz duty-cycled off) | Stated |
| ASSUMED average pack current | **≤ 200 mA** mean over 4 h (GPS on + ATSAMD21G18 + OpenLog + APRS/WSPR TX duty). Peak TX may exceed this; peaks do not relax the mean. | ASSUMED |
| Energy at 4 h | 200 mA × 4 h = **800 mAh** at pack current | Derived |
| L91 usable capacity | **≥ 1500 mAh** after **ASSUMED 50% cold/high-altitude derate** from ~3000 mAh class | ASSUMED |
| Design margin | Usable pack capacity **≥ 2×** flight energy → **≥ 1600 mAh** required vs 800 mAh load | ASSUMED budget |
| Verdict | **3s L91 meets capacity** (series does not add mAh; 1500–3000 mAh >> 800 mAh). Upsize cell **count** only for **voltage**, not for amp-hours. | Decision |

### 2.3 Quiescent / leakage (pre-flight and cutdown-off)

This vehicle is **GPS-on for the whole powered flight**; there is **no in-flight deep-sleep current budget**. Leakage still matters on the pad with the switch on and cutdown idle, and for any always-connected divider.

| Parameter | Value | Status |
| --- | --- | --- |
| Switch OFF pack current | **0 µA** except holder/switch leakage. Switch must **break the pack positive**. | ASSUMED |
| Switch ON, radios idle, cutdown OFF, GPS as firmware sets | Board-added Iq (LED off, MOSFET off, OpenLog idle) **≤ 2 mA** beyond the LightAPRS-W 2.0 module itself | ASSUMED |
| Cutdown MOSFET/relay OFF leakage | **≤ 50 µA** at max pack voltage | ASSUMED |
| Write LED OFF leakage | **≤ 1 µA** (no bleed path that looks like a glow) | ASSUMED |
| Pull-ups/downs on host GPIOs | Must not violate LightAPRS-W 2.0 strapping; extra leakage through straps **≤ 50 µA** total | ASSUMED — **check MCU strapping table before any pin** |

**A part that fits voltage/package but blows Iq is a bug.** Gate pulldown on the cutdown FET is **intentional** (missing pulldown looks like a mistake but a floating gate can false-fire nichrome).

### 2.4 Logic and rails on this board

| Rail | Value | Status |
| --- | --- | --- |
| GPIO / LED / FET gate | **3.3 V** logic, sourced from LightAPRS-W 3V3 (or equivalent regulated 3.3 V), not raw pack | ATSAMD21G18, 3.3 V |
| OpenLog VCC | **3.3–12 V** allowed by module; **tie to 3.3 V** unless current share on the 3V3 LDO is exceeded | Stated range; 3.3 V tie ASSUMED |
| OpenLog UART | 3.3 V one-way host TX → OpenLog RXI; OpenLog TXO is intentionally unused; no 5 V shifter | Stage-4 pin-budget decision |
| LED | 3V3 → **1 kΩ** → LED → UART_TX. UART idle-high is OFF; low UART bits sink **≤ 3 mA**, so each transmitted log record visibly flashes without a third GPIO. | Stage-4 pin-budget decision; activity proxy is not physical SD-commit proof |

Do **not** feed OpenLog or the LED from unregulated 4s (~7.2 V fresh) if a 3.3 V rail already exists — extra dissipation and LED overstress.

## 3. Antennas

| Item | Requirement | Status |
| --- | --- | --- |
| Radios | APRS **and** WSPR for the entire flight | Stated |
| Connectors | **Two SMA** (jacks) on this board, **facing downward** so coax/antennas run through the payload | Stated |
| Mapping | One SMA **APRS** (typically 2 m), one SMA **WSPR** (HF; LightAPRS-W 2.0 band as built) | ASSUMED split |
| Keepout | Copper/parts keepout around SMA center pins and keep RF path short; no battery metal in the near-field of the jacks **ASSUMED ≥ 5 mm** board keepout from SMA dielectric | ASSUMED |
| Impedance | **50 Ω** SMA | ASSUMED |

## 4. SD logger and write LED

| Item | Requirement |
| --- | --- |
| Module | SparkFun OpenLog with headers (ATmega328, preprogrammed), example Amazon B0BHL56BP5 |
| Interface | One-way UART: host A1/PB08 SERCOM4 TX → OpenLog RXI; OpenLog TXO is intentionally no-connect; GND common |
| Power | OpenLog VCC within 3.3–12 V; see §2.4 |
| Write LED | On **this** board (not only module LEDs). 3V3 → 1 kΩ → LED → UART_TX makes UART idle-high the OFF state and flashes on low bits of every transmitted log record. This preserves the requested visual activity check with the two confirmed free GPIOs; it is intentionally a transmit proxy rather than proof of physical SD commit |
| Absence of USB-serial bridge on this PCB | **Intentional** — OpenLog is the logger; programming the ATSAMD21G18 stays on LightAPRS-W 2.0 |

## 5. Cutdown (nichrome)

| Item | Requirement | Status |
| --- | --- | --- |
| Load | Nichrome wire heats and burns a cord at max altitude | Stated |
| Switch | Low-side driver preferred: **logic-level MOSFET**, not a 3.3 V relay module, unless FET cannot be fully enhanced at 3.3 V Vgs | ASSUMED (relay coil Iq and vibration) |
| Brief examples | IRLZ44N TO-220 (Amazon B0CBKH4XGL) **or** 3.3 V opto relay (B0D8PSX9WL) | Stated options |
| IRLZ44N at 3.3 V Vgs | **Constraint:** IRLZ44N Rds(on) is specified at **5 V Vgs**; at **3.3 V it may not be fully on**. Do **not** commit IRLZ44N until Vgs(th)/Rds(on) at 3.3 V is shown acceptable **or** pick a FET specified on at 3.3 V (e.g. logic-level with Rds(on) max at Vgs=2.5–3.3 V). | ASSUMED risk — **stop rather than silently use IRLZ44N** |
| Cutdown current | **ASSUMED ≤ 2 A** burst for ≤ 30 s; FET/relay and trace must carry this | ASSUMED |
| Default-off | Gate/input **pulldown**; cutdown **must not** fire on host reset or strap default | Required |
| Connector | 2-pin for nichrome, away from SMA keepout | ASSUMED |

## 6. Pin and strapping rules (host)

LightAPRS-W 2.0 (ATSAMD21G18 / ARM Cortex-M0) breaks out only "I2C, SPI, 2× Analog"; most GPIO are already used by GPS, the Si4463/Si5351 radios, and flash.

- **MCU is ATSAMD21G18, not ESP32:** the SAMD21 has no ESP32-style GPIO boot straps (no GPIO0/2/12/15 rules). It boots from internal flash; the bootloader is a double-tap on RESET; SWDIO/SWCLK/RESET are not on the extension header. The governing rule is the verified occupied-pin map, not strap avoidance.
- **Occupied (do not reuse):** D0/D1 GPS UART, D3 VHF PTT, D4 Si4463 SDN, D7 GPS power, D8 Si4463 nSEL, D9 Si4463 nIRQ, A3 Si5351 power, A4 TCXO power, A5 battery sense; SDA/SCL (I2C: BMP180 + Si5351); MOSI/MISO/SCK (SPI: Si4463).
- **Available (extension header):** A0, A1 free GPIO/analog (A1=PB08 SERCOM4-capable, A2=PB09 if broken out), plus the shared I2C and SPI buses.
- **Cutdown default-off** via gate pulldown is still required (a floating gate can false-fire nichrome on reset).
- OpenLog uses one-way firmware SERCOM4 UART TX on exposed A1/PB08; do not steal the GPS UART (D0/D1), and do not assume A2 is exposed.
- A0 drives CUTDOWN_CTRL through R2; the intentional R3 pulldown keeps Q1 off during reset. UART_TX also sinks the write LED, so the design uses exactly the two confirmed free GPIOs.
- RTC: **not required** on this carrier (host RTC/GPS time is sufficient). Absence of a carrier RTC is **intentional**.

The authoritative connector and component pin table is `docs/PINOUT.md`; J2 pins 5–6 and A1 pins 1, 4, and 6 are intentional no-connects.

## 7. Mechanical / environment

| Item | Value | Status |
| --- | --- | --- |
| SMA orientation | Perpendicular to board, **mates pointing down** (through payload) | Stated |
| Temperature | **ASSUMED −40 °C to +40 °C** (ascent to burst). L91 chosen because alkaline fails cold. |
| Conformal / enclosure | Out of scope for this spec seed | — |
| Mass / outline | Unspecified; **ASSUMED** fit under a typical HAB payload foam; no kg budget stated | ASSUMED unspecified |

## 8. What this spec does **not** include (intentional)

- On-board MCU, GPS, or APRS PA — those are the LightAPRS-W 2.0 module.
- Charging circuitry — primary L91 cells.
- 5 V USB power as a flight source.
- High-side nichrome without an explicit later decision.
- `openspec/` capability specs — not seeded unless that tree already exists.

## 9. Constraint index (must match `record_constraint`)

| Key | Bound |
| --- | --- |
| `flight.duration_h` | min 4 |
| `power.pack_chemistry` | L91 AA Li-FeS2 |
| `power.series_cells` | min 3, max 4 |
| `power.pack_voltage_V` | 3.0–7.2 (covers 3s and 4s) |
| `power.mean_flight_current_mA` | max 200 |
| `power.flight_energy_mAh` | min usable 1600 after derate (2× 800 mAh) |
| `power.switch_off_current_uA` | max 0 (ideal; switch breaks pack+) |
| `power.board_added_idle_mA` | max 2 (excluding LightAPRS-W 2.0) |
| `power.cutdown_off_leakage_uA` | max 50 |
| `power.led_off_leakage_uA` | max 1 |
| `power.gpio_logic_V` | 3.3 |
| `openlog.vcc_V` | 3.3–12 |
| `antenna.connector` | SMA 50 Ω, two jacks, downward |
| `antenna.keepout_mm` | min 5 (ASSUMED, SMA dielectric) |
| `cutdown.load_current_A` | max 2 burst |
| `cutdown.vgs_fully_on_V` | must be valid at 3.3 V (IRLZ44N not auto-approved) |
| `power.strap_leakage_uA` | max 50 extra through host straps |
