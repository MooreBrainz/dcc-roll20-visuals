# DR1 R2 — Combat Status pilot graphics

**Status: PROVISIONAL TEST ASSETS. Not an approved visual standard.**

These three WebP segments derive from the DR1 R1 hybrid header concept. They are slices, not a whole-panel image:

- `header-left.webp` — 51 × 71 px (end-cap artwork)
- `header-center.webp` — 7 × 71 px (repeat-x texture strip)
- `header-right.webp` — 51 × 71 px (end-cap artwork)

In Roll20, CSS renders each image at **48px high**, with left/right caps locked to opposite sides and the center strip repeating. The panel body, all text, actions and sizing remain pure HTML/CSS.

These are decorative, non-interactive images; no game values or text are embedded. This pilot is **not** a replacement for existing race/class header graphics.

Do not rename/move approved asset paths. Production candidate CSS pins URLs to the exact commit that publishes these files; no `main` image references are required.

**Artifact naming:** `DR1 R2` design test. **Mechanical authority:** exact V41 R05. **Visual source:** U01 R24. Roll20 hands-on testing is still required.
