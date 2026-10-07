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

## Current milestone

**VIS-06E — Roll20 Rendering Proof** is now populated with its first real reusable proof assets and a browser specimen. It is mapped back to the current R42 relationships rather than inventing replacement systems.

Current proof assets include:

- Tigran race-header proof SVG.
- Neutral industrial fallback SVG.
- Barbarian-family claw/impact overlay SVG.
- Reusable panel-border, corner, and bronze-divider SVGs.
- Crown emblem.
- HTML/CSS rendering specimen.
- R42 relationship mapping notes.

The race-header SVG is intentionally a replaceable proof asset. Final cinematic race artwork can later take its place without changing the structural layering.

## Asset philosophy

Race banners should be independent from class overlays. Avoid generating every Race × Class combination as a flattened image. Shared chrome, borders, textures, and badges should be reusable and optimized so the final sheet remains maintainable and performant.

## Status

Visual repository only. Production HTML/CSS/workers remain outside this repository until an explicit handoff is approved.
