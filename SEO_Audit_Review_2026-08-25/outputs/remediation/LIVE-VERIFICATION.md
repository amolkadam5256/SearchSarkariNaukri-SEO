# Local and Live Verification

Verification date: 25 August 2026

## Local project

Project: `C:\Users\Administrator\Projects\SakariNaukariN`

- Backend test suite: 74 passed.
- Frontend production build: passed.
- Post-build checks: no localhost URLs; all five required production markers present; no forbidden patterns.
- Changed frontend files passed targeted ESLint checks. The repository-wide lint command still reports unrelated pre-existing lint findings outside this remediation scope.

## Live production

- `https://www.searchsarkarinaukri.com/`: 200
- `https://www.searchsarkarinaukri.com/quiz`: 200
- `https://api.searchsarkarinaukri.com/api/v1/jobs?page=1`: 200
- `https://www.searchsarkarinaukri.com/sitemap.xml`: 200
- Nginx: active
- PM2 `naukri-api`: online
- Unknown-route behavior: 404
- Trailing-slash canonicalization: 301
- Active job: emits `JobPosting`
- Expired job sample: `noindex,follow`, no `JobPosting`

## Complete live sitemap run

Source: `live-sitemap-verification-summary.json`, generated at 2026-08-25T08:42:10.508Z.

| Check | Result |
|---|---:|
| Child sitemaps | 12 |
| Child sitemap failures | 0 |
| URL occurrences | 1,124 |
| Unique URLs | 1,057 |
| Duplicate primary sitemap URLs | 0 |
| URLs verified | 1,057 |
| URLs with issues | 0 |
| Non-200 URLs | 0 |
| Redirects in sitemap | 0 |
| Noindex URLs in sitemap | 0 |
| Missing canonical | 0 |
| Non-self canonical | 0 |
| Invalid x-default | 0 |
| Expired JobPosting | 0 |

## Accessibility and performance

- Final axe-core WCAG A/AA browser audit: HTTP 200, zero violations, 29 passed rules. One contrast rule is incomplete because automated tooling cannot calculate backgrounds behind gradients; it is not a detected failure.
- Last valid post-core-remediation Lighthouse: Performance 74, Accessibility 89, Best Practices 100, SEO 100, FCP 1.79 s, LCP 4.58 s, TBT 321 ms, CLS 0.090.
- Four later Lighthouse attempts were excluded because Chrome returned `NO_NAVSTART`; those invalid reports are retained under `invalid-lighthouse-runs/` and are not used as evidence.
- Final accessibility corrections after the valid Lighthouse run were verified with axe-core, which reported zero WCAG A/AA violations.

## Rollback

- Full remediation backup: `/root/backups/ssn-seo-remediation-20260825T0810Z`
- Previous frontend build retained: `/var/www/sarkarinaukri/frontend/dist.pre-final-aria-20260825`
- Earlier frontend build retained: `/var/www/sarkarinaukri/frontend/dist.pre-final-a11y-20260825`
