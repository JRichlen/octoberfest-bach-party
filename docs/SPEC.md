# BUILD SPEC — Andrew & Megan's Joint Bach Party Weekend
Single-page site. `docs/CONTENT.md` is the locked content authority — read it first, in full.

## Hard technical constraints (non-negotiable)
- ONE static HTML file: `index.html`. Inline CSS, inline JS. No build step, no backend.
- No browser storage of any kind (no localStorage/sessionStorage/cookies/IndexedDB).
- The ONLY permitted external requests are Google Fonts (fonts.googleapis.com / fonts.gstatic.com).
  Everything else — images included — is inlined.
- Deploys to Vercel as `index.html` untouched. Must also open correctly from `file://`.
- Mobile-first, designed at 380px. Tap targets >= 44px.
- `prefers-reduced-motion: reduce` collapses all animation.
- Visible focus rings. Real `<label>`s bound to inputs. `aria-live` on generated content.
- Keyboard-operable throughout. No horizontal page scroll at 380px.

## Information architecture (this order)
Masthead (both taglines) -> jump nav -> sections:
1. The Tap — persona generator (the hero moment)
2. The Weekend — full itinerary, both parties
3. Weekend Attire — assigned-outfit grid
4. Things to Bring
5. The Stay — the Barndominium VRBO
6. Meet the Party — The Lads / The Ladies rosters
7. Budget & Venmo — all TBD
8. German 101 — glossary

There is NO ballot / vote / RSVP form anywhere on this page. Friday is settled.
Nav must GROUP (eight raw links will not fit a 380px phone). E.g. a "Plan" group covering 2–5.

## Section 1 — The Tap (the signature moment)
Name in -> "Pour my fate" -> an Oktoberfest alter ego, revealed like something poured or tapped.
Baseline metaphor: a filling stein + a stamped beer-mat (Bierdeckel) card. Elevate it, but KEEP the pour.

LOCKED RULES:
- Deterministic. The persona is a pure function of a 32-bit hash of the name, lowercased and
  trimmed. Same name -> same fate, forever. NO reroll button. The page states this in copy.
- Use a real avalanche-quality hash (FNV-1a or xmur3), and derive each field from a DIFFERENT
  slice/advance of the hash state so fields are not correlated.

PAYLOAD (all required):
- Rank, in the format `Fassmeister — Master of the Barrel` (German title + em dash + English gloss)
- Festival name: [German given name] + von/zu/aus + [real Des Moines suburb], drawn ONLY from:
  Ankeny, Waukee, Grimes, Norwalk, Urbandale, Indianola, Johnston, Altoona
- An epithet
- Three stats, with plain-English labels on the face and the German in a legend:
  - litres before wobble — 1.0 to 6.5
  - shoe-slap skill — out of 10
  - cheers volume — 84 to 119 dB
- A Tracht line (what they are wearing)
- A Prüfung (dare) that is doable completely sober. At least one dare in the pool centres
  the root beer keg.
- A translated toast
- A "copy for the group chat" action producing PLAIN ENGLISH with ZERO German words.

Flavor text may be rewritten. Structure and rules may not. Pools should be large enough
(>= 16 ranks, >= 24 given names, >= 20 epithets, >= 16 dares, >= 12 toasts) that 33 guests
mostly get distinct results.


## Section 6 — Meet the Party (PHOTOS)
Two rosters, The Lads and The Ladies, names + roles exactly as in CONTENT.md.
Photos ARE included this iteration, recovered from the incumbent site.

Emit each roster entry with an image element shaped EXACTLY like this:

    <img class="roster-photo" data-person="Megan Elgersma" alt="Megan Elgersma" src="" hidden>

and a sibling monogram fallback element:

    <span class="roster-monogram" aria-hidden="true">ME</span>

Then include this EXACT script block near the end of body — a build step injects the data:

    <script id="photo-data" type="application/json">{}</script>
    <script>
    (function(){
      var P={};
      try{P=JSON.parse(document.getElementById('photo-data').textContent)||{};}catch(e){}
      document.querySelectorAll('img.roster-photo').forEach(function(img){
        var src=P[img.getAttribute('data-person')];
        if(src){img.src=src;img.hidden=false;
          var mono=img.parentNode.querySelector('.roster-monogram');
          if(mono)mono.remove();}
        else{img.remove();}
      });
    })();
    </script>

Do NOT put any image data in the file yourself — leave `photo-data` as `{}`.
Photos exist for 29 of the 33 people. These four have NO photo and must look intentional
via the monogram, never broken: Kenzie Nilles, Cindy Elgersma, Quinten Wynia, Jackson Agey.
Photos are candid group shots cropped to the person — style them as square, cover-fit,
consistent, and never stretched.

DO NOT publish anyone's phone number. The source had them; they are deliberately excluded.

## Design direction
- PRIMARY, locked in spirit: **Bavarian beer tent at night.**
  Ground near-black blue `#101a2e`, Bavarian blue `#2a5ca8`, foam cream `#f4efe2`,
  lager amber `#d99527`, gingerbread red `#b0342a`. Refine the values; keep the temperament.
- The incumbent Canva palette is the DAYTIME version of the same idea — cream `#eee2cd`,
  warm white, dusty blues (`#13417d`, `#3d87c3` were its actual inks). Use it where it serves:
  the Ladies' Friday column, the attire grid, The Stay may warm toward daylight
  cream-and-dusty-blue without breaking the night-tent frame.
- Do NOT import the incumbent's script fonts or wedding-soft styling. This is the party;
  the wedding website already exists.
- Fraktur EXACTLY ONCE (the masthead). Condensed grotesk for display, mono for data/stats.
- Lozenge (Bavarian diamond) pattern as a faint masked texture only — never a loud backdrop.
- ONE signature moment: the pour.
- Butter-amber CTAs. Square corners.
- Banned: gradient-mesh heroes, glassmorphism, the cream-and-terracotta default look.

## Tone
32-ish guests, ages ~19–60, Iowans, no German. Link arrives by group text; assume a 380px
phone and one thumb. Warm, funny, deadpan — the best man's party page, not the wedding website.
One guest does not drink; there is a root beer keg; alcohol-optional inclusion is a RUNNING JOKE,
never a disclaimer.

## The German rule (non-negotiable)
Every German word is glossed in English at first use, with a phonetic respelling wherever it
will be spoken aloud. Any text the user COPIES or SHARES must read clean with ZERO German.

## Acceptance checklist
- One HTML file; opens from disk; deploys to Vercel untouched
- Same name poured twice -> identical persona
- Every fact from CONTENT.md present and accurate; every [PENDING] a VISIBLE TBD; zero invented values
- NO lake-house / waterfront / dock / hot-tub copy anywhere
- Both Friday columns, all addresses, the currywurst caterer credit, the full attire grid, both taglines
- The lads' Friday is presented as a SETTLED, timed schedule — no vote, no ballot, no 'TBD' on it
- No unglossed German anywhere, including copied text
- 380px clean, >=44px targets, reduced motion, visible focus, keyboard-operable
- Footer: "Root beer counts. It has always counted."
