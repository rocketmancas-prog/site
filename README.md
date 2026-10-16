# Quotex India landing page

Responsive static website in English and Hindi. No build step, package installation, API keys or backend required.

## Local development

From `/workspace/site`, run:

```sh
python3 -m http.server 3000 --bind 0.0.0.0
```

Serve `index.html`, `style.css` and `app.js` together on any static host. HTTPS enables the clipboard feature. Language preference is stored locally in the browser. Optional Google Fonts have system-font fallbacks.

All call-to-action destinations are configured in `app.js`. The chart is illustrative; the page does not provide live prices, authentication or payment processing. Offer availability is not asserted. No analytics or tracking scripts are installed.
