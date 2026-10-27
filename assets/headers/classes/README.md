# Class atmosphere overlays

Class overlays are subtle transparent graphical treatments composited over both the race background and race character, but **below interactive sheet controls**. These are not scene art or stand-alone frames. Preserve character faces and the legibility of Crawler/Race/Class/Level fields.

- Path convention: `<class-slug>/overlay.webp`
- First class: Blizzardmancer (`blizzardmancer/overlay.webp`)
- Overlay opacity: start at 0.18 (18%) and tune in live Roll20 visual tests; keep a conservative ceiling of 0.25.
- The asset is 1920×240 transparent WebP, sized to match the wide, shallow 1280px header with CSS `background-size:100% 100%` and `pointer-events:none`.
- One class overlay at a time, driven by the sheet's existing Class selection; if unset or unrecognized, omit it.
- The existing Race imagery is independent and must remain unchanged.
