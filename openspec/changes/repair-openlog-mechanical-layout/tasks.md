# Tasks

- [ ] Read the actual PCB anchors and baseline normal DRC report.
- [ ] Select the smallest top/right outline extension and A1/C1/C2 placement that contains the real courtyard and preserves access.
- [ ] Surgically edit the PCB placement, outline, local silk, and only A1-related GND/3V3/UART_TX copper.
- [ ] Verify A1 pads 2/3/5 remain GND/3V3/UART_TX and unused pins remain unconnected.
- [ ] Update layout, footprint-audit, decision, and changelog documentation.
- [ ] Run normal DRC to zero violations and zero unconnected items; run ERC, schematic legibility, drift, and Copperhead verification checks.
- [ ] Reconcile every blocking finding and finish only when all gates pass.
