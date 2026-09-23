# Weather Balloon Logger LightHAB carrier

This repository contains a hand-solderable through-hole carrier for the QRP Labs LightHABTracker 1.0 and SparkFun OpenLog. LightHAB's exposed 3.3 V rail powers the logger directly.

| Directory | Contents |
| --- | --- |
| `docs/` | Electrical, mechanical, BOM, purchasing, and release records |
| `library/` | Project KiCad symbols and through-hole footprints |
| `firmware/` | LightHAB upstream integration scaffold and test plan |
| `outputs/` | Review renders, fit sheet, BOM, Gerbers, drill, DXF, and STEP |
| `scripts/` | Deterministic board rebuild, export, and audit tools |

## Project release status

This repository now contains the Weather Balloon Logger carrier design and its
review exports. It is **not yet released for fabrication** because the purchased LightHAB must be measured before its connector and mounting geometry can be finalized. See
[`docs/FABRICATION_READINESS.md`](docs/FABRICATION_READINESS.md) for the exact
engineering-prototype and flight-candidate gates.

## Working locally

The CLI needs no account and no cloud:

```bash
npm i -g copperhead
copperhead check          # ERC, DRC, and doc drift. No model, no network.
copperhead do "..."       # propose, edit, verify, commit
```

The current PCB has zero SMD pads, zero unconnected items, and a prominent no-fabrication warning in the provisional module area.
