# Implementation Scope — 12th Pass Government Jobs

**Canonical route:** `/12th-pass-government-jobs`
**Primary user task:** Find current government vacancies that accept Class 12 candidates, compare eligibility and deadlines, and reach the official application source.

## Non-negotiable rules

- Treat this as an enhancement of the existing route. Do not create a duplicate page.
- Preserve all existing useful content, routes, data, filters, pagination, internal links, metadata, analytics, schema and working behavior.
- Follow existing `.agents` instructions and the no-delete policy before changing implementation.
- Use real vacancy records and official sources. Do not invent jobs, counts, deadlines, salaries, eligibility, source URLs or status.
- Never show an expired vacancy as active or leave an expired “Apply Now” action enabled.
- Distinguish this listing page from the related evergreen article.
- Build at least 15 meaningful sections and 15 useful FAQs, reusing or improving existing content without deleting useful information or adding redundant blocks.
- No implementation can guarantee a number-one ranking.

## Page-level deliverables

- [ ] One focused page introduction and a working job finder.
- [ ] Data-driven active/upcoming/closed summary.
- [ ] At least 15 useful sections and 15 relevant FAQs.
- [ ] Verified job cards with supported facts and official links.
- [ ] Useful internal paths to existing qualification, category, result, admit-card and calendar pages.
- [ ] Contextual link to the separate 12th-pass guide article, with the article linking back.
- [ ] Exact URL metadata and robots audit, crawlable content, valid structured data and sitemap decision.
- [ ] Responsive, accessible controls and useful loading/empty/error states.
- [ ] Two independent verification passes with evidence.

## Existing-record concern to verify

The supplied brief reports 50 active vacancies and several deadlines dated 27 October 2026. Treat both as leads for investigation, not confirmed facts. Recompute the current count from job data and verify each record, deadline, timezone, extension, cancellation and status from the relevant official notice before display.
