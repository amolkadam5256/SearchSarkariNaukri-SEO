# Security Privacy and Reliability — Sitewide Developer Audit Instructions

**Scope:** Entire SearchSarkariNaukri project  
**Status:** Instructions prepared; findings require repository and site evidence.

## Complete checklist

## 17. Security, Privacy, and Reliability

- [ ] Check for exposed secrets and credentials.
- [ ] Ensure private environment variables are not shipped to the browser.
- [ ] Review dependency vulnerabilities.
- [ ] Validate and sanitize untrusted inputs appropriately.
- [ ] Check external link handling and unsafe HTML rendering.
- [ ] Review API authorization and access controls where applicable.
- [ ] Check rate limiting and abuse protection for relevant endpoints.
- [ ] Ensure personal data is not unnecessarily collected or logged.
- [ ] Verify privacy and consent behaviour where legally required.
- [ ] Check error messages for accidental disclosure of sensitive information.
- [ ] Preserve secure headers and deployment configuration.
- [ ] Do not introduce third-party scripts, packages, or services without evaluating their necessity and risk.

## Detailed developer instructions

Check secrets without exposing values, private env vars, input handling, unsafe HTML, auth/access, abuse controls, personal-data logging, consent, error disclosure, headers and dependencies. Assess new services/packages for risk. Escalate security-sensitive findings through project process.

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
