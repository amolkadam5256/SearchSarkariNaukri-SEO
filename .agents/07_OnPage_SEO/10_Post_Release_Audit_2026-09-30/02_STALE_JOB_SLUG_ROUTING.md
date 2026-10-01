# P0 — Stale job slug routing (slug ≠ job ID)

**Status:** Open on live site (verified 1 Oct 2026)  
**Release note:** 30 Sep fix addressed **title duplication**, not **legacy wrong slugs**.

---

## Problem

Job pages must resolve by **numeric ID suffix** (`--5015`), not by slug string alone.

**Live example:**

- URL: `/jobs/canara-bank-graduate-apprentice-recruitment-2026-apply-online-for-3500-posts--5015`
- DB job ID **5015** content: NHSRCL (Marathi), deadline passed  
- User expectation from URL: Canara Bank  
- Correct Canara example: `...--6681` shows Canara Bank Uttarakhand correctly

So `--5015` in the path is authoritative for **which row loads**, but the **path prefix is stale marketing slug** from an earlier slug generation or reused ID.

---

## Required behaviour (no job row deletes)

1. Parse ID from path: regex `--(\d+)$`.
2. Load job row by **primary key ID**.
3. Compute `canonicalSlug` from shared helper (org + post + year + `--{id}`).
4. If request path ≠ canonical path → **301** to `https://www.searchsarkarinaukri.com/jobs/{canonicalSlug}`.
5. Render H1, `<title>`, JSON-LD from that ID only.
6. Invalidate prerender cache key: `job:{id}:{updated_at}`.

---

## Acceptance tests

| Test | Pass criteria |
|------|----------------|
| `...--6681` | 200, H1 contains “Canara” |
| `...canara...--5015` | **301** to NHSRCL canonical slug OR 200 with NHSRCL title matching URL after redirect |
| Sitemap | Only canonical slugs OR only IDs that 301 once (prefer canonical URLs in sitemap) |
| Regression script | Samples use **valid** slug+ID pairs (6681, 6682) |

---

## SEO impact

- Wrong slug + correct ID = **cloaking/trust** risk in GSC  
- External links and old Google URLs may still hit stale Canara slugs  
- 301 to canonical fixes indexing and user trust

---

## Reference

`SEO_Audit_Review_2026-09-29/01_REGRESSION_FIX_IMPLEMENTATION_NO_DELETE.md` — section R2
