# Canonical Conflict QA Checklist

## Round 1 Audit

- [ ] `/jobs/1689` status checked.
- [ ] Redirect chain checked.
- [ ] Robots meta and X-Robots-Tag checked.
- [ ] User-declared canonical captured.
- [ ] Google-selected canonical inferred/checked in GSC.
- [ ] Final desired canonical chosen from DB/CMS record.
- [ ] Sitemap presence checked for numeric and slug variants.
- [ ] Internal links checked for numeric and slug variants.
- [ ] BreadcrumbList, JobPosting URL, OG URL, and Twitter URL checked.

## Fix Validation

- [ ] Only one canonical job URL remains.
- [ ] Duplicate URL redirects or canonicalizes correctly.
- [ ] Final canonical returns `200 OK`.
- [ ] Final canonical is `index,follow` if intended to rank.
- [ ] Sitemap includes only final canonical URL.
- [ ] No redirect chain or loop exists.
- [ ] GSC live test passes before validation request.

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue.
