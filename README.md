# DCC Roll20 Visuals

Visual-design and reusable-asset repository for the Dungeon Crawler Carl Roll20 character sheet.

This repository is intentionally separate from production engineering. It contains visual assets, design tokens, Roll20 rendering specimens, documentation, and eventual handoff material. It does **not** define game mechanics or production release revisions.

## Current state

The earlier VIS-06E proof assets and test specimen have been removed so the repository can be rebuilt from a clean implementation baseline.

The directory scaffold, documentation, and provisional design tokens are retained. New assets and Roll20 specimens should be created only after they have been checked against the current sheet HTML/CSS/worker relationships.

## Governing direction

- **Drama in the frame; clarity in the fields.**
- Cinematic, race-reactive header artwork.
- Race defines the primary banner imagery.
- Class adds a restrained secondary overlay.
- Dark metal, charcoal, slate, bronze seams, and orange-gold emphasis.
- Distress is concentrated around frames and edges; working surfaces remain quiet.
- Header identity is display-only: Name / Race / Class / Entity / Level / Floor.
- No Health or Mana indicators in the header.
- The current Roll20 sheet systems and relationships remain authoritative.
- Visual approval does not equal production promotion.

## Repository structure

```
assets/
  brand/
  textures/
  chrome/
  banners/
  badges/
  icons/
  chat/

specimens/
  header/
  panels/
  chat/

tokens/
docs/
```

## Next work

1. Audit the current sheet HTML/CSS/worker relationships against the approved visual layouts.
2. Build a new Roll20 rendering proof from that audit.
3. Add only the reusable assets required by the new proof.
4. Validate wide and narrow Roll20 layouts before final visual handoff.

Reusable assets should be production-intentional rather than remnants of exploratory mockups.

## Collaboration / GitHub workflow

**For future ChatGPT visual-design sessions:** this repository is connected through the GitHub connector and ChatGPT has successfully committed visual assets, CSS and documentation to `main`. Check the available GitHub connector actions before claiming GitHub uploads are unavailable. The local sandbox not supporting `git clone` or direct network access does **not** mean the connected GitHub integration is unavailable. Keep visual changes separate from production engineering.

**Current asset set:** VIS-21 chrome components are in `assets/chrome/` and documented in `assets/chrome/README.md`; CSS integration and Roll20 verification are separate future steps.


## VIS-25 — Source-Mapped Component Bridge

The first **integration-preparation package** is ready at [`components/VIS-25/`](components/VIS-25/README.md). It includes:

- an opt-in R42-selector-based CSS bridge (separate from the visual proof CSS);
- an exact component-to-HTML/CSS contract map;
- a machine-readable chrome asset manifest;
- a read-only source compatibility checker and a live Roll20 QA/rollback checklist.

The scoped bridge **does not modify the development branch** and must not be treated as ready for promotion. Use it only in a disposable engineering-source sandbox after checking the latest development HTML/CSS/worker. The earlier VIS-20/VIS-24 proof is a visual reference, not production markup.

## VIS-26 — 1496 × 144 Header Artwork

The new [Tigran race banner and transparent Berserker class overlay](assets/banners/README.md) are now published. Use the [dedicated VIS-26 header fit specimen](specimens/VIS-26-header-fit/README.md) to test the new 144px height.

The old 245px VIS-20 proof retains its earlier banner intentionally: repointing it would distort the newly sized art. Integrate into the actual development header only after the latest engineering snapshot is reviewed and the VIS-26 fit is confirmed in Roll20.
