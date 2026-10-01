# Decision brief — “Jobs for Female Candidates” homepage card

**Current live behaviour (per release PDF):** Card opens **graduate jobs** page — intent mismatch.  
**Existing spec:** `01_Home_Page/17_WOMEN_JOBS/SECTION_SPEC.md`

---

## Options

| Option | Route | Pros | Cons |
|--------|-------|------|------|
| **A (recommended)** | `/women-government-jobs` or `/government-jobs-for-women` | Matches card label; owns “government jobs for women” long-tail | Needs 200+ words unique copy + filtered job list or curated links |
| **B** | `/jobs?qualification=graduate` | Zero build | Misleading; ignores 10th/12th women candidates |
| **C** | `/jobs` with `?tag=women` or category filter | Reuses listing | Needs backend filter + official “women only” posts are rare — mostly general posts open to all genders |
| **D** | Remove card | No maintenance | Loses discovery slot |

---

## If Option A — minimum page content

**H1:** Government Jobs for Women — Sarkari Naukri Opportunities 2026

**Intro (factual):** Most government vacancies are open to all eligible candidates regardless of gender. Some notifications mention women-specific quotas, relaxation, or posts in departments commonly searched by women candidates (teaching, health, banking clerical, police where notified). Always read the official notification.

**Sections:**

- Browse all jobs → `/jobs`
- Teaching → `/exams/ctet` or teaching category
- Health → medical jobs category if live
- Police → state police exam pages
- Banking → `/exams/sbi-po-clerk`
- Eligibility → `/eligibility-checker`

**Do not claim** reservation for women unless the notification states it.

**Internal link from homepage card:** update href to chosen route.

---

## SEO

- Primary: `government jobs for women`, `Sarkari Naukri for female candidates`
- Do not cannibalize `/jobs` — this is a **guidance/discovery** page

---

## Decision required from TR / SEO

- [ ] Option A / B / C / D  
- [ ] Preferred URL slug  
- [ ] Approve build in next dev sprint
