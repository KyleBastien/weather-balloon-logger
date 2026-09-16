# Tasks

- [ ] Validate this change proposal.
- [ ] Build the board from the authoritative schematic footprint/net identities using surgical KiCad s-expression edits.
- [ ] Establish a practical outline and explicit connector/functional-block coordinates.
- [ ] Add SMA keepouts and place all footprints without courtyard or keepout conflicts.
- [ ] Route only power and short critical nets; preserve remaining nets as intentional ratsnest.
- [ ] Write LAYOUT.md with exact coordinates/rules and the required `## Draft quality` assessment, including the missing-ESD capture limitation.
- [ ] Update changelog and decision records.
- [ ] Run DRC, inspect every violation, fix all violations affecting routed nets/layout legality, and rerun until clean.
- [ ] Export/review a board render, run drift checks, and finish only after all obligations pass.
