# Tasks

- [x] Read the current schematic and intent anchors and confirm installed connector/resistor pin contracts.
- [x] Add and group A2 in Power and R4 in UART SD logger without disturbing existing interfaces or no-connects.
- [x] Rewire the OpenLog supply/bypass nodes to `LOGGER_5V` and its receive input to `OPENLOG_RXI`.
- [x] Synchronize BOM, PINOUT, SPEC/SUBSYSTEMS/DEVPLAN/LAYOUT/FOOTPRINT_AUDIT as applicable, CHANGELOG, DECISIONS, and this run's OpenSpec tasks while truthfully deferring PCB work.
- [x] Verify symbols, run ERC, schematic legibility/score, unchanged-board DRC, and drift; reconcile every blocking finding.
- [x] Finish only when electrical checks are clean and the PCB deferral is explicit.
