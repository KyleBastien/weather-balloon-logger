# Tasks

- [ ] Validate this change proposal.
- [ ] Preflight the schematic, PCB, BOM, and output directory.
- [ ] Run ERC and DRC and reconcile any violations.
- [ ] Export JLC Gerbers and drill files; verify every required file exists and is non-empty.
- [ ] Export outline DXF and STEP; verify both exports succeed and are non-empty.
- [ ] Run `export_svg` for schematic and PCB and include both renders in `outputs/`.
- [ ] Generate and read back `outputs/BOM.csv` with columns `refdes,MPN,qty`, consolidating identical MPNs without dropping UNVERIFIED markers.
- [ ] Record the Stage 6 packaging decision and append the changelog entry.
- [ ] Run legibility, drift, ERC, and DRC final checks; finish only after all exports and gates pass.
