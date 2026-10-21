# DCC Action Tracker — E08 R6 LIVE-TRUSTED

Status: **USER-APPROVED LIVE-TRUSTED**, 2026-10-20 (user confirms visuals and mechanics work in live Roll20).

**Release artifact:** `DCC_Action_Tracker_E08_R6_TEST_CANDIDATE.zip` (complete package held in the conversation). This GitHub release record documents the verified package, but **the actual ZIP and JavaScript have NOT yet been uploaded to GitHub**. Do not mistake this manifest for a full source-code backup.

## Frozen artifact checksums (SHA-256)

- E08 R6 JavaScript (`DCC_Action_Tracker_E08_R6.js`): `83113f0e95a259abb471d84e1dcb80830f3b580fa6671bba133ed93b98150c50`
- ZIP (`DCC_Action_Tracker_E08_R6_TEST_CANDIDATE.zip`): `87df3e798079ad891c0aa4e88fd8a9a92f3f1b609a3a4825b2db181440001a59`
- Approved HUD PNG (`cyberpunk_dcc_combat_actions_hud.png`): `e6425e84888cba1156be5e59200164ef4e50ccceacc33f2db65a74463c5cd4b4`

## Locked requirements

- Six Roll20 grid squares wide by eight high (420 × 560 at 70px per square).
- Five crawler rows; champagne-gold names with magenta aura treatment.
- Two cut-corner gold standard-action pips per crawler, exposing baked-in red X sockets when spent.
- Separate Surprise and Bonus indicators, both usable concurrently.
- Token-verified player use/undo; GM grants (individual and all); encounter reset to Round 01; persistent roster, Roll20-registered artwork URL, and GM footprint.
- Existing chat command prefix `!dcc07`, including `!dcc07 grantall bonus`, `!dcc07 grantall surprise`, and `!dcc07 encounter reset`.
- Image source master belongs in this repository, runtime image is imported once to the Roll20 Art Library.

## Change control

Freeze E08 R6 exact source and assets; develop any improvements as newer test candidates. Do not overwrite the approved baseline. Recheck the checksums before treating a copied ZIP or script as identical.

## Archival gap

The connected GitHub file-writing interface presently supports UTF-8 text creation but does not transfer local binary files. Upload the original ZIP from this conversation to the release folder through GitHub's web uploader to complete the archival copy; alternatively commit both the JS and PNG separately with exact bytes. Only then can this release be considered fully backed up on GitHub.
