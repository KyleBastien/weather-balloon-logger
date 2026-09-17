# Subsystems — Weather Balloon Logger harness

Carrier PCB only. Firmware, GPS, and radios live on LightAPRS-W 2.0. This document freezes the block diagram and per-subsystem budgets. Stage 4 checked the LightAPRS-W 2.0 (ATSAMD21G18) occupied-pin map and records the final two-GPIO allocation in `docs/PINOUT.md`.

## Prose block diagram

Exactly three series Energizer L91 AA cells (3.0–5.4 V) feed pack+ through a mechanical switch **SW1 that breaks pack positive**. Switched `PACK_SW` goes directly to LightAPRS-W 2.0 **RAW** on J2.1 and directly to cutdown J5.1; neither path may pass through a regulator. A dedicated Pololu S7V8F5 item 2123 takes VIN and SHDN from `PACK_SW`, shares GND, and creates fixed `LOGGER_5V` from VOUT for OpenLog A1 VCC only. The tracker’s regulated **3V3** continues to power U1 PCF8574T and the write-activity path 3V3 → 1 kΩ → LED → U1 P0; P0 is active-low and powers up high/off. A2/PB09 drives the cutdown MOSFET gate through R2 with an **intentional pulldown** to GND so nichrome cannot false-fire on reset. A1/PB08 provides one-way SERCOM4 UART TX to OpenLog RXI; OpenLog TXO is intentionally unused. J2.7/J2.8 expose the shared SCL/SDA bus to U1 at address 0x20; P1–P7 are reserved no-connect outputs for future GPS-status LEDs. Two **50 Ω SMA jacks** take RF from separate opposite-corner module contacts: J6 VHF→J3 APRS and J7 HF→J4 WSPR. No second MCU, carrier RTC, USB-serial bridge, L91 charger, or 5 V flight source is added.

```text
L91 exactly 3s --pack+--> SW1 --PACK_SW--> LightAPRS-W RAW/J2.1 (continuous GPS)
                                      +---------> J5.1 cutdown high side
                                      +---------> S7V8F5 VIN+SHDN --LOGGER_5V--> OpenLog A1 VCC
LightAPRS 3V3 ----------------------------------> U1 + LED anode path
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
| Topology | Exactly 3 series L91 cells | Fixed approved architecture; series cells do not add mAh |
| Pack voltage | 3.0–5.4 V | Fixed 3s EOD–fresh range |
| Host and cutdown feeds | LightAPRS RAW/J2.1 and cutdown J5.1 directly on switched `PACK_SW` | Continuous GPS and the 2 A cutdown path must not pass through the logger regulator |
| Logger supply | Pololu S7V8F5 item 2123, 2.7–11.8 V input, fixed 5 V output | VIN+SHDN on `PACK_SW`, VOUT=`LOGGER_5V`, GND common; OpenLog only |
| Mean pack current | ≤ 200 mA over 4 h | GPS on + ATSAMD21G18 + OpenLog + APRS/WSPR TX duty; peaks do not relax the mean |
| Flight energy | Four-hour demand ≤800 mAh; usable pack ≥1600 mAh under the actual cold/load profile | Fixed 3s L91 requires measured capacity qualification at the real temperature and mission load |
| Switch OFF | **0 µA** (ideal) except holder/switch leakage | SW1 **must break pack+**; any always-on divider on pack+ is a budget bug |
| Board-added idle | ≤ **8 mA** beyond LightAPRS-W 2.0 | Includes OpenLog idle ≤7 mA, U1 ≤100 µA, S7V8F5 Iq <0.2 mA, and leakage margin |
| Board-added active/write peak | ≤ **30 mA** beyond LightAPRS-W 2.0 | Includes OpenLog write ≤25 mA and regulator/U1/margin |
| Cutdown OFF leakage | ≤ **50 µA** at max pack V | FET Idss / relay off |
| LED OFF leakage | ≤ **1 µA** | No bleed path that looks like a glow |
| Strap leakage | ≤ **50 µA** total extra | Pull-ups/downs on host GPIOs |
| Logic rail | **3.3 V** from tracker 3V3, not raw pack | GPIO, LED, FET gate |
| OpenLog VCC | Fixed **5 V** on `LOGGER_5V` from S7V8F5 | Dedicated OpenLog-only rail; A1 no longer loads LightAPRS 3V3 |
| S7V8F5 module | 0.1-inch four-pin direct-solder straight header; no reverse-polarity protection; temperature rating unverified | Enforce pack polarity and require cold qualification |

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

OpenLog is powered only from `LOGGER_5V` and is limited to ≤7 mA idle and ≤25 mA during writes. The S7V8F5 must remain below 0.2 mA quiescent current; board-added current is limited to ≤8 mA idle and ≤30 mA active/write peak beyond LightAPRS. U1 remains on LightAPRS 3V3 with its ≤100 µA limit, and all existing safety leakage limits remain in force. The regulator module has no reverse-polarity protection and an unverified temperature rating, so polarity control and cold qualification are mandatory.

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

**LightAPRS-W 2.0 module mounting (verified from the vendor dimensioned drawing).** Sources: pinout `github.com/lightaprs/LightAPRS-W-2.0/blob/main/images/lightaprs-w-2-0-pinout.png` and dimensions `.../lightaprs-w-2-0-dimensions.png`. Exact board outline is **54.80 mm (long) × 32.77 mm (short)**, ~4.6 g, SMD both sides, with a small antenna-feed tab on one end. **Mounting orientation: the module mounts FACE UP** — its component/top side faces away from the carrier and its pins pass down into the carrier — so the carrier's mating pads must reproduce the module's **top-view** geometry **directly, with NO left-right mirror**. Reserve a **32.77 × 54.80 mm** module zone (long axis vertical) with standoff/component-height clearance; keep the SMA jacks, pack input, switch, OpenLog, PCF8574 (U1), and cutdown hardware outside it.

Verified connector/mechanical geometry (top view, module face-up):
- **Interface header:** single row, **2.5480 mm** pitch, 11 positions on the module's long edge (2 larger VBAT/GND power pads + 9 signal), order `RAW(VBAT), GND, A1/AIN2 (PB08), A2/AIN3 (PB09), 3V3, GND, SCL (PA23), SDA (PA22), SCK (PB11), MISO (PA12), MOSI (PB10)`. Carrier J2 sits on the zone edge matching the module's header edge.
- **RF contacts:** `HF` (WSPR) at the **bottom-left** corner and `VHF` (APRS) at the **bottom-right** corner (top view), plus a dedicated `HF GND` pad near the top-left. Carrier mapping: **J7 HF (bottom-left) → J4 WSPR; J6 VHF (bottom-right) → J3 APRS.** The two SMA jacks are edge-mounted with mates **facing down** through the payload.
- **USB micro-B** on one long edge; keep accessible if in-field reflash is wanted.
- **Mounting holes:** four holes, fully dimensioned in the drawing (outer horizontal span ≈ **42.73 mm**); use `≈M2` standoffs and transcribe exact hole XY from `lightaprs-w-2-0-dimensions.png` at footprint creation. Reference spacings on the drawing: 5.51 / 2.86 / 5.51 mm (left pad groups), 7.00 / 3.60 / 2.82 / 5.97 mm (top), 4.33 / 2.84 / 5.97 mm (bottom-right), 2.00 / 1.29 mm (top-left), 0.98 mm (antenna tab).

**Correction to prior layout:** the earlier 32 × 55 mm zone with J2 on the left edge and VHF bottom-left / HF bottom-right assumed a mirrored (face-down) mount and is **superseded**. For the FACE-UP module, resize the zone to **32.77 × 54.80 mm**, put J2 on the edge matching the module header, place **HF bottom-left (J7) and VHF bottom-right (J6)**, and route SMAs accordingly (APRS/J3 toward the VHF side, WSPR/J4 toward the HF side).

**Measured coordinate transcription** (from `lightaprs-w-2-0-dimensions.png` by image analysis; overall dims and the 2.548 mm pitch are exact from the drawing labels, derived coordinates ≈ ±0.3 mm — refine against the vendor drawing at footprint creation). Module own frame: rectangular **body 42.73 mm (long) × 32.77 mm (short)**, with the antenna tab occupying the remaining **12.07 mm** of the 54.80 mm long axis.
- **4 mounting holes** (≈M2, ~2.2 mm dia) inset **≈2.28 mm** from the body corners → hole rectangle **38.16 mm (long) × 28.18 mm (short)**.
- **11-pin header:** 2.548 mm pitch along one long edge, ~1.8 mm from that edge, ~25.48 mm total span centered on the body length.
- **HF/VHF** RF contacts at the two corners of the short edge opposite the tab.

Carrier placement (zone x 123.615–156.385, y 101–155.8; module **face-up**, long axis vertical, antenna tab at the top edge y≈101, rectangular body y≈113.07–155.8):
- Mounting holes: **H1 (125.9, 115.35), H2 (154.1, 115.35), H3 (125.9, 153.52), H4 (154.1, 153.52)** — ≈M2, 28.18 mm (x) × 38.16 mm (y) rectangle.
- **J2** 11-pin header: right edge x≈154.9, y ≈121.7→147.2, 270°, 2.548 mm pitch.
- **J7 HF** bottom-left ≈(125.9, 154.5) → J4 WSPR; **J6 VHF** bottom-right ≈(154.1, 154.5) → J3 APRS.

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
| `power.series_cells` | exactly 3 | Fixed 3s architecture |
| `power.pack_voltage_V` | 3.0–5.4 V | LightAPRS RAW and J5.1 remain directly on `PACK_SW`; S7V8F5 input is compatible |
| `power.mean_flight_current_mA` | max 200 | Mean energy; TX peaks allowed |
| `power.flight_energy_mAh` | min 1600 usable | Do not upsize cell count for mAh |
| `power.switch_off_current_uA` | max 0 | SW1 breaks pack+ |
| `power.board_added_idle_mA` | max 8 | OpenLog idle ≤7 mA + U1 ≤0.10 mA + S7V8F5 Iq <0.2 mA + margin |
| `power.board_added_active_peak_mA` | max 30 | Logger active/write peak beyond LightAPRS |
| `power.openlog_idle_mA` | max 7 | Dedicated `LOGGER_5V` load |
| `power.openlog_write_mA` | max 25 | OpenLog write qualification |
| `power.logger_regulator_iq_mA` | max 0.2 | S7V8F5 quiescent-current ceiling |
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
