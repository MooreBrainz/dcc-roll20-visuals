# VIS-20 — R42 System Audit + Roll20 Proof Map

Status: visual-development artifact only. No production HTML/CSS/worker changes.

## 1. Source boundary

This pass is grounded in the exact R42 engineering source supplied for the visual project:

| Source | Bytes | SHA-256 |
| --- | ---: | --- |
| `r42_work/vNext_38_0_dcc_digital.html` | 1,176,211 | `4285595832099087437b322c149ea008319a3ab795e81d8d4672ef586d85b012` |
| `r42_work/vNext_38_0_dcc_digital.css` | 266,907 | `3adb3b590f7f33580e3a5b2b0b6e0824eee524cb5076cfecf41962b218608024` |
| `r42_work/vNext_38_0_worker.js` | 807,537 | `a0b240a2e14c31bdf0314eccdbc722fbfc1e828786b56b338263f311c99ab3a7` |
| `r42_work/sheet.json` | 18 | `ac1ee6b846e23059b5de58cc0cecc7f968c7668361bf25ad0b5dd0b9505881a4` |

The worker is embedded in the release HTML. `sheet.json` uses `legacy:false`.

The visual repository does not become a production branch. All bindings below are preservation targets for later engineering handoff.

## 2. Global contracts

Top navigation is exactly:

**Character / Combat / Skills & Spells / Inventory / Achievements / Deities / Socials**

R42 action mapping:

- Character — `act_vn_tab_4`
- Combat — `act_vn_tab_1`
- Skills & Spells — `act_vn_tab_3`
- Inventory — `act_vn_tab_2`
- Achievements — `act_vn_tab_5`
- Deities — `act_vn_tab_6`
- Socials — `act_vn_tab_7`

Quests remain under Achievements. Entity mode remains separate from crawler tabs and uses `attr_vn_entity_mode` with CRAWLER / COMPANION / ADVERSARY / PERSONAL_SPACE.

The current header owns the portrait, entity selector, crawler identity readout, Race, Class, Level, Floor and Player Killer marks. The approved visual header may reposition these surfaces, but later implementation must not change their underlying ownership.

No Health Bar or Mana indicator is added to the cinematic header.

## 3. Character preservation map

Primary identity fields:

- `attr_character_name`
- `attr_race`
- `attr_class`
- `attr_lvl`
- `attr_floor_current`
- `attr_gender`
- `attr_crawl_num`
- `attr_size`

Race/Class setup is not decorative metadata. It includes readiness, persistent choices, context gates, race actions, class lifecycle controls and source-aware effects. Beautification must not collapse those systems into an inert profile card.

Core Stats remain the five R42 stats: STR / INT / CON / DEX / CHA. Their base/unenhanced, enhanced and modifier relationships must remain distinct.

Status must preserve separate ownership for Internal Buffs, selected External Buffs and Debuffs/Injuries. The explicit 3-selection treatment belongs to External Buffs, not to all effects.

Floor progression, Advancement, titles/achievements/quests and long-term state retain their current system boundaries.

## 4. Combat preservation map

Combat contains active runtime state, not merely a combat-action table. Its major current surfaces are:

- Status / Health Bar / DR / AI Favor / Move / Step / Mana
- Evade / Injuries / Rest
- Spell Casting Resolution HUD
- source-aware Combat Modifiers
- Class lifecycle/reward resolution
- Companion control
- repeating Combat Actions
- known Defense / Interrupt / Combat Utilities
- Action Reference

The visual pass must not replace the Health Bar slot system or invent a simplified HP bar.

## 5. Skills & Spells preservation map

The approved visual direction is two vertically stacked libraries to preserve horizontal room.

### Skill Library

Current repeating section: `repeating_skills`.

Important existing controls/state:

- `act_vn_add_skill` — +ADD SKILL
- `attr_improve` — ADVANCE mark
- `act_focus` — DETAIL
- `act_rollskill` — ROLL when rollable
- `act_combat` — ADD COMBAT for attack actions
- `attr_vn_open` — expanded/collapsed editor state
- action/family type pills and compact rank/stat/check summary are already derived

The detail body is hidden until the row is opened/focused. The proof must not invent a permanently visible third detail panel.

### Spell Library

Current repeating section: `repeating_knownspells`.

Important existing controls/state:

- `act_vn_learn_spell` — +LEARN SPELL
- `attr_improve` — ADVANCE where eligible
- `act_prepare` — PREP
- `act_hotlistadd` — HOT
- `attr_vn_open` — expanded/collapsed editor state
- existing type/family, rank, Mana and geometry readouts

Search, filters, sort and collapse controls remain library-level functions.

## 6. Inventory preservation map

`repeating_inventory` remains the canonical mutable item store. Equipped Gear and Hotlist are views/relationships, not independent item databases.

Current major surfaces:

- Equipped Gear
- Hotlist — 10 ready slots
- Inventory — canonical item records
- Spell Scrolls
- Spellbooks

Visual treatment must preserve equip/use/prep/hot relationships and should not duplicate item ownership.

## 7. Achievements preservation map

Achievements owns:

- Titles
- Achievement history/rewards
- Quests — Active / Completed / Failed

There is no standalone Quests tab.

## 8. Deities preservation map

Deities remains the worship system, including deity choice, worship/church Rank, offering state, active/suspended relationships, benefits and source-aware club relationships. Visual hierarchy may become more ceremonial, but rules state must remain explicit.

## 9. Socials preservation map

R42 Socials contains four primary system families:

1. **Members-Only Clubs** — existing full-color badge rail with anonymous/grey locked state and provenance gates.
2. **Public Profile / Popularity / Top Ten** — Popularity, official rank, bounty, review state and related GM-owned controls.
3. **Sponsors** — up to three active contract records, catalog/custom identity, state, Benefactor Box tier and contract actions.
4. **Media / Interviews / Playing to Cameras** — deferred integration in exact R42.

The current club logo family is retained as-is in the new visual proof. The proof uses the same hosted Roll20 badge artwork rather than replacing it with generated club icons.

The local R42 Top Ten HUD snapshot is intentionally not promoted as a visual pattern. Later project direction rejected that optional duplicate leaderboard surface; the visual proof focuses on the crawler's own Popularity/official-rank information.

## 10. Alternate entity modes

Crawler tabs do not replace the separate entity-mode surfaces.

Protected modes:

- Companion — Pet / Mount / Minion actor
- Adversary — GM stat block / attacks / effects / clues
- Personal Space / Safe Room — loot-box opening and resolution workflow

These require later dedicated visual validation; they are not folded into crawler tabs.

## 11. Visual mapping decisions for this proof

The proof intentionally demonstrates the approved system without production mutation:

- Cinematic race-first banner.
- Tigran artwork occupies the left/center header space.
- Berserker-family class language is a restrained scratch/impact overlay, not a second competing illustration.
- Identity controls are quiet and readable on the right.
- Header contains no Health or Mana.
- Dark industrial body chrome remains consistent regardless of race/class art.
- Orange-gold is the default functional hierarchy; contextual race/class color is concentrated in the banner.
- Working surfaces remain flatter and quieter than the header.
- Club badges use current R42 art.
- Skills and Spells are stacked, entry-heavy libraries.
- Socials follows the approved composition: profile + Popularity left; wide club rail upper-right; Media and Sponsors adjacent below.

## 12. Proof limitations

This specimen is a rendering/design proof, not a fork of R42.

- It does not embed the R42 worker.
- Action buttons are representative and mapped to real R42 labels/bindings, but this specimen does not claim runtime equivalence.
- Only Character, Skills & Spells and Socials receive representative body compositions in this proof; the seven-tab navigation is shown globally.
- The cinematic header is fixed to Tigran + Berserker-family styling for this pass. Dynamic race/class switching is a later engineering integration.
- No production release revision is created by this repository.

The next engineering handoff must rebase these visual hooks onto the then-current production source and rerun the normal regression suite before any promotion.
