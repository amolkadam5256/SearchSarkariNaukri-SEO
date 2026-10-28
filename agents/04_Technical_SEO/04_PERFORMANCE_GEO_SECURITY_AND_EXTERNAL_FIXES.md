# Performance, GEO, Security And External Link Fixes

## Performance Issues

Reported:

- Site load speed can improve.
- Desktop PageSpeed Insights flagged poor.
- All page scripts complete around 5.5s.
- Rendered content percentage is 336%.

Good signals:

- Server response about 0.545s.
- All page content loaded about 2.5s.
- Download size about 0.80MB.
- HTTP/2+ enabled.
- Compression enabled.
- No JavaScript errors reported.
- No deprecated HTML reported.
- No inline styles reported.

## Performance Fix Plan

Inspect:

- Bundle size by route
- Third-party scripts
- Analytics duplication
- Client-rendered SEO sections
- Dynamic imports
- Images
- Fonts
- API/data requests
- Hydration warnings

Fix:

- Defer non-critical scripts.
- Remove duplicate script injection.
- Server-render critical SEO text and primary listings.
- Lazy-load non-critical below-fold widgets.
- Use route-level code splitting where supported.
- Avoid shipping large data blobs for all jobs.
- Cache stable taxonomy data.
- Compress and optimize images.
- Avoid duplicate API calls on initial load.

Do not:

- Remove important crawlable content.
- Hide sections only to improve lab score.
- Break analytics or conversion tracking without approval.

## GEO / Rendered Content Fix

Issue:

- Rendered content percentage is high at 336%.
- Important content may depend heavily on rendering.

Fix:

- Ensure primary page content is present in initial HTML:
  - H1
  - Intro
  - Key links
  - Primary job/listing content
  - FAQ content if schema is used
  - Organization/entity schema
- Reduce client-only rendering for static SEO sections.
- Avoid generating important links only after hydration.
- Ensure `llms.txt` and structured data point LLMs toward canonical content.

QA:

- Disable JavaScript and confirm essential content/links remain visible where architecture supports SSR/SSG.
- Use view-source/server HTML to confirm key content exists.

## Security Issues

Reported:

- 1 subdomain does not support HSTS.
- SPF record missing.
- DMARC exists and is valid.
- SSL is enabled.
- HTTPS redirect works.

## HSTS Fix

Tasks:

- Identify affected hostname/subdomain.
- Confirm all production hostnames redirect to HTTPS.
- Add HSTS header at server/CDN level:
  `Strict-Transport-Security: max-age=31536000; includeSubDomains; preload`
- Use `includeSubDomains` only after confirming all subdomains support HTTPS.
- Consider preload only after full validation.

QA:

- Check headers for root, WWW, and affected subdomain.
- Confirm no mixed content.

## SPF Fix

Issue:

- SPF record missing.

Fix:

- Identify actual mail sender providers.
- Add DNS TXT SPF record through DNS provider.
- Do not guess providers.

Example pattern only:

`v=spf1 include:provider.example -all`

Do not use this exact value unless provider confirms it.

QA:

- SPF validates.
- DMARC alignment remains healthy.
- No legitimate email flow is broken.

## External Nofollow Review

Issue:

- 70 outgoing external links contain nofollow attributes.

Important:

- Nofollow is not automatically bad.
- Official notification/apply links may intentionally use nofollow/sponsored/ugc depending on editorial policy.

Fix:

- Export affected links.
- Classify:
  - Official government/recruitment links
  - Social/community links
  - User-generated/external references
  - Paid/affiliate links
- Remove nofollow only when it is clearly accidental.
- Keep nofollow where editorial risk, paid relationship, or policy requires it.

QA:

- No accidental crawl restriction on trusted official references.
- No policy violation from removing nofollow too broadly.

## Link URL Readability

Issue:

- Some links are not human/search-engine friendly.

Fix:

- Do not change existing indexed URLs casually.
- Improve new URLs going forward.
- For old important URLs, create readable aliases only with canonical/redirect strategy.
- Avoid long query-string URLs for indexable landing pages.

QA:

- No broken links.
- No redirect chains.
- Canonicals are correct.

## Local Business And Social Recommendations

Rules:

- Add Local Business schema only if SearchSarkariNaukri has a real eligible business identity and address to publish.
- Add official Facebook/X/Instagram/YouTube/LinkedIn links only if real official profiles exist.
- Do not create fake schema or fake profiles just to satisfy audit tools.
- Facebook Pixel is optional and should be added only if marketing/ads retargeting is planned and consent/privacy requirements are handled.

## QA Checklist

- [ ] Desktop PSI reviewed after fixes
- [ ] Duplicate/unused scripts removed or deferred
- [ ] Important content exists in server HTML where possible
- [ ] Script completion time improved
- [ ] Rendered content percentage reduced where practical
- [ ] HSTS validated for all production hostnames/subdomains
- [ ] SPF DNS record added with real mail provider includes
- [ ] External nofollow usage reviewed and documented
- [ ] No fake social/schema added
- [ ] URL readability improved only where safe
