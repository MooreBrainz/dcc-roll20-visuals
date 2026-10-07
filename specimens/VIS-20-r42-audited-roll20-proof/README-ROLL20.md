# VIS-20 — R42-Audited Roll20 Rendering Proof

This is a **visual-development specimen**, not a production sheet revision.

## Load in Roll20

Use a disposable Custom Sheet Sandbox / test sheet with Legacy Sanitization OFF.

- HTML: `roll20-preview.html`
- CSS: `roll20-preview.css`
- Translation: `translation.json`

The specimen intentionally does **not** embed the R42 worker. It exists to validate the approved visual system in Roll20 while keeping the visual project separate from production engineering.

## What is source-grounded

The accompanying audit was made against the exact R42 engineering source. The preview therefore uses the real seven-tab names, real R42 identity field names, real Skills & Spells action labels/bindings, the existing Roll20-hosted club badge family, and the R42 Socials ownership boundaries.

Representative action buttons are present to validate size/hierarchy, but the specimen does not claim runtime behavior.

## Preview navigation

Character, Skills & Spells, and Socials are interactive preview pages using CSS-only radio state. Combat, Inventory, Achievements and Deities remain visible in the navigation but are not implemented in this rendering specimen because their visual directions have already been explored and this pass is focused on the highest-risk reusable structures.

## Header

The Tigran banner is a raster asset for Roll20 reliability. The Berserker-family treatment is deliberately a secondary CSS overlay. Later production integration should make race imagery dynamic and class treatment conditional without moving Race/Class selection into the header.

No Health or Mana appears in the header.

## Important

Do not copy this specimen directly over production R42. The later engineering handoff must port the approved visuals into the then-current source while preserving worker/binding/repeating-section/gate contracts and rerunning the normal regression suite.
