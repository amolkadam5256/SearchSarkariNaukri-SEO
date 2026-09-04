# 07 — New Landing Pages: Qualification / Category / Location / Recruiter (Additive Only)

> These are **new routes** added alongside your existing ones. Your existing `/jobs?qualification=12th`-style filters, and your existing `/districts/...` architecture, keep working exactly as they do today — these new pages are separate, dedicated, indexable pages that link back into the existing filtered views.

## New URL structure to add (does not replace anything existing)

```
/qualification/10th-pass-government-jobs
/qualification/12th-pass-government-jobs
/qualification/iti-government-jobs
/qualification/diploma-government-jobs
/qualification/graduate-government-jobs
/qualification/engineering-government-jobs
/qualification/post-graduate-government-jobs

/category/mpsc-jobs
/category/ssc-jobs
/category/railway-jobs
/category/banking-jobs
/category/police-jobs
/category/teaching-jobs
/category/health-jobs
/category/defence-jobs
/category/forest-jobs
/category/talathi-jobs
/category/zilla-parishad-jobs

/recruiters/upsc
/recruiters/ssc
/recruiters/ibps
/recruiters/mpsc
/recruiters/rrb
/recruiters/sbi

/maharashtra-government-jobs
/closing-soon-government-jobs
```

For districts, **reuse your existing `/districts/{slug}` pages** rather than creating a second set — just make sure each one meets the content bar below (see file 09 §7 for district-page depth requirements).

## Page template for each new page

```
H1: {Qualification/Category/Location} Government Jobs 2026
Intro: 150–300 original words — what this page covers, who it's for
Live job list: filtered from the same API/data source as /jobs (reuse existing logic)
H2: Eligibility / Who Can Apply (for qualification pages)
H2: Related Categories
H2: Related Locations
H2: FAQs (3–6 questions specific to this page)
Breadcrumb: Home > Government Jobs > {this page}
```

Each page can call the same underlying job API/filter logic your existing `/jobs?qualification=12th` filter already uses — this is a new presentation layer on top of existing data, not new backend logic.

## Keyword map (primary keyword per URL — avoid overlap/cannibalization)

| URL | Primary keyword | Secondary keywords |
|---|---|---|
| `/jobs` | latest government jobs 2026 | sarkari naukri, govt jobs |
| `/maharashtra-government-jobs` | Maharashtra government jobs 2026 | Maharashtra govt jobs |
| `/qualification/10th-pass-government-jobs` | 10th pass government jobs | 10th pass govt jobs |
| `/qualification/12th-pass-government-jobs` | 12th pass government jobs | 12th pass govt jobs |
| `/qualification/iti-government-jobs` | ITI government jobs | ITI govt jobs |
| `/qualification/diploma-government-jobs` | diploma government jobs | diploma govt vacancies |
| `/qualification/graduate-government-jobs` | graduate government jobs | graduate govt jobs |
| `/category/mpsc-jobs` | MPSC recruitment 2026 | MPSC Bharti 2026 |
| `/category/police-jobs` | police bharti 2026 | police recruitment |
| `/category/railway-jobs` | railway recruitment 2026 | railway government jobs |
| `/category/ssc-jobs` | SSC recruitment 2026 | SSC government jobs |
| `/category/banking-jobs` | banking government jobs | IBPS recruitment |
| `/districts/pune` | Pune government jobs 2026 | govt jobs in Pune |
| `/districts/mumbai` | Mumbai government jobs 2026 | govt jobs in Mumbai |
| `/districts/nagpur` | Nagpur government jobs 2026 | govt jobs in Nagpur |
| `/closing-soon-government-jobs` | government jobs last date | govt jobs closing soon |

## Rollout priority (easiest wins first)

**Priority 1 — build first:**
12th Pass · 10th Pass · ITI · Diploma · Graduate · Maharashtra · Pune · Nagpur · Nashik · Mumbai

**Priority 2 — build next:**
Police Bharti · Talathi Bharti · MPSC · Railway · Closing Soon

## Marathi keyword coverage (optional, additive)

If genuinely localized Marathi content exists or is planned, target (via existing bilingual content, not necessarily separate URLs unless content is truly distinct):

```
महाराष्ट्र सरकारी नोकरी 2026 · महाराष्ट्र सरकारी भरती 2026 · पोलीस भरती 2026
तलाठी भरती 2026 · जिल्हा परिषद भरती 2026 · 12वी पास सरकारी नोकरी
```

Only create separate Marathi URLs when you have real, distinct localized content — otherwise keep it as bilingual copy on the existing English URL, and skip `hreflang` entirely (it's only needed for true separate-URL translations).

## Checklist for this file

- [ ] New qualification pages created (7)
- [ ] New category pages created (11)
- [ ] New recruiter pages created (6)
- [ ] `/maharashtra-government-jobs` and `/closing-soon-government-jobs` created
- [ ] Each new page reuses existing job data/filter logic (no duplicate backend)
- [ ] Keyword map respected — no two pages targeting the same primary keyword
- [ ] Existing `/jobs?qualification=...` filters and `/districts/...` pages untouched
