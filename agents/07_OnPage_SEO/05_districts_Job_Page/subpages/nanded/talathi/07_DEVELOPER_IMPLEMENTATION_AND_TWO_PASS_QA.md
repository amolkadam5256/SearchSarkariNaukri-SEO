# Developer Implementation and Two-Pass QA

## Build order

1. Inspect the existing route, shared template, data model, metadata source and current page behavior.
2. Capture existing page content, working links, records and exact-URL indexability baseline.
3. Verify recruitment claims and official sources; separate Nanded-specific from Maharashtra-wide information.
4. Implement the 15 useful sections, 15 FAQs, data-driven status UI and valid related links.
5. Check responsive behavior, accessibility, metadata, canonical, robots, schema and state handling.
6. Complete Pass 1, then run a separate Pass 2 against the rendered route.
7. Report content implementation and index status separately.

10. Two-pass completion checklist
Developer verification
0/15 checked



Pass 1 — Implementation
[ ] Inspect the existing route, page template, data model and metadata configuration.
[ ] Implement at least 15 useful content sections and all 15 FAQs.
[ ] Preserve existing navigation and relevant internal links.
[ ] Add official sources and verify every external destination.
[ ] Implement responsive status cards, quick navigation and accessible FAQs.
[ ] Check SEO metadata, canonical URL, robots directives and structured data.
[ ] Test active, empty, loading, error and expired recruitment states.
Pass 2 — Independent verification
[ ] Verify all 15 sections and 15 FAQ answers are present and readable.
[ ] Confirm no existing content or working feature was unintentionally removed.
[ ] Verify all vacancy facts against authoritative sources.
[ ] Check internal links, external links, redirects and broken destinations.
[ ] Inspect the rendered HTML and HTTP headers for noindex directives.
[ ] Validate mobile, tablet and desktop layouts and keyboard accessibility.
[ ] Run lint, type checks, applicable tests and production build.
[ ] Record unresolved issues and provide evidence for every passed check.

Copy verification checklist
Final acceptance rule: Do not mark this task complete merely because the new copy has been added. The page must render correctly, retain existing functionality, use verifiable information, and pass both implementation and independent verification checks. The indexing status must be reported separately from the content implementation status.

## Acceptance rule

Do not mark complete because copy was added. Confirm the page renders, preserves existing useful behavior, uses verified information, and passes both reviews. Report the route indexing result only with exact-URL evidence.
