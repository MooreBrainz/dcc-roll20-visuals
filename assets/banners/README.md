# Race and Class Banner Assets

## VIS-26 — 1496 × 144 header format

**Development reference:** 1496.36 CSS px wide × 143.86 CSS px high. Raster artboard is 1496 × 144 pixels (approx. 10.39:1).

| Asset | Role | Format | Integrity SHA-256 |
| --- | --- | --- | --- |
| `races/race-tigran-1496x144.jpg` | Primary Tigran race artwork | JPEG RGB, 1496 × 144, 61,457 bytes | `3297ebd90b682318edb3d2898b9d6959b385188929ce92fb76c009f5a8d1b2d4` |
| `class-overlays/class-berserker-1496x144.png` | Berserker class overlay only | Indexed PNG with alpha, 1496 × 144, 38,179 bytes | `f19f1e6a0e626ffa1f3eb7529d0722be235fe49eeb471a5f2303b45536fc056b` |

The race and class assets must remain separate. Hide the class layer when no eligible class overlay is selected, without changing the race art. The class overlay should be presented subtly (the new VIS-26 test starts at 34% opacity). Avoid stretching art meant for a 10.39:1 aspect ratio into the older 245px VIS-20 preview hero.

The previously tested `races/gritty_tiger_warrior_banner_roll20.jpg` remains as an **unmodified fallback** until the new banner is approved in live Roll20.

[Roll20 header fit specimen](../../specimens/VIS-26-header-fit/README.md) · [Integration hooks](../../components/VIS-26/header-layer-hooks.css) · [Header fit contract](../../components/VIS-26/header-fit-contract.md)

These assets and instructions are **VIS-only**. They are not approved production changes.
