# 00 — MASTER IMPLEMENTATION MAP: /jobs Page SEO + GEO + AEO Complete Rebuild

**URL:** https://www.searchsarkarinaukri.com/jobs  
**Prepared:** 4 September 2026  
**Purpose:** Production-ready SEO + UX + technical SEO + GEO + AEO implementation for the `/jobs` hub  
**Status:** Implementation Ready

---

## Executive Decision

The `/jobs` page should own the broad topic **Government Jobs**. It must NOT try to be the primary ranking page for every exam, state, qualification and department query. Those should be supported by dedicated landing pages and exam/district pages.

### Primary Keyword
**Government Jobs**

### Secondary Entity
**Sarkari Naukri**

### Recommended Title
```
Government Jobs 2026 – Latest Sarkari Naukri & Govt Jobs
```

### Recommended Meta Description
```
Find the latest Government Jobs 2026 and Sarkari Naukri in India. Browse active govt vacancies by qualification, department, state, district and exam.
```

### Only H1
```
Government Jobs 2026 – Latest Active Sarkari Naukri
```

---

## Exact Page Order

1. Hero / H1 / breadcrumb
2. Search Government Jobs
3. Closing Soon
4. Latest Government Jobs
5. Government Jobs by Qualification
6. Government Jobs by State
7. Government Jobs by Department
8. Government Jobs by Exam
9. How to Find the Right Government Job
10. Useful Government Job Resources
11. About These Government Job Listings / Trust
12. FAQ
13. Final alert CTA

---

## File Map

| File | Section | Priority |
|---|---|---|
| 01_ground_rules_do_not_delete_UPDATED.md | Ground Rules (KEEP) | P0 |
| 00_MASTER_IMPLEMENTATION_MAP.md | This File | P0 |
| 01_HERO_SECTION_METADATA.md | H1, intro, metadata, breadcrumb | P0 |
| 02_SEARCH_FILTERS_SECTION.md | Search, filters, chips, faceted SEO | P0 |
| 03_CLOSING_SOON_SECTION.md | Deadline-focused job block | P0 |
| 04_LATEST_JOBS_SECTION.md | Main dynamic inventory | P0 |
| 05_BY_QUALIFICATION_SECTION.md | 10th/12th/ITI/Diploma/Graduate/Engineering/PG | P1 |
| 06_BY_STATE_SECTION.md | India + Maharashtra + districts | P1 |
| 07_BY_DEPARTMENT_SECTION.md | Railway, Banking, Police, Teaching, etc. | P1 |
| 08_BY_EXAM_SECTION.md | UPSC, MPSC, SSC, Railway, Banking, Police, CTET | P1 |
| 09_HOW_TO_FIND_JOB_SECTION.md | AEO/GEO explainer | P1 |
| 10_RESOURCES_SECTION.md | Eligibility, age, calendar, admit card, results, etc. | P1 |
| 11_ABOUT_TRUST_SECTION.md | E-E-A-T, source, disclaimer, editorial process | P1 |
| 12_FAQ_SECTION.md | Long-tail/AEO questions | P1 |
| 13_INTERNAL_LINKING_MAP.md | Contextual internal links | P1 |
| 14_KEYWORD_MAP.md | Keyword architecture and placement | P1 |
| 15_TECHNICAL_SEO_GEO_AEO_CHECKLIST.md | Developer handoff | P0 |
| 16_CONTENT_COMPONENT_SPEC.md | UI/component implementation rules | P1 |
| 17_KEYWORD_RESEARCH_FRAMEWORK.md | Short-tail, long-tail, low-competition strategy | P2 |

---

## Non-Negotiable SEO Rules

- **One H1 only.**
- **One primary keyword: Government Jobs.**
- **Do not repeat the exact primary phrase in every heading.**
- **Keep the jobs/search experience above long-form content.**
- **Do not create thousands of indexable filter combinations.**
- **Do not fabricate search volume, salary, vacancies, dates or eligibility.**
- **Use real official sources on individual job pages.**
- **Expired jobs should become Closed, not disappear without a strategy.**
- **Use JobPosting on eligible individual job pages, not the `/jobs` hub as one giant job.**
- **Use server-rendered/crawlable pagination.**
- **Clean broken data such as `[email protected]`.**
- **Replace "0 days left" with "Closes Today".**
- **Display a real last-updated timestamp.**
- **Do not claim "verified" unless an actual verification workflow exists.**

---

## Implementation Priority

### P0 - Critical (Do First)
1. Update H1, title, meta description (approved edit exception)
2. Add breadcrumb navigation
3. Improve search/filter UX
4. Add "Government Jobs Closing Soon" section
5. Fix job card semantic HTML
6. Clean up data artefacts
7. Implement proper expiry handling
8. Add crawlable pagination
9. Add basic FAQ section
10. Add contextual internal links

### P1 - High Priority (Next Sprint)
11. Add "Government Jobs by Qualification" section
12. Add "Government Jobs by State" section (Maharashtra focus)
13. Add "Government Jobs by Department" section
14. Add "Government Jobs by Exam" section
15. Add "How to Find the Right Government Job" section
16. Add "Useful Government Job Resources" section
17. Add "About These Government Job Listings" trust section
18. Expand FAQ with long-tail questions
19. Implement structured data (JobPosting on individual pages only)
20. Add BreadcrumbList structured data

### P2 - Medium Priority (When Time Allows)
21. Create dedicated qualification landing pages
22. Create Maharashtra/location landing pages
23. Create department landing pages
24. Implement advanced GEO/AEO optimizations
25. Build related jobs recommendation engine
26. Improve Core Web Vitals
27. Add comprehensive internal linking architecture

---

## Success Criteria

The page is considered production-ready only when:

- [ ] Search intent is clear within 3 seconds
- [ ] Users can find jobs by keyword, qualification, location, department and deadline
- [ ] Google can crawl the important job URLs without JS interaction
- [ ] AI/answer engines can parse organisation, role, location, qualification, vacancies and dates
- [ ] High-value category pages receive contextual links
- [ ] Expired inventory is correctly handled
- [ ] Core Web Vitals are monitored
- [ ] Search Console indexing/crawl errors are reviewed after deployment
- [ ] All changes are additive (no deletions except approved fixes)
- [ ] Existing functionality remains intact

---

## Developer Instructions

1. **Read this file first** - This is the master map
2. **Read 01_ground_rules_do_not_delete_UPDATED.md** - This governs everything
3. **Audit the actual React project** - Before making any changes
4. **Create implementation plan** - Map requirements to actual components
5. **Review plan against these files** - Before coding
6. **Implement in priority order** - P0 → P1 → P2
7. **Test thoroughly** - Each phase before moving to next
8. **Validate with SEO tools** - Google Rich Results Test, URL Inspection
9. **Monitor performance** - Core Web Vitals, Search Console
10. **Document any deviations** - Flag conflicts before implementing

---

## Important Notes

> **No SEO plan can guarantee a #1 ranking.** This architecture is designed to maximize relevance, crawlability, topical authority, user satisfaction and answer-engine discoverability.

> **All changes must be additive.** Do not delete existing code, components, or sections unless explicitly approved as a fix in the ground rules.

> **This is a living document.** Update as implementation progresses and new insights are discovered.

---

## Next Steps

1. Review all files in this folder
2. Audit the current `/jobs` page implementation
3. Create detailed implementation plan
4. Begin with P0 items
5. Validate each phase before proceeding
6. Monitor results and iterate based on data

---

**Last Updated:** 4 September 2026  
**Version:** 1.0  
**Status:** Ready for Implementation