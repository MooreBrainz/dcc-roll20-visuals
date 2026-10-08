# VIS-22 — Engraved Navigation and Action Controls

**Status:** CSS implementation committed to the visual Roll20 proof; live Roll20 review required.  
**Boundary:** Visual proof only. No source R42 HTML/CSS/worker, data bindings, action names, mechanics or tab state mappings were modified.

## Visual direction

The review of VIS-21E established that bright gold/orange chrome was uncomfortable over dense working areas. VIS-22 applies that lesson to navigation and controls:

- All seven navigation plates receive dark, distressed metal using the existing `field-frame-dark.png` with a charcoal scrim.
- The currently selected **working preview** tab uses `field-frame-active.png` with stronger dark scrim and a subdued warm-bronze edge, not a broad neon glow.
- The four unimplemented preview tabs remain inert `<span>` elements; the three existing working preview tabs remain clickable `<label>` elements mapped to their original radio controls. No fake page functionality is introduced.
- Navigation hover and keyboard-focus highlights are limited to active/clickable labels.
- Representative buttons use a shared angular beveled-metal control style (about 31px min-height) for compact dense layouts.
- `+ ADD SKILL` / `+ LEARN SPELL` and `HOT` receive quiet warm-bronze priority.
- `ROLL` uses readable steel; `ADD COMBAT` uses muted rust; `DETAIL`, `PREP`, `CHECK` and `SEARCH` remain neutral.
- Disabled buttons have distinct subdued treatment, and keyboard focus receives a visible outline.

## Implementation

**Changed:** `roll20-preview.css` only. A single, labeled `VIS-22 / ENGRAVED NAVIGATION AND ACTION CONTROLS` section appends theme overrides. It reuses these already committed assets:

- `assets/chrome/fields/field-frame-dark.png`
- `assets/chrome/fields/field-frame-active.png`

No new raster files were necessary. The previous muted chrome and page nameplates remain in place.

**Important:** Action buttons in VIS-20 are visual layout proofs. There is no embedded R42 sheet worker and VIS-22 does not claim these actions actually perform Roll20 mechanics.

## Local smoke inspection (not Roll20)

A separate stand-alone Chromium navigation/controls specimen was rendered with the same source chrome imagery and tab/action design rules at:

| Viewport | Tabs per row | Tab label overflow | Document horizontal overflow |
| --- | --- | --- | --- |
| 1450px | 7 | None | None |
| 950px | 4 | None | None |
| 550px | 2 | None | None |
| 320px | 2 | None | None |

A <=390px responsive font/padding adjustment was included for long labels such as Achievements.

This local sample reproduces the control styling, **not the entire proof or Roll20's sanitization behavior**. Browser rendering at these sizes does not establish live Roll20 compatibility.

## Roll20 review checklist

1. Copy the newest `roll20-preview.css` into the disposable visual-proof Roll20 sandbox; **leave HTML unchanged**.
2. Confirm all seven tabs display engraved dark-metal plates and only Character / Skills & Spells / Socials are clickable in this limited proof.
3. Switch among the three working pages: the selected plate should be warm but not aggressively illuminated.
4. Inspect Skill Library `+ ADD SKILL`, `DETAIL`, `ROLL`, `ADD COMBAT`; Spell Library `+ LEARN SPELL`, `PREP`, `HOT`.
5. Check keyboard focus, narrow Roll20 window wrapping, and label readability.
6. Confirm the muted panel frames and page title nameplates remain unchanged.

**Stop/adjust criteria:** Too much amber light, stretched tab corners, lost text contrast, collapsed action labels, misleading appearance of inactive preview tabs, or any change in the proof's navigation behavior.

No production promotion is implied by a successful visual review.
