# 03 — `/jobs` Page: New Content Sections to Append (Additive Only)

> These are **new blocks to add**, positioned above/below the existing job grid. Nothing existing is removed or reordered — the current hero, search bar, quick filters, and job cards stay exactly where they are.

## Placement map

```
[Existing breadcrumb — new, see file 02]
[Existing H1 — text updated per file 02, block itself untouched]
[NEW: Intro paragraph — insert directly below H1]
[Existing search bar — untouched]
[Existing quick filters — untouched]
[Existing job cards/grid — untouched]
[Existing/new pagination — see file 02]
[NEW SECTION: Government Jobs by Qualification]
[NEW SECTION: Government Jobs by Category]
[NEW SECTION: Government Jobs by Location]
[NEW SECTION: Recruitment Organizations]
[NEW SECTION: How to Find the Right Government Job]
[NEW SECTION: Frequently Asked Questions]
[Existing footer — untouched]
```

## 1. New intro paragraph (insert below H1, above search bar)

```
Find the latest active government jobs and Sarkari Naukri in India, including
Central Government, Maharashtra Government, MPSC, SSC, Railway, Banking,
Police, Teaching, Health and other recruitment opportunities. SearchSarkariNaukri
lists active government recruitment with eligibility, vacancy details,
application deadlines and official application links. Browse jobs by
qualification, department, location and recruitment organization below.
```

Keep this to 150–250 words; expand naturally rather than padding with repeated keywords.

## 2. New section — "Government Jobs by Qualification"

```html
<h2>Government Jobs by Qualification</h2>
<ul>
  <li><a href="/qualification/10th-pass-government-jobs">10th Pass Government Jobs</a></li>
  <li><a href="/qualification/12th-pass-government-jobs">12th Pass Government Jobs</a></li>
  <li><a href="/qualification/iti-government-jobs">ITI Government Jobs</a></li>
  <li><a href="/qualification/diploma-government-jobs">Diploma Government Jobs</a></li>
  <li><a href="/qualification/graduate-government-jobs">Graduate Government Jobs</a></li>
  <li><a href="/qualification/engineering-government-jobs">Engineering Government Jobs</a></li>
  <li><a href="/qualification/post-graduate-government-jobs">Post Graduate Government Jobs</a></li>
</ul>
```

These links point to the new pages defined in file 07. Do not build these as new filter-only links; they must resolve to real indexable pages.

## 3. New section — "Government Jobs by Category"

```html
<h2>Government Jobs by Category</h2>
<ul>
  <li><a href="/category/mpsc-jobs">MPSC Jobs</a></li>
  <li><a href="/category/ssc-jobs">SSC Jobs</a></li>
  <li><a href="/category/railway-jobs">Railway Jobs</a></li>
  <li><a href="/category/banking-jobs">Banking Jobs</a></li>
  <li><a href="/category/police-jobs">Police Jobs</a></li>
  <li><a href="/category/teaching-jobs">Teaching Jobs</a></li>
  <li><a href="/category/health-jobs">Health Jobs</a></li>
  <li><a href="/category/defence-jobs">Defence Jobs</a></li>
  <li><a href="/category/forest-jobs">Forest Jobs</a></li>
  <li><a href="/category/talathi-jobs">Talathi Jobs</a></li>
  <li><a href="/category/zilla-parishad-jobs">Zilla Parishad Jobs</a></li>
</ul>
```

## 4. New section — "Government Jobs by Location"

```html
<h2>Government Jobs by Location</h2>
<ul>
  <li><a href="/maharashtra-government-jobs">Maharashtra Government Jobs</a></li>
  <li><a href="/districts/pune">Pune Government Jobs</a></li>
  <li><a href="/districts/mumbai">Mumbai Government Jobs</a></li>
  <li><a href="/districts/nagpur">Nagpur Government Jobs</a></li>
  <li><a href="/districts/nashik">Nashik Government Jobs</a></li>
  <li><a href="/districts/thane">Thane Government Jobs</a></li>
</ul>
```

Reuse your existing district architecture (`/districts/...`) rather than creating a competing structure — see file 07 for how these connect to the existing noscript district links you already have.

## 5. New section — "Recruitment Organizations"

```html
<h2>Recruitment Organizations</h2>
<ul>
  <li><a href="/recruiters/upsc">UPSC Recruitment</a></li>
  <li><a href="/recruiters/ssc">SSC Recruitment</a></li>
  <li><a href="/recruiters/ibps">IBPS Recruitment</a></li>
  <li><a href="/recruiters/mpsc">MPSC Recruitment</a></li>
  <li><a href="/recruiters/rrb">RRB Recruitment</a></li>
  <li><a href="/recruiters/sbi">SBI Recruitment</a></li>
</ul>
```

## 6. New section — "How to Find the Right Government Job"

Add a short explainer (100–200 words) describing how to use the search/filter tools that already exist on the page — this adds context for both users and Google, without touching the filter UI itself.

## 7. New section — "Frequently Asked Questions"

```html
<h2>Frequently Asked Questions About Government Jobs 2026</h2>
<h3>What are the latest government jobs available in India?</h3>
<p>...</p>
<h3>How can I find government jobs by qualification?</h3>
<p>...</p>
<h3>Which government jobs are available for 10th-pass candidates?</h3>
<p>...</p>
<h3>Which government jobs are available for 12th-pass candidates?</h3>
<p>...</p>
<h3>How can I find Maharashtra government jobs?</h3>
<p>...</p>
<h3>How can I find government jobs whose last date is near?</h3>
<p>...</p>
<h3>Where can I find the official recruitment notification?</h3>
<p>...</p>
<h3>Is SearchSarkariNaukri an official government website?</h3>
<p>SearchSarkariNaukri is an independent career-information portal and is not
affiliated with any government department. Always verify eligibility, dates
and application details on the official recruitment notification.</p>
```

Also add a short, visible disclaimer line near the job listings (not just in the FAQ):

```
Disclaimer: SearchSarkariNaukri is an independent job-information portal and
is not affiliated with any government department. Always verify eligibility,
dates and application details on the official recruitment notification.
```

Wire this FAQ into FAQPage JSON-LD — see file 05.

## Checklist for this file

- [ ] Intro paragraph added below H1
- [ ] "By Qualification" section added
- [ ] "By Category" section added
- [ ] "By Location" section added
- [ ] "Recruitment Organizations" section added
- [ ] "How to Find the Right Job" explainer added
- [ ] FAQ section added with 8+ Q&As
- [ ] Disclaimer line added near listings
- [ ] No existing section removed or reordered
