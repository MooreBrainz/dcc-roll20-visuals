# VIS-06F — R42 Visual Normalization Audit

**Status:** COMPLETE  
**Scope:** Visual-design normalization only. No production HTML, CSS, worker, attributes, mechanics, or release state changed.

## 1. Purpose

This audit is the required bridge between the approved visual mockups and a new Roll20 rendering proof.

The generated mockups are treated as **visual references only**. The supplied R42 engineering package is treated as the **structural and relationship reference**. Where a mockup invents a field, button, state, panel, tab, or mechanic that does not exist in the R42 source, the R42 source wins.

This audit does **not** promote R42. The engineering package itself marks R42 as a frozen test candidate and R41 as live-trusted. For this visual project, R42 is used read-only to understand the latest supplied structure.

## 2. Audited source snapshot

Audited from the supplied `V38_R42_ENGINEERING.zip`:

- `vNext_38_0_dcc_digital.html`
- `vNext_38_0_dcc_digital.css`
- `vNext_38_0_worker.js`
- `README_FIRST_V038_R42.md`
- `FREEZE_RECORD_V038_R42.txt`
- `SOURCE_BOUNDARY_AUDIT_V038_R42.txt`
- `ENGINEERING_HANDOFF_V038_R42.md`
- `DEITIES_WORSHIP_RULES_V038_R31.md`

R42 freeze-record product hashes:

- HTML: `4285595832099087437b322c149ea008319a3ab795e81d8d4672ef586d85b012`
- CSS: `3adb3b590f7f33580e3a5b2b0b6e0824eee524cb5076cfecf41962b218608024`
- worker: `a0b240a2e14c31bdf0314eccdbc722fbfc1e828786b56b338263f311c99ab3a7`

Structural audit sanity check:

- 7 crawler tabs confirmed.
- 20 repeating-section families found across crawler/entity views.
- 221 `type="action"` button instances / 214 unique action names.
- Every action-button instance resolves to a worker click handler, including repeating-section and wildcard handlers.
- No visual implementation changes were made during this audit.

## 3. Global invariants for every future mockup/proof

### Header

The approved visual direction remains the cinematic race-reactive banner with restrained class overlay. The **functional header contract** is:

- live character avatar remains represented; race artwork does not silently replace the character portrait;
- `attr_vn_entity_mode` remains the live Entity selector;
- crawler identity is display-only in the header via `attr_vn_crawler_identity`;
- Race is display-only via `attr_vn_race_display_name`;
- Class is display-only via `attr_vn_class_display_name`;
- Level is display-only via `attr_lvl`;
- Floor is display-only via `attr_floor_current`;
- Player-Killer skull marks remain available through the existing header rail;
- the current disabled `LEVEL UP!` placeholder remains a structural element unless the engineering stream later removes it.

**No Health Bar or Mana indicator belongs in the header.**

Several later generated mockups replaced the identity rail with six stat tiles. That is not accepted for the implementation proof. The five core Stats belong in working content.

### Character editing ownership

Name, Race, Class, Level, and Floor are edited on Character. Race and Class selection must not be reintroduced as editable header controls.

Character also owns Gender, Crawler Number, and Size.

### Navigation

Only these seven crawler tabs exist:

| Visual order | Existing action | Existing page state |
| --- | --- | --- |
| Character | `act_vn_tab_4` | `attr_vn_tabpage_4` |
| Combat | `act_vn_tab_1` | `attr_vn_tabpage_1` |
| Skills & Spells | `act_vn_tab_3` | `attr_vn_tabpage_3` |
| Inventory | `act_vn_tab_2` | `attr_vn_tabpage_2` |
| Achievements | `act_vn_tab_5` | `attr_vn_tabpage_5` |
| Deities | `act_vn_tab_6` | `attr_vn_tabpage_6` |
| Socials | `act_vn_tab_7` | `attr_vn_tabpage_7` |

The numeric tab IDs are intentionally non-visual-order. A new visual layer must not renumber them.

Generated `Overview`, `Notes`, and standalone `Quests` tabs are rejected. Quests live inside Achievements.

Current responsive navigation is 7 columns normally, 4 columns at <=700 px, and 3 columns at <=500 px. The new design may restyle this behavior but must preserve readable access to all seven tabs.

### Entity modes

The header's Entity selector is not decorative. Current values are:

- `CRAWLER`
- `COMPANION`
- `ADVERSARY`
- `PERSONAL_SPACE` (Safe Room)

Current CSS hides the crawler tab bar and crawler tab viewport in Companion and Adversary mode. Safe Room also hides the normal crawler tab system. A new header must remain usable when the crawler tabs disappear.

### Five-stat model

The source uses only:

- STR
- INT
- CON
- DEX
- CHA

Do not add Agility, Stamina, Perception, Luck, Wisdom, or a sixth Stat based on generated imagery.

## 4. Header / banner normalization

### Approved visual intent

Keep:

- cinematic race image as the primary background;
- class as secondary environmental/symbolic overlay;
- strong dark-metal outer frame;
- DCC brand plate;
- compact identity plaques shifted toward the left/center;
- open art area on the right for race silhouette/emblem and class treatment;
- restrained selected-tab glow.

### Required R42 relationships

The new proof must preserve:

- character avatar;
- entity-mode selector;
- derived crawler identity;
- Player-Killer marks;
- race display;
- class display;
- level;
- floor;
- disabled Level-Up placeholder.

The banner artwork is a skin around these relationships, not a new data model.

### Rejected mockup carry-over

Do not carry forward:

- header Health or Mana;
- header core-stat tiles;
- selectable Race/Class fields in the header;
- `Survive / Adapt / Entertain` slogan;
- old Overview / Notes / Quests navigation;
- banner-specific mechanics.

## 5. Character tab normalization

### R42 systems that must remain visible

Character currently owns:

1. **Crawler Identity**
   - Name
   - Race selector
   - Class selector
   - Level
   - Floor
   - Gender
   - Crawler Number
   - Size

2. **Race/Class summary rail**
   - current race identity / state
   - current class identity / category / type
   - custom Race entry
   - race-specific controls such as City Elf allocation and Lajabless aspect when gated

3. **Race Setup**
   - persistent race-specific choices and inherited configuration
   - shown only when applicable

4. **Class Setup**
   - eligibility, source review, prerequisite confirmations, class choices, access checks, and gated class configuration
   - shown/collapsed through the existing setup gates

5. **Core Stats**
   - Base
   - Enhanced
   - Modifier
   - Stat Check
   - STR / INT / CON / DEX / CHA

6. **Buff / Debuff Management**
   - `repeating_internalbuffs`
   - `repeating_externalbuffs`
   - `repeating_debuffs`
   - source-aware and mechanically active status relationships

7. **Floor Progression**
   - Descend Floor
   - end-of-floor advancement state

8. **Advancements**
   - `repeating_advancement`
   - explicit Advancement checks

9. **Other Stat Bonuses**
   - advanced/fallback stat adjustments
   - Armor DR / DR Buff / Total DR

10. **Crawler Profile / Long-Term State**
    - race profile and integrated Race actions
    - class profile and automated/manual Class rules
    - shared daily ability state
    - class-specific lifecycle controls
    - benefits/access entitlements
    - crawler notes

### Approved mockup elements that survive

- compact five-stat visual treatment;
- strong Character identity/profile visual hierarchy;
- status/provenance pills;
- quieter body panels under a dramatic header.

### Required corrections to the approved Character mockup

- **Remove Health Bar slots from Character.** The existing Health Bar is on Combat.
- **Remove the generic Features & Traits repeating panel.** There is no matching generic repeating section; use the actual Race/Class profile and benefits/access systems.
- **Remove the embedded Chat Card panel.** Chat visuals belong in the roll-template specimen, not as a Character-tab system.
- **Add the real Race Setup and Class Setup relationships.**
- **Add Buff/Debuff Management, Floor Progression, and Advancement access.**
- The stat treatment may be compact, but Base / Enhanced / Mod / Check cannot be discarded.

## 6. Combat tab normalization

### R42 panel ownership

Combat currently contains:

1. **Status / Live**
   - Health percentage
   - DR
   - AI Favor display
   - Move
   - Step
   - internal/external Buff counts
   - current/max Mana and Mana spend
   - Injuries
   - Player Kill controls
   - the existing 10 Health Bar slots
   - post-defense damage and healing controls
   - compact Buff/Debuff mirrors

2. **Evade / Injuries / Rest**
   - Evade roll
   - pending advantage
   - injury queue / resolution
   - manual injury controls
   - Short / Long / Full Day Rest
   - Regeneration recovery controls
   - Mana-recovery environment state

3. **Spell Casting Resolution HUD**
   - prepared spell
   - casting data
   - Mana cost
   - targeting/range/area
   - spell-specific gates
   - Cast / Damage
   - GM degree controls
   - second-attack resolver where applicable

4. **Combat Modifiers**
   - combat modes
   - movement / position
   - class context
   - race context
   - active modifiers / clear
   - class-specific gated resolvers
   - class lifecycle / rewards

5. **Companion Control**
   - `repeating_companioncontrollers`
   - add/collapse companion
   - command/control relationship only; full companion stats live on separate actor sheet

6. **Combat Actions**
   - `repeating_combatactions`
   - collapse all
   - add Combat Action
   - add Companion
   - End Combat
   - ATK
   - DMG
   - Double Tap when eligible

7. **Defense / Interrupts / Combat Utilities**
   - Catcher
   - Shield Block / Shield Bash
   - Attack of Opportunity
   - Zone of Control
   - Ropework
   - Throwing
   - Dodge
   - Taunt

8. **Action Reference**
   - quick CRB reminders

### Approved mockup elements that survive

- large Health Bar treatment inside Combat;
- compact Mana/casting area;
- clear Combat Status hierarchy;
- action-deck presentation;
- strong Defense/Interrupts block;
- source-aware modifier presentation.

### Required corrections to the approved Combat mockup

- Remove the invented `+ ADD` control from the Active Effects / Modifiers panel. Current Combat modifiers are explicit existing context controls, not a generic repeating effect list.
- Do not replace actual Combat Action controls with a single generic `ROLL`. Preserve ATK / DMG / DOUBLE TAP state and the real row relationships.
- Do not invent generic actions such as Defend or Ready as permanent system rows unless they are represented by real current actions.
- Remove the on-sheet Roll/Chat Preview panel. Chat output is a separate template surface.
- Restore Spell Casting Resolution, class/race context, lifecycle/reward controls, Companion Control, and Action Reference.

## 7. Skills & Spells normalization

### Current structure

The page contains:

- Skill Library: `repeating_skills`
- conditional Skill Detail panel
- Spell Library: `repeating_knownspells`

The Skill Detail panel is correctly **hidden until a Skill's DETAIL action opens it**:

- `attr_vn_focus_open = 0`: Skill Library expands to full width and Skill Detail is hidden.
- `attr_vn_focus_open = 1`: wide layout becomes library + detail; at <=900 px it stacks to one column.

### Skill Library controls that are real

Top controls:

- filters: ALL / ATTACK / DAMAGE EFFECT / UTILITY / PASSIVE / ACTIONABLE / MARKED
- Search / Clear
- Collapse All
- `+ADD SKILL`
- Sort A-Z

Per-row summary/control state:

- Skill name
- action/type pill
- family pill
- Rank
- optional CAP 20
- Stat
- Check
- row-level **ADVANCE** heart/checkbox when eligible
- **DETAIL**
- **ROLL** when rollable
- **ADD COMBAT** when it is an eligible Attack

### Spell Library controls that are real

Top controls:

- filters: ALL / ATTACK / PASSIVE / CHECK / HEAL / AREA
- Search / Clear
- Collapse All
- `+LEARN SPELL`
- Sort A-Z

Per-row summary/control state:

- Spell name
- type pill
- family pill
- Rank
- Mana
- range/geometry
- row-level **ADVANCE** heart/checkbox when eligible
- **PREP**
- **HOT**

Expanded spell rows expose the spell selection, rank, What It Does, Check, Base, Favored, State, Advancement, and upgrade/progression text.

### Corrections to the approved Skills & Spells mockup

- **Keep the stacked Skill Library above Spell Library direction.**
- Remove the mockup's global `ADVANCED` toggle. Advancement is per row through `attr_improve`.
- Keep `DETAIL / ROLL / ADD COMBAT` on Skill rows because those actions exist.
- For Spell rows, do **not** add separate DETAIL or ROLL actions in the new proof. Current R42 exposes PREP and HOT; the row itself expands/collapses for detail and casting resolves through Combat.
- Use the actual `+LEARN SPELL` action label unless the engineering stream later renames it.
- Source/type/status pills may be visually rich, but they must bind to actual type/family/rank/source data rather than invented Race/Class/Background categories.

## 8. Inventory normalization

### R42 systems

1. **Equipped Gear**
   - canonical active sources
   - Head / Torso / Arms / Legs / Feet / Gloves
   - Hand 1 / Hand 2 / Hand 3 / Hand 4
   - accessory loadout and capacity
   - gear-dependent Combat readiness
   - active equipment effects
   - loadout validation

2. **Hotlist**
   - exactly 10 ready slots
   - each slot retains source linkage and action state
   - Use/linked action + Clear

3. **Canonical Inventory**
   - `repeating_inventory`
   - Gold / Misc Junk / lift-limit state
   - filters for All, Gear, Weapon, Armor, Consumable, Spell Item, Explosive, Material, Upgrade, Quest, Misc, Loot Box, Equipped, Hotlist
   - Collapse All
   - `+ ADD ITEM`
   - `+ ADD LOOT BOX`
   - Sort A-Z / Sort Type
   - row actions: Use, Equip, Unequip, Hotlist, Junk It, Sell It, Open in Safe Room / Ready state as gated

4. **Spell Scrolls**
   - `repeating_spellscrolls`
   - Add Scroll
   - Prep
   - Hot

5. **Spellbooks**
   - `repeating_spellbooks`
   - Add Spellbook
   - Learn Spell

### Corrections to the approved Inventory mockup

- Keep the strong Inventory Library / Equipped Gear / Hotlist / Scrolls-Spellbooks visual separation.
- The mockup's generic Search field is not currently implemented in R42 Inventory.
- The mockup's generic `DETAIL` and `DROP` actions are not R42 Inventory actions.
- Use the actual action vocabulary: Use / Equip / Unequip / Hotlist / Junk It / Sell It / Safe Room box actions.
- Loot Boxes are canonical Inventory records; do not create a second independent Loot Box database.
- A visually separated Loot Box region may only be a presentation/filter of canonical Inventory state.
- Loot Box opening/resolution belongs to Safe Room, not ordinary Inventory.

## 9. Achievements normalization

### R42 systems

The Achievements tab owns three distinct canonical systems:

1. **Titles**
   - `repeating_titles`
   - one displayed Title at a time
   - `DISPLAY TITLE`
   - `CLEAR DISPLAY TITLE`
   - Player Killer Title may be system-managed

2. **Achievements**
   - `repeating_achievements`
   - `+ ADD ACHIEVEMENT`
   - Sort A-Z
   - Create Reward Box
   - Grant Title
   - Announce to Chat
   - reward bridges track created-state IDs to avoid duplicate grants

3. **Quests**
   - `repeating_quests`
   - `+ ADD QUEST`
   - Sort A-Z
   - Complete Quest
   - Fail Quest
   - Reopen / Set Active
   - Create Quest Box
   - Create Linked Achievement
   - Active / Completed / Failed lifecycle

### Corrections to the approved Achievements mockup

- Keep the three-area composition: Achievements, Titles, Quests.
- Remove the invented search controls unless later added in production.
- Remove `+ ADD TITLE`; Titles are owned/granted records and currently do not have that custom action.
- Replace generic Achievement `DETAIL` with the actual expandable record/actions.
- Replace generic Quest `CLAIM` with the actual Complete / Fail / Reopen / Create reward bridges.
- Do not display arbitrary stat bonuses as if every Achievement directly mutates the sheet; reward state is explicit and typed.

## 10. Deities normalization

### Current R42 worship model

The tab currently uses one source-backed Deities/Worship foundation with:

- Deity selector:
  - Apito
  - Eileithyia
  - Emberus
  - Eris
  - Grull
  - Hellik
  - Nekhebit
  - Ogun
  - Taranis
  - Custom / GM-specified
- Custom/other deity name
- Church Rank:
  - Acolyte / Tier 1
  - Devotee / Tier 2
  - Zealot / Tier 3
- Consecutive Devotion Days
- Missed Daily Offerings
- Zealot Exception checkbox
- Worship State / rule note
- deity profile fields:
  - deity / symbol
  - temple / High Supreme Cleric
  - daily offering / rival
  - signature Skills / signature Stat
  - likely Sponsor
  - tithe / boon reference
- Acolyte / Devotee / Zealot benefit text
- Current Rank Rules
- Current Deity Benefits
- Core Obligations
- explicit automation-boundary text

R42 intentionally leaves deity-specific mechanical effects reference-only where the worker does not own them.

### Approved Deities visual idea that survives

The Deities mockup's hierarchy is strong:

- worship setup strip;
- deity profile;
- rank/tier benefits;
- obligations/current requirements.

That hierarchy may be used to **rearrange the existing fields visually**.

### Required corrections

- Replace invented `The Frozen Weave` content with real catalog/custom state.
- Do not invent Rank IV / V beyond the current three church ranks.
- Remove mockup-only `LOG DAY`, `OFFER`, `PRAY`, and `VIEW FULL TREE` buttons; R42 has no corresponding actions.
- Do not turn reference-only deity effects into automatic bonuses.
- The Arachnid/Blizzardmancer race/class theme belongs to the header; the Deities body remains the shared DCC component system.

## 11. Socials normalization

### Clubs

The existing club badge rail is authoritative and already matches the user's preferred logo-forward visual treatment.

The six existing badges are:

1. ALL CLUB ACCESS
2. CLUB VANQUISHER
3. THE DESPERADO CLUB
4. BOOK OF THE FLOOR CLUB
5. GUILD OF SUFFERING
6. NAUGHTY BOYS EMPLOYMENT AGENCY

Each badge has:

- an existing Roll20-hosted logo;
- an access visibility gate;
- locked anonymous/grey presentation when unavailable;
- full-color named state when access is surfaced;
- source/provenance text when present.

The footer includes the surfaced club summary and `GM // SPECIAL MEMBERSHIP ACCESS`.

**Do not replace these with invented club brands from generated mockups.**

### Public Profile / Popularity / Top Ten

Current state includes:

- `attr_popularity`
- official Top Ten rank, Floor 4+
- Top Ten status
- Sponsor-advantage eligibility reference
- current public bounty
- public HUD listing
- GM rank review controls
- Floor-exit Venison income and award bridge
- local `repeating_toptenboard` snapshot with max ten rows
- Rank / Name / Race / Class / Level / derived Bounty / notes

The approved circular Popularity presentation can be retained as a visual readout, but generated `Known / Noted / Renowned` tier bands are not current R42 state and should not be presented as mechanics unless later implemented.

### Sponsors

Current `repeating_sponsors` supports:

- up to three active Sponsors;
- prospective interest before sponsorship is active;
- current floor state;
- Playing-to-Sponsors reference;
- catalog selection / custom override;
- type;
- reason;
- contract state;
- Benefactor Box tier;
- demands/complications/notes;
- Sign / Activate;
- Sponsor Drops Crawler;
- Transfer / End;
- GM Send Benefactor Box.

The final Socials layout decision is retained: Sponsors should sit beside Media/Interviews below the Club rail.

### Media / Interviews

This is deliberately a **deferred integration destination**. Current R42 explicitly defers Interview Shows, Playing to Cameras, AI Favor, recap/media resolution, and automated Sponsor consequences.

The mockup's coming-soon treatment is therefore appropriate. Do not create fake interview controls.

### Required Socials corrections

- Keep the final layout: profile/popularity at left, wide club badge rail, Media and Sponsors adjacent below.
- Use the six actual club badges and names.
- Remove Quick Links.
- Remove mockup-only Sponsor Guide controls.
- Do not let a simplified profile card hide the actual Top Ten rank-review/bounty/Venison/leaderboard state. Those can be nested/collapsed, but they must remain reachable.
- No Overview or Notes tab.

## 12. Entity-mode surfaces that the new visual system must not break

### Companion

Current alternative actor view:

- Companion Actor
- Pet / Mount / Minion subtype
- Control / Source command state
- `repeating_entityattacks`
- Roll Check / Roll Damage

### Adversary

Current GM actor view:

- Adversary Actor
- Mob / Elite / Boss subtype
- `repeating_adversaryattacks`
- `repeating_adversaryclues`
- Roll Damage
- Clues / Intel

### Safe Room / Personal Space

Current view owns the Loot Box lifecycle:

- Enter Safe Room / Return to Crawler & Inventory
- Loot Resolution
- GM Spell Selection
- Random Magic Resolution
- Owned Loot Boxes
- `repeating_saferoomboxes`
- Open Box / Mark Ready
- Finalize / Complete / Cancel flows

The new asset/chrome system must support these actor modes even though the first rendering proof does not need to beautify all of them at once.

## 13. Roll20 structural constraints for the next visual proof

The next proof may restyle and wrap existing surfaces, but must treat these as protected relationships:

- all existing `attr_*` names;
- all existing `act_*` names;
- all `repeating_*` section names;
- hidden state/gate inputs;
- sibling order where CSS uses gate + sibling selectors;
- tab numeric mapping;
- entity-mode visibility behavior;
- source/provenance fields;
- worker-owned derived fields;
- action-result state;
- current conditional controls.

Important CSS relationships already in use include:

- tab buttons selected by adjacent hidden `sheet-vn-tabstate`;
- pages shown by adjacent hidden `sheet-vn-pagestate`;
- Skill Detail shown by `attr_vn_focus_open`;
- many action buttons shown/hidden by hidden gate inputs;
- club logos shown/obscured by access gate state;
- responsive club rail: 6 columns normally, 3 <=900 px, 2 <=520 px;
- Inventory two-column top layout collapses at <=850 px;
- Skills detail layout collapses at <=900 px;
- crawler tabs wrap to 4 columns <=700 px and 3 columns <=500 px.

A visual implementation should prefer **adding styling hooks/classes** over rearranging gate/control adjacency.

## 14. Approved visual references after normalization

The following mockups remain useful as visual references, but only after applying this audit:

- Character: `tigran_tiger_character_sheet_interface.png`
- Combat: `tiger_berserker_combat_interface.png`
- Skills & Spells: `necromancer_skills_spells_dashboard.png`
- Inventory: `necromancer_s_crocodilian_inventory_ledger.png`
- Achievements: `arachnid_blizzardmancer_achievement_dashboard.png`
- Deities: `frozen_weave_deity_character_sheet.png`
- Socials: `z_thax_s_icy_socials_profile.png`

Their **composition, chrome, density, hierarchy, race/class banner language, and component styling** are the approved design material.

Their generated example mechanics, extra tabs, fake buttons, sample catalogs, and invented state are not authoritative.

## 15. Step-1 result / gate for the new Roll20 proof

**PASS — ready for Step 2.**

The visual direction can be built on top of R42 without redesigning the game systems, provided the next Roll20 proof follows these rules:

1. build around the real header and seven-tab relationships;
2. preserve avatar/entity/PK/state relationships;
3. use actual tab content and actions rather than the generated mockup mechanics;
4. use the cinematic race banner and separate class overlay only as visual layers;
5. keep Health/Mana in working content, never the header;
6. retain collapsible/detail/gated behavior rather than flattening it into static panels;
7. keep canonical repeating sections as the source of truth;
8. treat Safe Room as the Loot Box resolution owner;
9. preserve the real club logo rail and Socials provenance;
10. keep deferred systems visibly deferred.

**No production implementation was performed. Step 2 — the fresh Roll20 rendering proof — has not started.**
