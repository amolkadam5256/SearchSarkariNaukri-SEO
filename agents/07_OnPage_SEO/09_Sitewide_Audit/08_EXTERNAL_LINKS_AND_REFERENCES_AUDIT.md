# External Links and References — Sitewide Developer Audit Instructions

**Scope:** Entire SearchSarkariNaukri project  
**Status:** Instructions prepared; findings require repository and site evidence.

## Complete checklist

## 10. External Links and Official References

- [ ] Verify every important external URL.
- [ ] Prefer the official website of the responsible department or examination authority.
- [ ] Link directly to the relevant notice or document instead of an unrelated homepage where possible.
- [ ] Identify broken, redirected, expired, suspicious, or misleading destinations.
- [ ] Clearly label official application links, notification PDFs, and third-party references.
- [ ] Ensure link text accurately describes the destination.
- [ ] Use appropriate `rel` attributes for sponsored, user-generated, or untrusted links.
- [ ] Use safe new-tab behaviour where applicable.
- [ ] Avoid unnecessary `nofollow` on legitimate editorial references.
- [ ] Do not sell or disguise links as official resources.
- [ ] Do not remove useful external citations simply to retain users on the website.
- [ ] Establish a process for reviewing important external links periodically.

## Detailed developer instructions

Verify destinations and redirects, prefer official direct notices, label source type accurately, flag expired/suspicious links, and review rel/new-tab behavior. Preserve useful citations and do not disguise third-party destinations as official.

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
