# VIS-23 — Fields, Stat Tiles & Status Indicators

**Status:** Integrated into the VIS-20 Roll20 rendering proof CSS. **Live Roll20 visual approval pending.**

**Project boundary:** Strictly a VIS visual-build artifact. This is not a production update, and no engineering HTML/CSS/worker, attribute behavior or release state was changed.

## Design aim

Following approved muted chrome (VIS-21E) and engraved navigation (VIS-22), working data should be more readable than its decorative frame.

- **Quiet recessed fields:** dark inset wells and neutral steel borders, warm keyboard focus only.
- **Read-only data:** differentiated from editable fields without dimming the text beyond readability.
- **Compact five-stat tiles:** Strength / Intelligence / Constitution / Dexterity / Charisma only; totals reduced from 31px to 28px nominal, 26px on narrow viewports, with slightly reduced padding.
- **Stat detail retention:** example unenhanced values and CHECK controls remain reachable; these preview tiles do not replace R42's full Base / Enhanced / Mod / Stat Check relationship.
- **Status distinctions:** Internal Effects, External Buffs, and Debuffs/Injuries remain separate, with larger, muted, explicitly labeled state badges.
- **Source/provenance text:** increased line-height and wrap behavior for long explanations.
- **Type/family chips:** quiet, non-action category labels for Skill/Spell entries.

## Exact change surface

Only `specimens/VIS-20-r42-audited-roll20-proof/roll20-preview.css` was modified.

The new appended CSS section is:

`VIS-23 / RECESSED FIELDS, COMPACT STATS, READABLE STATUS`

Affected classes include:

- `.sheet-vis20-identity`, `.sheet-vis20-fields`, `.sheet-vis20-tools input`;
- `.sheet-vis20-stat` and its label/total/number input;
- `.sheet-vis20-statusrow` and `.sheet-vis20-pill`;
- `.sheet-vis20-row i` type/family chips and `.sheet-vis20-advance`.

Responsive tweaks: <=900px status descriptions move below name and pill; <=720px stat inputs stack beneath their labels; <=390px stat totals/labels are slightly smaller.

**Not changed:** HTML, R42 data/action names, tab mapping, navigation styling, club logos, Race banner, gameplay state, or production mechanics. No new assets were required.

## Interpretation boundaries

The VIS-20 proof uses illustrative sample values. VIS-23 is not a source of new DCC mechanics, social tiers, or status calculations. When visuals are ported to engineering, worker-owned derived fields and state gates remain authoritative.

The focus outline is a CSS fallback when the decorative input background cannot load. The proof remains a visual demonstration rather than a working mechanics implementation.

## Live Roll20 checklist

1. Use the newest `roll20-preview.css` with existing proof HTML; leave JSON and worker unchanged.
2. Character: inspect five compact stat tiles, editable base values, totals/modifiers, and CHECK controls.
3. Character: edit Crawler Number / Size and inspect the focus state; READY readouts should appear read-only.
4. Character: examine Internal Effects / External Buffs / Debuffs-Injuries badges and their long source descriptions.
5. Skills & Spells: type chips should look informational, distinct from ADVANCE / DETAIL / ROLL / ADD COMBAT / PREP / HOT actions.
6. Socials: popularity circle, club badges and Sponsors/Media layout should remain unchanged.
7. Test normal and narrow Roll20 widths; flag any clipped stat labels, obscured inputs, too-small provenance, or excessive amber emphasis.

## Quality gate

Verify committed CSS contains VIS-23, CSS braces are balanced, VIS-21E/VIS-22 are retained, and proof HTML SHA is unchanged. Roll20 rendering remains for user approval. No production promotion is implied.
