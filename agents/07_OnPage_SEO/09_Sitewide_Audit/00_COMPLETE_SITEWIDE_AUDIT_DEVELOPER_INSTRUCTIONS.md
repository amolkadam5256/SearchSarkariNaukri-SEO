# SearchSarkariNaukri — Complete Website Audit & Implementation Instructions

## 1. Objective

Conduct a complete audit of the entire SearchSarkariNaukri React project and create a detailed, actionable checklist for every page, section, component, template, and relevant technical feature.

The objective is to improve:

- Technical SEO and organic search visibility.
- GEO (Generative Engine Optimization).
- AEO (Answer Engine Optimization).
- Content quality, readability, accuracy, and search intent.
- Internal linking and external source references.
- UI/UX, navigation, mobile usability, and engagement.
- Page speed, Core Web Vitals, accessibility, and security.
- Indexability, structured data, and crawl efficiency.
- Trustworthiness of government exam, recruitment, result, admit card, and related information.

**Critical rule:** Do not delete, overwrite, shorten, or remove existing content, sections, exam records, features, or working functionality merely to simplify implementation. Preserve the existing information and improve its structure, clarity, presentation, accuracy, and usefulness. Obtain approval before any necessary removal or material content change.

## 2. First: Understand the Existing Project

Before making changes, inspect the repository and document its current architecture.

- [ ] Identify the React framework: React, Next.js, Vite, or another setup.
- [ ] Identify the package manager and inspect package scripts and dependencies.
- [ ] Map the application routes and dynamic routes.
- [ ] Identify all public-facing pages, page templates, and content types.
- [ ] Inspect shared layouts, navigation, footer, cards, tables, forms, and reusable components.
- [ ] Identify the CMS, database, APIs, content files, or other data sources.
- [ ] Identify the rendering strategy for each page: server-rendered, static, client-rendered, or hybrid.
- [ ] Review metadata generation, canonical URL handling, robots directives, sitemap generation, and structured data.
- [ ] Inspect existing analytics, Search Console integrations, and consent mechanisms.
- [ ] Identify redirects, legacy URLs, duplicate pages, broken routes, and known technical issues.
- [ ] Check existing project rules, agent instructions, documentation, and development conventions.
- [ ] Establish the current baseline before modifying code.

Deliverable: a route inventory, architecture summary, baseline findings, and prioritized audit checklist.

## 3. Website-Wide Page Inventory

Create a central inventory of all discoverable routes. Include, where applicable:

- [ ] Homepage.
- [ ] Government exam listings.
- [ ] Individual exam detail pages.
- [ ] Latest government jobs and recruitment notifications.
- [ ] Individual job detail pages.
- [ ] Admit cards.
- [ ] Results and merit lists.
- [ ] Answer keys.
- [ ] Syllabus and exam patterns.
- [ ] Previous-year question papers.
- [ ] Exam calendars and important dates.
- [ ] Eligibility, age limits, application fees, and selection processes.
- [ ] State-wise recruitment pages.
- [ ] Organization- or department-wise pages.
- [ ] Category and archive pages.
- [ ] Search results and filters.
- [ ] Educational articles and guides.
- [ ] About, contact, editorial policy, corrections policy, and privacy pages.
- [ ] Other existing routes discovered in the project.

For each route, record its URL, page type, purpose, indexability, canonical URL, title, meta description, H1, content status, internal links, source references, schema, performance, and audit status.

Do not assume that every route should be indexed. Determine indexation based on actual value, uniqueness, search intent, and the site's technical rules.

## 4. Technical SEO Checklist

### Crawlability and indexation

- [ ] Verify that important pages return the correct HTTP status.
- [ ] Identify accidental 404s, soft 404s, redirect chains, redirect loops, and unnecessary redirects.
- [ ] Check `robots.txt` and ensure important content is not unintentionally blocked.
- [ ] Check page-level `noindex`, `nofollow`, and robots meta directives.
- [ ] Verify canonical URLs and detect conflicting or incorrect canonicals.
- [ ] Identify duplicate URLs caused by query parameters, filters, pagination, trailing slashes, and URL variants.
- [ ] Confirm that important pages can be discovered through crawlable links.
- [ ] Ensure essential content and metadata are available to search engines without requiring unsupported client-side interactions.
- [ ] Review pagination and filtered listing behaviour.
- [ ] Check orphan pages and unnecessarily deep navigation paths.
- [ ] Verify that expired recruitment pages are handled according to their continuing usefulness.
- [ ] Check that removed pages return appropriate responses or redirects based on the replacement and user intent.

### XML sitemaps

- [ ] Verify sitemap validity and accessibility.
- [ ] Include only eligible, canonical, indexable URLs that return successful responses.
- [ ] Exclude redirects, errors, `noindex` pages, and noncanonical duplicates.
- [ ] Use accurate `lastmod` values based on meaningful content updates.
- [ ] Split large sitemaps where necessary and provide a sitemap index.
- [ ] Confirm that important page types are covered.
- [ ] Check that the sitemap is referenced correctly in `robots.txt`.
- [ ] Compare sitemap URLs against actual routes and indexation data.

### URL structure

- [ ] Use stable, readable, descriptive URLs.
- [ ] Maintain a consistent trailing-slash and lowercase policy.
- [ ] Avoid unnecessary URL parameters and duplicate paths.
- [ ] Preserve existing URL equity when routes change.
- [ ] Implement appropriate permanent redirects for approved URL migrations.
- [ ] Avoid changing established URLs solely to insert additional keywords.

### Metadata and HTML structure

- [ ] Provide unique, descriptive title tags for indexable pages.
- [ ] Write useful meta descriptions aligned with the page's actual content.
- [ ] Ensure a clear primary H1 and logical heading hierarchy.
- [ ] Use semantic HTML landmarks and meaningful page structure.
- [ ] Add appropriate language metadata.
- [ ] Verify Open Graph and social sharing metadata where relevant.
- [ ] Check image alternative text and meaningful link text.
- [ ] Avoid duplicate metadata across dynamic routes.
- [ ] Prevent incorrect titles and metadata during loading, errors, or data-fetching failures.

## 5. On-Page SEO Checklist

For every important page:

- [ ] Identify the primary search intent.
- [ ] Map one main topic and its relevant secondary topics.
- [ ] Research relevant keywords using reliable data where available.
- [ ] Include natural keyword variations without keyword stuffing.
- [ ] Align the title, H1, introduction, subheadings, and page content.
- [ ] Answer the user's main question early.
- [ ] Organize information into clear sections.
- [ ] Improve paragraphs, lists, tables, labels, and explanatory text.
- [ ] Add relevant contextual internal links.
- [ ] Verify dates, eligibility, fees, vacancies, and other factual details.
- [ ] Check for duplicate, thin, outdated, misleading, or contradictory content.
- [ ] Add useful related information only when it serves the user.
- [ ] Provide a clear next action where appropriate.
- [ ] Avoid fabricated statistics, unsupported claims, and repetitive SEO text.
- [ ] Keep content readable on mobile and accessible to assistive technology.

## 6. GEO — Generative Engine Optimization

Optimize content so that search engines and generative AI systems can understand, identify, and accurately reference useful information.

- [ ] Clearly identify the entity, topic, organization, exam, or recruitment process covered by each page.
- [ ] Provide direct, factual answers to common questions.
- [ ] Use descriptive headings that match real user questions.
- [ ] Present important facts in well-structured text, lists, and HTML tables.
- [ ] Identify the information source and relevant publication or update date.
- [ ] Distinguish official facts from editorial explanation.
- [ ] Maintain consistent organization names, exam names, dates, and terminology.
- [ ] Link to original authoritative sources where appropriate.
- [ ] Make important information accessible in crawlable HTML.
- [ ] Add useful contextual explanations rather than repeating keywords.
- [ ] Use structured data only when the content meets the relevant schema requirements.
- [ ] Keep important information accurate, current, and traceable to sources.
- [ ] Avoid fabricated expert quotations, statistics, reviews, and claims of authority.
- [ ] Do not promise inclusion in AI-generated answers or assume that any special AI file guarantees visibility.
- [ ] Monitor available search and referral data to evaluate results over time.

## 7. AEO — Answer Engine Optimization

Make pages useful for users seeking concise answers through search snippets, voice search, AI assistants, and question-based queries.

- [ ] Identify frequently asked questions from actual user needs and reliable keyword or Search Console data.
- [ ] Provide a concise, direct answer near the beginning of the relevant section.
- [ ] Expand with supporting details, conditions, and exceptions.
- [ ] Use clear question-based headings where they are helpful.
- [ ] Provide eligibility, dates, fees, age limits, and application steps in easy-to-scan formats.
- [ ] Distinguish confirmed facts from information that is pending or unavailable.
- [ ] Add FAQs only when they answer genuine user questions.
- [ ] Keep visible FAQ content consistent with any FAQ structured data.
- [ ] Do not add repetitive questions solely to target more keywords.
- [ ] Do not promise featured snippets, rich results, or AI citations.

## 8. Content Accuracy, Trust, and Source Verification

This is a high-priority requirement for a government recruitment information website.

### Source hierarchy

- [ ] Prefer official recruitment notifications, official department websites, and authorized application portals.
- [ ] Use official exam authorities for admit cards, answer keys, results, schedules, and examination notices.
- [ ] Use the original notification PDF whenever it is available and relevant.
- [ ] Use reputable secondary sources only for context or corroboration where appropriate.
- [ ] Do not treat an unofficial blog, social post, or search snippet as proof of an official announcement.

### Fact-checking

- [ ] Verify the organization and examination name.
- [ ] Verify notification number and publication date when available.
- [ ] Verify application start and end dates.
- [ ] Verify vacancy counts and category-wise breakdowns.
- [ ] Verify age limits, age-relaxation rules, qualifications, fees, and selection stages.
- [ ] Verify official application, notification, result, and admit-card URLs.
- [ ] Check whether dates or vacancy details have changed in later notices.
- [ ] Record source publication dates and the latest meaningful update.
- [ ] Flag conflicting sources rather than silently choosing one.
- [ ] Mark unresolved details for manual review.
- [ ] Never invent official sources, citations, deadlines, or recruitment details.

### Source attribution on pages

Where appropriate, provide a visible source or official-notification section containing:

- Issuing organization.
- Notification or document title.
- Publication or notification date, if confirmed.
- Direct link to the official source.
- Last verified or updated date, where supported.
- A short note when information remains unconfirmed.

Preserve existing content while correcting confirmed errors through the project's approved content workflow.

## 9. Internal Linking Checklist

- [ ] Ensure every important indexable page is reachable through relevant internal links.
- [ ] Link listing pages to individual detail pages.
- [ ] Link detail pages to genuinely relevant syllabus, admit-card, result, answer-key, and application resources.
- [ ] Connect state-wise, organization-wise, exam-wise, and category-wise content where useful.
- [ ] Add breadcrumbs where appropriate.
- [ ] Use descriptive, natural anchor text.
- [ ] Avoid excessive exact-match keyword anchors.
- [ ] Identify orphan pages and pages with very few useful internal links.
- [ ] Review links in the header, navigation, footer, related-content sections, and article body.
- [ ] Check for broken internal links, redirecting links, and links to noncanonical URLs.
- [ ] Ensure important links are actual crawlable anchors with valid destinations.
- [ ] Avoid relying only on JavaScript click handlers for navigation.
- [ ] Ensure related-content modules are genuinely relevant.
- [ ] Prevent circular, repetitive, or automatically generated link blocks that add no value.
- [ ] Verify that pagination and filters do not create uncontrolled URL duplication.

## 10. External Links and Official References

- [ ] Verify every important external URL.
- [ ] Prefer the official website of the responsible department or examination authority.
- [ ] Link directly to the relevant notice or document instead of an unrelated homepage where possible.
- [ ] Identify broken, redirected, expired, suspicious, or misleading destinations.
- [ ] Clearly label official application links, notification PDFs, and third-party references.
- [ ] Ensure link text accurately describes the destination.
- [ ] Use appropriate `rel` attributes for sponsored, user-generated, or untrusted links.
- [ ] Use safe new-tab behaviour where applicable.
- [ ] Avoid unnecessary `nofollow` on legitimate editorial references.
- [ ] Do not sell or disguise links as official resources.
- [ ] Do not remove useful external citations simply to retain users on the website.
- [ ] Establish a process for reviewing important external links periodically.

## 11. Structured Data and Entity Markup

- [ ] Audit existing JSON-LD, Microdata, or RDFa before changing it.
- [ ] Select schema types based on actual page content and current supported guidelines.
- [ ] Consider `Organization`, `WebSite`, `BreadcrumbList`, and appropriate `Article` or `NewsArticle` markup where eligible.
- [ ] Use job-related structured data only if the page and vacancy genuinely meet the current requirements.
- [ ] Do not mark a general exam listing as a job posting merely to gain visibility.
- [ ] Populate properties from verified page data.
- [ ] Keep structured data consistent with visible content.
- [ ] Use accurate canonical page URLs and entity identifiers.
- [ ] Avoid fake ratings, reviews, author credentials, dates, salaries, or availability.
- [ ] Avoid duplicate conflicting schema generated by multiple components.
- [ ] Validate representative pages using current schema validation tools.
- [ ] Monitor Search Console enhancements and structured-data warnings where available.

## 12. Keyword Research and Content Gap Analysis

- [ ] Identify the main keyword and search intent for each page type.
- [ ] Use Search Console performance data when access is available.
- [ ] Research related long-tail and question-based queries.
- [ ] Map keywords to the most relevant existing page.
- [ ] Identify cannibalization between pages targeting the same intent.
- [ ] Identify valuable missing topics and genuinely useful content gaps.
- [ ] Review impressions, clicks, CTR, average position, and landing-page engagement where data exists.
- [ ] Prioritize improvements using opportunity, user value, effort, and risk.
- [ ] Avoid generating thin pages for every minor keyword variation.
- [ ] Do not invent keyword volume, ranking position, or traffic estimates.
- [ ] Record the data source and date for keyword research.

## 13. UI/UX and Readability

### Navigation and page layout

- [ ] Make primary navigation understandable and consistent.
- [ ] Ensure breadcrumbs reflect the actual hierarchy.
- [ ] Make page purpose obvious above the fold.
- [ ] Establish clear visual hierarchy between headings, body text, metadata, and actions.
- [ ] Keep spacing, typography, buttons, colors, and component behaviour consistent.
- [ ] Improve dense sections without deleting useful information.
- [ ] Present important dates, status labels, and actions clearly.
- [ ] Ensure long pages have useful section navigation where appropriate.
- [ ] Make tables readable on small screens.
- [ ] Prevent overlapping, clipped, or horizontally overflowing content.
- [ ] Ensure advertisements or promotional modules do not obscure essential content.
- [ ] Provide clear loading, empty, error, and success states.

### Engagement and usability

- [ ] Make application and notification links easy to identify.
- [ ] Add related content only when useful to the current task.
- [ ] Make search, filtering, and sorting understandable.
- [ ] Preserve user-entered values when validation errors occur.
- [ ] Ensure buttons perform the action described by their labels.
- [ ] Avoid intrusive pop-ups and misleading calls to action.
- [ ] Ensure key information is not hidden behind unnecessary interactions.
- [ ] Test all important journeys from homepage to detail page and official source.

## 14. Mobile Responsiveness and Accessibility

- [ ] Test narrow mobile, standard mobile, tablet, laptop, and large desktop layouts.
- [ ] Verify navigation menus, dropdowns, accordions, tables, forms, and modals.
- [ ] Ensure text remains readable without pinch-to-zoom.
- [ ] Check touch target sizes and spacing.
- [ ] Confirm visible keyboard focus and logical tab order.
- [ ] Use semantic buttons, links, form labels, and headings.
- [ ] Add appropriate image alternative text.
- [ ] Ensure sufficient text/background contrast.
- [ ] Do not use color alone to convey status.
- [ ] Verify accessible names and states for interactive controls.
- [ ] Respect reduced-motion preferences.
- [ ] Check accessibility using automated tools and manual keyboard testing.
- [ ] Resolve meaningful WCAG 2.2 AA issues where applicable.

## 15. Performance and Core Web Vitals

- [ ] Measure representative pages before and after changes.
- [ ] Evaluate Largest Contentful Paint (LCP), Interaction to Next Paint (INP), and Cumulative Layout Shift (CLS).
- [ ] Use field data where available and lab data for debugging.
- [ ] Optimize image dimensions, formats, compression, and loading priority.
- [ ] Lazy-load appropriate below-the-fold images without delaying critical content.
- [ ] Reduce unnecessary JavaScript and large client-side bundles.
- [ ] Avoid hydration errors and excessive client-side rendering where they harm usability or crawlability.
- [ ] Review font loading and layout shifts.
- [ ] Remove unused dependencies only after confirming they are unnecessary.
- [ ] Review caching, compression, and static asset delivery.
- [ ] Avoid unnecessary third-party scripts.
- [ ] Prevent layout shifts caused by ads, images, and dynamic content.
- [ ] Check slow API requests and repeated data fetching.
- [ ] Avoid sacrificing essential functionality for a marginal performance score.

Use current Core Web Vitals guidance and record actual measurements rather than assuming that a build passing means the site is fast.

## 16. React and Application Quality

- [ ] Review component responsibilities and duplication.
- [ ] Use reusable components consistently.
- [ ] Verify correct list keys and stable rendering.
- [ ] Check for unnecessary re-renders and expensive computations.
- [ ] Review state management and effect dependencies.
- [ ] Handle asynchronous requests, cancellation, errors, and loading states.
- [ ] Prevent stale data from being presented as current.
- [ ] Check hydration errors where server rendering is used.
- [ ] Review server/client component boundaries where applicable.
- [ ] Validate route parameters and dynamic page data.
- [ ] Handle missing records without crashing the application.
- [ ] Check forms and validation rules.
- [ ] Ensure navigation, filters, pagination, and search work correctly.
- [ ] Check browser console warnings and errors.
- [ ] Review TypeScript types or PropTypes where applicable.
- [ ] Run linting, type checks, unit tests, and production builds using existing project scripts.
- [ ] Do not replace the framework, router, or core architecture without a clear reason and approval.

## 17. Security, Privacy, and Reliability

- [ ] Check for exposed secrets and credentials.
- [ ] Ensure private environment variables are not shipped to the browser.
- [ ] Review dependency vulnerabilities.
- [ ] Validate and sanitize untrusted inputs appropriately.
- [ ] Check external link handling and unsafe HTML rendering.
- [ ] Review API authorization and access controls where applicable.
- [ ] Check rate limiting and abuse protection for relevant endpoints.
- [ ] Ensure personal data is not unnecessarily collected or logged.
- [ ] Verify privacy and consent behaviour where legally required.
- [ ] Check error messages for accidental disclosure of sensitive information.
- [ ] Preserve secure headers and deployment configuration.
- [ ] Do not introduce third-party scripts, packages, or services without evaluating their necessity and risk.

## 18. Search Console, Analytics, and Monitoring

- [ ] Verify the correct Search Console property where access is available.
- [ ] Review indexing reports and URL inspection for representative pages.
- [ ] Check sitemap processing and crawl anomalies.
- [ ] Review clicks, impressions, CTR, average position, and page-level trends.
- [ ] Review Core Web Vitals and mobile usability signals where available.
- [ ] Confirm analytics events and conversions are implemented correctly.
- [ ] Avoid duplicate page views or duplicate conversion events.
- [ ] Ensure tracking does not block essential functionality.
- [ ] Establish a baseline report before implementation.
- [ ] Compare results after deployment using consistent dates and filters.
- [ ] Record external factors that may affect results.
- [ ] Do not claim improved rankings or indexing without measured evidence.

## 19. Content Maintenance and Expired Information

- [ ] Identify outdated recruitment notifications and examination dates.
- [ ] Confirm whether each expired page still provides historical or reference value.
- [ ] Keep useful historical content when it helps users.
- [ ] Clearly label closed applications and completed examination stages.
- [ ] Update information only after verifying the new source.
- [ ] Preserve stable URLs when practical.
- [ ] Avoid redirecting every expired page to the homepage.
- [ ] Remove or redirect pages only under an approved policy.
- [ ] Record who verified the content and when, where the workflow supports it.
- [ ] Establish a recurring review process for high-impact pages.

## 20. Two-Pass Audit and Implementation Verification

Create a separate Markdown checklist for every major page type or implementation area. Each checklist must include both verification passes.

### Pass 1 — Implementation

- [ ] Review the existing implementation and supporting data.
- [ ] Record the issue and its evidence.
- [ ] Assign priority: Critical, High, Medium, or Low.
- [ ] Document the recommended change and expected outcome.
- [ ] Implement approved changes without removing unrelated functionality.
- [ ] Verify the change locally.
- [ ] Record changed files and any unresolved dependency.

### Pass 2 — Independent verification

- [ ] Recheck the original issue against the implemented result.
- [ ] Verify page content and data preservation.
- [ ] Verify metadata, canonical URLs, indexation directives, and schema.
- [ ] Verify internal and external links.
- [ ] Test desktop and mobile behaviour.
- [ ] Test interactions, loading, empty, and error states.
- [ ] Run applicable automated checks.
- [ ] Inspect the browser console and network errors.
- [ ] Confirm no unrelated routes or components were broken.
- [ ] Record evidence of the final result.
- [ ] Mark failed or unverified items as unresolved rather than passed.

A documentation checklist passing is not evidence that the website itself passes.

## 21. Priority and Tracking Format

Every finding must include:

- **ID:** Unique audit reference.
- **Category:** Technical SEO, GEO, AEO, content, links, UI/UX, performance, security, or another applicable category.
- **Affected URL/component:** Exact route or code location.
- **Issue:** Clear description of the problem.
- **Evidence:** Reproducible observation, source, measurement, or test result.
- **Priority:** Critical, High, Medium, or Low.
- **Recommended fix:** Specific implementation steps.
- **Dependencies:** Any data, approval, or technical dependency.
- **Pass 1 status:** Not started, in progress, passed, blocked, or failed.
- **Pass 2 status:** Not started, in progress, passed, blocked, or failed.
- **Verification evidence:** Test result or recorded observation.
- **Owner and date:** Where applicable.

Do not mark an item complete because code was written. Completion requires verification.

## 22. Required Documentation Structure

Create a site-wide audit folder that follows existing project conventions. If no suitable location exists, use a clearly named folder such as:

`/.agents/07_OnPage_SEO/09_Sitewide_Audit/`

Recommended documents:

- `README.md` — audit scope, instructions, index, and status.
- `01_PROJECT_ARCHITECTURE_AND_ROUTE_INVENTORY.md`
- `02_TECHNICAL_SEO_CHECKLIST.md`
- `03_ON_PAGE_SEO_AND_KEYWORD_CHECKLIST.md`
- `04_GEO_CHECKLIST.md`
- `05_AEO_CHECKLIST.md`
- `06_CONTENT_ACCURACY_AND_SOURCE_VERIFICATION.md`
- `07_INTERNAL_LINKING_AUDIT.md`
- `08_EXTERNAL_LINKS_AND_REFERENCES_AUDIT.md`
- `09_STRUCTURED_DATA_AND_ENTITY_MARKUP.md`
- `10_UI_UX_READABILITY_AND_ENGAGEMENT.md`
- `11_MOBILE_ACCESSIBILITY_AND_RESPONSIVENESS.md`
- `12_PERFORMANCE_AND_CORE_WEB_VITALS.md`
- `13_REACT_APPLICATION_QUALITY.md`
- `14_SECURITY_PRIVACY_AND_RELIABILITY.md`
- `15_SEARCH_CONSOLE_ANALYTICS_AND_MONITORING.md`
- `16_CONTENT_FRESHNESS_AND_MAINTENANCE.md`
- `17_TWO_PASS_TESTING_AND_RELEASE_CHECKLIST.md`
- `18_AUDIT_FINDINGS_AND_PRIORITIZED_ACTION_PLAN.md`

Adapt this list to the real project and its existing documentation. Avoid duplicate instructions and preserve all existing agent rules.

## 23. Final Acceptance Criteria

The project audit is complete only when:

- [ ] The actual repository and route structure have been inspected.
- [ ] Every discovered public route is inventoried or explicitly excluded with a reason.
- [ ] Each applicable audit category has a detailed checklist.
- [ ] Each checklist has a separate Pass 1 and Pass 2 verification process.
- [ ] Existing page content, sections, records, and functionality are preserved unless an approved change states otherwise.
- [ ] Important official information has a verifiable source or is clearly flagged for verification.
- [ ] Internal and external links have been checked using recorded evidence.
- [ ] SEO metadata, indexability, canonical URLs, and structured data have been tested on representative routes.
- [ ] Responsive layouts, accessibility, and critical user journeys have been tested.
- [ ] Applicable lint, type, test, and production-build checks have been run.
- [ ] Remaining issues are listed with priority, evidence, and recommended actions.
- [ ] The final report distinguishes completed, failed, blocked, and untested items.
- [ ] No claim is made that a ranking, indexing outcome, or performance improvement is guaranteed.

**Final developer instruction:** Start with the audit and documentation. Do not begin a broad redesign or mass content rewrite before establishing the baseline. Use verified project evidence, follow existing repository conventions, implement changes in controlled stages, and independently verify each stage before reporting completion.