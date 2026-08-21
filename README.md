# Andrew & Megan's Joint Bach Party Weekend

Single-page site for the Sep 18–20, 2026 joint bach party in Des Moines, Iowa.
Replaces the couple's Canva site and merges in two features built since: the
"Der Zapfhahn" Oktoberfest persona generator and the guys' Friday-morning ballot.

## Layout

- `index.html` — the entire site. One file, inline CSS/JS, no build step.
  The only permitted external request is Google Fonts.
- `docs/CONTENT.md` — the locked content inventory, recovered from the incumbent
  Canva site's embedded document model. Treat it as fact; `[PENDING]` means
  genuinely unfinished and must render as a visible TBD.
- `docs/SPEC.md` — the build contract (constraints, IA, behaviour, design direction).
- `docs/photos.json` — 29 roster portraits as WebP data URIs, keyed by person name.
- `docs/inject-photos.py` — injects `photos.json` into the `photo-data` block in
  `index.html`. Idempotent; re-run after any edit that touches that block.

## Editing

Edit `index.html` directly. If you regenerate it from the spec, re-run:

    python3 docs/inject-photos.py

## Deploy

    vercel --prod

`index.html` is served untouched.

## Notes

- Roster phone numbers exist in the incumbent site but are deliberately NOT published here.
- Four people have no photo on the incumbent site and render as a monogram:
  Kenzie Nilles, Cindy Elgersma, Quinten Wynia, Jackson Agey.
- `vercel.json` sets `X-Robots-Tag: noindex, nofollow` so the page stays out of search results.
