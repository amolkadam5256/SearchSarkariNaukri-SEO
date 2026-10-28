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

---

# Implementation Addendum — Clear Content, Page Flow and Review Checklist

Keep every existing section, paragraph, exam entry, filter, useful link and working feature. Treat the requirements below as additions that clarify how to implement the page. Do not remove or silently shorten approved content while improving its layout or wording.

## Developer outcome

Build `/exams` as a clear, easy-to-scan guide that helps a candidate:

1. Find an exam by name, qualification, conducting body, location or career goal.
2. Understand the basic eligibility and selection process.
3. Check current dates, notifications, admit cards and results from reliable data.
4. Continue to relevant exam details, official sources and preparation resources.

Use plain English, short paragraphs, descriptive headings and familiar labels. Explain abbreviations on first use where space allows. Keep factual information distinct from guidance, and make every visible button or link perform its stated action.

## Required page order and section content

Keep all existing material and arrange the full page in this candidate journey. If a matching section already exists, improve and reuse it rather than creating a duplicate.

1. **Breadcrumb and page introduction** — Show `Home > Government Exams`, one clear H1, a short explanation of what the directory helps candidates do, a last-verified date only when supported by data, and visible links to the exam finder, calendar and eligibility checker.
2. **Government Exam Finder** — Provide a labeled search field plus functional qualification, conducting-body, category and recruitment-status filters. Include a reset action, selected-filter state, useful no-results message and links to existing exam detail pages.
3. **Popular Government Exams** — Show the established popular exams as compact, consistent cards. Each card identifies the exam, conducting body, qualification, coverage and a direct descriptive action.
4. **Government Exams by Qualification** — Provide distinct entry points for 10th pass, 12th pass, ITI, diploma, graduate, postgraduate, engineering, medical/professional and agriculture qualifications where supported. State that exact requirements depend on the post and current notification. Link each option to actual filtered results or relevant maintained content.
5. **All Government Exams Directory** — Preserve all 40 listed exams and every existing category. Keep the Maharashtra, UPSC, SSC, banking, railway, defence, police/uniformed services, teaching, engineering/technical, agriculture/forest and Women & Child Development/CDPO groups. Do not remove a record because its detail page is not yet available; show an honest availability state and do not link to an empty route.
6. **Upcoming Government Exams** — Show only sourced events, with exam, event type, date, status, source and detail link. Visibly distinguish official dates from tentative schedules. If no verified events exist, show the approved empty-state message rather than invented dates.
7. **Latest Notifications and Application Windows** — Present supported updates with exam, authority, update type, relevant date, current state and official notice link. Sort consistently and deduplicate the same update using its exam and recruitment-cycle identity.
8. **Admit Cards, Results and Cutoffs** — Link each item to the correct exam and recruitment cycle. Retain distinct stages or outcomes; remove only genuine duplicate records. Do not label an item as released unless the source confirms it.
9. **State-Wise Government Exams** — Group records by the actual state or national coverage. Keep Maharashtra content prominent where appropriate. Correct the mapping of TPSC to Tripura, BPSC to Bihar and JPSC to Jharkhand; do not place them under Maharashtra. Explain domicile, language and state-specific requirements only when supported by the applicable notice.
10. **Government Exams by Career Goal** — Offer concise paths for civil services/administration, banking/finance, railways/technical services, defence/uniformed services, teaching/education, clerical/support roles and child development/welfare. Link to existing exams or working filtered results.
11. **Compare Popular Government Exams** — Keep factual comparison rows for the currently supported popular exams. Use semantic column headers for exam, authority, qualification, age criteria, selection stages, current status and official source when verified. On small screens, preserve readable access to every column. Explain that requirements vary by post, category and recruitment cycle.
12. **Syllabus and Preparation Resources** — Provide useful links for syllabus, exam pattern, previous-year papers/answer keys, daily assessment, current affairs and available study material. Link only to resources that exist and accurately describe access.
13. **How to Choose the Right Government Exam** — Give a short numbered guide covering qualification, age/category rules, career type, location, selection stages, preparation needs and checking the current official notification. Link to the existing eligibility checker.
14. **Official Exam Authorities** — Group and validate relevant authority links. Prefer the specific notice or recruitment portal for an exam when available; use the official organization homepage only when that is the appropriate maintained destination.
15. **How We Verify Exam Information** — Explain in plain language that schedules and eligibility can change, cite official sources in the interface, show verification time only when the system records it, and clearly identify the service as independent.
16. **Frequently Asked Questions** — Answer candidate questions about exams by qualification, dates, notifications, eligibility, age relaxation, syllabus and the site's independent status. Keep answers short, visible in rendered content and consistent with the actual directory. Use FAQ structured data only when it matches visible content and current eligibility rules.
17. **Related resources and final navigation** — Keep useful links to jobs, job updates, calendar, admit cards, results, current affairs, quizzes, daily assessment, digital library, eligibility checker, age calculator, career guidance and district jobs where those routes exist.

## Content format for each section

Use this consistent pattern so candidates can scan the page quickly:

```text
Section heading
One short sentence explaining what the section helps the candidate do.
Cards, filters, a compact table or a short numbered list, as appropriate.
One clear action with a descriptive label.
Source, eligibility caveat or freshness label where relevant.
```

Use cards for exam discovery and resource links, tables for comparisons and time-based records, and numbered steps for guidance. Keep card text concise: exam name; conducting body; qualification; coverage; key stages or posts when verified; current event only when sourced; and a clear detail action. Do not repeat the same long explanation in multiple sections. Avoid unexplained acronyms, dense paragraphs, decorative keyword lists and labels such as “Click here.”

## Content and data handling

- Preserve the complete 40-exam directory, existing useful copy, currently working filters and internal routes.
- Treat the underlying recruitment data and official notices as the source of truth for dates, eligibility, age, vacancies, status and results. Static editorial copy must not override newer verified records.
- Verify category totals, qualification counts, state mapping, official URLs and detail links against the actual records before display. An exam may appear in more than one qualification group when its posts permit it; calculate counts from the displayed records.
- Distinguish job/service coverage from the city where an exam is held.
- Mark information as tentative when the authority describes it as tentative. Do not infer a date or status from a previous cycle.
- Keep a clear fallback state for missing data. Hide unsupported values or say that details are not available; never fill gaps with guesses.
- Do not promise automatic, hourly or live verification unless the running system performs and records it.

## Readability and interaction requirements

- Keep the existing site header, footer, navigation and global tools working.
- Use one H1, then a logical H2/H3 structure. Keep headings specific and short.
- Keep the exam finder and main discovery actions near the beginning of the page.
- Use consistent card layouts, readable spacing, clear status labels and responsive type sizes.
- Make filters, accordions, links and buttons keyboard accessible with visible focus states and clear labels.
- Make status understandable without relying on color alone. Avoid horizontal overflow; make wide tables usable on mobile.
- Keep core exam names and links available in rendered HTML. Do not hide the directory behind client-only interaction.
- Preserve stable routes and avoid adding duplicate content pages for keyword variations.

## Developer completion checklist

Use the individual section instruction sheets in [`sections/README.md`](sections/README.md). Complete both verification passes and the completion record in every section sheet. The shared page-level checklist below remains required as well.

### Content and completeness

- [ ] All 40 directory entries remain available and are assigned to accurate categories.
- [ ] Every existing section and useful piece of content remains represented.
- [ ] Each of the 17 page sections above is present or is satisfied by an improved existing section.
- [ ] Maharashtra, UPSC, SSC, banking, railway, defence, police, teaching, technical, agriculture/forest and CDPO/WCD content is retained.
- [ ] Qualification groups, state mappings, counts and caveats match the underlying exam records.
- [ ] No placeholder text, unsupported claim or fabricated recruitment detail is visible.

### Functionality and links

- [ ] Search matches exam names, abbreviations and supported aliases.
- [ ] Qualification, authority, category and supported status filters work together; reset and empty states work.
- [ ] Every visible card action and resource link leads to the stated destination.
- [ ] Exam, calendar, notification, admit-card, result and official-source links resolve to the correct records.
- [ ] No empty routes, dead buttons or duplicate updates remain.

### Readability, accessibility and responsive behavior

- [ ] The page uses one H1 and a logical heading hierarchy.
- [ ] Copy uses short, plain-language descriptions and explains important abbreviations.
- [ ] Inputs and controls have labels, keyboard support and visible focus states.
- [ ] Status is not conveyed by color alone; tables and accordions remain accessible.
- [ ] Mobile layout has no unintended overflow and keeps the main actions easy to use.

### SEO and technical quality

- [ ] Title, description, canonical, robots directive and visible breadcrumb agree with the implemented page.
- [ ] Structured data reflects visible, accurate content and has no duplicate objects.
- [ ] Important content and links are present in crawlable rendered HTML.
- [ ] Existing site architecture, data sources, routes, global navigation and performance behavior are preserved.

### Review and handoff

- [ ] Review the implementation against this checklist and the existing page behavior.
- [ ] Report completed changes, data corrections, unresolved source gaps and verification results clearly.
- [ ] Do not state that work is tested, deployed or production-verified unless that step was actually completed.

---

**Addendum Last Updated:** 28 October 2026
