# Content Accuracy and Source Verification — Sitewide Developer Audit Instructions

**Scope:** Entire SearchSarkariNaukri project  
**Status:** Instructions prepared; findings require repository and site evidence.

## Complete checklist

## 8. Content Accuracy, Trust, and Source Verification

This is a high-priority requirement for a government recruitment information website.

### Source hierarchy

- [ ] Prefer official recruitment notifications, official department websites, and authorized application portals.
- [ ] Use official exam authorities for admit cards, answer keys, results, schedules, and examination notices.
- [ ] Use the original notification PDF whenever it is available and relevant.
- [ ] Use reputable secondary sources only for context or corroboration where appropriate.
- [ ] Do not treat an unofficial blog, social post, or search snippet as proof of an official announcement.

### Fact-checking

- [ ] Verify the organization and examination name.
- [ ] Verify notification number and publication date when available.
- [ ] Verify application start and end dates.
- [ ] Verify vacancy counts and category-wise breakdowns.
- [ ] Verify age limits, age-relaxation rules, qualifications, fees, and selection stages.
- [ ] Verify official application, notification, result, and admit-card URLs.
- [ ] Check whether dates or vacancy details have changed in later notices.
- [ ] Record source publication dates and the latest meaningful update.
- [ ] Flag conflicting sources rather than silently choosing one.
- [ ] Mark unresolved details for manual review.
- [ ] Never invent official sources, citations, deadlines, or recruitment details.

### Source attribution on pages

Where appropriate, provide a visible source or official-notification section containing:

- Issuing organization.
- Notification or document title.
- Publication or notification date, if confirmed.
- Direct link to the official source.
- Last verified or updated date, where supported.
- A short note when information remains unconfirmed.

Preserve existing content while correcting confirmed errors through the project's approved content workflow.

## Detailed developer instructions

Use official notices/departments/authorized portals as primary sources. Verify names, cycle, notification number/date, dates, vacancies, age, qualification, fees, selection and official URLs. Check amendments/conflicts, record source and verification dates, flag gaps, and preserve useful content while correcting confirmed errors.

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
