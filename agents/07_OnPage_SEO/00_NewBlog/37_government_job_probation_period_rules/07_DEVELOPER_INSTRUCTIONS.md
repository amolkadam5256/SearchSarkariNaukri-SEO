# Developer Instructions

## Route and source files

| Field | Value |
|---|---|
| Assignment | Update existing evergreen blog; do not create a second URL |
| Target route | `/blogs/what-happens-during-probation-in-a-government-job-can-you-lose-the-job` |
| Canonical | `https://www.searchsarkarinaukri.com/blogs/what-happens-during-probation-in-a-government-job-can-you-lose-the-job` |
| Reader-facing source | `01_BLOG.md` |
| SEO fields | `02_SEO_METADATA.md` |
| Link recommendations | `03_INTERNAL_LINKS.md` |
| Verified source register | `04_EXTERNAL_SOURCES.md` |
| Structured data proposal | `05_SCHEMA_JSONLD.md` |
| Creative brief | `06_IMAGES_AND_CTA.md` |

## Implementation steps

1. Obtain editorial/legal-policy review and recheck the official sources in `04_EXTERNAL_SOURCES.md` immediately before publish.
2. Edit the existing CMS record at the target route. Preserve its URL, canonical, and actual published date. Do not create or publish `/blogs/government-job-probation-period-rules`.
3. Before editing, record the existing page's GSC performance and indexing state if access is available. Keep the existing datePublished; set dateModified only after the substantive update is live.
4. Render the article from `01_BLOG.md`. If the CMS title supplies the H1, remove the Markdown H1 from the body during import so the page has one visible H1.
5. Preserve semantic heading order, real HTML tables, lists, visible FAQs, and source citations. Ensure article content is present in rendered HTML and not injected only after interaction.
6. Set a unique title, description, self-canonical, robots directive, Open Graph fields, and breadcrumb from verified CMS data. Do not use placeholder category URLs or image URLs.
7. Add relevant internal links only after confirming each route; do not add the unconfirmed termination-article URL until found.
8. Upload the original featured image, optimize it per current site standards, and provide meaningful alt text. Keep infographic information available in text.
9. Add `BlogPosting` and `BreadcrumbList` only if the CMS does not already generate equivalent valid schema. Do not publish placeholder dates, author credentials, category URL, or duplicate global schema. FAQPage is intentionally omitted from the proposal.
10. Keep the existing URL in the blog sitemap. After the update, perform `08_PUBLISH_QA.md` and record evidence; do not add a second probation URL.

## Acceptance criteria

- Article is factually reviewed, scoped as general information, and contains the Central-versus-other-employers caveat.
- One H1; heading hierarchy, tables, FAQ, citations, and disclaimer render correctly on desktop and mobile.
- Existing URL is preserved; canonical remains the existing URL before and after client hydration; page returns HTTP 200 and is indexable as intended.
- No duplicate schema; schema values match visible content; all links resolve to the intended destinations.
- Sitemap includes the published URL. Search Console inspection is requested only after deployment; indexing is not guaranteed.
