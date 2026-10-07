# DCC Roll20 Visuals

Visual-design and reusable-asset repository for the Dungeon Crawler Carl Roll20 character sheet.

This repository is intentionally separate from production engineering. It contains visual assets, design tokens, Roll20 rendering specimens, documentation, and handoff material. It does **not** define game mechanics or production release revisions.

## Governing direction

- **Drama in the frame; clarity in the fields.**
- Cinematic, race-reactive header artwork.
- Class identity appears as a restrained secondary overlay.
- Dark metal, charcoal, slate, bronze seams, and orange-gold emphasis.
- Distressed wear is concentrated around frames and edges; working surfaces remain quiet.
- Name / Race / Class are edited on the Character tab and displayed contextually in the header.
- No Health or Mana indicators in the header.
- Preserve the current sheet's systems and relationships; visuals must not silently redefine mechanics.

## Repository structure

```
assets/
  brand/
    logo/
    emblems/
    marks/
  textures/
    metal/
    wear/
    noise/
    seams/
  chrome/
    corners/
    borders/
    dividers/
    panel-caps/
  banners/
    races/
    neutral/
    class-overlays/
  badges/
    clubs/
    statuses/
    provenance/
  icons/
  chat/

specimens/
  VIS-06E-roll20-rendering-proof/
  header/
  panels/
  chat/

tokens/
  colors.css
  spacing.css
  typography.css
  effects.css

docs/
  asset-guidelines.md
  naming-conventions.md
  roll20-constraints.md
  visual-handoff.md
  vis-specs/
```

## Milestones

Visual deliverables use the `VIS-xx` namespace. The immediate implementation-proof milestone is **VIS-06E — Roll20 Rendering Proof**, which will demonstrate that the approved ornate treatment can be built from reusable assets and Roll20-compatible HTML/CSS rather than flattened mockup art.

## Asset philosophy

Race banners should be independent from class overlays. Avoid generating every Race × Class combination as a flattened image. Shared chrome, borders, textures, and badges should be reusable and optimized so the final sheet remains maintainable and performant.

## Status

Repository scaffold created for the visual-design stream. Production HTML/CSS/workers remain outside this repository until an explicit handoff is approved.
