# Round 1 Fix Tracker - GSC Error Folder

Date: 2026-08-29
Use after completing `01_ROUND_1_AUDIT_CHECKLIST.md`.

## How To Use

For every failed item found in Round 1, add one row here before changing code. Fix only the failing issue. Do not widen scope into footer, navbar, global layout, or unrelated pages.

## Fix Tracker

| No | Issue Folder | URL / Template / Sitemap | Failure Found | Required Fix | Owner | Status | Retest Evidence |
|---:|---|---|---|---|---|---|---|
| 1 | TO_FILL | TO_FILL | TO_FILL | TO_FILL | TO_FILL | OPEN | TO_FILL |

## Required Fix Order

1. Fix P0 technical blockers first: 404 for valid records, redirect errors, wrong sitemap URLs, accidental noindex.
2. Fix template-level content problems next: thin landing pages, thin admit-card detail pages, missing FAQ answers.
3. Fix canonical/internal-link/schema mismatches.
4. Regenerate sitemap only after final canonical URLs are correct.
5. Run Round 2 audit after deployment or staging verification.

## Do Not Mark Fixed Until

- Live/staging URL behavior matches the audit rule.
- Sitemap output is regenerated and checked.
- Canonical and robots meta are correct.
- Internal links and structured data use the same final URL.
- Evidence is added in the `Retest Evidence` column.

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix a specific Google Search Console indexing issue.
