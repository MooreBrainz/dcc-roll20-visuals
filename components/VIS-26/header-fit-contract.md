# VIS-26 — Development Header Fit Contract (draft)

**Visual-design milestone only; no production engine files changed.**

The development sheet's reported header inner bounds are approximately **1496.36 × 143.86 CSS px**. Use **1496 × 144 px** as the nominal 1× raster artboard and match its aspect ratio (10.39:1). In live Roll20 the container should remain responsive; dimensions are a design target, not a fixed-width production viewport.

## Artwork ownership

- Race is the primary artwork layer. The approved cinematic Tigran treatment keeps orange/black fur over the left/center and a recognizable Tigran portrait on the right, with unobstructed text area.
- Class is **separate transparent overlay**, not permanently baked into the race art. The current candidate is Berserker; it must remain hidden or replaced when other classes are selected.
- Class overlays require true alpha transparency. Do not convert them to ordinary opaque JPEGs.
- Production Race/Class selection and header identity fields are owned by the source sheet and worker; this visual branch does not invent or replace that logic.
- Preserve avatar, Entity mode, PK marks, Name/Race/Class readouts, Level/Floor, and other source-owned header controls. No HP/Mana in header.

## Fit contract

- Nominal target rectangle: `1496 × 144`, CSS container `width:100%; height:143.86px` only when consistent with the actual development layout.
- Default render for correctly composed images: `background-position:center; background-size:100% 100%; background-repeat:no-repeat`.
- Raster assets should be composed for that aspect ratio, not vertically squeezed from earlier 1600×260 artwork.
- Right-side race portrait must remain legible with one-line header control overlays.
- If header width differs materially, fit needs explicit responsive design review rather than distorting or cropping the portrait.
- Class alpha overlays: `pointer-events:none`; no child element should intercept input clicks.

## Current local candidate files

- `tigran_race_banner_1496x144.png` — composed from the new Tigran artwork for the current header ratio.
- `tigran_berserker_overlay_1496x144.png` — transparent Berserker art layer, same pixel dimensions.

These are **local candidate assets pending binary publication and live Roll20 fit testing**. Their file names are not to be referenced from the proof CSS until the actual binary objects exist in `assets/banners/`. The old working race banner remains in GitHub as a safe fallback until the replacement is validated.

## Review sequence

1. Publish both full-quality rasters to the race/class-overlay folders and verify file byte integrity / alpha.
2. Add a VIS-only responsive header specimen around the actual `1496 × 144` artwork.
3. Confirm Name/Race/Class/Entity/Level/Floor remain readable at normal and narrow widths; class overlay is visibly subtle.
4. Check disabled/none class fallback and race fallback.
5. Handoff the approved assets and measurements to the **latest** development branch via a separate engineering review (not from R42 reference alone).

No production release or main engineering stream promotion is authorized here.
