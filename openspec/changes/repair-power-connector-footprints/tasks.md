# Tasks

- [ ] Read the actual PCB/project anchors and confirm J1/J5/SW1 pads, positions, orientations, affected nets, and existing exclusions.
- [ ] Reposition only J1/J5/SW1 and surgically replace only stale local power/cutdown routing.
- [ ] Verify SW1 pad 3 remains unconnected and current-path widths are maintained.
- [ ] Update docs/FOOTPRINT_AUDIT.md plus decision/changelog rationale.
- [ ] Run normal DRC to zero violations and zero unconnected items, then run ERC, drift, and other Copperhead verification gates.
- [ ] Finish only after all bounded-pass obligations are clean.
