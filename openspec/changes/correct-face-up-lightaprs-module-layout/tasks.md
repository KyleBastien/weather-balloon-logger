# Tasks

- [ ] Read the existing PCB s-expressions and identify unique anchors for the module zone, J2/J6/J7, J3/J4, mounting holes, keepout drawings, and affected routing.
- [ ] Surgically edit the board placement, graphics, and affected traces without regenerating the file.
- [ ] Update docs/LAYOUT.md with exact FACE-UP coordinates, corrected RF-side mapping, standoff approximation, keepouts, and remaining fabrication holds.
- [ ] Record the mechanical/layout decision and revised constraint.
- [ ] Run DRC, inspect and fix every violation, then run drift checks and finish only when clean.
