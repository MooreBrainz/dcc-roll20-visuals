# Asset Guidelines

## Production intent

The visual system should preserve the ornate quality of the approved mockups while remaining maintainable in Roll20. Use a hybrid of CSS and reusable image assets.

## Asset classes

### Race banners
- Wide cinematic artwork.
- Race identity owns roughly 80–90% of banner visual weight.
- Reserve readable zones for live identity text and Level/Floor.
- Avoid embedded UI text.

### Class overlays
- Transparent.
- Approximately 10–20% of banner visual weight.
- Add motifs such as claw scoring, arcane glyphs, shadow cuts, devotional geometry, arena laurels, frost haze, or hazard striping.
- Do not replace the race artwork.

### Chrome
- Corners, seams, borders, dividers, and caps should be reusable.
- Distress should concentrate at edges.
- Center surfaces remain quiet enough for dense content.

### Texture
- Keep noise subtle.
- Prefer tileable or stretch-safe sources where appropriate.
- Avoid large decorative textures behind form fields.

## Optimization targets

Use the smallest asset that survives Roll20 display scaling cleanly. Favor compressed WebP for large opaque artwork and transparent PNG/WebP for overlays. Document source dimensions, intended rendered dimensions, crop behavior, and repeat behavior beside finalized assets.
