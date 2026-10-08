# VIS-25 — R42 Structural Component Map

**Basis:** supplied `V38_R42_ENGINEERING.zip` → `r42_work/vNext_38_0_dcc_digital.html` and `vNext_38_0_dcc_digital.css`. These are read-only source snapshots, not claims about the latest development build.

| Approved component | Real R42 selector / location | VIS-25 treatment | Protected ownership |
| --- | --- | --- | --- |
| Root visual scope | `.sheet-vn-wrapper` | Opt-in with added `sheet-vis25-skin`; muted colours | All original descendants and layout remain |
| Header identity | `.sheet-vn-header`, `.sheet-vn-headsummary`, `.sheet-vn-portraitstack` | **No banner changes in this pilot** | Avatar, Crawler/Race/Class/Level/Floor, Entity mode, PK rail, Level Up placeholder |
| Main navigation | `.sheet-vn-tabbar` / `.sheet-vn-tabbtn` | Dark engraved textures + subdued selected state | Seven buttons; `act_vn_tab_4/1/3/2/5/6/7` remain; do not move `.sheet-vn-tabstate` |
| Tab pages | `.sheet-vn-pagestate[value="1"] + .sheet-vn-page` | **Untouched** | Hidden page gates and entity-mode visibility |
| Panels | `.sheet-vn-panel` | Optional `sheet-vis25-panel` ornate 9-slice edge | All panel bodies, child controls and nested gates |
| Sidebar panel | `.sheet-vn-panel` | Optional `sheet-vis25-panel--sidebar` with tall corner source | Existing panel row and text order |
| Quiet panel | `.sheet-vn-panel` | Optional `sheet-vis25-panel--quiet` no raster border | Useful for dense repeating libraries |
| Panel headings | Direct child `header` of selected `.sheet-vn-panel` | Dark metal plus thin bronze seam; **not** a full-width stretched frame | Existing heading/help labels and actions |
| Action controls | `.sheet-vn-btn` | Optional `sheet-vis25-control`; preserve gold/blue/red/ghost variants | Every `name="act_*"` handler, keyboard and disabled behavior |
| Editable data | `.sheet-vn-input` | Optional `sheet-vis25-field`; colours and focus only | `attr_*`, input size/height and validation |
| Read-only derived | `.sheet-vn-input[readonly]` with opt-in | Lower-contrast recess | Worker derived values stay readonly |
| Compact core stats | `.sheet-vn-stat` (5 source rows) | Optional `sheet-vis25-stat` background/border only | STR / INT / CON / DEX / CHA, Base, Enhanced, Mod and Check |
| Skill type + family | `.sheet-vn-skillsummary .sheet-vn-summarypills .sheet-vn-typepill` | Preserve colour states, enforce round corners / text legibility | `.sheet-vn-summarytone` and `.sheet-vn-familytone` sibling gates |
| Spell type + family | `.sheet-vn-spellsummary .sheet-vn-summarypills .sheet-vn-typepill` | Same rounded treatment | `PREP`, `HOT`, rank / mana / geometry remain |
| Skill detail | `.sheet-vn-focusopen`, `.sheet-vn-skilldetails`, `.sheet-vn-focus15` | **Untouched** | DETAIL toggles visibility and grid arrangement |
| Club badge gallery | `.sheet-vn-clubrail`, `.sheet-vn-clublogo` | **Untouched in pilot** | Six existing logos, access-gated silhouettes, provenance |
| Status source text | `.sheet-vn-statussource` | **Untouched in pilot** | Provenance should not be hidden or synthesized |
| Health slots / Mana | `.sheet-vn-hp`, Combat Status and spell HUD | **Untouched** | No header resource indicators |
| Safe Room / Loot | `.sheet-vn-personalspacepage`, repeating loot sections | **Untouched** | Safe Room owns box opening and resolution |

## Action and tab IDs — intentionally non-sequential

| Visual tab | Action | Page state |
| --- | --- | --- |
| Character | `act_vn_tab_4` | `attr_vn_tabpage_4` |
| Combat | `act_vn_tab_1` | `attr_vn_tabpage_1` |
| Skills & Spells | `act_vn_tab_3` | `attr_vn_tabpage_3` |
| Inventory | `act_vn_tab_2` | `attr_vn_tabpage_2` |
| Achievements | `act_vn_tab_5` | `attr_vn_tabpage_5` |
| Deities | `act_vn_tab_6` | `attr_vn_tabpage_6` |
| Socials | `act_vn_tab_7` | `attr_vn_tabpage_7` |

## Source-driven pill colours — do not hard-code

R42 already uses sibling selectors like `.sheet-vn-summarytone[value="ATTACK"] ~ .sheet-vn-actionpill` and `.sheet-vn-familytone[value="ANIMAL"] ~ .sheet-vn-familypill`.

Existing examples: Attack red, Utility/Check cyan, Passive purple, Heal green; source families include Animal purple and ranged/edged/etc. distinct colours. Colours are not new values and should not be recomputed from display text. **Do not use the VIS-20 fixture labels MOVEMENT/SENSE/COLD/AREA as authoritative catalog categories.**

## Existing assets (remote CSS background URLs)

- `assets/chrome/panels/panel-frame-wide.png` — selected content-panel 9-slice
- `assets/chrome/panels/panel-frame-sidebar-tall.png` — narrow/sidebar 9-slice
- `assets/chrome/fields/field-frame-dark.png` — inactive nav metal
- `assets/chrome/fields/field-frame-active.png` — selected nav metal
- `assets/chrome/panels/panel-frame-large.png` — previously approved page-title art, deferred until source heading wrappers are mapped
- `assets/chrome/dividers/divider-bar-amber.png` — existing asset, deferred if native R42 heading needs less glow
- `assets/banners/races/gritty_tiger_warrior_banner_roll20.jpg` — tested Tigran artwork, **not** installed as universal R42 header

## Caveats

The source R42 CSS is large and heavily uses `!important`. CSS cascade validation against the **latest development** build is required. The pilot uses high-specificity opt-in selectors and `!important` only where an existing R42 component already has them. The ornate frame is intentionally behind an extra per-panel opt-in because pseudo-elements may interact with overflow, positioning or clickable content.
