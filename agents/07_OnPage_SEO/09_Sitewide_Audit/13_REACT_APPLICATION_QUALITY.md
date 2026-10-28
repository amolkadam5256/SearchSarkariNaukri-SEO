# React Application Quality — Sitewide Developer Audit Instructions

**Scope:** Entire SearchSarkariNaukri project  
**Status:** Instructions prepared; findings require repository and site evidence.

## Complete checklist

## 16. React and Application Quality

- [ ] Review component responsibilities and duplication.
- [ ] Use reusable components consistently.
- [ ] Verify correct list keys and stable rendering.
- [ ] Check for unnecessary re-renders and expensive computations.
- [ ] Review state management and effect dependencies.
- [ ] Handle asynchronous requests, cancellation, errors, and loading states.
- [ ] Prevent stale data from being presented as current.
- [ ] Check hydration errors where server rendering is used.
- [ ] Review server/client component boundaries where applicable.
- [ ] Validate route parameters and dynamic page data.
- [ ] Handle missing records without crashing the application.
- [ ] Check forms and validation rules.
- [ ] Ensure navigation, filters, pagination, and search work correctly.
- [ ] Check browser console warnings and errors.
- [ ] Review TypeScript types or PropTypes where applicable.
- [ ] Run linting, type checks, unit tests, and production builds using existing project scripts.
- [ ] Do not replace the framework, router, or core architecture without a clear reason and approval.

## Detailed developer instructions

Review component reuse, keys, rerenders, state/effects, async cancellation/errors/loading, stale data, server/client boundaries, route validation, missing records, forms and console. Follow current framework/router. Run existing lint/type/test/build scripts as applicable; do not replace core architecture without clear reason and approval.

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
