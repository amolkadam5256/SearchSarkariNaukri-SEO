# AEO GEO SEO Requirements - Crawled Currently Not Indexed

## Goal

Make every indexable page useful enough for Google and AI answer systems to understand the entity, location, intent, status, dates, source, and next action.

## Required Page Blocks For Indexable Pages

- Clear H1.
- Short factual summary.
- Current status block.
- Important dates or latest update.
- Authority/source/official link.
- Main details table.
- How to apply/download/check/result steps when relevant.
- Eligibility, location, category, exam/result/admit-card/job context where relevant.
- Related internal links.
- 10-15 specific FAQs with non-empty answers.
- Last updated date.
- Visible verification note.

## AEO/GEO/LLM Rules

- Use concise answer-first sections.
- Keep facts visible in HTML, not only client-side interaction.
- Use schema that matches visible text.
- Avoid keyword stuffing.
- Avoid copied FAQ answers across many pages.
- Mention location and authority only when truly relevant.
- Use final canonical URLs consistently.

## Sitemap Rule

Only final canonical, indexable, useful, `200 OK`, self-canonical URLs belong in sitemap.

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue. Keep implementation changes limited to affected URL routing, HTTP status handling, canonical logic, robots/indexability, sitemap, metadata, structured data, contextual internal links, page content quality, redirects, and QA.
