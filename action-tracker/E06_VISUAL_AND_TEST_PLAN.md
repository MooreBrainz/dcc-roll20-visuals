# DCC Action Tracker E06 — Test candidate

**Do not promote.** E04 remains the trusted positioning baseline; E05 has passed most live tests but its typed SET command is rejected. E06 is a separate new script and uses `!dcc06` commands to avoid interference.

## Approved artwork

Reference: transparent PNG artwork generated in this conversation, 1774 × 887 pixels (2:1 aspect ratio). The binary PNG is **not yet uploaded into GitHub**; do not claim this document or a link to it represents the binary.

Art requirements:
- Five fixed empty crawler name fields with no baked player numbers or names.
- Empty dynamic ROUND-number box.
- Two standard gold pip locations in each row.
- Quiet, compact SPECIAL slot: magenta starburst Surprise, teal Bonus indication. Icons light only when granted.
- True alpha transparency around the HUD, not a scene/background.
- Artwork is an underlying static skin. API overlays names, round, pip states, and special tokens.

## E06 manual actions

- Players: select their Roll20 Character token, `!dcc06 use` or `!dcc06 undo`.
- GM: `!dcc06 add Exact Character Name`, `!dcc06 remove Exact Character Name`, `!dcc06 anchor`, `!dcc06 on`, `!dcc06 off`, `!dcc06 reposition`, `!dcc06 round`, `!dcc06 reset`, `!dcc06 status`.
- GM with selected controlled character token: `!dcc06 grant bonus`, `!dcc06 grant surprise`, `!dcc06 take bonus`, `!dcc06 take surprise`.
- GM: `!dcc06 phase surprise` / `!dcc06 phase normal`.
- When the artwork is publicly hosted with a Roll20-usable URL: `!dcc06 art https://.../asset.png`.

**Test gate:** script installation and fallback panel, five-row roster, action use/undo, permission checks with two player accounts, bonus and surprise accounting, surprise-phase gating, round reset, page change, art URL rendering and GM footprint location.

## Important behavior

E06 uses two base Actions per crawler each round; bonus/surprise pools are separate. Surprise can be spent only in the Surprise phase; during the normal phase, Bonus is spent before Base. Undo reverses the last spend by that crawler in the same round. Next Round clears both special pools. None of this is linked to character sheet rolls.

No automatic promotion; verify in Roll20 first.
