# Missing Status Audit - Homepage Section Folder

Date: 2026-09-01
Folder: `.agents/07_OnPage_SEO/01_Home_Page`
Page target: `https://www.searchsarkarinaukri.com/`

## Executive Status

Documentation status: `COMPLETE`

Live implementation status: `NOT PROVABLE FROM THIS FOLDER`

Final verdict: `READY FOR DEVELOPER IMPLEMENTATION / NOT READY FOR PRODUCTION SIGNOFF`

All homepage section folders from `01_Hero` through `60_SHARE_ALERT_CTA` now contain at least one markdown specification file. The previous gap was that Sections `11-60` existed as folders but did not have detailed markdown implementation specs in the current workspace.

## Critical Developer Instruction

Do not delete existing homepage sections.

Do not remove, rename, rebuild, or replace the existing approved homepage section structure just to add the new specs.

The developer must:

1. Keep all existing homepage sections that are already implemented.
2. Preserve approved Sections `01-10` unless a verified bug requires a small scoped fix.
3. Update existing sections only for real issues such as broken links, wrong data, accessibility problems, performance problems, technical SEO problems, schema mismatch, canonical/robots/sitemap errors, or factual mistakes.
4. Add missing Sections `11-60` as new modular sections after the current approved flow.
5. If a section already exists in code with a different filename/component name, map the spec to that existing component instead of deleting and recreating it.
6. If any section destination URL returns `404` and is not needed, remove only that broken link or page reference. Do not delete the whole section unless the whole section is intentionally not needed and approved.
7. Do not change navbar, footer, header, logo, global menu, analytics, tracking, global styles, or unrelated routes.

Implementation approach:

- `EXISTING SECTION`: review, preserve, and patch only verified issues.
- `MISSING SECTION`: add as a new module using the matching `SECTION_SPEC.md`.
- `BROKEN LINK`: remove, restore `200`, one-hop `301`, or `410` according to the URL decision rules.
- `THIN/NOINDEX PAGE`: do not link from SEO/internal-link blocks until improved.

## Verified Local Coverage

| Area | Status | Evidence |
|---|---|---|
| Section folders `01-60` exist | `PASS` | Folder audit confirmed all section folders are present |
| Sections `01-10` have existing specs | `PASS` | Existing approved `.md` files are preserved |
| Sections `11-60` have specs | `PASS` | Each folder now has `SECTION_SPEC.md` |
| Root audit files exist | `PASS` | Files `00`, `03`, `06`, and `07` exist |
| Root prompt files exist | `PASS` | Files `01`, `02`, `04`, and `05` exist |
| Navbar/footer/header changes | `PASS` | No navbar, footer, header, logo, analytics, tracking, or global style files were changed |
| Live website source code checked | `FAIL / NOT AVAILABLE` | This workspace contains documentation/spec files, not the live app implementation |
| Live homepage crawl checked | `FAIL / NOT DONE` | No live crawl was run from this folder |

## Current File Structure Summary

Root-level homepage audit and prompt files:

1. `00_HOMEPAGE_TECHNICAL_SEO_AEO_GEO_AUDIT_2026-09-01.md`
2. `01_PROMPT_HOMEPAGE_FULL_TECHNICAL_AUDIT_AND_URL_CLEANUP.md`
3. `02_PROMPT_HOMEPAGE_IMPLEMENTATION_FIX_AND_FINAL_SIGNOFF.md`
4. `03_AUDIT_EXPANDED_HOMEPAGE_SECTIONS_11_TO_60_AND_OFFICIAL_PORTALS_2026-09-01.md`
5. `04_PROMPT_EXPANDED_HOMEPAGE_SECTIONS_11_TO_60_IMPLEMENTATION.md`
6. `05_PROMPT_OFFICIAL_GOVERNMENT_PORTALS_SECTION_AND_DIRECTORY.md`
7. `06_FIX_AUDIT_FAST_LOAD_SEMANTIC_SEO_AND_NO_ERROR_SIGNOFF.md`
8. `07_MISSING_STATUS_AUDIT_2026-09-01.md`
9. `08_MASTER_HOMEPAGE_AUDIT_FIRST_IMPLEMENTATION_PROMPT.md`
10. `09_HOMEPAGE_60_SECTION_AUDIT_SCORE_REPORT_TEMPLATE.md`

Section specification coverage:

- Sections `01-10`: existing approved section specs remain in place.
- Sections `11-60`: `SECTION_SPEC.md` added to every section folder.

## Completed Section Spec Coverage

The following missing folders are now filled:

| Range | Coverage |
|---|---|
| `11-17` | Career command, department/exam, qualification, job type, age eligibility, freshers, women jobs |
| `18-22` | Maharashtra jobs, district jobs, city jobs, state jobs, organization/recruiter directory |
| `23-27` | Admit cards, results, exam calendar, tools, study material |
| `28-32` | How it works, verification, trust, SEO introduction, official government job portals |
| `33-38` | UPSC, SSC, Railways/RRB, banking, defence, police/CAPF |
| `39-45` | Maharashtra authorities, Maharashtra department jobs, district SEO, city SEO, state SEO, qualification SEO, post-wise SEO |
| `46-54` | Jobs without written exam, document guide, how to apply, verification process, application journey, prep hub, popular searches, admit/result discovery, internal linking hub |
| `55-60` | UPSC updates, videos, job news, AEO direct answers, expanded FAQ, share alert CTA |

## Required Developer Implementation Next

Developers must now implement the homepage from the specs in the actual website code.

Priority order:

1. Read `08_MASTER_HOMEPAGE_AUDIT_FIRST_IMPLEMENTATION_PROMPT.md`.
2. Use `09_HOMEPAGE_60_SECTION_AUDIT_SCORE_REPORT_TEMPLATE.md` to score all 60 sections before implementation.
3. Audit first, report second, implement third, verify fourth.
4. Preserve Sections `01-10` exactly unless a verified bug requires a scoped fix.
5. Do not delete existing implemented sections. Update only the part that is wrong, missing, slow, inaccessible, non-semantic, technically broken, or SEO unsafe.
6. Add Sections `11-60` as modular homepage sections around the existing approved structure.
7. Keep the homepage fast by lazy-loading lower sections and caching expensive database calls.
8. Add Section `32_OFFICIAL_GOVERNMENT_JOB_PORTALS` as a concise trust/reference module.
9. Create or update the full internal directory page at `/official-government-job-portals`.
10. Use government portal links as official-source references, not as a homepage link farm.
11. Check every internal and external URL before publishing.
12. Remove any unneeded 404 URL from homepage links, sitemap, schema, breadcrumbs, related links, and internal-link hubs.
13. Use one-hop `301` only when there is a close relevant replacement.
14. Use `410 Gone` for permanently removed pages with no replacement.
15. Keep 404, 410, noindex, duplicate, redirected, and thin pages out of the sitemap.
16. Never invent vacancies, dates, salary, eligibility, age, selection process, government approval, subscriber count, job counts, or exam dates.

## Official Government Portal Requirement

Section `32_OFFICIAL_GOVERNMENT_JOB_PORTALS` must include grouped highlights for:

- Central recruitment sources such as NCS, Employment News, UPSC, SSC, India.gov.in, MyGov, Digital India, DoPT, and Ministry of Labour and Employment.
- Railway sources such as Railway Recruitment Control Board and verified regional RRBs.
- Banking sources such as IBPS, SBI Careers, RBI, NABARD, SEBI, SIDBI, LIC, NIACL, and GIC Re.
- Defence sources such as Indian Army, Indian Navy, Indian Air Force, Indian Coast Guard, DRDO, Ministry of Defence, Territorial Army, and NCC.
- Science/PSU sources such as ISRO, CSIR, BARC, ICMR, DBT, DST, NPCIL, HAL, BEL, BHEL, GAIL, ONGC, NTPC, and Coal India.
- Maharashtra sources such as MPSC, Maharashtra Police, Mahaswayam, Maharashtra Government, Public Health, Forest, Revenue, Education, Skill Development, Rural Development, and Urban Development.
- State employment portals verified through official sources such as NCS or state domains.

Do not publish unverified official URLs.

## Live QA Required Before Production Signoff

Final production signoff requires:

1. Website source code or deployment commit.
2. Live homepage crawl.
3. Live check that all homepage section links return valid status.
4. Confirmation that no 404, 410, noindex, redirect, duplicate, or thin page is linked from SEO/internal-link sections.
5. XML sitemap check.
6. Robots meta and `robots.txt` check.
7. Canonical URL check.
8. Structured data validation.
9. Lighthouse/PageSpeed check.
10. Mobile screenshot.
11. Desktop screenshot.
12. Accessibility check for search, cards, chips, accordions, and CTAs.

## Final Decision

Spec/documentation coverage: `COMPLETE`

Missing folder issue: `SOLVED`

Actual website implementation: `PENDING`

Production SEO signoff: `PENDING LIVE QA`

---

## Universal Developer Guardrail

Apply this rule before using this file for implementation:

1. Audit the existing homepage/component first.
2. Do not delete existing sections, components, internal links, SEO copy, metadata, schema, job data, or URLs without explicit approval.
3. Preserve approved Sections `01-10`; patch only verified issues.
4. If this section already exists in code, improve the existing component instead of rebuilding it unnecessarily.
5. Never invent vacancies, dates, salary, eligibility, age limits, selection process, official links, job counts, subscriber counts, exam dates, or government approval.
6. Verify every internal URL and official external URL before publishing.
7. Remove or replace links to true `404`/`410` pages; keep those URLs out of sitemap, schema, breadcrumbs, related links, and internal-link hubs.
8. Use one-hop `301` only when there is a close relevant replacement.
9. Do not create thin doorway pages, duplicate SEO pages, keyword-stuffed sections, or fake urgency.
10. Do not change navbar, footer, header, logo, global menu, global styles, analytics, tracking, or unrelated routes unless a documented bug requires it and regression QA is completed.
11. SearchSarkariNaukri must be described as an independent information portal, not an official government website.
12. Final signoff requires audit, implementation, live URL/status checks, sitemap/canonical/robots/schema validation, mobile QA, accessibility QA, and performance QA.
