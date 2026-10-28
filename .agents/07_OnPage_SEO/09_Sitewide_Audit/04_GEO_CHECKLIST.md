# GEO — Sitewide Developer Audit Instructions

**Scope:** Entire SearchSarkariNaukri project  
**Status:** Instructions prepared; findings require repository and site evidence.

## Complete checklist

## 6. GEO — Generative Engine Optimization

Optimize content so that search engines and generative AI systems can understand, identify, and accurately reference useful information.

- [ ] Clearly identify the entity, topic, organization, exam, or recruitment process covered by each page.
- [ ] Provide direct, factual answers to common questions.
- [ ] Use descriptive headings that match real user questions.
- [ ] Present important facts in well-structured text, lists, and HTML tables.
- [ ] Identify the information source and relevant publication or update date.
- [ ] Distinguish official facts from editorial explanation.
- [ ] Maintain consistent organization names, exam names, dates, and terminology.
- [ ] Link to original authoritative sources where appropriate.
- [ ] Make important information accessible in crawlable HTML.
- [ ] Add useful contextual explanations rather than repeating keywords.
- [ ] Use structured data only when the content meets the relevant schema requirements.
- [ ] Keep important information accurate, current, and traceable to sources.
- [ ] Avoid fabricated expert quotations, statistics, reviews, and claims of authority.
- [ ] Do not promise inclusion in AI-generated answers or assume that any special AI file guarantees visibility.
- [ ] Monitor available search and referral data to evaluate results over time.

## Detailed developer instructions

Check that pages identify the relevant entity and topic, answer common questions clearly, structure facts for extraction, cite authoritative sources, distinguish official facts from editorial context and use consistent names/dates. Do not promise AI answer inclusion or citations.

## Pass 1 — Audit and implementation

- [ ] Inspect current code/data and capture reproducible baseline evidence.
- [ ] Identify affected routes/components; preserve useful content, records, URLs and working behavior.
- [ ] Record confirmed findings and distinguish evidence from assumptions.
- [ ] Assign priority; document fix, expected result, dependencies and approvals.
- [ ] Implement only scoped approved changes using project conventions.
- [ ] Run applicable local checks; record exact commands/results.
- [ ] Record changed files/components and unresolved items.

## Pass 2 — Independent verification

- [ ] Recheck the original issue against rendered routes or actual system behavior.
- [ ] Verify content/data preservation and applicable metadata, schema and links.
- [ ] Exercise desktop/mobile, keyboard and relevant loading/empty/error/success states.
- [ ] Inspect relevant console/network output and regression paths.
- [ ] Attach reproducible evidence; mark passed, failed, blocked or untested.
- [ ] Keep unresolved items open; code changes or a passing build alone do not prove success.

## Completion record

- Pass 1 owner/date/status: ____________________
- Pass 1 evidence: ____________________
- Pass 2 reviewer/date/status: ____________________
- Pass 2 evidence: ____________________
- Open issues/dependencies: ____________________
