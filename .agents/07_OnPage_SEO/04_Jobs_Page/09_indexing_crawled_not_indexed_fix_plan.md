# 09 — Fixing "Crawled – Currently Not Indexed" (No Deletions, No Bulk Resubmission)

## Context

Google has already crawled these URLs but chose not to add them to the index — this is a content/quality/architecture signal, not primarily a "please crawl me again" problem. Don't mass-click "Request Indexing" on all affected URLs; that isn't the fix and won't scale.

## Step 1 — Classify, don't delete

Export the affected URLs and sort into four groups. **No URL is deleted in this step** — classification only decides what gets *optimized first*.

| Group | Description | Action |
|---|---|---|
| A — High priority | Current job pages, major category/state pages (MPSC, SSC, Railway, Police, Banking) | Optimize using files 04/06 first |
| B — Category/landing pages | e.g. `/department/maharashtra-police`, `/districts/thane/upsc` | Add unique content per file 07 |
| C — Thin programmatic pages | e.g. `/districts/gadchiroli/mpsc` with almost no unique content | Add real content before expecting indexing; don't mass-produce more of these until content bar is met |
| D — Low-value duplicates | Pages that substantially overlap another page | Leave live; add canonical to the stronger page (see Step 4) — do not delete |

## Step 2 — Fix the job page template first (highest impact)

Apply file 04 in full to every Group A job page: Quick Information table, original 2–4 sentence overview per job, FAQ block, Related Jobs. The goal is that no two job pages are ≥70–90% identical template with only 3–4 fields swapped.

## Step 3 — Fix district/category page depth (Group B/C)

Each page like `/districts/thane/upsc` needs, in addition to what it has today:

```
- Thane-specific intro paragraph (not reused verbatim across districts)
- Current UPSC vacancies relevant to Thane
- Related Jobs in Thane (SSC, MPSC, Police)
- FAQs
```

Don't create more Group-C-style thin pages until existing ones meet this bar.

## Step 4 — Canonical & indexability audit (no deletions — tag corrections only)

For every URL in the export, add/verify (don't remove existing working tags):

```
- HTTP 200
- robots.txt allows crawling
- No accidental <meta name="robots" content="noindex"> on pages meant to be indexed
- Self-referencing canonical for unique pages
- For genuine near-duplicates, canonical pointing to the stronger version (Group D)
```

Use URL Inspection → "Crawl allowed?" and "Indexing allowed?" to verify each, starting with Group A.

## Step 5 — Sitemap hygiene (ties to file 08)

Remove only **non-indexable URLs from the sitemap listing itself** (not the pages) — i.e., stop *submitting* noindex/duplicate/parameter URLs in the sitemap, without touching the pages themselves.

## Step 6 — Internal linking (ties to file 08)

Ensure every Group A/B page is reachable within a few clicks from the homepage via the new hub pages (file 07) and cluster links (file 08). Orphaned or deep-buried pages are less likely to be indexed regardless of content quality.

## Step 7 — Selective indexing requests (last, not first)

Only after Steps 2–6 are applied to a batch of URLs, request indexing for that batch's highest-priority pages via URL Inspection. Let the rest be discovered naturally through the improved sitemap + internal links. Expect this to take days to weeks — indexing is not guaranteed or immediate.

## What NOT to do

- Don't bulk "Request Indexing" all 136+ URLs as a first move.
- Don't use the Indexing API for non-JobPosting pages (districts, categories, results) — it's scoped to JobPosting/BroadcastEvent content.
- Don't delete Group C/D pages by default — reclassify and improve, or canonicalize; only remove pages with genuinely zero standalone value after content improvements haven't helped.
- Don't pad pages with repetitive filler text to hit a word count — add genuinely useful, differentiated information instead.

## Checklist for this file

- [ ] Affected URLs exported and classified into A/B/C/D
- [ ] Group A job page templates upgraded (file 04)
- [ ] Group B/C district/category pages given unique depth (file 07)
- [ ] Canonical/robots/noindex audited per URL, corrections added (not existing tags removed)
- [ ] Sitemap stops submitting non-indexable URLs
- [ ] Internal links added so Group A/B pages are easily reachable
- [ ] Indexing requested only for top-priority pages after fixes, not in bulk upfront
