# Bing Site Scan Master Audit

## Summary

Bing Site Scan reports 110 HTTP 400-499 errors and 247 title-too-long warnings. These overlap with Google Search Console indexing issues and should be fixed with the same URL governance rules: correct status, canonical, sitemap, robots, internal links, content quality, and page speed.

## Exact Developer Actions

1. Export full Bing Site Scan CSV for all 110 HTTP errors and all 247 title warnings.
2. For every 400-499 URL, decide: restore 200, redirect to exact replacement, keep 404, or return 410.
3. For every long-title URL, rewrite title under 70 characters without losing intent.
4. Check canonical, sitemap, robots meta, internal links, schema, and page speed after each fix.
5. Do not remove useful pages just to reduce errors.
6. Run Bing Site Scan again after deployment.
7. Submit changed important URLs through IndexNow where appropriate.

## AEO GEO SEO Requirements

- Page titles must be concise, unique, and entity-specific.
- Job pages should include organization, post, year, location, vacancy/status, and action intent.
- Location pages should include location + job/category intent.
- Avoid duplicate or overlong titles generated from raw database strings.
- Add FAQ and content sections only from real page data.
- Keep schema and canonical URLs aligned.
- Improve Core Web Vitals and mobile rendering for templates affected by Bing errors.

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Bing Webmaster Site Scan issue.
