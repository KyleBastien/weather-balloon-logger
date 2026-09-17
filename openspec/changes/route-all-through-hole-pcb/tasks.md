# Tasks

- [ ] Inspect the current PCB footprints, pads, nets, tracks, vias, keepouts, and fixed geometry.
- [ ] Identify and remove only obsolete SMD-era tracks and vias in the affected local areas.
- [ ] Route all affected and new through-hole component pads with the required minimum widths and no net-name changes.
- [ ] Confirm the board contains zero SMD component pads and zero unconnected items.
- [ ] Run normal KiCad DRC and iteratively correct every violation without global suppression.
- [ ] Run ERC, schematic legibility, and drift checks to prove the PCB-only pass did not disturb authoritative design data.
- [ ] Finish without committing.
