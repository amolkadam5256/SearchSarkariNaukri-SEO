# Related Resources and Final Navigation — Developer Instructions

**Page:** `/exams`
**Section:** Related Resources and Final Navigation
**Purpose:** Retain relevant working links to jobs, job updates, calendar, admit cards, results, current affairs, daily quiz/assessment, digital library, eligibility checker, age calculator, career guidance and district jobs. Group with meaningful labels, validate destinations and avoid keyword-only link lists.

## Content and presentation format

- Use one clear heading and a short sentence explaining the section's purpose.
- Choose cards for discovery/resources, tables for comparisons/date records, and numbered steps for guidance.
- Use concise plain English, descriptive actions, clear caveats and verified sources.
- Reuse existing components, data sources, design tokens and routes; preserve existing useful content and behavior.
- Do not add placeholders, unsupported facts, dead controls or duplicate content.

## Pass 1 — Implementation review

- [ ] Section is present in the correct page order with the required content and layout.
- [ ] Existing useful content, records, links and working behavior are preserved.
- [ ] Data, counts, dates, eligibility labels and sources match the source of truth.
- [ ] Every relevant control/action connects to the intended data or destination.
- [ ] Semantics, heading structure, labels and accessibility behavior are correct.
- [ ] Missing/stale data has an honest fallback; no values were guessed.
- [ ] Record inspected component/data source and unresolved gaps.

## Pass 2 — Independent implementation verification

After implementation, repeat the review on the rendered `/exams` page and relevant interactions. Do not rely on Pass 1 notes alone.

- [ ] Confirm visibility, readability and section order on desktop and mobile.
- [ ] Exercise each applicable filter, link, button, accordion or table interaction and confirm results.
- [ ] Recheck completeness, URLs, source labels, dates/statuses and empty states against source data.
- [ ] Check keyboard operation, focus, accessible names/semantics and mobile overflow.
- [ ] Confirm no broken links or console/runtime errors attributable to the section.
- [ ] Mark every item pass/fail and record evidence or defects; leave unverified items incomplete.

## Completion record

- Pass 1 reviewer/date: ____________________
- Pass 1 result: ☐ Pass ☐ Fail
- Pass 2 reviewer/date: ____________________
- Pass 2 result: ☐ Pass ☐ Fail
- Evidence/open issues: ____________________

---

**Instruction status:** Ready for implementation
