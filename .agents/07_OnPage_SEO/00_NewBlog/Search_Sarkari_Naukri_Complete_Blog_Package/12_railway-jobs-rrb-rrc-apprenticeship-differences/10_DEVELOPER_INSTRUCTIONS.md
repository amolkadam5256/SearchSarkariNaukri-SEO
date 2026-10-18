# Developer Instructions

| Field | Value |
|---|---|
| Target route | `/blogs/railway-jobs-rrb-rrc-apprenticeship-differences` |
| Assignment | NEW |
| Canonical | `https://www.searchsarkarinaukri.com/blogs/railway-jobs-rrb-rrc-apprenticeship-differences` |
| Source article | `01_BLOG.md` |
| Metadata | `02_SEO_METADATA.md` |
| FAQ | `05_FAQ.md` |
| Schema | `07_SCHEMA_JSONLD.md` |

## Implementation

1. Import the reader-facing article only from `01_BLOG.md`; do not import audit notes into the public body.
2. Preserve one H1 only. If the CMS title renders H1, remove the body H1 during import.
3. Set title, description, slug, canonical and social fields from `02_SEO_METADATA.md`.
4. Add internal links from `03_INTERNAL_LINKS.md` only where contextually relevant.
5. Add external citations from `04_EXTERNAL_SOURCES.md` after live verification.
6. Add schema from `07_SCHEMA_JSONLD.md` only if the CMS does not already generate equivalent schema.
7. Add breadcrumbs: Home > Blogs > Railway Jobs: RRB, RRC and Apprenticeship Differences.
8. Add to blog sitemap only after publish.

## Acceptance Tests

- [ ] Route returns HTTP 200 after publish.
- [ ] Canonical remains `https://www.searchsarkarinaukri.com/blogs/railway-jobs-rrb-rrc-apprenticeship-differences` before and after hydration.
- [ ] Meta title and description are unique.
- [ ] FAQ schema exactly matches visible FAQ content.
- [ ] No duplicate BlogPosting/Article schema.
- [ ] All internal and external links return acceptable status and are relevant.
- [ ] Sitemap includes the URL after publish.
- [ ] GSC URL Inspection is requested after publish.

## Internal Link Count

Selected internal destinations: 24. Requirement target: 20-30 relevant destinations. If fewer than 20 are used in the final article, record the editorial reason rather than adding unrelated links.
