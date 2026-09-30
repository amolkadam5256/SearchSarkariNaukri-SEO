# Section 62 — Trending exam chips (developer full spec)

## Placement

After hero or before “Latest Government Jobs” — **additive block**. Keep section `52_POPULAR_SEARCHES` if it exists; link both ways.

## H2

Trending government exams and recruitments 2026

## Helper line (optional)

“Shortcuts to exams candidates search most often this month.”

## Chips (anchor text → URL)

Implement as `<nav aria-label="Trending exams">` with `<ul>` of links.

| Chip label | Href |
|------------|------|
| SSC CGL 2026 | `/department/ssc` or live exam slug |
| SSC CHSL 2026 | `/department/ssc` |
| UPSC Civil Services 2026 | `/department/upsc` |
| IBPS PO 2026 | `/category/banking-jobs` |
| IBPS Clerk 2026 | `/category/banking-jobs` |
| RRB NTPC 2026 | `/category/railway-jobs` |
| RRB Group D 2026 | `/category/railway-jobs` |
| MPSC Rajyaseva 2026 | `/department/mpsc` |
| Police SI / Constable | `/category/police-jobs` |
| Teaching / CTET | `/category/teaching-jobs` |

Verify each URL is 200 before ship; swap to exam detail page when available.

## Marathi optional secondary chip row

One row max, e.g. “MPSC भरती 2026” → `/department/mpsc` — only if homepage already uses Marathi in hero.

## Schema

None required; links are internal discovery.

## QA

- [ ] Keyboard focus visible on chips  
- [ ] No horizontal overflow on 320px width  
