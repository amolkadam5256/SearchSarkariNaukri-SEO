# 00 - MASTER EXAMS PAGE AUDIT

**Page:** `/exams`  
**Audit Date:** 21 September 2026  
**Priority:** P0  
**Status:** Implementation Required

---

## Core Finding

The `/exams` page framework is good, but the actual exam hub is incomplete. The page promises coverage for UPSC, SSC, MPSC, Banking, Railway, Defence, Police Bharti, Teacher and CDPO, but the current body is overwhelmingly MPSC.

The fix is not more generic exam text. The fix is a complete, structured Government Exam Directory.

## Current Gap Summary

| Section | Current Status | Action |
| --- | --- | --- |
| Breadcrumb | Missing | Add visible `Home > Government Exams` |
| Hero / H1 | Present | Improve wording |
| Short intro | Thin | Add 2-3 useful lines |
| Exam finder/search | Missing | Add near top |
| Quick filters | Partial | Expand |
| Popular Government Exams | Missing | Add |
| All Government Exams Directory | Incomplete | Major rebuild |
| Exams by Location | Missing | Add |
| Exams by Qualification | Missing | Add |
| Exams by Career/Department | Missing | Add |
| Upcoming Exam Dates | Missing | Add |
| Latest Exam Notifications | Missing | Add |
| Admit Cards / Results / Cutoffs | Missing | Add |
| Compare Government Exams | Missing | Add |
| Preparation Resources | Missing | Add |
| Daily Practice | Weak | Add links to existing tools |
| How to Choose an Exam | Missing | Add |
| Official Exam Authorities | Missing | Add |
| FAQ | Missing | Add |
| Editorial / verification note | Missing | Add |
| Related resources | Weak in body | Add contextual block |
| Footer | Present | Keep |

## Recommended Final Page Order

1. Header / navigation
2. Breadcrumb: `Home > Government Exams`
3. H1: `Government Exams 2026 - UPSC, SSC, MPSC, Banking, Railway & More`
4. Short 2-3 line intro
5. Exam Finder
6. Popular Government Exams
7. All Government Exams Directory
8. Exams by Location
9. Exams by Qualification
10. Exams by Career Goal
11. Upcoming Government Exam Dates
12. Latest Government Exam Notifications
13. Admit Cards / Results / Cutoffs / Exam Calendar
14. Compare Popular Government Exams
15. Preparation Resources
16. Daily Practice and Learning Tools
17. How to Choose the Right Government Exam
18. Official Exam Authorities
19. FAQ
20. Verification / disclaimer
21. Related resources
22. Footer

## P0 Sprint

- Build a reusable ExamCard component.
- Populate non-MPSC exam groups.
- Add Exam Finder filters.
- Add visible breadcrumb.
- Ensure every card has standardized fields.
- Keep cards concise and link to detail pages.

## P1 Sprint

- Add location, qualification and career sections.
- Connect Exam Calendar, Admit Cards and Results.
- Add latest exam notifications from real data.
- Add preparation tools and practice resources.

## P2 Sprint

- Add comparison table.
- Add official authorities.
- Add FAQ.
- Add page-specific disclaimer.
- Optimize performance and accessibility.

---

**Last Updated:** 21 September 2026
