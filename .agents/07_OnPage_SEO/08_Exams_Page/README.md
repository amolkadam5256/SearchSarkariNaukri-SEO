# Government Exams Page - Implementation Package

**Project:** SearchSarkariNaukri  
**Target:** `/exams` page  
**Status:** Implementation Ready  
**Date:** 21 September 2026

---

## Package Purpose

This folder contains the complete on-page SEO, GEO, AEO, content, UX, schema, performance and QA specification for rebuilding `/exams` into a true Government Exam Directory.

The current `/exams` page framework is good, but the page body is incomplete. It promises UPSC, SSC, MPSC, Banking, Railway, Defence, Police Bharti, Teacher and CDPO coverage, while the current directory is mostly MPSC. The next update should make `/exams` a full India + Maharashtra exam hub, not only an MPSC directory.

## Files

- `00_MASTER_EXAMS_PAGE_AUDIT.md` - Full audit, priority order and missing sections.
- `01_PAGE_STRUCTURE_AND_SECTIONS.md` - Exact recommended section order and page layout.
- `02_EXAM_DIRECTORY_AND_CARD_SPEC.md` - Complete exam groups and reusable ExamCard specification.
- `03_SEO_GEO_AEO_SCHEMA_SPEC.md` - Metadata, canonical, GEO, AEO, schema and FAQ requirements.
- `04_DEVELOPER_IMPLEMENTATION_INSTRUCTIONS.md` - Developer-ready implementation steps and performance guidance.
- `05_FINAL_QA_CHECKLIST.md` - Complete acceptance checklist.
- `06_COMPLETE_PAGE_CONTENT.md` - Production-ready content for every `/exams` section, including exam groups, tables, FAQs, official links and related resources.

## Main Objective

Build `/exams` as:

```text
Government Exams 2026 - UPSC, SSC, MPSC, Banking, Railway & More
```

The page should help users:

- Find major central and state government exams.
- Compare exam eligibility, qualification, level, coverage, posts and selection stages.
- Discover exams by location, qualification and career goal.
- Track upcoming exam dates and latest notifications.
- Move naturally to syllabus, admit cards, results, cutoffs, current affairs, quizzes, exam calendar, eligibility checker and career guidance.

## Non-Negotiable Rules

- Do not make `/exams` another thin MPSC-only page.
- Do not create empty exam pages just for keywords.
- Do not fabricate exam dates, eligibility, cutoffs, syllabus or notification data.
- Do not put an entire exam card inside one link.
- Do not call exam-centre city a job location.
- Do not use JobPosting schema on `/exams`.
- Do not add huge generic SEO paragraphs.
- Do not slow the page with unnecessary JavaScript, images or layout shifts.

## Priority Summary

P0:

- Add visible breadcrumb.
- Improve H1 and intro.
- Add Exam Finder.
- Build reusable standardized ExamCard.
- Populate UPSC, SSC, Banking, Railway, Defence, Police, Teaching, Engineering, Agriculture/Forest and CDPO/WCD groups.
- Use `06_COMPLETE_PAGE_CONTENT.md` as the content source. Do not leave placeholder text such as "add section".

P1:

- Add Exams by Location.
- Add Exams by Qualification.
- Add Exams by Career Goal.
- Add Upcoming Exam Dates.
- Add Latest Exam Notifications.
- Add Admit Cards / Results / Cutoffs / Calendar block.
- Add Preparation Resources.

P2:

- Add Compare Government Exams.
- Add How to Choose an Exam.
- Add Official Exam Authorities.
- Add FAQ and verification note.
- Polish performance and accessibility.

---

**Last Updated:** 22 September 2026  
**Status:** Ready for Implementation
