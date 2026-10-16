# Three Quotex sites

Independent static site folders and matching deployable ZIP files:

- `quotexreview.in/`: a review of interface, account and practice checks.
- `quotexguide.in/`: a step-by-step registration, login and demo guide.
- `quotexhub.in/`: a resource page explaining account areas and trading terminology.

Each site contains its own HTML, CSS, JavaScript, robots.txt and sitemap.xml. English text is present directly in HTML; Hindi is selected through the language menu. Each main section contains at least 600 characters in each language. No build service, API keys or database are required. Optional Google Fonts fall back to system fonts.

## Preview and deployment

Run `python3 -m http.server 3000 --bind 0.0.0.0` from `/workspace/site`. Each site is served at `/sites/<domain>/`. For production, upload the **contents** of the relevant folder or ZIP to that domain's web root. Configure HTTPS in your hosting control panel; browser clipboard access requires a secure context. Configure DNS with the actual hosting provider's values. DNS, TLS and public deployment have not been performed here.

The affiliate destination and bingame promo code are preserved across all sites. No offer amount, guaranteed returns or official affiliation is asserted. Registration and account actions take place on the destination site.

## Editing

`content.json` stores the site metadata and initial editorial copy. `expanded.py` defines the expanded H1/H2/H3 structure, English/Hindi topic explanations and site-specific heading variants. Each site has 1 H1, 11 H2 and 33 H3 headings, with at least 600 characters of explanatory copy directly below each heading. A section navigation menu helps readers move through the long page. `python3 sites/build.py` from the repository root regenerates the three folders and ZIPs using the original root layout/runtime. Back up direct edits in generated folders before rebuilding. No package installation is needed.

Validation: JavaScript syntax, all section lengths, uniqueness across sites, static metadata, local HTTP responses and script-driven language/link/clipboard handlers. The redesigned pages were also checked in the installed Chromium browser at phone, tablet and desktop sizes in both languages, including menu opening/closing, language persistence and clipboard copying. `design.py` defines the screenshot-inspired layout and shared Quotex palette; `hero-trader.png` is the generated decorative hero illustration.
