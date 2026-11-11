# SSC CGL Page — Implementation, SEO, Data and QA

**Permanent route:** `/exams/ssc-cgl`  
**Deployment repository needed:** the SearchSarkariNaukri website application repository. This SEO documentation checkout does not contain the route or app data service.

## Required implementation outcome

Upgrade the existing examination page without changing its URL. Reuse the shared exam template and verified exam data architecture. Keep the page about SSC CGL; never show CPO/GD/CHSL records inside its status, admit-card or results modules.

## Release plan

### Release 1 — content and SEO foundation (P0)

- [ ] Replace the thin page with all core sections from `01_COMPLETE_PAGE_CONTENT.md`.
- [ ] Add hero, cycle status, quick facts, post/pay levels, eligibility, current exam pattern, syllabus, selection process, documents and preparation guidance.
- [ ] Remove Grade Pay content and universal salary/in-hand estimates.
- [ ] Filter all updates by exam ID `ssc-cgl` and cycle year.
- [ ] Add primary and related internal links and official citations.
- [ ] Implement responsive tables, accessible navigation and metadata/schema.

### Release 2 — useful tools (P1)

- [ ] Integrate the existing eligibility checker instead of duplicating age logic.
- [ ] Add syllabus progress and mock-score tracking with user privacy considered.
- [ ] Add pay estimator only when current allowance inputs are official and date-stamped.
- [ ] Add prior cut-off explorer only from sourced SSC results; store stage, post group, category and normalized/raw score basis for each row.

### Release 3 — measurement and refinement (P2)

- [ ] Validate accessibility and mobile behavior.
- [ ] Measure performance and analytics events.
- [ ] Review Search Console indexing and queries after release.

## SEO metadata and technical rules

- Title: `SSC CGL 2026: Eligibility, Syllabus, Exam Pattern & Salary`
- Description: `Check SSC CGL 2026 eligibility, posts, pay levels, Tier I and Tier II pattern, syllabus, selection process, preparation and official updates.`
- Canonical: `https://www.searchsarkarinaukri.com/exams/ssc-cgl`
- Robots: `index,follow`
- OG image: original 1200 × 630 image, with actual URL, dimensions and meaningful alt text.
- Breadcrumb: Home → Government Exams → SSC CGL.
- Preserve the route. Do not create near-duplicate pages for “SSC CGL 2026”, “latest SSC CGL” and “SSC CGL syllabus” where the exam hub can serve the shared intent.

### Structured data

Use `WebPage` and `BreadcrumbList` consistent with visible page content and actual site entities. If the CMS models this as an editorial reference, use the appropriate page type; do not label a maintained exam hub as news. Use real publisher/author entities only. Do not add `JobPosting` schema to a general examination guide. FAQ schema is optional and not a ranking guarantee. Do not fabricate a person reviewer or dates.

## Exam data contract

Use a shared typed model and treat update records as source-attributed data, rather than JSX constants scattered across the page.

```ts
type ExamCycle = {
  examId: "ssc-cgl";
  year: number;
  notificationDate?: string;
  applicationStart?: string;
  applicationEnd?: string;
  tier1Window?: string;
  tier2Window?: string;
  tentativeVacancyCount?: number;
  vacancyStatus?: "tentative" | "revised" | "final";
  vacancySourceUrl?: string;
  applicationStatus: "upcoming" | "open" | "closed";
  cycleStatus: "upcoming" | "active" | "in_progress" | "completed";
  officialNoticeUrl: string;
  lastVerifiedAt: string;
};

type ExamUpdate = {
  examId: "ssc-cgl";
  cycleYear: number;
  updateType:
    | "notification" | "application" | "tier1" | "answer_key"
    | "tier1_result" | "tier2" | "final_result" | "vacancy";
  title: string;
  status: "upcoming" | "open" | "closed" | "released" | "completed" | "pending";
  eventDate?: string;
  officialSourceUrl: string;
  verifiedAt: string;
};

type ExamPost = {
  id: string;
  examId: "ssc-cgl";
  cycleYear: number;
  postName: string;
  department: string;
  group: "B" | "C";
  payLevel: number | null;
  basicPayMin?: number;
  basicPayMax?: number;
  ageMin?: number;
  ageMax?: number;
  qualification: string[];
  physicalStandardsRequired: boolean;
  description: string;
  sourceUrl: string;
  verifiedAt: string;
};

type ExamResource = {
  id: string;
  examId: "ssc-cgl";
  title: string;
  resourceType: "notice" | "admit_card" | "answer_key" | "result" | "syllabus" | "paper";
  url: string;
  description: string;
  verified: boolean;
  verifiedAt: string;
};

type ExamCutoff = {
  examId: "ssc-cgl";
  year: number;
  stage: "tier1_shortlisting" | "tier2_qualifying" | "final_allocation";
  postGroup: "jso" | "statistical_investigator" | "other_posts" | string;
  category: string;
  score: number;
  scoreBasis: "normalized" | "raw" | "marks";
  officialSourceUrl: string;
  sourceNoticeDate: string;
  verifiedAt: string;
};
```

Filter every dashboard query on both `examId` and `cycleYear`. Validate all `officialSourceUrl` values and reject records without a verification date. Fall back to the official SSC notice board if no current data exists.

## Current verified 2026 snapshot for seed data

As of 12 November 2026:

- The 2026 notice was published 21 May 2026.
- Application submission ran 21 May–22 June 2026; fee payment through 23 June.
- The correction window ran 29 June–1 July 2026.
- The original notice gave Tier I as August–September and Tier II as December 2026, both tentative at notice time. SSC later published the Tier I response-sheet/tentative-key notice on 4 November; keep the result pending until SSC publishes a result notice.
- SSC's tentative vacancy list dated 24 September 2026 totals 10,731. This later figure supersedes the original notice's approximate 12,256 for current display. Label the vacancies tentative and retain the earlier figure only in the update history.
- SSC listed Tier I response sheets and tentative answer keys on 4 November 2026. Keep Tier I result pending until an SSC result notice is published.
- The full recruitment cycle remains `in_progress` while Tier II is pending; do not mark the cycle completed when only Tier I is complete.

Primary references:

- [SSC CGL 2026 notice PDF](https://ssc.gov.in/api/attachment/uploads/masterData/NoticeBoards/Notice_of_adv_cgl_2026.pdf)
- [SSC CGL 2026 tentative vacancy list (24 September 2026)](https://ssc.gov.in/api/attachment/uploads/masterData/NoticeBoards/Tentative_vacancy_CGLE2026_24092026.pdf)
- [SSC CGL Tier I 2025 result write-up with shortlisting cutoffs](https://ssc.gov.in/api/attachment/uploads/masterData/NoticeBoards/writeup_181225.pdf)
- [SSC notice board](https://ssc.gov.in/home/notice-board)
- [SSC answer key page](https://ssc.gov.in/home/answer-key)
- [SSC official website](https://ssc.gov.in/)

Recheck on implementation day. The page’s live status must follow the newest SSC notice even if that differs from this handoff snapshot.

## Internal linking plan

Use contextual links, not a repeated footer-like block:

| Destination | Anchor | Useful context |
|---|---|---|
| `/exams` | all government examinations | Comparison / related exams |
| `/exams/ssc-chsl` | SSC CHSL examination | Compare graduate and 10+2 paths |
| `/exams/upsc-cse` | UPSC Civil Services examination | Compare examination tracks |
| `/exams/mpsc-rajyaseva` | MPSC Rajyaseva examination | Compare state-service route |
| `/jobs` | latest government jobs | Candidate action / vacancies |
| `/admit-cards` | latest admit cards | Examination logistics |
| `/results` | government exam results | Result navigation |
| `/current-affairs` | daily current affairs | Preparation context |
| `/daily-quiz` | daily quiz | Practice tool |
| `/digital-library` | free study materials | Preparation resources |

Confirm each destination resolves. Add inbound contextual links to SSC CGL from the SSC CHSL page, central/graduate jobs pages, SSC recruitment hub and relevant CGL preparation guides. Vary anchor text and avoid identical sitewide blocks.

## UI implementation guardrails

- Reuse the site’s existing shared exam components, typography, spacing scale, card, table, CTA and responsive patterns.
- Use a distinctive but restrained navy hero and gold accent. Avoid unrelated generic cards and stock graphics.
- Build sticky section links that work without JavaScript, scroll to unique section IDs and show visible keyboard focus.
- Respect reduced motion. Use no heavy animation.
- Keep charts lazy-loaded and tools as small client components; render main text, tables, FAQs and sources server-side.
- Optimize image size and reserve aspect ratio to avoid layout shift.
- Do not render the quick-information table as an image.

## Analytics events

Use existing analytics conventions and consent controls. Suggested events:

- `ssc_cgl_official_click`
- `ssc_cgl_salary_estimator_use`
- `ssc_cgl_eligibility_checker_use`
- `ssc_cgl_syllabus_expand`
- `ssc_cgl_resource_click`
- `ssc_cgl_faq_expand`
- `ssc_cgl_quiz_start`
- `ssc_cgl_related_exam_click`

Do not collect sensitive eligibility inputs in analytics events.

## Content verification workflow

For every new cycle:

1. Find the SSC notification, corrigenda and later schedule/result notices.
2. Confirm the year, exam name, post, stage and effective date.
3. Record the exact official source URL and verification time.
4. Compare the update with the prior record; preserve history.
5. Update page copy, structured data and tracker together.
6. Confirm status labels and CTA states (especially application open/closed).
7. Recheck cross-exam data isolation.

Never fabricate vacancies, cut-offs, pay, age relaxations, dates, results, success rates, competition statistics or selection probabilities. Historical data must identify its year, group/category, score basis and source.

## Pre-release QA

### Content

- [ ] All page sections are implemented or explicitly assigned to a later release.
- [ ] No outdated Grade Pay or one-size salary statement remains.
- [ ] Post-level pay, eligibility, pattern and syllabus match the current SSC notice.
- [ ] Current vacancy count comes from SSC's latest vacancy sheet, is labelled tentative/final correctly, and preserves the earlier figure only as history.
- [ ] Minimum qualifying marks are not presented as competitive cutoffs; DEST/CKT requirements and post-specific higher standards are explained.
- [ ] Historical 2025 Tier I cutoffs are labelled as normalized shortlisting marks, never as 2026 predictions or final selection marks.
- [ ] Tier I and Tier II requirements, penalties and qualifying tests are accurately scoped.
- [ ] Normalization is explained without unsupported claims.
- [ ] Current status shows CGL-only records and a current source timestamp; Tier I completion is distinct from the full recruitment cycle still in progress.
- [ ] No Apply Now button appears while the application window is closed.
- [ ] Editorial independence notice and official citations are visible.

### SEO

- [ ] Exactly one H1, unique title and description.
- [ ] Canonical remains `/exams/ssc-cgl` and resolves to HTTP 200.
- [ ] Breadcrumb is visible and structured data matches it.
- [ ] Page is indexable and important copy is rendered in HTML.
- [ ] Internal links work; official links go to SSC.
- [ ] No accidental duplicate indexable CGL page was created.

### Technical and user experience

- [ ] Mobile responsive; no page-level horizontal overflow.
- [ ] Tables and post cards work at narrow widths.
- [ ] Controls are keyboard and screen-reader accessible.
- [ ] Calculators produce correct outputs for boundary cases and disclose assumptions.
- [ ] No console errors, stale state labels or cross-exam records.
- [ ] Core Web Vitals targets: LCP < 2.5s, INP < 200ms, CLS < 0.1.
- [ ] No layout shift from images; no unnecessary large chart library on initial load.

### Trust and operations

- [ ] Last reviewed and last verified timestamps are real.
- [ ] Every live data row has a source URL and verification time.
- [ ] Source update workflow and ownership are documented.
- [ ] Search Console URL inspection and query tracking are scheduled after deployment.

## Success measurement

Monitor query and page metrics in Search Console and analytics after release:

- Impressions, clicks, CTR and average position for SSC CGL 2026, syllabus, eligibility, salary, posts, age limit, pattern, Tier II syllabus, preparation and previous-year cut-off.
- Indexed status, canonical selected by Google and structured data issues.
- Official link clicks, section navigation, tool use, resource use and related exam clicks.

A “10/10 SEO score” or first-place ranking cannot be guaranteed. This package is designed to improve coverage, clarity, source attribution, technical readiness and user experience; rankings depend on competition, authority, implementation quality and ongoing updates.
