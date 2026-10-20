# DCC Action Tracker — Visual Design Workspace

Status: **E05 visual design candidate / not promoted**

This folder is deliberately independent from the LIVE-TRUSTED DCC Roll20 character sheet and from the E04 positioning baseline.

## Locked requirements

- Five crawler rows; fixed footprint rather than auto-resizing.
- Two circular gold action pips per crawler by default, dim when spent.
- Movable GM-layer footprint that matches the actual HUD dimensions precisely.
- Manual player and GM macro control only; never infer Action costs from character sheet rolls.
- Preserve page-local placement and shared action state independently.
- Gritty industrial metal, distressed brass/gold visual theme.

## Architecture notes

The Roll20 Mod API can render foreground graphic/image objects, paths and text, but it does **not** accept a generated mockup as a functional HUD by itself. For a usable implementation, prepare artwork as a background PNG (without baked-in player names, action pips or round number), and draw those data as separate API objects layered above it.

E05 code is currently a test candidate. Verify E05 macro permissions, action accounting, page positioning, transparent footprint dimensions and rendering before replacing its procedural background with finalized art.

## Visual asset production next

1. Approve a five-row visual concept.
2. Export a *blank* HUD background with five empty rows, no permanently baked-in names/pips/round values.
3. Determine the exact Roll20 footprint size and image URL hosting strategy.
4. Integrate graphical overlay into a new test candidate, keeping E04 and E05 immutable.
5. Complete hands-on testing before promotion.

Do not treat design mockups or prototype assets as LIVE-TRUSTED releases.
