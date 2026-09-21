# 04 - DEVELOPER IMPLEMENTATION INSTRUCTIONS

**Page:** `/exams`  
**Priority:** P0  
**Status:** Ready for Implementation

---

## Implementation Approach

Use existing site design and navigation. Add page-body sections and data structures without breaking existing header, footer, routes or internal tools.

Use `06_COMPLETE_PAGE_CONTENT.md` for production copy. The implementation should not ship placeholder instructions like "add UPSC section" or "add FAQ". Each section must use actual content, cards, tables and answers from the complete content file.

## Phase 1 - Foundation

1. Add visible breadcrumb.
2. Update H1 and intro.
3. Add Exam Finder.
4. Create reusable ExamCard.
5. Refactor existing MPSC cards into the ExamCard format.
6. Pull hero, finder labels and popular exam content from `06_COMPLETE_PAGE_CONTENT.md`.

## Phase 2 - Directory Expansion

Populate all groups:

- MPSC & Maharashtra State Exams
- UPSC
- SSC
- Banking
- Railway
- Defence
- Police / Uniformed Services
- Teaching
- Engineering / Technical
- Agriculture & Forest
- CDPO / WCD

Use only exams with maintainable content. If a detail page does not exist, either create a useful detail page or use a non-misleading disabled/coming-soon treatment. Do not create empty pages.

The required group intros and card rows are already written in `06_COMPLETE_PAGE_CONTENT.md`.

## Phase 3 - Discovery Sections

Add:

- Popular Government Exams
- Exams by Location
- Exams by Qualification
- Exams by Career Goal
- Compare Popular Government Exams

Use the exact section copy, tables and resource labels from `06_COMPLETE_PAGE_CONTENT.md`.

## Phase 4 - Freshness Sections

Add dynamic sections from real data:

- Upcoming Government Exam Dates
- Latest Government Exam Notifications
- Admit Cards / Results / Cutoffs / Exam Calendar block

Do not fabricate dates or expected timelines.

Use the fallback text from `06_COMPLETE_PAGE_CONTENT.md` when no upcoming date or notification data exists.

## Phase 5 - Learning and Trust

Add:

- Preparation Resources
- Daily Practice and Learning Tools
- How to Choose the Right Government Exam
- Official Exam Authorities
- FAQ
- Verification / disclaimer

Use the FAQ answers, official authority table, disclaimer and related-resource table from `06_COMPLETE_PAGE_CONTENT.md`.

## Performance Requirements

- Render meaningful HTML for H1, intro, exam groups and important links where practical.
- Avoid shipping all filters as heavy client-only JavaScript.
- Lazy-load noncritical sections if needed, but keep primary content crawlable.
- Use CSS grid/flex without layout shift.
- Reserve stable dimensions for cards.
- Avoid large images; this page can be mostly text and UI cards.
- Keep LCP <= 2.5 seconds, INP < 200 ms, CLS < 0.1.
- Cache static exam metadata where safe.
- Use paginated/lazy sections only if the initial page still exposes major exam categories.

## Accessibility Requirements

- One H1.
- Logical H2/H3 hierarchy.
- Search input has label.
- Filter chips are links or buttons with correct semantics.
- Cards are not one giant anchor.
- Focus states visible.
- Touch targets at least 44px on mobile.
- Tables have headers.
- No horizontal overflow on mobile.

## Data Model Guidance

Recommended exam fields:

- id
- name
- slug
- conducting_body
- exam_level
- coverage
- minimum_qualification
- age_summary
- major_posts
- selection_stages
- category
- career_goal
- location_group
- official_url
- detail_url
- next_event_type
- next_event_date
- last_updated

## Do Not

- Do not fabricate exam dates.
- Do not use inaccurate age limits.
- Do not create pages for unsupported exams.
- Do not duplicate cards across sections with different URLs.
- Do not hide core exam links behind JavaScript-only controls.
- Do not use JobPosting schema on `/exams`.
- Do not ship incomplete placeholder copy.

---

**Last Updated:** 22 September 2026
