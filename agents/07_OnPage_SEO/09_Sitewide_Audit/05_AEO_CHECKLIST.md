# AEO — Sitewide Developer Audit Instructions

**Scope:** Entire SearchSarkariNaukri project  
**Status:** Instructions prepared; findings require repository and site evidence.

## Complete checklist

## 7. AEO — Answer Engine Optimization

Make pages useful for users seeking concise answers through search snippets, voice search, AI assistants, and question-based queries.

- [ ] Identify frequently asked questions from actual user needs and reliable keyword or Search Console data.
- [ ] Provide a concise, direct answer near the beginning of the relevant section.
- [ ] Expand with supporting details, conditions, and exceptions.
- [ ] Use clear question-based headings where they are helpful.
- [ ] Provide eligibility, dates, fees, age limits, and application steps in easy-to-scan formats.
- [ ] Distinguish confirmed facts from information that is pending or unavailable.
- [ ] Add FAQs only when they answer genuine user questions.
- [ ] Keep visible FAQ content consistent with any FAQ structured data.
- [ ] Do not add repetitive questions solely to target more keywords.
- [ ] Do not promise featured snippets, rich results, or AI citations.

## Detailed developer instructions

Use genuine user questions. Put concise answers near relevant headings, follow with conditions and exceptions, and make eligibility/dates/fees/steps scannable. Keep FAQ and schema aligned. Avoid repetitive FAQs and do not promise snippets or rich results.

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
