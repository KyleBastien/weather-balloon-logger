# Proposal: final-documentation-consistency-pass

> Marker: AUTO (autonomous mode; auto-approved, reviewable after the fact)

## Why

The completed PCB uses real footprints and J2's embedded stock footprint is at 0 degrees, but LAYOUT.md and FOOTPRINT_AUDIT.md still describe placeholder-footprint substitution and the old placeholder-axis orientation. Correcting only those documents prevents fabrication review from relying on stale state while retaining all genuine release holds.

## What Changes

- Update docs/LAYOUT.md to state that all target footprint substitutions are complete, remove stale CopperheadDraft claims, and document J2 at 0 degrees with its unchanged vertical physical row, alignment, and net order.
- Update docs/FOOTPRINT_AUDIT.md to describe the completed real-footprint state and replace the obsolete next-pass substitution checklist with concise remaining fabrication holds.
- Preserve explicit non-fabrication-ready status and the physical module, exact-part/mock-up, RF stackup/return-via/VNA, cutdown, enclosure/cable, and post-qualification output-regeneration holds.
- Do not modify schematic, PCB, project settings, footprints, routing, outline, constraints, or outputs.
