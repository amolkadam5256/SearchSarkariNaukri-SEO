# 5. hreflang / International SEO

**Priority: 🟠 Medium**

## The problem
Current hreflang tags on the homepage:
```html
<link rel="alternate" hreflang="en-IN" href="https://www.searchsarkarinaukri.com/" />
<link rel="alternate" hreflang="mr-IN" href="https://www.searchsarkarinaukri.com/" />
<link rel="alternate" hreflang="x-default" href="https://www.searchsarkarinaukri.com/" />
```
The hreflang validator flags a warning: **missing a region-independent
link for each language** — Google's guidance recommends including a
plain-language tag (`en`, `mr`) in addition to the region-specific one
(`en-IN`, `mr-IN`) when you're not also serving other regional variants of
that language (e.g. `en-US`, `en-GB`).

## The fix
Add two more `<link>` tags so the full set becomes:
```html
<link rel="alternate" hreflang="en" href="https://www.searchsarkarinaukri.com/" />
<link rel="alternate" hreflang="en-IN" href="https://www.searchsarkarinaukri.com/" />
<link rel="alternate" hreflang="mr" href="https://www.searchsarkarinaukri.com/" />
<link rel="alternate" hreflang="mr-IN" href="https://www.searchsarkarinaukri.com/" />
<link rel="alternate" hreflang="x-default" href="https://www.searchsarkarinaukri.com/" />
```

### Important context specific to this site
Your English and Marathi content currently appear to live on the **same
URL** (self-referencing hreflang for both `en-IN` and `mr-IN` point to
`/`). This only makes sense if:
- (a) the page is genuinely bilingual (English + Marathi content mixed on
  one page, which your homepage content sample confirms — e.g. headings
  like "भरती जाहीर २०२६" mixed with English job titles), **or**
- (b) you intend to eventually split into separate English-only and
  Marathi-only URLs.

If (a) — keep hreflang as a light signal but don't expect it to do much
work, since hreflang is designed for **separate URLs per
language/region**, not one bilingual URL serving both.

If you later build true separate-language URLs (e.g.
`/mr/jobs-in-nashik` for a Marathi-only version), hreflang becomes far
more valuable — each language version should reciprocally reference all
others:
```html
<!-- On the English version -->
<link rel="alternate" hreflang="en-IN" href="https://www.searchsarkarinaukri.com/jobs-in-nashik" />
<link rel="alternate" hreflang="mr-IN" href="https://www.searchsarkarinaukri.com/mr/jobs-in-nashik" />
<link rel="alternate" hreflang="x-default" href="https://www.searchsarkarinaukri.com/jobs-in-nashik" />

<!-- On the Marathi version -->
<link rel="alternate" hreflang="en-IN" href="https://www.searchsarkarinaukri.com/jobs-in-nashik" />
<link rel="alternate" hreflang="mr-IN" href="https://www.searchsarkarinaukri.com/mr/jobs-in-nashik" />
<link rel="alternate" hreflang="x-default" href="https://www.searchsarkarinaukri.com/jobs-in-nashik" />
```

## Implementation checklist
- [ ] Add the two region-independent `en` / `mr` tags to the existing
      template (quick fix, ship first).
- [ ] Make sure hreflang tags are present in the **server-rendered** HTML
      (ties to file 01) — if they're injected only by client-side JS,
      many crawlers won't see them at all.
- [ ] Decide whether to keep the bilingual single-URL model or split into
      dedicated language paths — this is a bigger content-architecture
      decision, not a quick technical patch.
- [ ] Re-validate with a hreflang testing tool after deployment and
      confirm 0 warnings.
