# Regression Fix Implementation — Update Only (No Deletes)

**Site:** https://www.searchsarkarinaukri.com/  
**Date:** 29 September 2026  
**Rule:** Do **not** delete jobs, pages, URLs, DB rows, images, or UI sections. Only **add**, **correct**, **redirect**, **noindex**, or **exclude from sitemap** where required.

**Production codebase:** `C:\Users\Administrator\Projects\SakariNaukariN` (API + frontend + prerender + sitemap routes).  
**Reference (working baseline):** `SEO_Audit_Review_2026-08-25/outputs/remediation/DEVELOPER-REMEDIATION-REPORT.md`

---

## Live regressions to fix first (P0)

| ID | Error | Current live | Required end state |
|----|--------|--------------|-------------------|
| R1 | Sitemap | `/sitemap.xml` → **500** | **200** XML sitemap index, all child sitemaps **200** |
| R2 | Job URL integrity | Slug says Canara Bank; body shows other org (ID `--5015`, `--5020`) | URL, H1, JSON-LD, and DB record **same job** |
| R3 | JobPosting GSC | 0 valid | Active jobs emit valid JobPosting; expired jobs **keep page** but **no** JobPosting |
| R4 | GSC 404 jobs | ~613 URLs | Valid jobs **200**; gone jobs **410/404** + **301** from numeric to slug when replacement exists |

---

## R1 — Fix sitemap HTTP 500 (no content deleted)

### Diagnose (on server)

```bash
pm2 logs naukri-api --lines 200
curl -sI https://www.searchsarkarinaukri.com/sitemap.xml
curl -sI https://www.searchsarkarinaukri.com/sitemap-jobs.xml
```

### Common causes (Aug audit + regression)

1. **Unhandled exception** in sitemap route (DB timeout, null row, date parse).
2. **Empty child sitemap** (e.g. news) failing XSD/generator — Aug audit: empty `sitemap-news.xml` broke validation.
3. **PM2 process crash** or stale deploy.

### Fix pattern (additive / defensive)

1. **Sitemap index route:** try/catch → log error; return last-known-good cache or minimal valid index listing only **200** child sitemaps that generated successfully. Never return 500 to Google.
2. **Per-child generator:** if a section has **zero** eligible URLs, either:
   - **Omit** that child from the index (preferred), or
   - Emit valid `<urlset>` with no URLs only if your validator allows (Aug audit failed XSD on empty urlset).
3. **Include rules (unchanged from remediation):** only canonical, **200**, indexable URLs; **exclude** expired jobs from **job sitemap feed only** — pages stay live.
4. **Dates:** clamp `lastmod`; never future dates.
5. After deploy: run `SEO_Audit_Review_2026-09-29/live_seo_regression_check.py` and resubmit sitemap in GSC.

### Files to inspect (typical names in SakariNaukariN)

- API: `routes/sitemap*.js` / `controllers/sitemap*` / `services/sitemap*`
- Job feed query: ensure `status=active` OR `last_date >= today` for **sitemap list only**
- Nginx: proxy timeout for `/sitemap*.xml` (increase if DB slow)

---

## R2 — Fix job slug ≠ content (critical trust bug)

### Symptom

`/jobs/canara-bank-...--5015` renders a **different** recruitment (wrong org/title). Homepage links and slugs diverged from prerender/cache or wrong lookup key.

### Root cause (typical)

- Route resolves by **slug string** while numeric suffix `--5015` is ignored or stale cache keyed by slug only.
- Job **reused ID** after slug regeneration without cache purge.
- CDN/prerender serves **wrong HTML** for URL.

### Fix (no delete — correct routing + redirect)

1. **Parse ID** from path: regex `--(\d+)$` (or your canonical pattern).
2. **Load job by primary key ID** from DB (authoritative).
3. **Compute `canonicalSlug`** from shared helper (same as Aug remediation: org + post + year + id suffix).
4. **If path slug ≠ canonicalSlug:** respond **301** to `https://www.searchsarkarinaukri.com/jobs/{canonicalSlug}` (preserve ID in slug).
5. **Render** title, H1, meta, JSON-LD, BreadcrumbList from **that ID’s row** only.
6. **Prerender cache key:** `job:{id}:{updated_at}` — invalidate on any job update.
7. **Regression test:** for each homepage “Latest jobs” link, fetch URL → H1 must contain organization name from link text.

### Do not

- Delete old slugs — **301** old slug to new canonical.
- Delete expired job pages — show “deadline passed” banner (already present).

---

## R3 — JobPosting schema (GSC 0 valid)

### Rules

| Job state | Page | JobPosting JSON-LD | robots | In job sitemap |
|-----------|------|-------------------|--------|----------------|
| Active (last date ≥ today) | 200 | **Yes**, valid fields | index,follow | **Yes** |
| Expired | 200, full content kept | **No** | index,follow or noindex,follow (keep Aug policy) | **No** |
| Removed permanently | 410/404 | No | — | No |

### Required fields (active only)

`title`, `description`, `datePosted`, `validThrough` (end of day IST), `hiringOrganization`, `jobLocation`, `employmentType`, official application URL where available.

### After fix

- Rich Results Test on **one active** Canara Bank / MPSC job from homepage.
- GSC → Enhancements → Job postings (may take weeks to repopulate).

---

## R4 — GSC 404 job URLs (613) — restore or redirect, never mass homepage redirect

Per URL (automated batch from GSC export):

1. ID exists + published → **200** with descriptive slug.
2. ID exists + expired → **200** + closed state; optional **301** from `/jobs/1689` to slug URL.
3. ID missing, slug replacement known → **301** one hop.
4. Truly removed → **410**; **keep** no mass delete from DB unless already soft-deleted.

**Sitemap:** remove URL from XML **only** (not from site) for 404/410/noindex — “exclude from sitemap” ≠ delete page.

---

## P1 — Remaining audit errors (update only)

| Issue | Fix |
|-------|-----|
| Redirect error `/jobs?district_slug=pune` | **301** → `/districts/pune` (or `/jobs-in-pune` if that is canonical) |
| 2,785 broken internal links | Fix **link builder** to approved district slugs; **update** hrefs in templates/DB |
| 3,111 orphan sitemap URLs | **Add** contextual links from hubs (no new UI blocks — use existing related-jobs sections) |
| 896 admit-card discovered-not-indexed | Expand template content + FAQs per `.agents/.../06_EXACT_DEVELOPER_ACTION_CHECKLIST.md` |
| 81 soft 404 | **Add** copy, related jobs, FAQs when list empty |
| 56 noindex | Remove noindex **only** on valuable hubs; keep noindex on thin/filter pages |
| Duplicate titles/descriptions | **Regenerate** meta from record fields (same page, better text) |
| hreflang same URL | **Remove** invalid en/mr/x-default on identical URL; set correct `html lang` |
| Organization sameAs empty | **Add** verified social URLs only |
| Trailing slash | **301** duplicate to canonical (verify Aug fix still deployed) |

---

## P2 — Performance / CWV (no UI redesign)

- Defer noncritical JS; optimize LCP image; keep notification prompt non-blocking (Aug fix).
- Do not remove homepage SEO sections to chase scores.

---

## Deployment checklist

- [ ] `sitemap.xml` → 200  
- [ ] All referenced child sitemaps → 200  
- [ ] 10 random job URLs: slug matches H1 + organization  
- [ ] 1 active job: JobPosting in HTML  
- [ ] 1 expired job: no JobPosting, page still 200 with notice  
- [ ] `/jobs?district_slug=pune` → 301 → district hub  
- [ ] Run `live_seo_regression_check.py` → 0 critical failures  
- [ ] GSC: resubmit sitemap; validate 404 bucket separately  

---

## Rollback

Use server backup from Aug remediation if needed: `/root/backups/ssn-seo-remediation-20260825T0810Z` — restore **code**, not DB delete.
