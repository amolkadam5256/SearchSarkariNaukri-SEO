# Developer Instructions: Government Job Selection Process in India

## Deliverables and status

- Publication-ready Markdown article: [`government-job-selection-process-india.md`](./government-job-selection-process-india.md)
- Proposed route: `/blogs/government-job-selection-process-india`
- Canonical: `https://www.searchsarkarinaukri.com/blogs/government-job-selection-process-india`
- Publishing status: **Draft; do not publish until the checks below are complete.**
- Search intent: informational, full recruitment lifecycle. This article is the broad process guide; keep the application, result, verification and probation guides focused on their own subtopics.

## Content and SEO fields

Use the metadata in the article as the source of truth:

- SEO title: **Government Job Selection Process in India: Complete Guide**
- H1: **Government Job Selection Process in India: Complete Guide from Application to Final Appointment**
- Meta description: **Understand the government job selection process in India, from application scrutiny and exams to merit lists, verification, appointment and joining.**
- Primary keyword: `government job selection process in India`
- Suggested image: `government-job-selection-process-india.webp`, 1200 × 675 px
- Alt text: `Government job selection process in India from application to final appointment`
- Author and dates must be the real editorial author and actual publication/update dates. Never ship placeholders or invent a modified date.

Render Markdown through the site's existing blog content renderer and existing components. Preserve the article text, visible FAQ answers, source links and disclaimer. Do not put developer notes, checklist, SEO keyword lists or image production notes on the public page.

## Design direction for the existing blog UI

Make this long guide easy to scan on desktop and mobile by using the current design system and blog template:

1. Use the site's existing breadcrumb, article header, author/date row, featured-image treatment, typography, colors and spacing tokens.
2. Place a short “Quick answer” callout after the H1 and summary metadata if the template already has a suitable callout component. Keep it text-first, accessible and visually restrained.
3. Render the table of contents as an in-page navigation panel using native anchor links. It may be collapsible on small screens only if that interaction pattern already exists in the site.
4. Preserve clear H2/H3 hierarchy, generous line length, readable paragraph spacing, visible focus states and anchor offset for sticky headers.
5. Present the overview as a simple numbered progression or existing step-list component. Treat “where applicable” stages distinctly; avoid implying every recruitment uses every stage.
6. Keep document and tracking tables responsive using the site's established mobile table behavior. Do not introduce horizontal overflow.
7. Use the current related-article and CTA components for the relevant links and final job-discovery action. Avoid a new visual system, animation, decorative stock image grid or bespoke app-like widgets.
8. The featured image should be original or appropriately licensed and should illustrate an Indian candidate reviewing recruitment materials. Do not use the unrelated image-search examples pasted in the source material.

## Internal links

Use contextual links in article body copy (links below are proposed live site routes; confirm each destination resolves before release):

| Context | Anchor | Destination |
|---|---|---|
| Application submission | how to apply for government jobs in India | `/blogs/how-to-apply-government-jobs-india` |
| Scrutiny / eligibility | check government job age limits | `/blogs/age-limit-government-jobs-2026` |
| Answer key / results | check government exam results and merit lists | `/blogs/check-government-exam-results-merit-list` |
| Document verification | government job document verification process | `/blogs/government-job-verification-process-explained-what-happens-after-you-get-selected` |
| Training / probation | probation period in a government job | `/blogs/what-happens-during-probation-in-a-government-job-can-you-lose-the-job` |
| Find vacancies CTA | latest government job vacancies | `/jobs` |
| Optional career decision link | choose the right government examination after graduation | `/blogs/choose-government-exam-after-graduation` |

Use only links that help in context. Remove tracking query parameters and do not use a link block as a substitute for contextual linking. Add varied inbound links to the new guide from the application, verification and probation articles where relevant, with anchors such as “from application to appointment” and “government recruitment stages in India.”

## Official sources and accuracy

The article links to primary authorities: UPSC Recruitment Branch, UPSC Examination Division, UPSC Recruitment FAQs, SSC, and two PIB releases. Keep source links next to claims they support. Retain the date and careful attribution for dated policy announcements:

- PIB, 21 August 2025: SSC examination-cycle reforms. The release reports reductions for various SSC examinations; do not present those figures as a promise or as typical for all recruitment.
- PIB, 1 July 2016: central-government instruction regarding provisional appointment letters and character/antecedent verification. Clearly retain the scope limitation in the article; do not imply every state, PSU or authority applies the same process.

Before release, manually verify each official link and confirm it supports the adjacent claim. The current UPSC URLs use the official `cms.upsc.gov.in` paths. Never replace official links with job portal summaries as evidence. Confirm all internal links and remove any unavailable destinations or correct the route to the live canonical page.

## Technical implementation checklist

- [ ] Use the current `/blogs/` route and existing blog template; no new route pattern or site redesign.
- [ ] Return HTTP 200 for the canonical URL and ensure it is included in the XML sitemap.
- [ ] Set a self-referencing canonical to the final HTTPS URL.
- [ ] Confirm the page is indexable (`index,follow`) and not blocked by robots or access rules.
- [ ] Ensure one visible H1, logical H2/H3 order, descriptive page title and meta description.
- [ ] Add `BlogPosting` JSON-LD with visible headline, description, actual author/publisher, actual `datePublished` and `dateModified`, actual featured-image URL and canonical `mainEntityOfPage`.
- [ ] Add `BreadcrumbList` only if consistent with visible breadcrumbs. Suggested trail: Home → Blogs → Government Jobs → Government Job Selection Process.
- [ ] Make structured data values match visible page content; do not fabricate author identity or dates.
- [ ] Do not add FAQ schema solely to seek a rich result. Keep the FAQs visible and useful; follow current search policy and site conventions if FAQ schema is considered.
- [ ] Use descriptive image filename, alt text, responsive sizing and modern compressed format; avoid layout shift by reserving image dimensions.
- [ ] Validate keyboard navigation, contrast, focus visibility, heading anchors, mobile tables and screen-reader labels.
- [ ] Check Core Web Vitals and ensure the image and any callout/TOC behavior do not add unnecessary JavaScript or layout shift.
- [ ] Check all internal and external links, canonical, sitemap, schema and rendered page source before publishing.

## Release QA

- [ ] Compare final rendered article against the Markdown and check that no stage is presented as universal.
- [ ] Check for duplication/cannibalization with the application, exam-result, verification and probation pages; keep this page centered on the complete journey.
- [ ] Verify current official sources and every internal destination.
- [ ] Confirm the title, description, H1, image, author and dates are final.
- [ ] Review responsive layout and accessibility on a phone-sized viewport.
- [ ] Confirm HTTP 200, canonical, indexability, sitemap inclusion and valid structured data.
- [ ] Publish only after editorial and technical review; then inspect the URL in Search Console and monitor indexing and query performance.

## Known limitations at handoff

The repository contains the requested article draft and project archive, but no live CMS access was used. The domain destinations and technical release conditions must be checked in the staging or production environment by the implementer. The article is not published by this handoff.
