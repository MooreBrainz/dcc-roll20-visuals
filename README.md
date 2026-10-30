# DCC Roll20 Visual Assets

This repository hosts visual artwork for the **Dungeon Crawler Carl Roll20 CSE character sheet**, plus the independent Action Tracker HUD assets.

## Current supported artwork

- `assets/headers/races/<race>/background.webp` — race-specific header backgrounds (30 races).
- `assets/headers/races/<race>/character.webp` — race-specific transparent character art (30 races).
- `assets/headers/classes/<class>/overlay.webp` — class-specific header overlays (51 classes).
- `assets/brand/dcc-ttrpg-header-logo.webp` — DCC TTRPG sheet logo.
- `assets/banners/class-overlays/class-berserker-1496x144.png` — retained legacy Berserker header artwork, kept in place to preserve existing links.
- `action-tracker/` — separate approved Roll20 Action Tracker HUD and release materials; not part of the character-sheet beautification cleanup.

## Project streams

- **V## R##** — mechanically validated character-sheet systems.
- **U## R##** — established header/utility visual development.
- **DR# R#** — new independent visual design and UI test packages.

New DR assets will be added only after visual approval and a Roll20 compatibility review. The default DR direction is **hybrid artwork + CSS**: shared decorative assets for panel frames and textures, HTML/CSS for text, controls, layout and responsive behavior.

## Cleanup record

On 2026-10-30, abandoned VIS-series prototypes, chrome experiments, specimen sheets, and related drafts were removed from the default-branch repository tree. **This was a repository-structure cleanup, not a rewrite of Git history.** Their last complete state is preserved on branch `archive/pre-dr-cleanup-2026-10-30`. Existing race/class artwork, the DCC logo, and Action Tracker deliverables were not modified.

Do not delete or rename published header artwork without checking current Roll20 CSS references; external sheet stylesheets may link directly to GitHub paths or commit-pinned URLs.
