# Tasks

- [ ] Read the current PCB anchors, import script, audit, and baseline DRC report.
- [ ] Repair Q1 pad 1 CUTDOWN_GATE and pad 2 GND routing with no shorts, hole-clearance, or solder-mask errors.
- [ ] Adjust only necessary routing/vias near U1 pads 4 and 15.
- [ ] Add narrowly scoped H3/J7 and H4/J6 courtyard exclusions and document why the physical vendor features are valid despite stock courtyard overlap.
- [ ] Resolve A1/C1 reference-text overlap and J6 silk-over-hole warnings without moving footprints.
- [ ] Run DRC/connectivity, inspect every remaining finding, and iterate to zero unsuppressed errors.
- [ ] Run ERC and drift checks, record decisions, update changelog/audit, and commit the bounded pass if the available workflow exposes commit support.
