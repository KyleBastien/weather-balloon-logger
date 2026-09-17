# Tasks

- [x] Read the current PCB text and identify exact A1/C1/C2 UART/power copper, placement openings, keepouts, exclusions, and unique edit anchors.
- [x] Add and place A2/R4 without moving existing footprints; move only the nonfunctional board label if strictly necessary.
- [x] Remove stale OpenLog 3V3/direct-UART copper and route PACK_SW, GND, LOGGER_5V, UART_TX, and OPENLOG_RXI with practical widths and short loops.
- [x] Confirm J2.1 and J5.1 remain directly on PACK_SW and no cutdown path passes through A2.
- [x] Update layout/audit/decision/changelog/OpenSpec documentation with one-line rationales and actual coordinates/routing.
- [x] Run normal DRC to zero violations and zero unconnected items; run ERC, schematic legibility, drift, and all Copperhead completion checks.
- [x] Commit/finish only when schematic, PCB, BOM, and docs agree.
