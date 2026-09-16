# Tasks

- [x] Inspect existing project conventions and any firmware/build files.
- [x] Create the minimal firmware directory and ATSAMD21G18 HAL/build scaffold.
- [x] Derive `pins.h` solely from `docs/PINOUT.md`, with source and safety comments.
- [x] Implement driver stubs and the safe logging happy path.
- [x] Attempt the vendor build when available; otherwise document `not compiled here` explicitly in `firmware/DEVPLAN.md`.
- [x] Record the firmware architecture and default-off decision in design docs.
- [x] Run ERC, DRC, drift, and applicable consistency checks; reconcile every blocking result.
- [x] Finish only after all required verification gates pass.
