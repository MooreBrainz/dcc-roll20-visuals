# VIS-26 — 1496 × 144 Header Fit Specimen

This **new** dedicated specimen tests the latest proposed Tigran race art and separate Berserker alpha layer against the development sheet's reported header footprint (1496.36 × 143.86 CSS pixels).

## Load in disposable Roll20 Custom Sheet Sandbox

- HTML: `roll20-header-preview.html`
- CSS: `roll20-header-preview.css`
- Translation: `{}` if an empty JSON field is required
- The checkbox is **preview-only** and switches the class overlay on/off; it is **not a class-selection mechanic**.

## Linked assets (committed on main)

- `assets/banners/races/race-tigran-1496x144.jpg` — JPEG, 1496 × 144, 61,457 bytes, sha256 `3297ebd90b682318edb3d2898b9d6959b385188929ce92fb76c009f5a8d1b2d4`
- `assets/banners/class-overlays/class-berserker-1496x144.png` — indexed transparent PNG, 1496 × 144, 38,179 bytes, sha256 `f19f1e6a0e626ffa1f3eb7529d0722be235fe49eeb471a5f2303b45536fc056b`

The original images remain local source artwork. These smaller Roll20 candidates are integrity-checked. The portrait is visibly positioned at the right of the 1496×144 race banner, while the overlay retains transparent pixels for independent visibility.

## Behavior and constraints

At the nominal desktop width, artwork uses `background-size:100% 100%` and exact matching aspect ratio. At narrower widths the preview crops horizontally on the right rather than squeezing the tiger; the fields can wrap. **The source development header's responsive behavior still requires inspection** before applying this to the real sheet.

The **existing VIS-20 preview has intentionally NOT been replaced**: it uses a taller 245px hero; putting 1496×144 assets in it would stretch them and give an invalid fit comparison. Use this dedicated header-fit specimen instead.

This is a visual build. Real Race/Class selection, avatar, Entity mode, Player-Killer state, Level, Floor, all other header systems and sheet worker behavior stay owned by the latest development source.

## Approval gate

Confirm the Tigran face remains visible at target width, controls stay readable and usable, overlay does not obscure the face or header data, transparent regions are truly transparent, and the fallback (overlay off) looks correct. Then compare against latest engineering source before incorporating it.
