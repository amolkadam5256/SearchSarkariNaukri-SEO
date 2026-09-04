# Crawled Currently Not Indexed URL Brief 001

## URL
`https://www.searchsarkarinaukri.com/jobs/central-vigilance-commission-central-vigilance-commission-2026--1730`

## GSC Issue
`Crawled - currently not indexed`

## Last Crawled
`22 Aug 2026`

## Page Type
Job detail page

## Known Evidence
- This URL appears in the supplied `Crawled - currently not indexed` export/evidence.
- One supplied live HTML sample for job `1730` shows `<meta name="robots" content="noindex, follow" />`.
- Current noindex status for this URL: `YES - pasted live HTML shows noindex, follow`.

## Primary Action
`FIX_NOINDEX_AND_CONTENT_OR_REDIRECT`

## What To Test
1. HTTP status must be `200 OK` if the page should index.
2. Robots meta and `X-Robots-Tag` must not block indexing.
3. Canonical must point to the final preferred URL.
4. Sitemap must include only the final canonical indexable URL.
5. Page must have unique useful content, not thin/empty placeholder content.
6. Structured data URL, breadcrumb URL, OG URL, Twitter URL, canonical, and sitemap URL must match.
7. Internal links must point to final canonical URL, not duplicate/parameter/old variants.

## Fix If Page Is Useful And Should Rank
- Use `index,follow`.
- Keep or create one self-canonical URL.
- Add to sitemap only after final QA passes.
- Add strong crawlable sections: summary, dates/status, authority/source, eligibility or result/admit-card/job details, how-to/action steps, related links, FAQ, last updated.
- Add 10-15 FAQs specific to `central vigilance commission central vigilance commission 2026  1730`.

## Fix If Page Should Not Rank
- Keep/return intentional `noindex`, `404`, `410`, or redirect only when appropriate.
- Remove from sitemap.
- Remove or update internal links.
- Do not redirect to an unrelated hub page.

## Developer Scope Guardrail
Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue.
