# SSC CGL Page — Semantic Structure and UI Map

**Route:** `/exams/ssc-cgl`  
**Content source:** `01_COMPLETE_PAGE_CONTENT.md`

## Heading hierarchy

```text
h1 SSC CGL 2026: Complete Exam Guide, Eligibility, Syllabus & Salary

h2 Current SSC CGL 2026 status
h2 SSC CGL at a glance
h2 What is the SSC CGL examination?
  h3 Why candidates consider SSC CGL
h2 SSC CGL posts and departments
  h3 Explore job profiles
  h3 Physical and medical standards for selected posts
h2 SSC CGL salary and pay levels
  h3 Salary estimator — production requirements
h2 SSC CGL eligibility criteria
  h3 Educational qualification
  h3 Age limits and relaxations
  h3 Eligibility checker
h2 SSC CGL exam pattern 2026
  h3 Tier I
  h3 Tier II
  h3 Accessible timing note
  h3 Tier I vs Tier II
h2 SSC CGL syllabus 2026
  h3 Tier I subjects
  h3 Tier II Paper I
  h3 Tier II Papers II and III
h2 SSC CGL selection process
  h3 Minimum qualifying marks and DEST standards (2026)
h2 How to apply for SSC CGL
h2 Documents and information checklist
h2 SSC CGL preparation roadmap
  h3 Phase 1: Map the exam
  h3 Phase 2: Build foundations
  h3 Phase 3: Practice under section timing
  h3 Phase 4: Add post-specific Tier II work
  h3 Phase 5: Review and simulate
  h3 Optional 90-day plan
h2 Preparation tracker and tools
h3 Learning zone
h3 Recruitment and exam history
h2 Previous-year cut-offs and trend analysis
  h3 SSC CGL Tier I shortlisting cutoffs — 2025
h2 Official notices, admit cards, answer keys and results
h2 SSC CGL compared with other examinations
h2 Study resources and internal navigation
h2 Frequently asked questions
  h3 What is SSC CGL?
  h3 What qualification is required for SSC CGL?
  h3 Can final-year students apply for SSC CGL?
  h3 What is the SSC CGL age limit?
  h3 Is SSC CGL conducted online?
  h3 How many tiers are there in SSC CGL?
  h3 What is the SSC CGL salary?
  h3 Which SSC CGL post has the highest salary?
  h3 Is there negative marking in SSC CGL?
  h3 Does SSC CGL have an interview?
  h3 Where can I check SSC CGL results and notices?
  h3 Is SearchSarkariNaukri the official SSC website?
  h3 How many tentative vacancies are there in SSC CGL 2026?
  h3 What are the minimum qualifying marks for SSC CGL 2026?
  h3 What is the SSC CGL Tier II DEST requirement?
  h3 What is the difference between SSC CGL cutoff and minimum qualifying marks?
  h3 Can beginners prepare for SSC CGL?
  h3 Do SSC CGL posts have physical or medical tests?
h2 Official SSC sources
h2 Editorial verification note
```

## Stable section IDs

```text
#current-status
#quick-facts
#overview
#posts
#salary
#eligibility
#exam-pattern
#syllabus
#selection-process
#qualifying-marks
#application
#documents
#preparation
#preparation-tools
#learning-zone
#exam-history
#cutoffs
#official-updates
#compare-exams
#resources
#faq
#official-sources
#verification
```

## Semantic implementation notes

- Use one page-level `<main>` and exactly one `<h1>`.
- Use visible breadcrumb navigation with `aria-label="Breadcrumb"`.
- Use `<section aria-labelledby>` for each major section and stable IDs from the map above.
- Use a semantic `<dl>` for quick facts and actual `<table>` markup for post, pay, exam-pattern and status comparisons. Provide `<caption>`, `<thead>`, scoped column headers and an established mobile overflow/stack pattern.
- Render essential page copy and official sources in server-rendered HTML. Client JavaScript can enhance calculators and navigation but must not gate key content.
- Use accessible `<details>/<summary>` or the application’s existing disclosure component for syllabus/post cards. Keep all hidden text in the rendered DOM and keyboard operable.
- Use a real link for official SSC actions; open in a new tab only if the site’s external-link convention requires it, and then set safe `rel` attributes.
- Give the official status data a visible “Last verified” timestamp. A missing or stale data feed should show a neutral “Check official SSC notice” state, never stale active dates.

## Visual direction

Apply the site’s existing type, spacing, colors, components and accessible states. Create distinction with an exam-specific navy hero, restrained gold accent, clean status timeline and varied section treatments. Do not repeat identical cards for every section, add unnecessary motion, use text baked into an image, or introduce a separate design system.

- Desktop: wide but readable content column, sticky section navigation below the global header, compact status strip and multi-column data tables.
- Tablet: collapse post cards and overview facts to two columns where appropriate.
- Mobile: single-column reading flow, horizontally scrollable section links, full-width tool controls and responsive tables without page-level overflow.
- Sticky navigation: each item points to a unique section ID; account for sticky header offset. Respect `prefers-reduced-motion` and keyboard focus.
- Hero: keep one H1, concise overview, current cycle status and clear official-site action. Do not show Apply Now when the application window is closed.

## Interactive components

1. **SSC CGL cycle tracker:** render only records with `examId = "ssc-cgl"` and the matching cycle year. Each item, including vacancy updates, requires source URL, notice date, status (tentative/final where relevant) and `verifiedAt`.
2. **Post explorer:** expandable records grouped by function. Include official post names and pay level; avoid unsupported job-life claims.
3. **Salary estimator:** add only after current allowance and deduction data has verified values and effective dates. Show arithmetic, assumptions, gross/net distinction and “estimate” disclaimer.
4. **Eligibility checker:** reuse the existing eligibility/age-relaxation engine. Ask for date of birth, post, category and notification crucial date. It must not produce an unconditional official eligibility verdict.
5. **Syllabus explorer:** accessible disclosures; essential topics remain rendered and crawlable.
6. **Preparation tracker and mock score tool:** user-entered progress only; disclose storage and privacy. Calculate raw practice score using the selected notice marking scheme and clearly distinguish it from normalized SSC scores.
7. **Learning zone:** link to quiz, current-affairs and library resources; distinguish editorial material from official SSC resources. Keep optional gamified/peer features secondary.
8. **Exam history:** each number needs an official source, definition, status (tentative/final), cycle and verification time; preserve revisions.
9. **Cut-off explorer:** lazy-load charts. Every value must have year, tier/paper, post/category, score basis, normalization note and official result source. Distinguish shortlisting, qualifying and final allocation cut-offs.
10. **FAQ:** visible answers; no FAQ schema promise or ranking claim.
