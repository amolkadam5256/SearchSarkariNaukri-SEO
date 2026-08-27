# SearchSarkariNaukri.com --- Homepage Section 2 Implementation Specification

**Section Name:** `02_Latest_Government_Jobs`\
**Page:** Homepage `/` only\
**Section Position:** Immediately after `01_HeroSection`\
**Purpose:** Show current active government jobs and create a clean
internal-link bridge from the homepage to individual jobs and verified
hub pages.\
**Status:** Final implementation specification\
**Rule:** Preserve the approved content and architecture from the
previous Section 2 specification. This document adds the complete
developer implementation, internal-link, route-verification, SEO,
accessibility, performance and QA requirements.

------------------------------------------------------------------------

# 1. Scope

This document applies **only** to:

``` text
Homepage /
└── 02_Latest_Government_Jobs
```

Do not use this specification to redesign:

-   Hero
-   Qualification section
-   District section
-   Department section
-   Exam section
-   Results
-   Admit Cards
-   News
-   Blogs
-   Current Affairs
-   Footer
-   Individual job templates
-   Qualification pages
-   District pages

The Hero remains unchanged.

The approved homepage architecture is:

``` text
01_HeroSection
        ↓
02_Latest_Government_Jobs
        ↓
03_Qualification_Location_Department_Exam
        ↓
Later homepage sections
```

------------------------------------------------------------------------

# 2. SEO Purpose

The homepage primary intent remains:

**Sarkari Naukri 2026**

Section 2 supports:

**Latest Government Jobs 2026**

Supporting semantic terms:

-   Latest Government Jobs 2026
-   Government Job Vacancies 2026
-   Latest Sarkari Jobs 2026
-   Government Recruitment 2026
-   Current Government Vacancies
-   Sarkari Naukri 2026
-   Government Jobs in India
-   Latest Recruitment Notifications

Do not force all keywords into the section.

The section should naturally communicate that the homepage contains
current government vacancies.

------------------------------------------------------------------------

# 3. Approved H2

Use exactly:

## Latest Government Jobs 2026

Do not change the H2 to:

-   Latest Sarkari Jobs
-   Latest Government Vacancy
-   Latest Jobs in India
-   Government Jobs Near Me
-   New Government Jobs

The approved H2 has the clearest relationship with the homepage intent.

------------------------------------------------------------------------

# 4. Approved Intro Copy

Use exactly:

> **Explore the latest government job vacancies in India, with current
> recruitment updates, eligibility, important dates and application
> details. Check the official recruitment notification before
> applying.**

Do not expand this into a long keyword paragraph.

The homepage already has substantial content elsewhere. Section 2 is a
current-job discovery block.

------------------------------------------------------------------------

# 5. Section Layout

Use this order:

``` text
H2
Latest Government Jobs 2026
        ↓
Short introduction
        ↓
Small filter/navigation row
        ↓
Current active job cards
        ↓
View All Government Jobs
        ↓
Verified internal hub links
```

Recommended number:

**8 active jobs**

Allowed range:

**6--12**

Do not display hundreds of jobs.

------------------------------------------------------------------------

# 6. Job Card Structure

Every card should contain:

``` text
Organization / Department

Actual Job Title

Qualification
Location
Last Date

View Job Details
```

Example:

``` text
Maharashtra Government Department

Junior Assistant Recruitment 2026

Qualification: Graduate
Location: Pune, Maharashtra
Last Date: 21 Sep 2026

View Job Details →
```

Do not put the full recruitment notification into the card.

------------------------------------------------------------------------

# 7. Semantic HTML

Use:

``` html
<section aria-labelledby="latest-government-jobs-title">

  <h2 id="latest-government-jobs-title">
    Latest Government Jobs 2026
  </h2>

  <p>
    Explore the latest government job vacancies in India, with current
    recruitment updates, eligibility, important dates and application
    details. Check the official recruitment notification before applying.
  </p>

  <div class="job-grid">

    <article class="job-card">
      <p class="organization">Organization Name</p>

      <h3>
        <a href="/actual-job-url">
          Actual Job Title 2026
        </a>
      </h3>

      <ul>
        <li>Qualification: Graduate</li>
        <li>Location: Pune, Maharashtra</li>
        <li>Last Date: 21 Sep 2026</li>
      </ul>

      <a href="/actual-job-url">
        View Job Details
      </a>
    </article>

  </div>

</section>
```

The actual job URL must come from the production application's canonical
job record.

------------------------------------------------------------------------

# 8. Heading Hierarchy

Correct:

``` text
H1
Sarkari Naukri 2026 – Latest Government Jobs & Vacancies in India

H2
Latest Government Jobs 2026

H3
Job Title 1

H3
Job Title 2

H3
Job Title 3
```

Do not use H2 for every job.

Do not create another H1.

------------------------------------------------------------------------

# 9. Current Job Selection

Only display genuinely active/current jobs.

Selection priority:

``` text
Active
↓
Valid recruitment
↓
Application still open
↓
Valid canonical URL
↓
Relevant/current
↓
Recent publication or meaningful update
```

Do not sort only by database ID unless database ID is proven to
represent current freshness.

------------------------------------------------------------------------

# 10. Expired Job Rule

A job must not appear as an active vacancy if:

``` text
lastDate < current date
```

Exclude:

-   expired application;
-   deleted recruitment;
-   invalid recruitment;
-   404 URL;
-   410 URL;
-   broken canonical;
-   closed job presented as open.

Useful expired job pages may remain accessible according to the site's
historical-content strategy, but they must not appear in the active
homepage list.

------------------------------------------------------------------------

# 11. Duplicate Job Rule

Every recruitment must appear once.

Do not solve duplicate records with:

``` css
display:none;
```

or JavaScript hiding.

Deduplicate at:

``` text
database/query
        ↓
data normalization
        ↓
render
```

Use the site's stable job/recruitment identifier.

The audit identified duplicate-result/admit/job data issues elsewhere,
so this must be a hard regression test.

------------------------------------------------------------------------

# 12. Canonical Job URL Rule

Before rendering a card, verify:

-   URL exists;
-   URL is the canonical job URL;
-   response is valid;
-   job is not deleted;
-   job is not 404;
-   job is not 410;
-   job is not an unrelated redirect;
-   job title matches the destination;
-   job data matches the destination.

Never manually create job URLs from a title.

------------------------------------------------------------------------

# 13. Job Title Rule

Use the actual recruitment title.

Good:

``` text
Junior Assistant Recruitment 2026
```

Bad:

``` text
Latest Government Job 2026 Sarkari Naukri Government Vacancy Junior Assistant
```

Do not keyword-stuff individual job titles.

------------------------------------------------------------------------

# 14. Organization Rule

Use the actual organization or department name.

Good:

``` text
Maharashtra Public Service Commission
```

Bad:

``` text
MPSC Maharashtra Government Sarkari Naukri Recruitment Jobs
```

The organization field is an entity signal, not a keyword container.

------------------------------------------------------------------------

# 15. Qualification Rule

Use standardized values:

-   10th Pass
-   12th Pass
-   ITI
-   Diploma
-   Graduate
-   Post Graduate
-   Engineering

Do not create inconsistent variations for the same qualification.

------------------------------------------------------------------------

# 16. Location Rule

Keep location concise.

Good:

``` text
Pune, Maharashtra
Mumbai, Maharashtra
Nagpur, Maharashtra
All India
```

Do not place a full postal address in the card.

The individual job page can contain detailed location information.

------------------------------------------------------------------------

# 17. Last Date Rule

Use one consistent display format.

Example:

``` text
Last Date: 21 Sep 2026
```

The date must come from the live recruitment data.

Never hard-code example dates into production.

------------------------------------------------------------------------

# 18. Optional Status

If the application has a reliable recruitment status field, a card may
show:

-   Open
-   Closing Soon
-   Closed

Only active cards should be shown in this section.

Do not use artificial urgency.

If `Closing Soon` is used, define a real rule based on the application
deadline.

------------------------------------------------------------------------

# 19. Small Filter Row

Keep this lightweight.

Recommended:

``` text
All Jobs
Maharashtra
Central Jobs
Latest
```

These are navigation/filter controls, not a second full search system.

The Hero already contains the main search.

Do not add 15--20 filters here.

------------------------------------------------------------------------

# 20. Filter Link Rule

Do not create indexable URL combinations merely because a filter exists.

Before linking a filter:

1.  confirm the URL works;
2.  confirm it has useful content;
3.  confirm canonical behavior;
4.  confirm indexability strategy;
5.  confirm it is not a thin search-result URL.

The site's master implementation guidance explicitly requires controlled
expansion and warns against creating large numbers of thin programmatic
pages.

------------------------------------------------------------------------

# 21. Main CTA

Use exactly:

**View All Government Jobs →**

Destination:

``` text
/jobs
```

This is a confirmed homepage/job-hub route in the existing project
documentation.

The Hero also links to `/jobs`; this repetition is intentional:

``` text
Hero
→ search/discovery

Section 2
→ latest current vacancies

/jobs
→ complete job inventory
```

------------------------------------------------------------------------

# 22. Job Card Internal Links

Every visible job card must link to its actual canonical job page.

Use:

``` html
<a href="/actual-canonical-job-url">
  Actual Job Title
</a>
```

The title link should be the primary link.

A secondary:

``` text
View Job Details
```

link may point to the same URL.

Do not link one card to a filter URL when an individual canonical job
page exists.

------------------------------------------------------------------------

# 23. Internal Link Architecture

Section 2 creates this first layer:

``` text
Homepage
    ↓
Latest Government Jobs 2026
    ↓
Individual Job Pages
```

Then the section begins the hub architecture:

``` text
Homepage
    ↓
Qualification Hub
Location Hub
Department Hub
    ↓
Individual Jobs
```

------------------------------------------------------------------------

# 24. Confirmed Internal Links

The project documentation confirms these important public routes:

  ------------------------------------------------------------------------
  Anchor                  URL                      Use in Section 2
  ----------------------- ------------------------ -----------------------
  View All Government     `/jobs`                  **Yes**
  Jobs                                             

  Browse Maharashtra Jobs `/districts`             **Yes**
  / Districts                                      

  Check Eligibility       `/eligibility-checker`   Existing Hero / not
                                                   necessary again

  Exams                   `/exams`                 Later homepage section

  Results                 `/results`               Later homepage section

  Admit Cards             `/admit-cards`           Later homepage section

  News                    `/news`                  Later homepage section

  Blogs                   `/blogs`                 Later homepage section

  Current Affairs         `/current-affairs`       Later homepage section

  Job Updates             `/job-updates`           Later homepage section

  Exam Calendar           `/exam-calendar`         Later homepage section

  Age Calculator          `/age-calculator`        Later homepage section

  Quiz                    `/quiz`                  Later homepage section

  Career Guidance         `/career-guidance`       Later homepage section
  ------------------------------------------------------------------------

The audit specifically identifies `/jobs`, `/districts`, `/exams`,
`/admit-cards`, `/results`, `/news`, `/blogs`, `/current-affairs`,
`/job-updates`, `/exam-calendar`, `/eligibility-checker`,
`/age-calculator`, `/quiz`, and `/career-guidance` as homepage/public
architecture routes, while account routes such as
dashboard/saved-jobs/reminders/preferences should not automatically be
treated as SEO destinations.

------------------------------------------------------------------------

# 25. Qualification Link --- Important Verification Rule

The project contains references to:

``` text
/qualifications
```

and separate qualification landing-page specifications.

However, the current audit materials also contain proposed future
qualification URLs such as:

``` text
/qualification/10th-pass-government-jobs
/qualification/12th-pass-government-jobs
/qualification/iti-government-jobs
/qualification/diploma-government-jobs
/qualification/graduate-government-jobs
/qualification/engineering-government-jobs
/qualification/post-graduate-government-jobs
```

These are **not automatically interchangeable**.

Therefore:

### Developer must NOT guess.

Before adding:

``` text
Browse Jobs by Qualification
```

verify the actual production canonical route.

If `/qualifications` is the live public hub, use:

``` text
/qualifications
```

If the application has implemented the individual qualification landing
pages, use the actual canonical pages.

Do not create a broken link simply because a URL appears in a planning
document.

------------------------------------------------------------------------

# 26. Location Link

The sitemap architecture confirms:

``` text
sitemap-locations.xml
sitemap-districts.xml
```

The project also confirms the public:

``` text
/districts
```

route.

Therefore the safe Section 2 location pathway is:

``` text
Browse Jobs by Location
        ↓
/districts
        ↓
Maharashtra district pages
        ↓
Individual Jobs
```

Do not invent `/locations` unless the production application actually
exposes it.

------------------------------------------------------------------------

# 27. Department Link

The sitemap architecture confirms:

``` text
sitemap-departments.xml
```

but the project materials reviewed here do **not** establish a final
public `/departments` route with enough certainty to hard-code it as a
verified production link.

Therefore:

**Do not use `/departments` blindly.**

Developer must first inspect the live route/application and use the
actual canonical department hub.

If no public department hub exists yet:

-   do not create a broken link;
-   leave the Department pathway for the next implementation section;
-   or implement the verified route after route creation.

------------------------------------------------------------------------

# 28. Why This Route Rule Is Important

The project contains both:

``` text
existing production routes
```

and:

``` text
planned SEO landing-page routes
```

These must not be mixed.

A planning URL is not automatically a working URL.

The final Section 2 implementation must use:

``` text
Working production URL
+
200/valid response
+
canonical URL
+
indexability appropriate to the page
```

before a link is published.

------------------------------------------------------------------------

# 29. Internal Link Validation Matrix

Before release, create this exact test:

  Link                Expected                      Test
  ------------------- ----------------------------- ------------------
  `/jobs`             Working public job hub        HTTP + canonical
  `/districts`        Working public district hub   HTTP + canonical
  Qualification hub   Existing production route     HTTP + canonical
  Department hub      Existing production route     HTTP + canonical
  Job 1               Active canonical job          HTTP + canonical
  Job 2               Active canonical job          HTTP + canonical
  Job 3               Active canonical job          HTTP + canonical
  Job 4               Active canonical job          HTTP + canonical
  Job 5               Active canonical job          HTTP + canonical
  Job 6               Active canonical job          HTTP + canonical
  Job 7               Active canonical job          HTTP + canonical
  Job 8               Active canonical job          HTTP + canonical

No link should be marked **Pass** based only on a URL string.

------------------------------------------------------------------------

# 30. HTTP Link Test

For every production Section 2 link:

``` text
Request URL
    ↓
HTTP response
    ↓
2xx / intended response
    ↓
Canonical check
    ↓
Robots/indexability check
    ↓
Content relevance check
    ↓
Pass
```

Do not treat a 3xx or 200 placeholder/error page as automatically valid.

------------------------------------------------------------------------

# 31. Job "Not Found" Rule

The master audit identified public URLs that can show:

``` text
Job not found
```

and specifically requires verification of:

1.  HTTP status;
2.  canonical;
3.  robots;
4.  sitemap inclusion;
5.  internal links;
6.  true 404/410 behavior.

Therefore Section 2 must never select such records.

A job card pointing to a "Job not found" page is a **hard failure**.

------------------------------------------------------------------------

# 32. Server-Rendered Content

The initial HTML must contain:

-   H2;
-   intro;
-   visible job titles;
-   job URLs;
-   organization;
-   qualification;
-   location;
-   last date.

Do not require a client-side API call before Googlebot can discover the
core job links.

The existing audit specifically identified `/jobs` server-render
verification as an important open check, so Section 2 should follow the
same SSR requirement.

------------------------------------------------------------------------

# 33. Googlebot Parity

Compare:

``` text
Normal user HTML
vs
Googlebot HTML
```

The following must be equivalent:

-   H2;
-   intro;
-   job titles;
-   job links;
-   organization;
-   qualification;
-   location;
-   dates;
-   CTA;
-   internal hub links.

Do not show different SEO content to Googlebot.

------------------------------------------------------------------------

# 34. Dynamic Job Query

Recommended application logic:

``` text
Fetch active jobs
        ↓
Validate status
        ↓
Validate deadline
        ↓
Validate canonical URL
        ↓
Deduplicate
        ↓
Sort by current relevance/freshness
        ↓
Take 8
        ↓
Render server-side
```

Do not send the entire jobs table to the browser.

------------------------------------------------------------------------

# 35. Database Query Rule

Do not implement:

``` text
SELECT everything
```

for the homepage.

Return only the fields required:

``` text
job_id
title
organization
qualification
location
last_date
status
canonical_url
updated_at
```

Adapt field names to the actual production schema.

------------------------------------------------------------------------

# 36. Data Validation Before Render

Each record must pass:

``` text
job_id exists
AND
title exists
AND
canonical_url exists
AND
canonical URL is valid
AND
status is active
AND
last_date is current
```

If a record fails validation, skip it.

Do not render broken data merely to keep the card count at eight.

------------------------------------------------------------------------

# 37. If Fewer Than 8 Jobs Exist

Do not use fake/example jobs.

Correct:

``` text
5 valid active jobs
→ show 5
```

Incorrect:

``` text
5 valid jobs
+
3 fake placeholder jobs
```

Never fabricate recruitment data.

------------------------------------------------------------------------

# 38. Freshness

The section is named:

**Latest Government Jobs 2026**

Therefore the displayed jobs must genuinely be current.

Possible ranking signals:

-   current open status;
-   latest publication;
-   meaningful update;
-   closing date;
-   recruitment relevance.

Do not hard-code:

``` text
Last Updated: 27 August 2026
```

unless the value is dynamically generated from real data.

The broader audit specifically found a stale homepage freshness label as
a verification issue.

------------------------------------------------------------------------

# 39. ItemList Schema

The homepage may maintain an `ItemList` for visible latest jobs.

If 8 cards are visible:

``` text
ItemList = same 8 jobs
```

Requirements:

-   canonical job URLs;
-   no duplicate jobs;
-   no expired jobs;
-   no invisible jobs;
-   visible/schema parity;
-   same ordering.

Do not place 100 invisible jobs in ItemList.

------------------------------------------------------------------------

# 40. JobPosting Schema

Do not add generic JobPosting schema to Section 2.

Detailed JobPosting structured data belongs to the applicable individual
job page.

Section 2 can use ItemList to represent the visible collection where
appropriate.

------------------------------------------------------------------------

# 41. Keyword Cannibalization

Section 2 should not try to rank for every recruitment category.

Homepage:

**Sarkari Naukri 2026**

Section 2:

**Latest Government Jobs 2026**

Dedicated pages should own:

-   MPSC Bharti 2026
-   SSC Recruitment 2026
-   Railway Jobs 2026
-   Police Bharti 2026
-   12th Pass Government Jobs 2026
-   Pune Government Jobs 2026

Do not add these as repetitive keywords to every card.

------------------------------------------------------------------------

# 42. Job Card Link Text

Primary link:

``` text
Actual Job Title
```

Secondary link:

``` text
View Job Details
```

Do not use:

``` text
Click Here
Read More
More
Explore
```

The actual job title provides strong contextual anchor text.

------------------------------------------------------------------------

# 43. Accessibility

Every card must have:

-   semantic `<article>`;
-   H3 title;
-   descriptive link;
-   keyboard-accessible link;
-   visible focus;
-   adequate contrast;
-   adequate mobile tap target.

Icons are decorative unless they communicate information.

For decorative icons:

``` html
aria-hidden="true"
```

------------------------------------------------------------------------

# 44. Mobile UI

Recommended:

``` text
Latest Government Jobs 2026

Short intro

[ All Jobs ]
[ Maharashtra ]
[ Central Jobs ]
[ Latest ]

--------------------------------
Organization
Job Title
Qualification
Location
Last Date
View Job Details
--------------------------------

Job Card
--------------------------------

[ View All Government Jobs ]

Browse Jobs by Qualification →
Browse Jobs by Location →
Browse Jobs by Department →
```

Cards should stack vertically.

No horizontal overflow.

------------------------------------------------------------------------

# 45. Desktop UI

Recommended:

``` text
             Latest Government Jobs 2026
          Short supporting introduction

       [All Jobs] [Maharashtra] [Central] [Latest]

 ---------------------------------------------------------
 | Job Card | Job Card | Job Card | Job Card |
 ---------------------------------------------------------

                 [ View All Government Jobs ]

       Qualification | Location | Department
```

The visual style should follow the Hero's existing dark-blue/orange
design system without copying the entire Hero.

------------------------------------------------------------------------

# 46. Performance

The previous homepage audit found poor mobile performance.

Therefore Section 2 must remain lightweight.

Do not add:

-   video;
-   large organization images;
-   heavy animations;
-   unnecessary sliders;
-   external widgets;
-   third-party embeds;
-   large JavaScript libraries.

Text-first cards are preferred.

------------------------------------------------------------------------

# 47. Images

Job cards do not need large images.

If organization logos are already part of the production design:

-   optimize them;
-   define width/height;
-   prevent layout shift;
-   lazy-load non-critical images;
-   use accurate alt text.

If the logo is decorative, do not use keyword-heavy alt text.

------------------------------------------------------------------------

# 48. JavaScript

Core content should not depend on JavaScript.

JavaScript may enhance:

-   filters;
-   sorting;
-   UI animation;
-   interaction.

But the initial page must still expose:

``` text
H2
Job titles
Job links
```

------------------------------------------------------------------------

# 49. No Infinite Scroll

Do not make the homepage job links dependent on infinite scroll.

The initial HTML should expose the visible jobs.

The full inventory remains:

``` text
/jobs
```

------------------------------------------------------------------------

# 50. No Homepage Pagination

Do not paginate Section 2.

Use:

**View All Government Jobs → `/jobs`**

Pagination belongs to the `/jobs` page.

------------------------------------------------------------------------

# 51. No Sitemap XML Navigation

Do not put:

``` text
sitemap-jobs.xml
sitemap-locations.xml
sitemap-qualifications.xml
```

as user-facing Section 2 links.

XML sitemaps are crawler resources.

Users need HTML landing pages.

------------------------------------------------------------------------

# 52. Location Architecture

The sitemap index supplied for the project contains:

``` text
sitemap-locations.xml
sitemap-districts.xml
```

The desired architecture is:

``` text
Homepage
 ↓
Location / District Hub
 ↓
Maharashtra
 ↓
Pune / Mumbai / Nagpur / Nashik / ...
 ↓
Individual Job
```

Section 2 should only provide the top-level verified location pathway.

The full district list belongs in the dedicated location section later.

------------------------------------------------------------------------

# 53. Qualification Architecture

The desired architecture is:

``` text
Homepage
 ↓
Qualification Hub
 ↓
10th Pass
12th Pass
ITI
Diploma
Graduate
Post Graduate
Engineering
 ↓
Relevant Jobs
```

The project's planning documents include both `/qualifications` and more
granular `/qualification/...` proposals.

Use only routes that are confirmed to exist in production.

------------------------------------------------------------------------

# 54. Department Architecture

The sitemap index contains:

``` text
sitemap-departments.xml
```

Desired architecture:

``` text
Homepage
 ↓
Department Hub
 ↓
MPSC
SSC
Railway
Banking
Police
Education
Health
Forest
Central Government
 ↓
Relevant Jobs
```

Do not publish `/departments` until it is confirmed as a real production
route.

------------------------------------------------------------------------

# 55. Cross-Filter Architecture

The project contains:

``` text
sitemap-cross-filter.xml
```

Potential combinations include:

``` text
Qualification × Location
Qualification × Department
Location × Department
```

Do not expose all combinations from Section 2.

Only high-value, canonical, useful combinations should eventually be
linked.

Avoid thousands of thin pages.

------------------------------------------------------------------------

# 56. Orphan-URL Consideration

The broader audit identified a large number of sitemap URLs without
discovered internal links, particularly job URLs.

Section 2 improves discovery for the highest-priority current jobs, but
it does not solve all orphan URLs.

The complete architecture must eventually be:

``` text
Homepage
 ↓
Category / Department
 ↓
Qualification
 ↓
Location / District
 ↓
Individual Job
```

This is why Section 2 must use real job links and later sections must
create the hub links.

------------------------------------------------------------------------

# 57. Existing `/jobs` Architecture

The project audit indicates `/jobs` already exposes crawlable navigation
for:

-   departments;
-   districts;
-   results;
-   admit cards;
-   exam calendar;
-   qualification/category/location resources;
-   sitemap.

Therefore Section 2 should complement `/jobs`, not duplicate the entire
`/jobs` page.

------------------------------------------------------------------------

# 58. No Duplicate Search Interface

The Hero already has the main search.

Section 2 should use only lightweight filters/navigation.

Do not create another large search form here.

------------------------------------------------------------------------

# 59. Section 2 and Hero Relationship

Hero:

``` text
What is the site?
How can I search?
```

Section 2:

``` text
What jobs are available now?
```

Therefore:

``` text
Hero
 ↓
Latest Government Jobs 2026
 ↓
Individual Job
```

This is the correct user journey.

------------------------------------------------------------------------

# 60. Approved Section Copy

### H2

**Latest Government Jobs 2026**

### Intro

**Explore the latest government job vacancies in India, with current
recruitment updates, eligibility, important dates and application
details. Check the official recruitment notification before applying.**

### Main CTA

**View All Government Jobs →**

### Supporting navigation

**Browse Jobs by Qualification →**

**Browse Jobs by Location →**

**Browse Jobs by Department →**

The wording above must not be changed without SEO review.

------------------------------------------------------------------------

# 61. Developer Route Registry

Before production implementation, create a route registry:

``` text
ROUTE_REGISTRY_SECTION_02

/jobs
/districts
/qualification-hub-or-confirmed-route
/department-hub-or-confirmed-route
/actual-job-url-1
/actual-job-url-2
...
```

For each route record:

``` text
URL
HTTP status
Canonical
Indexability
Page type
Last verified
```

Do not mark a route "working" because it appears in a document.

------------------------------------------------------------------------

# 62. Link Validation Script Requirement

The developer should run a link validation check against every URL
rendered by Section 2.

Conceptually:

``` text
for each section2_link:
    fetch URL
    verify response
    verify canonical
    verify intended page type
    verify no "not found" content
    verify indexability
    record result
```

The final implementation should contain no known broken internal links.

------------------------------------------------------------------------

# 63. Job Card Automated QA

For every rendered job card:

``` text
title exists
organization exists
qualification exists
location exists
lastDate exists
canonical URL exists
status active
not duplicate
not expired
```

If any critical field is missing, the record should be rejected from the
homepage component.

------------------------------------------------------------------------

# 64. ItemList Automated QA

Before generating ItemList:

``` text
visibleJobs = rendered jobs
schemaJobs = ItemList jobs

assert visibleJobs.length == schemaJobs.length
assert visibleJobs.urls == schemaJobs.urls
assert no duplicates
assert all canonical
```

This prevents schema/content mismatch.

------------------------------------------------------------------------

# 65. Accessibility QA

Run:

-   axe;
-   Lighthouse Accessibility;
-   keyboard navigation;
-   focus test;
-   mobile tap-target test.

Check:

-   H2 accessible;
-   H3 accessible;
-   links named correctly;
-   no icon-only unnamed links;
-   no contrast failure;
-   no keyboard trap.

------------------------------------------------------------------------

# 66. Responsive QA

Test:

``` text
320px
360px
375px
390px
414px
768px
1024px
1280px
1440px
1536px
```

Check:

-   card width;
-   title wrapping;
-   last-date wrapping;
-   CTA wrapping;
-   filters;
-   no horizontal overflow.

------------------------------------------------------------------------

# 67. Performance QA

Run:

-   Lighthouse mobile;
-   Lighthouse desktop;
-   Core Web Vitals;
-   total transferred bytes;
-   JavaScript execution;
-   layout shift.

Targets from the broader SEO implementation guidance:

``` text
LCP < 2.5s
INP < 200ms
CLS < 0.1
```

Section 2 must not worsen the homepage baseline.

------------------------------------------------------------------------

# 68. Rendering QA

Test:

``` text
Normal Browser
Googlebot User Agent
Raw HTTP HTML
```

Confirm that all three expose the core section.

Required initial HTML:

``` text
Latest Government Jobs 2026
intro
job titles
job links
job metadata
View All Government Jobs
```

------------------------------------------------------------------------

# 69. SEO QA

Check:

-   exactly one H1 on homepage;
-   Section 2 uses H2;
-   job cards use H3;
-   primary keyword is not unnecessarily repeated;
-   no hidden SEO text;
-   no keyword stuffing;
-   descriptive anchors;
-   canonical job URLs;
-   no broken links.

------------------------------------------------------------------------

# 70. Content QA

Check:

-   current jobs only;
-   accurate organization;
-   accurate qualification;
-   accurate location;
-   accurate deadline;
-   no duplicate records;
-   no fake jobs;
-   no stale dates;
-   no unsupported claims.

------------------------------------------------------------------------

# 71. Trust Rule

Do not claim:

> Official Government Jobs Portal

or:

> Government Authorized Portal

The site is an independent job-information portal.

Keep the official-notification verification principle:

> **Check the official recruitment notification before applying.**

------------------------------------------------------------------------

# 72. Do Not Change

The following approved elements remain unchanged:

``` text
H2:
Latest Government Jobs 2026

Intro:
Explore the latest government job vacancies in India, with current recruitment updates, eligibility, important dates and application details. Check the official recruitment notification before applying.

CTA:
View All Government Jobs →

Supporting:
Browse Jobs by Qualification →
Browse Jobs by Location →
Browse Jobs by Department →
```

Only the actual destination URLs may be adjusted after route
verification if a planning URL is not a live production route.

------------------------------------------------------------------------

# 73. Do Not Use Placeholder Production Data

The development HTML previously used examples such as:

``` text
/example-job-1
/example-job-2
/example-job-3
/example-job-4
```

These are **development placeholders only**.

They must never be deployed.

Production must use actual current job records and canonical URLs.

------------------------------------------------------------------------

# 74. Developer Do Not

Do not:

-   create fake job records;
-   hard-code expired dates;
-   hard-code current jobs;
-   use example URLs in production;
-   create duplicate job cards;
-   hide duplicate records with CSS;
-   show expired jobs as active;
-   invent department URLs;
-   invent qualification URLs;
-   invent location URLs;
-   link to XML sitemap files;
-   create thousands of filter links;
-   add hidden SEO text;
-   keyword stuff;
-   add another H1;
-   add fake urgency;
-   use JavaScript-only internal navigation;
-   load the entire jobs database;
-   add heavy images;
-   add video;
-   add unnecessary third-party widgets.

------------------------------------------------------------------------

# 75. Acceptance Checklist --- Content

-   [ ] H2 exactly `Latest Government Jobs 2026`
-   [ ] Approved intro used exactly
-   [ ] 6--12 active jobs
-   [ ] Recommended 8
-   [ ] No expired jobs
-   [ ] No duplicate jobs
-   [ ] No fake jobs
-   [ ] Organization shown
-   [ ] Qualification shown
-   [ ] Location shown
-   [ ] Last date shown
-   [ ] Actual job title shown

------------------------------------------------------------------------

# 76. Acceptance Checklist --- Internal Links

-   [ ] `/jobs` verified and working
-   [ ] `/districts` verified and working
-   [ ] Qualification hub verified before linking
-   [ ] Department hub verified before linking
-   [ ] Every job URL verified
-   [ ] No example URL
-   [ ] No 404 URL
-   [ ] No 410 URL
-   [ ] No "Job not found" page
-   [ ] Canonical destination confirmed
-   [ ] Internal links use `<a href>`
-   [ ] No sitemap XML user links
-   [ ] No invented route

------------------------------------------------------------------------

# 77. Acceptance Checklist --- SEO

-   [ ] H2 is correct
-   [ ] Job titles use H3
-   [ ] Job titles are HTML text
-   [ ] Primary job links are crawlable
-   [ ] Descriptive anchor text
-   [ ] No keyword stuffing
-   [ ] No hidden text
-   [ ] No duplicate headings
-   [ ] ItemList matches visible jobs
-   [ ] No fake JobPosting schema on homepage

------------------------------------------------------------------------

# 78. Acceptance Checklist --- Technical

-   [ ] Server-rendered core section
-   [ ] Googlebot sees same core content
-   [ ] Current job query is validated
-   [ ] Job data is deduplicated
-   [ ] Canonical URLs validated
-   [ ] HTTP status validated
-   [ ] No broken links
-   [ ] No client-only dependency for core links
-   [ ] No entire database sent to browser

------------------------------------------------------------------------

# 79. Acceptance Checklist --- Accessibility

-   [ ] Semantic `<section>`
-   [ ] H2 has clear accessible name
-   [ ] Job titles use H3
-   [ ] Links have descriptive names
-   [ ] Keyboard navigation works
-   [ ] Visible focus states
-   [ ] Adequate tap targets
-   [ ] Adequate contrast
-   [ ] Decorative icons use appropriate accessibility handling
-   [ ] No horizontal overflow

------------------------------------------------------------------------

# 80. Acceptance Checklist --- Performance

-   [ ] Text-first cards
-   [ ] No unnecessary large images
-   [ ] No video
-   [ ] No heavy animation
-   [ ] No unnecessary third-party scripts
-   [ ] No layout shift
-   [ ] Mobile performance does not regress
-   [ ] LCP remains healthy
-   [ ] INP/TBT remains healthy

------------------------------------------------------------------------

# 81. Acceptance Checklist --- Data Freshness

-   [ ] Active status verified
-   [ ] Last date verified
-   [ ] Current update verified
-   [ ] Organization verified
-   [ ] Qualification verified
-   [ ] Location verified
-   [ ] Official notification exists where required
-   [ ] Expired records excluded
-   [ ] Deleted records excluded
-   [ ] Duplicate records excluded

------------------------------------------------------------------------

# 82. Final Internal-Link Graph

``` text
                           HOMEPAGE
                              │
                              ↓
               ┌───────────────────────────┐
               │ Latest Government Jobs    │
               │ 2026                      │
               └───────────────────────────┘
                    │       │       │
                    ↓       ↓       ↓
                  Job 1   Job 2   Job 3 ... Job 8
                    │       │
                    ↓       ↓
             Individual Job Pages
                    │
                    ↓
           Official Recruitment Source


Homepage
   │
   ├── /jobs
   │      ↓
   │   Full Active Jobs
   │
   ├── /districts
   │      ↓
   │   Maharashtra Districts
   │      ↓
   │   District Jobs
   │
   ├── Qualification Hub
   │      ↓
   │   Qualification Jobs
   │
   └── Department Hub
          ↓
       Department Jobs
```

Only the routes confirmed in production should be rendered.

------------------------------------------------------------------------

# 83. Relationship to Future Homepage Sections

Section 2 should NOT contain the complete
location/qualification/department architecture.

The intended sequence is:

``` text
01 Hero
   ↓
02 Latest Government Jobs
   ↓
03 Government Jobs by Qualification
   ↓
04 Government Jobs by Location / District
   ↓
05 Government Jobs by Department / Exam
   ↓
06 Maharashtra Government Jobs
   ↓
07 Qualification × Location
   ↓
08 Tools / Quick Links
   ↓
09 AEO / FAQ
   ↓
Footer
```

This keeps every section focused.

------------------------------------------------------------------------

# 84. Final Developer Instruction

Implement **only**:

``` text
02_Latest_Government_Jobs
```

Use the approved Section 2 wording and structure.

Do not change the Hero.

Do not modify unrelated homepage sections.

Before publishing any internal link:

``` text
find actual production route
        ↓
HTTP check
        ↓
canonical check
        ↓
indexability check
        ↓
content relevance check
        ↓
publish link
```

For qualification and department routes, the developer must verify the
real production route instead of assuming a route from a sitemap
filename or planning document.

For jobs, use actual live recruitment records and canonical URLs.

After implementation run:

1.  Raw HTML test
2.  Googlebot HTML test
3.  Job-data validation
4.  Duplicate test
5.  Expired-job test
6.  Link-status test
7.  Canonical test
8.  ItemList parity test
9.  Accessibility test
10. Responsive test
11. Lighthouse mobile test
12. Lighthouse desktop test
13. Final internal-link crawl

**Section 2 is complete only when all critical checks pass.**

------------------------------------------------------------------------

# 85. Final Section Definition

``` text
SECTION NAME
02_Latest_Government_Jobs

H2
Latest Government Jobs 2026

PRIMARY INTENT
Latest Government Jobs 2026

CARD COUNT
6–12
Recommended: 8

PRIMARY CTA
View All Government Jobs →

PRIMARY DESTINATION
/jobs

LOCATION PATH
/districts

QUALIFICATION PATH
Use verified production qualification hub

DEPARTMENT PATH
Use verified production department hub

JOB DESTINATION
Actual canonical individual job URL

CORE REQUIREMENT
Only current, valid, non-duplicate jobs

SEO REQUIREMENT
Visible HTML + crawlable internal links + accurate ItemList

PERFORMANCE REQUIREMENT
Lightweight, server-rendered, mobile-first

STATUS
Ready for controlled implementation and QA
```

------------------------------------------------------------------------

# 86. Source/Project Reconciliation Notes

This specification is based on the existing project materials reviewed
for the homepage, Hero, keyword architecture, sitemap architecture,
FAQ/internal-link specifications, jobs-page architecture and master
developer SEO instructions.

Important project findings carried into this section:

-   The homepage has a strong existing information architecture and
    already contains job, qualification, state/city/recruiter and other
    browse pathways.
-   `/jobs` is an important public job hub.
-   `/districts` is an established public district route.
-   The sitemap architecture includes jobs, locations, qualifications,
    departments, cross-filter, districts, results and admit-card sitemap
    areas.
-   The project requires controlled programmatic SEO expansion and warns
    against creating large numbers of thin/duplicate pages.
-   The broader audit requires raw HTML/Googlebot verification for
    dynamic job content.
-   Job-not-found URLs require
    status/canonical/robots/sitemap/internal-link verification.
-   The homepage's visible freshness data must be dynamic and truthful.
-   Account/product routes such as dashboard, saved jobs, reminders and
    preferences should not be treated as normal SEO landing pages
    without a separate indexing decision.

This section therefore prioritizes **verified internal links, real
current jobs and controlled crawlable architecture** rather than adding
large numbers of speculative links.
