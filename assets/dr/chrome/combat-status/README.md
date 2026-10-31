# DR1 hybrid Combat → STATUS artwork

The assets in this directory are **provisional tests**, not an approved production visual standard.

## Current DR1 R7 test

- `header-center-muted-framed.webp` — 398×71 WebP, 2,314 bytes. Sparse muted rivets, with original orange upper/lower framing preserved in the same graphic.
- `header-left.webp` and `header-right.webp` — original end caps, unchanged.
- R7 uses a single CSS background stack: caps above center strip; no foreground pseudo-element overlays or stretching panels.
- Center strip repeats horizontally and is compressed vertically by the same ratio as the caps. Text and LIVE badge remain real HTML.

## Retained rollback assets

- `header-center-muted-rivets.webp` — R5/R6 version without orange rails.
- `header-center.webp` — original dense-rivet R2/R3 center.

All production-style CSS URLs should be commit-pinned. Race and class artwork are separate, under `assets/headers/`. No DR asset should redefine mechanics or editable data. R7 must pass live Roll20 visual review before promotion.
