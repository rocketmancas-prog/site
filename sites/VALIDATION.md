# Neon design verification

Validated all three generated sites in installed Chromium after applying the neon styling and radial image masks.

- English and Hindi at viewport widths 320, 390, 768, 1024, 1440 and 1920 pixels: no horizontal document overflow.
- Each site retains 1 H1, 11 H2 and 33 H3 headings; all 45 explanatory sections render at least 600 characters in both languages.
- Hero images load and use a radial alpha mask; desktop and mobile screenshots were visually inspected.
- Menu opens, closes with Escape and closes after selecting a section.
- Language preference persists on reload; promo-code copying returns `bingame`.
- All partner buttons retain the supplied destination URL; no JavaScript page errors were observed.
- Internal fragment targets and all referenced local assets return successfully; icon and manifest files remain included.
- JavaScript syntax checks passed for all three generated scripts.
- Individual deployment ZIPs and the combined ZIP passed integrity and file-content checks.

These checks validate the local static sites. Domain DNS, hosting, the destination platform's registration/payment flows and search rankings are outside this validation.
