# DR1 R29 — Player Kill artwork (TEST assets)

Approved visual concept from DR1 R28, extracted into separate transparent WebP graphics and optimized for their intended Roll20 display size.

- `player-kill-small-white.webp` — 80×80px, small skull for each remaining Player Kill (3,000 bytes).
- `player-kill-ten-white.webp` — 72×72px, white ten-kill emblem (2,666 bytes).
- `player-kill-leaderboard-gold.webp` — 72×72px, gold leaderboard emblem (2,914 bytes).

Art is decorative; counters and title entitlements are not derived from images. R29 uses the existing three output mark attributes in the header kill/boss rail and retains the existing Combat → STATUS counter controls. The worker emits equal-width display cells, and CSS paints one image per cell. Marker categories remain gold, ten-kill, then individual.

Production-style sheet references use a fixed Git commit rather than `main`. This directory contains test assets; publishing them does not promote DR1 R29. Master source artwork is retained in the DR1 R28 project files.
