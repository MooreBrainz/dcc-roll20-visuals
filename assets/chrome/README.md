# VIS-21 — reusable industrial chrome assets

These seven PNG assets are **visual-design assets**, separate from the production Roll20 sheet. They are optimized transparent PNGs derived from the approved chrome concepts; the original source compositions are intentionally not introduced as full-page mockups.

| Asset | Purpose | Optimized size |
| --- | --- | --- |
| `panels/panel-frame-large.png` | Large content panel frame | 1600 × 533 |
| `panels/panel-frame-sidebar-tall.png` | Narrow/tall side panel frame | 1050 × 1400 |
| `panels/panel-frame-wide.png` | Wide framed content region | 1500 × 1125 |
| `fields/field-frame-horizontal.png` | Horizontal inset plate | 1600 × 533 |
| `fields/field-frame-dark.png` | Quiet / resting inset plate | 1600 × 533 |
| `fields/field-frame-active.png` | Emphasized / selected inset plate | 1600 × 533 |
| `dividers/divider-bar-amber.png` | Industrial visual section divider | 1600 × 533 |

All seven images have been PNG-decoded and verified locally before GitHub upload. Preserve alpha transparency.

## Integration boundaries

These files are first-pass art assets, **not yet validated as repeatable CSS borders inside Roll20**. Do not stretch the full frame over arbitrarily tall or wide panels: metal corner geometry and rivets would distort. First validate edge/corner slicing or CSS `border-image` inset values on a specimen panel.

- Continue using existing R42 fields/actions/repeating sections unchanged.
- Keep body interiors quiet and accessible.
- Use stronger orange light for active/selected states only.
- Do not silently apply these assets to production HTML/CSS.
- Keep the Tigran banner independent of panel chrome.
