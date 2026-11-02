# LEVEL UP header control artwork (DR1)

- `level-up-badge.webp` — R26 opaque WebP; retained for rollback.
- `level-up-badge-transparent.webp` — R27 transparent WebP with original badge art, 160 × 53 pixels, 4,442 bytes, alpha channel. Removes only the exterior black canvas; retains the dark inlay and green glow.

R27 CSS applies the new image only to the existing Roll20 action button `act_vn_levelup_open`, with a transparent button surface and original dimensions and interaction behavior. LEVEL and FLOOR labels are centered, with their numbers remaining gold/bold. This is a TEST CANDIDATE, not a promoted release. Keep all artwork URLs pinned to an immutable commit.
