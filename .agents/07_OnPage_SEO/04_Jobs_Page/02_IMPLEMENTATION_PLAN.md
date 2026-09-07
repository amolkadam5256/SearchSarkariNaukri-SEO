# `/jobs` Page Implementation Plan

## Phase 0 - Inspect Before Coding

Before implementation, inspect the existing project architecture:

- Current `/jobs` route/page file
- Current job listing components
- Current API calls or server loaders
- Current database schema/model
- Current search implementation
- Current filter implementation
- Current pagination implementation
- Current SEO metadata handling
- Current structured data implementation
- Existing route map for qualification, state, district, city, category, exam, and job detail pages
- Existing sitemap/canonical/robots behavior

Do not assume the stack or data shape.

## Phase 1 - Protect Existing SEO And Data

Tasks:

- Do not change the existing site header, navbar, main navigation, or footer.
- Do not add, remove, rename, reorder, or redesign header/navbar/footer links or CTAs.
- Add all new SEO sections, internal links, CTAs, and discovery blocks inside the `/jobs` page body only.
- Preserve all existing job URLs and slugs.
- Preserve all existing category, district, qualification, exam, and indexed landing URLs.
- Preserve existing jobs, IDs, and database records.
- Preserve existing WhatsApp/Telegram channels.
- Preserve existing header/navbar/footer links and legal/trust links exactly as they are.
- Add redirects only if a URL must change for unavoidable technical reasons.

Deliverable:

- URL preservation notes and no-deletion confirmation.

## Phase 2 - Fix Core Data Accuracy

Tasks:

- Implement reliable status logic: `UPCOMING`, `ACTIVE`, `CLOSING_SOON`, `CLOSED`, `EXPIRED`.
- Exclude expired jobs from active listing queries.
- Keep expired/closed job pages accessible when appropriate.
- Add related active jobs for closed listings.
- Normalize vacancy display.
- Normalize location display.
- Normalize deadline display.
- Fix active count vs displayed range.

Deadline display:

- `Last Date: 15 September 2026`
- `Closing Today`
- `Closing Tomorrow`
- `3 Days Left`
- `5 Days Left`
- `Closed`

Deliverable:

- Accurate active jobs, no negative countdowns, no expired jobs labeled active.

## Phase 3 - Upgrade Above The Fold

Tasks:

- Breadcrumb with semantic nav.
- One H1:
  `Latest Government Jobs 2026 - Sarkari Naukri & Government Vacancies`
- Updated intro copy from the master prompt.
- Dynamic statistics row:
  - Active Government Jobs
  - New Jobs Today
  - Closing Today
  - Closing This Week
  - States Covered
  - Districts Covered
- Prominent search:
  `Search Government Jobs by Job Title, Organization, Post or Keyword`
- Quick chips:
  - Closing Today
  - New Today
  - 10th Pass
  - 12th Pass
  - ITI
  - Diploma
  - Graduate
  - Railway
  - Banking
  - Police
  - MPSC
  - SSC
  - UPSC
  - Talathi
  - ZP Jobs
  - Forest Guard
  - NHM

Deliverable:

- User can immediately search, filter, or enter a high-intent browsing path.

## Phase 4 - Add Advanced Filters

Tasks:

- Build accessible filter panel.
- On mobile, use drawer/modal behavior.
- Ensure filters work server-side or through efficient backend query patterns.
- Preserve query parameters across pagination.
- Do not fetch/render all jobs client-side.

Filters:

- Qualification
- State
- District dependent on state
- Department
- Job type
- Application mode
- Exam
- Deadline
- Experience

Deliverable:

- Working filters that use real fields and return accurate results.

## Phase 5 - Upgrade Core Listings

Tasks:

- Add `Government Jobs Closing Today`.
- Improve `Government Jobs Closing Soon` with tabs/categories.
- Add `New Government Jobs Today`.
- Improve `Latest Government Jobs 2026`.
- Improve job-card UI and metadata.
- Add contextual internal links on each job card where URLs exist.
- Improve crawlable pagination:
  `Previous 1 2 3 4 5 ... Next`

Deliverable:

- Job discovery sections are dynamic, accurate, useful, and crawlable.

## Phase 6 - Build The SEO/Internal-Link Hub

Add sections in this order:

1. Government Jobs by Qualification
2. Government Jobs by State
3. Government Jobs by District
4. Government Jobs by City
5. Government Jobs by Department
6. Government Jobs by Exam
7. Government Jobs by Organization
8. Government Jobs by Type
9. Government Jobs by Post / Designation
10. Government Jobs for Freshers
11. Government Jobs by Application Mode
12. Government Jobs by Salary, only if verified salary data exists
13. Central Government Jobs
14. State Government Jobs
15. Popular Government Job Categories
16. Find Government Jobs by Deadline

Rules:

- Link only to existing valid URLs or supported generated pages.
- Do not create thin pages.
- Do not add giant random link dumps.
- Use cards, grids, accordions, tabs, or short contextual paragraphs.

Deliverable:

- `/jobs` becomes the central hub for all major Government Jobs discovery paths.

## Phase 7 - Add Informational Content

Tasks:

- Expand `How to Find the Right Government Job`.
- Add `How to Apply for Government Jobs`.
- Add `Common Documents Required for Government Jobs`.
- Add recruitment lifecycle links.
- Improve Useful Resources.
- Improve About/Trust section.
- Expand FAQ with accurate answers only.
- Improve Job Alerts CTA copy.

Deliverable:

- Useful supporting content without burying job listings.

## Phase 8 - SEO And Structured Data

Tasks:

- Correct title/meta/canonical.
- Ensure one H1 and clean H2/H3 hierarchy.
- Add BreadcrumbList structured data.
- Add ItemList structured data where valid.
- Ensure individual job pages use accurate JobPosting schema.
- Use FAQ schema only where eligible.
- Review canonical/noindex strategy for filtered pages.
- Ensure sitemap discovers important pages.

Deliverable:

- Technically sound SEO implementation with no fake schema.

## Phase 9 - UX, Accessibility, Performance

Tasks:

- Verify mobile layout.
- Verify desktop layout.
- Ensure filters are keyboard accessible.
- Ensure labels and focus states exist.
- Avoid horizontal overflow.
- Keep cards readable.
- Avoid unnecessary animations/heavy UI.
- Lazy-load non-critical content if needed.
- Avoid duplicate API calls.
- Confirm Core Web Vitals are not harmed.

Deliverable:

- Fast, professional, mobile-friendly Government Jobs portal page.

## Phase 10 - Final QA

Run the checklist in `05_FINAL_QA_ACCEPTANCE_CHECKLIST.md`.

The page is done only when all critical data, UX, SEO, accessibility, URL preservation, and internal-linking checks pass.
