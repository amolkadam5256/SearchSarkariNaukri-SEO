# 16 — Developer Audit Checklist & Complete Fix Instructions

> **Page**: `https://www.searchsarkarinaukri.com/daily-assessment`
> **Audit Date**: 21 September 2026
> **Status**: Soft 404 resolved on live test. Developer fixes required to lock in indexing.
> **This file**: Complete instructions for the developer to fix every open issue and pass a full technical SEO audit.

---

## HOW TO USE THIS FILE

Work through each section **top to bottom**. Each fix has:
- **What**: What the problem is
- **Why**: Why it matters for SEO / indexing
- **Where**: Exact file or route to edit
- **Fix**: The exact code or command to apply
- **Test**: How to verify the fix worked

Mark each checkbox `[x]` when done.

---

## ──────────────────────────────────────────────────
## PHASE 1 — CRITICAL FIXES (Do Today)
## ──────────────────────────────────────────────────

---

### ✅ FIX 1 — Add `noindex` to the `/assessment` Route

**What**: The authenticated quiz app at `/assessment` is publicly crawlable. Google can visit it and see a login wall or empty state → Soft 404 risk on the wrong route.

**Why**: Google must never index the authenticated assessment shell. It must only index `/daily-assessment` (the SEO landing page). These two routes serve completely different purposes.

**Where**: The React component rendered at the `/assessment` route (e.g., `AssessmentPage.jsx` or `Assessment.jsx`)

**Fix — Add to the `<head>` of the `/assessment` route component:**

```jsx
// Using react-helmet-async (recommended)
import { Helmet } from 'react-helmet-async';

const AssessmentApp = () => {
  return (
    <>
      <Helmet>
        <title>Daily Assessment – Search Sarkari Naukri</title>
        <meta name="robots" content="noindex, nofollow" />
        <link rel="canonical" href="https://www.searchsarkarinaukri.com/assessment" />
      </Helmet>
      {/* rest of authenticated component */}
    </>
  );
};
```

**Also fix in `robots.txt` — add this line:**

```
Disallow: /assessment
```

Full updated `robots.txt` should be:

```
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /assessment
Disallow: /dashboard
Disallow: /saved-jobs
Disallow: /my-saved-jobs
Disallow: /profile-setup
Disallow: /preferences
Disallow: /reminders
Disallow: /api/
Disallow: /login
Disallow: /register
Disallow: /*?utm_*
Disallow: /*?search=
Disallow: /*&search=
Disallow: /*?q=
Disallow: /*&q=
Disallow: /*?category=
Disallow: /*&category=

Sitemap: https://www.searchsarkarinaukri.com/sitemap.xml
```

**Test**:

```bash
# 1. Check robots.txt is updated
curl https://www.searchsarkarinaukri.com/robots.txt | grep assessment

# 2. Check /assessment page source contains noindex
curl -s https://www.searchsarkarinaukri.com/assessment | grep -i "noindex"
```

Expected output for test 1: `Disallow: /assessment`
Expected output for test 2: `content="noindex`

- [ ] `noindex` meta added to `/assessment` route component
- [ ] `Disallow: /assessment` added to `robots.txt`
- [ ] Verified with curl commands above

---

### ✅ FIX 2 — Verify True HTTP 404 for Unknown Routes

**What**: React SPAs commonly return `HTTP 200` for every URL (including completely fake ones), with a React "Page Not Found" screen. This is a **Soft 404** — one of the most common React SEO bugs.

**Why**: Google's definition of a Soft 404 is a page that returns `HTTP 200` but has the characteristics of a missing/empty page. This affects the entire site's crawl quality, not just one page.

**Test first:**

```bash
# Run this command and check the status code
curl -I https://www.searchsarkarinaukri.com/this-url-does-not-exist-at-all

# Expected: HTTP/2 404
# Bad result: HTTP/2 200
```

**If result is 200 (broken) — Fix depends on your hosting platform:**

#### Option A — Vercel

Create or update `vercel.json` in project root:

```json
{
  "routes": [
    {
      "src": "/[^.]+",
      "dest": "/index.html",
      "status": 200
    }
  ],
  "rewrites": [
    { "source": "/(.*)", "destination": "/index.html" }
  ]
}
```

And in your React `404.jsx` component, add a server-side status code hint. The proper Vercel approach is to use a `404.html` file and configure custom error pages:

```json
{
  "rewrites": [{ "source": "/(.*)", "destination": "/index.html" }],
  "routes": [
    { "handle": "filesystem" },
    { "src": "/(.*)", "dest": "/index.html", "status": 200 }
  ]
}
```

Note: For true 404s on Vercel with React Router, the recommended pattern is:

```json
{
  "cleanUrls": true,
  "trailingSlash": false,
  "rewrites": [
    { "source": "/(.*)", "destination": "/index.html" }
  ]
}
```

Then in React, the `NotFoundPage` must send the proper HTTP status. Use `react-router-dom` v6 with a loader that throws a 404 response.

#### Option B — Netlify

In `public/_redirects`:

```
/*  /index.html  200
```

For true 404s, add a custom `public/404.html` and configure:

```
/*  /index.html  200!
/404  /404.html  404
```

#### Option C — Nginx

```nginx
server {
  listen 80;
  root /var/www/html;
  index index.html;

  location / {
    try_files $uri $uri/ /index.html;
  }

  # Return true 404 for API-style unknown paths
  location ~* ^/(api|fake|nonexistent) {
    return 404;
  }
}
```

#### Option D — React Router v6 (App-level fix)

In your main `App.jsx` router, ensure the catch-all `*` route uses a `NotFoundPage` that signals 404:

```jsx
import { Routes, Route, useNavigate } from 'react-router-dom';

// NotFoundPage component
const NotFoundPage = () => {
  // This doesn't set HTTP status by itself, but signals to hosting config
  return (
    <div>
      <Helmet>
        <title>404 – Page Not Found | Search Sarkari Naukri</title>
        <meta name="robots" content="noindex, follow" />
      </Helmet>
      <h1>Page Not Found</h1>
      <p>The page you are looking for does not exist.</p>
    </div>
  );
};

// In your Routes:
<Routes>
  <Route path="/" element={<HomePage />} />
  <Route path="/daily-assessment" element={<DailyAssessmentLanding />} />
  <Route path="/assessment" element={<ProtectedRoute><AssessmentApp /></ProtectedRoute>} />
  <Route path="/login" element={<LoginPage />} />
  <Route path="/register" element={<RegisterPage />} />
  {/* ... all other valid routes ... */}
  <Route path="*" element={<NotFoundPage />} />   {/* Catch-all */}
</Routes>
```

**Test after fix:**

```bash
curl -I https://www.searchsarkarinaukri.com/this-url-does-not-exist-at-all
# Must return: HTTP/2 404
```

- [ ] Tested unknown URL with curl — confirmed HTTP 404 response
- [ ] `NotFoundPage` has `noindex` meta tag
- [ ] Hosting config updated if needed

---

### ✅ FIX 3 — Verify SSR / Pre-render for `/daily-assessment`

**What**: React pages that render entirely in the browser (client-side rendering) can cause indexing delays or gaps because Google must execute JavaScript to see the content.

**Why**: The previous Soft 404 may have occurred because Google's crawler hit `/daily-assessment` at a moment when JavaScript didn't execute properly. Server-side or pre-rendered HTML eliminates this risk.

**Test:**

```bash
# Fetch the page WITHOUT executing JavaScript (raw HTML response)
curl -s https://www.searchsarkarinaukri.com/daily-assessment | grep -i "daily upsc"

# Also check for H1 specifically
curl -s https://www.searchsarkarinaukri.com/daily-assessment | grep -i "<h1"

# Check title tag
curl -s https://www.searchsarkarinaukri.com/daily-assessment | grep -i "<title"
```

**Expected (SSR working):**

```
Daily UPSC & MPSC Quiz – Current Affairs & Practice Questions
<h1>Daily UPSC & MPSC Assessment 2026...</h1>
<title>Daily UPSC & MPSC Assessment 2026 | Free Current Affairs Quiz...</title>
```

**Bad result (client-side only):**

```
<div id="root"></div>
<!-- Nothing else before the script tags -->
```

**If SSR is NOT working — Fix options:**

#### Option A — Use Vite + vite-plugin-ssr (SSR)

```bash
npm install vite-plugin-ssr
```

#### Option B — Use React with Static Pre-rendering

For public SEO pages like `/daily-assessment`, pre-render the HTML at build time:

```bash
npm install react-snap
```

Add to `package.json`:

```json
{
  "scripts": {
    "postbuild": "react-snap"
  },
  "reactSnap": {
    "routes": [
      "/daily-assessment",
      "/",
      "/current-affairs",
      "/quiz",
      "/exams",
      "/digital-library",
      "/exam-calendar"
    ]
  }
}
```

#### Option C — Use Next.js for public SEO pages (recommended long-term)

If the project is ever migrated, Next.js `getStaticProps` or `getServerSideProps` gives the cleanest SSR for SEO landing pages.

#### Option D — Immediate workaround: ensure static content does NOT depend on async API

If full SSR is not feasible right now, ensure the `/daily-assessment` landing page renders its static content (H1, intro, how it works, sample questions, FAQs) synchronously — not inside a `useEffect` with an API call:

```jsx
// ❌ BAD — Google sees empty page if API is slow or fails
const DailyAssessmentLanding = () => {
  const [content, setContent] = useState(null);
  
  useEffect(() => {
    fetch('/api/daily-assessment-content')
      .then(r => r.json())
      .then(data => setContent(data));
  }, []);

  if (!content) return <div>Loading...</div>;  // Google sees this
  return <h1>{content.title}</h1>;
};

// ✅ GOOD — Static content always renders immediately
const DailyAssessmentLanding = () => {
  const [quizData, setQuizData] = useState(null);

  useEffect(() => {
    fetch('/api/today-quiz').then(r => r.json()).then(setQuizData);
  }, []);

  return (
    <>
      {/* Static SEO content — always renders, no API dependency */}
      <h1>Daily UPSC & MPSC Assessment 2026 | Free Current Affairs Quiz</h1>
      <p>Solve 10 fresh questions every day for UPSC and MPSC preparation...</p>
      <HowItWorksSection />
      <StaticSampleQuestions />   {/* Hard-coded, not from API */}
      <FAQSection />
      <InternalLinksSection />
      
      {/* Dynamic content — renders after API responds */}
      {quizData ? (
        <LiveQuizSection data={quizData} />
      ) : (
        <QuizLoadingPlaceholder />
      )}
    </>
  );
};
```

- [ ] curl test shows H1 and title in raw HTML response
- [ ] Static content sections do NOT depend on API calls
- [ ] Page does not show blank/loading state in raw HTML

---

### ✅ FIX 4 — API Failure Must Not Remove SEO Content

**What**: If the quiz API (`/api/today-quiz` or similar) returns an error or timeout, the page must NOT collapse to show only an error message with no other content.

**Why**: Google's crawler may hit the page during an API outage. If only an error message is displayed, Google sees a near-empty page → Soft 404.

**The rule:** All static SEO content (H1, intro, how it works, sample questions, FAQs, internal links) must be hardcoded in the component and always render regardless of API state.

**Fix — Implement API error boundary:**

```jsx
const DailyAssessmentLanding = () => {
  const [quizData, setQuizData] = useState(null);
  const [apiError, setApiError] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 5000); // 5s timeout

    fetch('/api/today-quiz', { signal: controller.signal })
      .then(r => {
        if (!r.ok) throw new Error('API error');
        return r.json();
      })
      .then(data => {
        setQuizData(data);
        setLoading(false);
      })
      .catch(() => {
        setApiError(true);
        setLoading(false);
      })
      .finally(() => clearTimeout(timeout));

    return () => controller.abort();
  }, []);

  return (
    <main>
      {/* ✅ Always renders — static SEO content */}
      <section id="hero">
        <h1>Daily UPSC & MPSC Assessment 2026 | Free Current Affairs Quiz & Government Exam Practice Questions</h1>
        <p>Solve 10 fresh questions every day for UPSC and MPSC preparation. Each assessment combines recent current affairs with syllabus-based practice.</p>
      </section>

      <section id="how-it-works">
        <h2>How the Daily UPSC & MPSC Quiz Works</h2>
        {/* 5-step workflow content */}
      </section>

      <section id="sample-questions">
        <h2>Today's Assessment Preview: Sample Questions & Explanations</h2>
        {/* Static sample questions — hardcoded, not from API */}
        <StaticSampleQuestionsComponent />
      </section>

      {/* ✅ Dynamic section — gracefully handles API errors */}
      <section id="live-quiz">
        <h2>Start Today's Assessment</h2>
        {loading && <div>Loading today's questions...</div>}
        {apiError && (
          <div className="quiz-unavailable">
            <p>Today's quiz is temporarily unavailable. Please try again in a few minutes.</p>
            <p>In the meantime, practice with the sample questions above or explore our <a href="/quiz">Quiz Archive</a>.</p>
          </div>
        )}
        {quizData && <LiveQuizComponent data={quizData} />}
      </section>

      {/* ✅ Always renders — FAQs and internal links */}
      <section id="faq">
        <h2>Frequently Asked Questions About Daily Assessment</h2>
        <FAQComponent />
      </section>

      <section id="related-resources">
        <h2>Explore Supporting Study Resources</h2>
        <RelatedLinksComponent />
      </section>
    </main>
  );
};
```

- [ ] API failure shows helpful message, not blank page
- [ ] Static content (H1, intro, sample questions, FAQs) renders without API
- [ ] Added fetch timeout to prevent indefinite loading state

---

## ──────────────────────────────────────────────────
## PHASE 2 — HIGH PRIORITY FIXES (This Week)
## ──────────────────────────────────────────────────

---

### ✅ FIX 5 — Update `sitemap-static.xml` for `/daily-assessment`

**What**: The `/daily-assessment` entry in `sitemap-static.xml` is missing `<lastmod>` and uses incorrect `<changefreq>` for a daily-updated page.

**Current (line 50–53 of sitemap-static.xml):**

```xml
<url>
  <loc>https://www.searchsarkarinaukri.com/daily-assessment</loc>
  <changefreq>weekly</changefreq>
  <priority>0.8</priority>
</url>
```

**Fix — Replace with:**

```xml
<url>
  <loc>https://www.searchsarkarinaukri.com/daily-assessment</loc>
  <lastmod>2026-09-21</lastmod>
  <changefreq>daily</changefreq>
  <priority>0.9</priority>
</url>
```

**Why `lastmod` matters**: Google uses `<lastmod>` to prioritize recrawling recently updated pages. After the Soft 404 fix and content improvements, setting `lastmod` to today signals to Googlebot that this page is fresh and should be recrawled.

**Why `changefreq=daily`**: Quiz content changes every day. `weekly` undersells the update frequency and may slow recrawl rate.

**Why `priority=0.9`**: This is a core tool page alongside `/current-affairs` and `/quiz`. It should have the same priority tier as those pages, not a lower tier.

**After updating sitemap — Resubmit via Google Search Console:**

```
Google Search Console → Indexing → Sitemaps → [Your Sitemap URL] → Resubmit
```

- [ ] `<lastmod>` added with today's date
- [ ] `<changefreq>` changed from `weekly` to `daily`
- [ ] `<priority>` updated from `0.8` to `0.9`
- [ ] Sitemap resubmitted in Google Search Console

---

### ✅ FIX 6 — Align the Page Title (Two Versions Found)

**What**: Two different page titles exist in the project documentation:

| Source File | Title |
|:---|:---|
| `00_meta-and-schema.md` | `Daily UPSC & MPSC Quiz – Current Affairs & Practice Questions` |
| `Sample-daily-assessment.html` | `Daily UPSC & MPSC Assessment 2026 \| Free Current Affairs Quiz & Government Exam Practice Questions` |

**Fix — Use the Sample HTML version** (it is more descriptive, includes the year, and includes "Free"):

```
Daily UPSC & MPSC Assessment 2026 | Free Current Affairs Quiz & Government Exam Practice Questions
```

**Update in `00_meta-and-schema.md` — Section "Page Title":**

```markdown
## Page Title
Daily UPSC & MPSC Assessment 2026 | Free Current Affairs Quiz & Government Exam Practice Questions
```

**Update in your React component:**

```jsx
<Helmet>
  <title>Daily UPSC & MPSC Assessment 2026 | Free Current Affairs Quiz & Government Exam Practice Questions</title>
</Helmet>
```

- [ ] `00_meta-and-schema.md` title updated to match Sample HTML
- [ ] React component `<title>` verified to use the agreed final version

---

### ✅ FIX 7 — Remove `<meta name="keywords">` from React Code

**What**: `Sample-daily-assessment.html` still has a keywords meta tag. Your own documentation (`00_meta-and-schema.md`) correctly says to remove it.

**Why**: Google has not used the keywords meta tag since 2009. It adds no ranking value and contradicts your internal SEO documentation.

**Find and remove in your React component:**

```jsx
// ❌ REMOVE THIS — no SEO value
<meta name="keywords" content="daily upsc quiz, daily mpsc quiz, upsc daily assessment..." />
```

**Search for it across the codebase:**

```bash
# Run from project root
grep -r "meta name=\"keywords\"" src/
grep -r "keywords" src/ --include="*.jsx" --include="*.tsx"
```

- [ ] Searched for keywords meta across all src files
- [ ] Removed from `/daily-assessment` component
- [ ] Checked other page components for the same issue

---

### ✅ FIX 8 — Remove `Quiz` Schema from Landing Page

**What**: `Sample-daily-assessment.html` includes a `Quiz` schema block on the main landing page. Your own `00_meta-and-schema.md` correctly says this schema should only be on dated archive URLs (`/daily-assessment/upsc/YYYY-MM-DD`), not on the main landing page.

**Fix — In the landing page JSON-LD, remove the Quiz block:**

```jsx
// ❌ REMOVE from landing page JSON-LD:
{
  "@type": "Quiz",
  "name": "Daily UPSC & MPSC Assessment",
  "about": { "@type": "Thing", "name": "..." },
  "educationalLevel": "Competitive Government Exam",
  "provider": { "@id": "https://www.searchsarkarinaukri.com/#organization" }
}
```

**Landing page `/daily-assessment` should only have this @graph:**

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://www.searchsarkarinaukri.com/#organization",
      "name": "Search Sarkari Naukri",
      "url": "https://www.searchsarkarinaukri.com/",
      "logo": "https://www.searchsarkarinaukri.com/logo.png",
      "sameAs": [
        "https://whatsapp.com/channel/0029Vb8nq6A7z4kjcV0R5K29",
        "https://t.me/searchsarkarinaukri"
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://www.searchsarkarinaukri.com/#website",
      "url": "https://www.searchsarkarinaukri.com/",
      "name": "Search Sarkari Naukri",
      "publisher": { "@id": "https://www.searchsarkarinaukri.com/#organization" }
    },
    {
      "@type": "WebPage",
      "@id": "https://www.searchsarkarinaukri.com/daily-assessment#webpage",
      "url": "https://www.searchsarkarinaukri.com/daily-assessment",
      "name": "Daily UPSC & MPSC Assessment 2026 | Free Current Affairs Quiz & Government Exam Practice Questions",
      "description": "Solve 10 new UPSC, MPSC, SSC, Railway & Banking questions every day. Free daily current affairs quiz and syllabus-based practice test with instant score, explanations and progress dashboard.",
      "isPartOf": { "@id": "https://www.searchsarkarinaukri.com/#website" },
      "about": { "@id": "https://www.searchsarkarinaukri.com/#organization" },
      "inLanguage": "en-IN"
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://www.searchsarkarinaukri.com/daily-assessment#breadcrumb",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.searchsarkarinaukri.com/" },
        { "@type": "ListItem", "position": 2, "name": "Daily Assessment", "item": "https://www.searchsarkarinaukri.com/daily-assessment" }
      ]
    }
  ]
}
```

**Add `Quiz` schema ONLY on dated archive pages** (`/daily-assessment/upsc/2026-09-10` etc.) where full questions and visible answers appear in DOM:

```json
{
  "@type": "Quiz",
  "name": "UPSC Daily Quiz – 10 September 2026",
  "about": { "@type": "Thing", "name": "UPSC Civil Services General Studies" },
  "educationalLevel": "Competitive Government Exam",
  "provider": { "@id": "https://www.searchsarkarinaukri.com/#organization" },
  "url": "https://www.searchsarkarinaukri.com/daily-assessment/upsc/2026-09-10"
}
```

**Validate schema after change:**

```
https://search.google.com/test/rich-results
URL: https://www.searchsarkarinaukri.com/daily-assessment
```

- [ ] `Quiz` schema removed from landing page JSON-LD
- [ ] `BreadcrumbList` schema remains (it's working — 1 valid item detected by Google)
- [ ] Validated schema via Rich Results Test
- [ ] `Quiz` schema added to dated archive URLs

---

### ✅ FIX 9 — Add `noindex` Meta to All Auth/Utility Routes

**What**: While `/login`, `/register`, `/dashboard` etc. are already in `robots.txt` Disallow, they do NOT have `<meta name="robots" content="noindex">` in their HTML. These are two separate signals.

**Why**: `robots.txt Disallow` prevents crawling. `noindex` meta prevents indexing. Google needs to crawl a page to read its `noindex` directive. If Google finds a link to `/login` from an external site (that isn't blocked by robots.txt), it could still index it. Best practice is to use both signals together.

**Fix — Add to each auth/utility route component:**

```jsx
// LoginPage.jsx
<Helmet>
  <title>Login – Search Sarkari Naukri</title>
  <meta name="robots" content="noindex, nofollow" />
</Helmet>

// RegisterPage.jsx
<Helmet>
  <title>Create Account – Search Sarkari Naukri</title>
  <meta name="robots" content="noindex, nofollow" />
</Helmet>

// DashboardPage.jsx
<Helmet>
  <title>Dashboard – Search Sarkari Naukri</title>
  <meta name="robots" content="noindex, nofollow" />
</Helmet>

// ProfileSetupPage.jsx
<Helmet>
  <meta name="robots" content="noindex, nofollow" />
</Helmet>

// AssessmentApp.jsx (authenticated quiz)
<Helmet>
  <meta name="robots" content="noindex, nofollow" />
</Helmet>

// SavedJobsPage.jsx
<Helmet>
  <meta name="robots" content="noindex, nofollow" />
</Helmet>

// PreferencesPage.jsx
<Helmet>
  <meta name="robots" content="noindex, nofollow" />
</Helmet>
```

**Quick search to find all auth-gated components:**

```bash
grep -r "ProtectedRoute\|isAuthenticated\|requireAuth\|AuthGuard" src/ --include="*.jsx" --include="*.tsx" -l
```

Each file found should have `noindex, nofollow` in its Helmet/head.

- [ ] `/assessment` component has `noindex, nofollow`
- [ ] `/login` component has `noindex, nofollow`
- [ ] `/register` component has `noindex, nofollow`
- [ ] `/dashboard` component has `noindex, nofollow`
- [ ] `/profile-setup` component has `noindex, nofollow`
- [ ] `/preferences` component has `noindex, nofollow`
- [ ] `/saved-jobs` component has `noindex, nofollow`
- [ ] `/my-saved-jobs` component has `noindex, nofollow`
- [ ] `/reminders` component has `noindex, nofollow`
- [ ] Any other protected route has `noindex, nofollow`

---

## ──────────────────────────────────────────────────
## PHASE 3 — MEDIUM PRIORITY (Within 2 Weeks)
## ──────────────────────────────────────────────────

---

### ✅ FIX 10 — Add Inbound Links from Related Pages to `/daily-assessment`

**What**: Google Search Console previously showed "Referring page: None detected" for `/daily-assessment`. While the homepage now links to it, more contextual inbound links from relevant pages are needed.

**Why**: Internal links pass PageRank (link equity) and help Google understand the page's importance in the site architecture.

**Pages that should link to `/daily-assessment`:**

#### `/current-affairs` page — Add:
```html
<a href="/daily-assessment">Test your knowledge with today's Daily Assessment →</a>
```
or as a card:
```html
<div class="cta-card">
  <h3>Put Your Knowledge to the Test</h3>
  <p>Solve 10 UPSC & MPSC questions based on today's current affairs.</p>
  <a href="/daily-assessment">Start Daily Assessment →</a>
</div>
```

#### `/quiz` page — Add:
```html
<p>For exam-focused daily MCQs with UPSC/MPSC syllabus coverage, try the 
  <a href="/daily-assessment">Daily Assessment</a> — 10 questions with explanations.
</p>
```

#### `/exams/upsc-cse` page — Add:
```html
<p>Practice daily with the <a href="/daily-assessment">UPSC Daily Assessment</a> — 
10 current affairs and syllabus-based MCQs with explanations every day.</p>
```

#### `/exams/mpsc-rajyaseva` page — Add:
```html
<p>Strengthen your preparation with the <a href="/daily-assessment">MPSC Daily Assessment</a> — 
10 questions including Maharashtra-specific GK every day.</p>
```

#### `/digital-library` page — Add:
```html
<p>Complement your study materials with the <a href="/daily-assessment">Daily Assessment</a> — 
test your recall on what you've studied.</p>
```

#### Blog articles about UPSC/MPSC preparation — Add inline links:
Any blog post about UPSC or MPSC preparation should contain at least one contextual link to `/daily-assessment`.

- [ ] `/current-affairs` page links to `/daily-assessment`
- [ ] `/quiz` page links to `/daily-assessment`
- [ ] `/exams/upsc-cse` page links to `/daily-assessment`
- [ ] `/exams/mpsc-rajyaseva` page links to `/daily-assessment`
- [ ] At least 2 blog articles link to `/daily-assessment`

---

### ✅ FIX 11 — Audit All 13 Child Sitemaps for Auth URL Contamination

**What**: The sitemap index has 13 child sitemaps. Auth/private URLs must not appear in any of them.

**Check each sitemap:**

```bash
# Check each sitemap for private/auth routes
curl -s https://www.searchsarkarinaukri.com/sitemap-static.xml | grep -E "assessment|login|register|dashboard|profile|saved-jobs|preferences|reminders|admin"

curl -s https://www.searchsarkarinaukri.com/sitemap-exams.xml | grep -E "assessment|login|dashboard"

curl -s https://www.searchsarkarinaukri.com/sitemap-jobs.xml | grep -E "assessment|login|dashboard|saved"

curl -s https://www.searchsarkarinaukri.com/sitemap-blogs.xml | grep -E "assessment|login|dashboard"

# Repeat for remaining sitemaps:
# sitemap-locations.xml, sitemap-qualifications.xml, sitemap-departments.xml
# sitemap-cross-filter.xml, sitemap-news.xml, sitemap-images.xml
# sitemap-results.xml, sitemap-admit-cards.xml, sitemap-districts.xml
```

**URLs that must NOT appear in any sitemap:**

```
/assessment
/login
/register
/dashboard
/saved-jobs
/my-saved-jobs
/profile-setup
/preferences
/reminders
/admin/
/api/
Any URL with ?utm_
Any URL with ?search=
Any URL with ?q=
Any URL with ?category=
```

- [ ] `sitemap-static.xml` checked — no auth URLs
- [ ] `sitemap-exams.xml` checked — no auth URLs
- [ ] `sitemap-jobs.xml` checked — no auth URLs
- [ ] `sitemap-locations.xml` checked — no auth URLs
- [ ] `sitemap-qualifications.xml` checked — no auth URLs
- [ ] `sitemap-departments.xml` checked — no auth URLs
- [ ] `sitemap-cross-filter.xml` checked — no filter/query URLs
- [ ] `sitemap-news.xml` checked — no auth URLs
- [ ] `sitemap-blogs.xml` checked — no auth URLs
- [ ] `sitemap-images.xml` checked — no auth image references
- [ ] `sitemap-results.xml` checked — results pages are public, not private
- [ ] `sitemap-admit-cards.xml` checked — admit card pages are public
- [ ] `sitemap-districts.xml` checked — district pages are public

---

### ✅ FIX 12 — Strengthen the `/quiz` Page Content Depth

**What**: The `/quiz` page currently has very thin crawlable content (~17 lines). It faces the same Soft 404 risk that `/daily-assessment` had.

**Why**: If Google visits `/quiz` and finds minimal content, it may classify it as a Soft 404, harming the crawl quality across the site.

**Fix**: Apply the same content strategy used for `/daily-assessment` to `/quiz`:
- Strong H1 distinct from `/daily-assessment`
- Explanatory intro paragraph
- How it works section
- Sample quiz questions (static, not API-dependent)
- Subject coverage section
- FAQs
- Internal links

**Suggested H1 for `/quiz`:**
```
Daily Current Affairs Quiz 2026 – Topic-wise MCQs for Government Exams
```

This is differentiated from `/daily-assessment`'s:
```
Daily UPSC & MPSC Assessment 2026 | Free Current Affairs Quiz & Government Exam Practice Questions
```

- [ ] `/quiz` page content audited for depth
- [ ] Static content added to `/quiz` page (not API-dependent)
- [ ] `/quiz` H1 is distinct from `/daily-assessment` H1
- [ ] `/quiz` title and meta description are distinct

---

### ✅ FIX 13 — Add `Quiz` Schema to Dated Archive Pages

**What**: The daily archive section (`15_daily-archive.md`) links to dated quiz pages (`/daily-assessment/upsc/2026-09-10` etc.). These pages — when they exist and contain full questions and answers — are the correct place for `Quiz` structured data.

**Fix — Add to each dated quiz page component:**

```json
{
  "@context": "https://schema.org",
  "@type": "Quiz",
  "name": "UPSC Daily Quiz – 10 September 2026",
  "description": "10 UPSC Civil Services MCQs covering INSTC Corridors, Monetary Policy (SDF), Article 324, and Himalayan Rivers from 10 September 2026.",
  "about": {
    "@type": "Thing",
    "name": "UPSC Civil Services General Studies"
  },
  "educationalLevel": "Competitive Government Exam",
  "provider": {
    "@type": "Organization",
    "@id": "https://www.searchsarkarinaukri.com/#organization"
  },
  "url": "https://www.searchsarkarinaukri.com/daily-assessment/upsc/2026-09-10",
  "datePublished": "2026-09-10",
  "inLanguage": "en-IN"
}
```

**Also add `BreadcrumbList` to dated pages:**

```json
{
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.searchsarkarinaukri.com/" },
    { "@type": "ListItem", "position": 2, "name": "Daily Assessment", "item": "https://www.searchsarkarinaukri.com/daily-assessment" },
    { "@type": "ListItem", "position": 3, "name": "UPSC Daily Quiz – 10 September 2026", "item": "https://www.searchsarkarinaukri.com/daily-assessment/upsc/2026-09-10" }
  ]
}
```

- [ ] Quiz schema template created for dated archive pages
- [ ] BreadcrumbList (3 levels) added to dated archive pages
- [ ] Dated archive pages have unique title/description per date
- [ ] Dated archive pages added to sitemap (if they have real content)

---

## ──────────────────────────────────────────────────
## PHASE 4 — MONITORING & ONGOING
## ──────────────────────────────────────────────────

---

### ✅ MONITOR 1 — Google Search Console: Sitemaps Report

```
Google Search Console → Indexing → Sitemaps
```

Check that your submitted sitemap shows:

| Field | Expected Value |
|:---|:---|
| Status | ✅ Success |
| Last read | Within last 48 hours |
| Discovered URLs | > 0 |

If status shows "Couldn't fetch":
1. Verify `https://www.searchsarkarinaukri.com/sitemap.xml` loads in browser
2. Verify it is not blocked by `robots.txt` (currently it is NOT blocked — good)
3. Resubmit via Search Console

- [ ] Sitemap status = Success in Search Console
- [ ] Sitemap was resubmitted after `sitemap-static.xml` update (FIX 5)

---

### ✅ MONITOR 2 — Page Indexing Report for `/daily-assessment`

```
Google Search Console → Indexing → Pages → Filter by "Not indexed"
```

Watch for `/daily-assessment` to move from:
```
❌ Not indexed: Soft 404
→
✅ Indexed (appears in "All submitted pages")
```

This typically happens 1–4 weeks after the improved page is recrawled. **Do not submit Request Indexing more than once.** You have already submitted it.

- [ ] Checked Page Indexing report — status watched
- [ ] /daily-assessment moved to indexed (note date: ________)

---

### ✅ MONITOR 3 — Search Performance Report

```
Google Search Console → Performance → Search results
Filter: Page = /daily-assessment
```

Once indexed, you should start seeing:
- **Impressions**: How many times the page appeared in search results
- **Clicks**: How many users clicked through
- **Average Position**: Where the page ranks for relevant queries

Target queries to track:
```
daily upsc quiz
daily mpsc quiz
upsc daily assessment
mpsc daily quiz
current affairs quiz upsc
daily quiz for government exams
```

- [ ] Performance report monitored weekly after indexing confirmed

---

### ✅ MONITOR 4 — Coverage Report Check

```
Google Search Console → Indexing → Pages
```

Check these categories:

| Category | Expected |
|:---|:---|
| Indexed | `/daily-assessment` should appear here |
| Not indexed: Soft 404 | Should be empty or decreasing |
| Not indexed: Crawled – currently not indexed | Watch and investigate any pages here |
| Not indexed: Excluded by noindex | `/login`, `/register`, `/assessment`, `/dashboard` should appear here |

- [ ] Coverage report monitored
- [ ] No unexpected pages in "Soft 404" category

---

## ──────────────────────────────────────────────────
## COMPLETE MASTER CHECKLIST — 45 POINTS
## ──────────────────────────────────────────────────

Copy this section and use as a standalone tracking checklist.

### 🔴 CRITICAL (Do Today)

- [ ] `1.` `noindex, nofollow` meta added to `/assessment` React route component
- [ ] `2.` `Disallow: /assessment` added to `robots.txt`
- [ ] `3.` Unknown URL returns true HTTP 404 (tested with curl)
- [ ] `4.` View Source of `/daily-assessment` shows H1 and content (SSR confirmed)
- [ ] `5.` API failure shows helpful fallback message, not blank/error page
- [ ] `6.` Static SEO content (H1, intro, sample Qs, FAQs) renders without API call

### 🟡 HIGH PRIORITY (This Week)

- [ ] `7.` `<lastmod>2026-09-21</lastmod>` added to `/daily-assessment` in `sitemap-static.xml`
- [ ] `8.` `<changefreq>` updated from `weekly` → `daily` in sitemap for `/daily-assessment`
- [ ] `9.` `<priority>` updated from `0.8` → `0.9` in sitemap for `/daily-assessment`
- [ ] `10.` Sitemap resubmitted in Google Search Console after sitemap update
- [ ] `11.` `/assessment` absent from all 13 child sitemaps (verified)
- [ ] `12.` `<meta name="keywords">` removed from live React `/daily-assessment` component
- [ ] `13.` `Quiz` schema block removed from `/daily-assessment` landing page JSON-LD
- [ ] `14.` Page title aligned — use: `Daily UPSC & MPSC Assessment 2026 | Free Current Affairs Quiz & Government Exam Practice Questions`
- [ ] `15.` `00_meta-and-schema.md` updated with final agreed title

### 🟠 AUTH ROUTE HARDENING (This Week)

- [ ] `16.` `/login` component has `<meta name="robots" content="noindex, nofollow">`
- [ ] `17.` `/register` component has `<meta name="robots" content="noindex, nofollow">`
- [ ] `18.` `/dashboard` component has `<meta name="robots" content="noindex, nofollow">`
- [ ] `19.` `/profile-setup` component has `<meta name="robots" content="noindex, nofollow">`
- [ ] `20.` `/preferences` component has `<meta name="robots" content="noindex, nofollow">`
- [ ] `21.` `/reminders` component has `<meta name="robots" content="noindex, nofollow">`
- [ ] `22.` `/saved-jobs` component has `<meta name="robots" content="noindex, nofollow">`
- [ ] `23.` `/my-saved-jobs` component has `<meta name="robots" content="noindex, nofollow">`
- [ ] Any other ProtectedRoute component has `noindex, nofollow`

### 🟢 MEDIUM PRIORITY (Within 2 Weeks)

- [ ] `24.` `/current-affairs` page links to `/daily-assessment` with contextual anchor text
- [ ] `25.` `/quiz` page links to `/daily-assessment`
- [ ] `26.` `/exams/upsc-cse` page links to `/daily-assessment`
- [ ] `27.` `/exams/mpsc-rajyaseva` page links to `/daily-assessment`
- [ ] `28.` At least 2 blog articles link to `/daily-assessment` contextually
- [ ] `29.` All 13 child sitemaps verified — no auth/private URLs present
- [ ] `30.` `/quiz` page content depth improved (avoid Soft 404 risk)
- [ ] `31.` `/quiz` H1 and title are distinct from `/daily-assessment`
- [ ] `32.` `Quiz` schema added to dated archive pages (`/daily-assessment/upsc/YYYY-MM-DD`)
- [ ] `33.` BreadcrumbList (3-level) added to dated archive pages
- [ ] `34.` Dated archive pages added to sitemap if they have real content
- [ ] `35.` `/current-affairs` freshness reviewed — March 2026 content archived/separated

### 🔵 SCHEMA & STRUCTURED DATA

- [ ] `36.` BreadcrumbList on `/daily-assessment` confirmed working (GSC shows "1 valid item") ✅ Already passing
- [ ] `37.` Organization schema on `/daily-assessment` — confirmed correct `@id` and `sameAs`
- [ ] `38.` WebPage schema `name` field matches final agreed page title
- [ ] `39.` Rich Results Test run: `https://search.google.com/test/rich-results` for `/daily-assessment`
- [ ] `40.` No duplicate schemas across pages (SearchAction only on homepage)

### 🟣 MONITORING (Ongoing)

- [ ] `41.` GSC Sitemaps report shows "Success" for submitted sitemap
- [ ] `42.` GSC Page Indexing report watched — `/daily-assessment` moves to "Indexed"
- [ ] `43.` GSC Performance report monitored for clicks/impressions on `/daily-assessment`
- [ ] `44.` GSC Coverage report checked — no unexpected Soft 404s site-wide
- [ ] `45.` robots.txt periodically reviewed as new routes are added to the React app

---

## FINAL STATUS SUMMARY

| Area | Status Before Fixes | Status After All Fixes |
|:---|:---|:---|
| /daily-assessment accessible | ✅ | ✅ |
| /daily-assessment in sitemap | ✅ (but missing lastmod) | ✅ Complete |
| Google Live Test | ✅ URL available | ✅ |
| Soft 404 (historical 19 Sep crawl) | ❌ | ⏳ Clears on next recrawl |
| /assessment noindex | ❌ Missing | ✅ After Fix 1 |
| True HTTP 404 | ⚠️ Unknown | ✅ After Fix 2 |
| SSR / pre-render confirmed | ⚠️ Unknown | ✅ After Fix 3 |
| API failure fallback | ⚠️ Unknown | ✅ After Fix 4 |
| Sitemap lastmod + changefreq | ❌ Missing | ✅ After Fix 5 |
| Page title consistency | ⚠️ 2 versions | ✅ After Fix 6 |
| Keywords meta removed | ❌ Still present in HTML | ✅ After Fix 7 |
| Quiz schema removed from landing | ❌ Still in HTML | ✅ After Fix 8 |
| Auth routes noindex | ⚠️ Partial | ✅ After Fix 9 |
| Inbound links | ⚠️ Homepage only | ✅ After Fix 10 |
| /quiz content depth | ⚠️ Thin | ✅ After Fix 12 |
| Dated archive schema | ⚠️ Missing | ✅ After Fix 13 |

---

*File: `16_DEVELOPER_AUDIT_CHECKLIST.md`*
*Folder: `.agents/07_OnPage_SEO/02_Daily_Assessment/`*
*Last Updated: 21 September 2026*
*Total Fixes: 13 | Total Checklist Items: 45*
