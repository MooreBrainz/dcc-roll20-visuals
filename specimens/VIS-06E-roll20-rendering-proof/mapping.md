# VIS-06E R42 mapping notes

This specimen deliberately demonstrates visual feasibility without redefining the current sheet's systems.

| Proof element | Current R42 relationship |
| --- | --- |
| Header crawler display | `attr_vn_crawler_identity` |
| Header Race display | `attr_vn_race_display_name` |
| Header Class display | `attr_vn_class_display_name` |
| Level / Floor | `attr_lvl` / `attr_floor_current` |
| Entity mode selector | `attr_vn_entity_mode` with CRAWLER / COMPANION / ADVERSARY / PERSONAL_SPACE |
| Navigation | existing seven action tabs: Character / Combat / Skills & Spells / Inventory / Achievements / Deities / Socials |
| Core Stats | the actual five-stat model: STR / INT / CON / DEX / CHA; editable base values and derived enhanced/mod values remain separate |
| Health | existing 10-slot Health Bar with `attr_hpfill_10` … `attr_hpfill_100` and the corresponding slot values |
| Repeating row example | represents existing repeating-record behavior and source/provenance display; it is not a new record type |
| Chat card | visual-only example; final mapping must use the current sheet's roll-template data and logic |

## Deliberate omissions

- No Health or Mana in the header.
- No sixth core stat.
- No numeric-HP replacement for the Health Bar.
- No new race/class editing controls in the header.
- No mechanics encoded into the SVG artwork.

## Production translation

For a finite canonical race/class list, the safest Roll20 implementation is to expose normalized hidden visual-state attributes from existing sheet workers and use CSS state selectors to choose hard-coded hosted assets. This avoids relying on user-entered URLs or allowing artwork choice to become a new rules system.

The asset layer should remain replaceable: these SVG proof assets establish dimensions, crop behavior, layering, and chrome. Final cinematic race art can replace the proof race SVG without changing the HTML structure.
