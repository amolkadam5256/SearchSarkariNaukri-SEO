# 08 — Internal Linking & Sitemap Plan (Additive Only)

## Part A — Internal linking additions

Add new links; keep every existing nav/footer link exactly as-is.

### 1. Homepage → add links to new hub pages (in addition to existing nav)

```
Government Jobs → Central Government Jobs, Maharashtra Government Jobs,
SSC Jobs, UPSC Jobs, MPSC Jobs, Railway Jobs, Banking Jobs, Police Jobs,
Defence Jobs, Teaching Jobs
```

### 2. Category/topic clusters — add cross-links between related existing and new pages

```
MPSC cluster:
/category/mpsc-jobs → /exams/mpsc-rajyaseva → /mpsc-syllabus →
/mpsc-admit-card → /mpsc-result → /mpsc-current-affairs (add links only
where the target page already exists or is being created in this rollout)

SSC cluster:
/category/ssc-jobs → /exams/ssc-cgl → /exams/ssc-chsl → /ssc-syllabus →
/ssc-admit-card → /ssc-result

Railway cluster:
/category/railway-jobs → /exams/rrb-ntpc → /rrb-group-d →
/railway-admit-card → /railway-result
```

### 3. District pages — add links (district pages already exist; add these links to them)

```
/districts/thane → Thane UPSC Jobs, Thane SSC Jobs, Thane Police Jobs,
Thane Government Jobs (link to the relevant new category/qualification
pages filtered for that district)
```

### 4. Individual job pages — add "Related Jobs" and "Related Exam" links

Already specified in file 04 §6–7. Populate based on the job's own department/qualification/state — not random.

### 5. Anchor text rule (applies to every new link added anywhere)

Never use "Click Here" or "Read More" for new links. Use descriptive text, e.g. "Latest MPSC Government Jobs 2026" instead of "Click Here".

## Part B — Sitemap architecture (additive)

Do not delete or truncate the existing `sitemap.xml`. Convert it into an index (if it isn't already) and add new child sitemaps alongside whatever it currently references.

```
/sitemap.xml (index — keep existing entries, add new ones below)
   ├── sitemap-jobs-1.xml, sitemap-jobs-2.xml, ... (existing job URLs, unchanged)
   ├── sitemap-categories.xml       [NEW]
   ├── sitemap-qualifications.xml   [NEW]
   ├── sitemap-districts.xml        (existing, or new if not present)
   ├── sitemap-recruiters.xml       [NEW]
   ├── sitemap-exams.xml            (existing)
   ├── sitemap-results.xml          (existing)
   ├── sitemap-admit-cards.xml      (existing)
   └── sitemap-blog.xml             (existing)
```

### Sitemap hygiene rules (apply to new entries only — don't retroactively strip existing entries unless file 09's audit says to)

- Only include URLs that return HTTP 200, are self-canonical, and are **not** `noindex`.
- Do not include filter/parameter URLs like `/jobs?district=pune&sort=latest`.
- Do not include the `/jobs` pagination variants unless each is independently canonical and indexable (see file 02 §6).
- Set `<lastmod>` only when the page's meaningful content actually changed — don't bump it daily just to trigger a crawl.

```xml
<url>
  <loc>https://www.searchsarkarinaukri.com/jobs/{slug}</loc>
  <lastmod>2026-08-24</lastmod>
</url>
```

## Checklist for this file

- [ ] Homepage links to new hub pages added (existing nav untouched)
- [ ] Topic clusters cross-linked (MPSC, SSC, Railway, etc.)
- [ ] District pages get new category/qualification cross-links
- [ ] Job pages get Related Jobs + Related Exam links
- [ ] No new link anywhere uses "Click Here" / "Read More"
- [ ] Sitemap index extended with new child sitemaps, existing entries untouched
- [ ] New sitemap entries only include indexable, canonical, 200-status URLs
