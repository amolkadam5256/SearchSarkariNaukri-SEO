# 11 — DEVELOPER MASTER IMPLEMENTATION PROMPT

**Target Hub:** `https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030`  
**Alias Inbound Route:** `https://www.searchsarkarinaukri.com/jobs/dgft-recruitment-2026-notification-eligibility-vacancy-apply-online`  
**Implementation Priority:** P0 / P1 Engineering Sprint  
**Target Stack:** Next.js (App Router / Pages Router) + Tailwind / Vanilla CSS + PostgreSQL

---

## 1. Developer Hard Rules (Non-Negotiable)

1. **NO DELETE / PRESERVE ALL EXISTING CONTENT:**  
   Do NOT delete, overwrite, or hide the existing page, its URL slug, or its original core facts. Preserve:
   - Existing database ID and canonical slug: `dgft-dgft-2026--2030`.
   - Existing category navigation, exam links, calculator shortcuts, and footer.
   - Original reported vacancy count (`2`) and original closing date (`26 June 2026`).
2. **STRICT SERVER-SIDE RENDERING (SSR):**  
   All 16 component blocks, H1, headings, tables, bilingual copy, and the 12 FAQs must be rendered in the initial server HTML payload. Never load main content or FAQs via client-side `useEffect` or lazy client fetches.
3. **EXACT FLOW SEQUENCE:**  
   Implement the 16 master component blocks in the exact visual order defined in `05_PAGE_ARCHITECTURE_AND_COMPONENT_ORDER.md`.
4. **NO ACTIVE "APPLY NOW" BUTTON:**  
   Disable and remove any active `Apply Now` button. Render `Visit DGFT Official Website` and `Browse Active Government Jobs`.
5. **DO NOT INJECT `JobPosting` SCHEMA:**  
   Do not emit `JobPosting` structured data for this expired unverified listing. Emit safe `WebPage` and `BreadcrumbList` schema only.

---

## 2. Inbound URL Alias & Redirect Implementation

Configure the Next.js routing configuration (`next.config.js`) to handle inbound traffic from the user's requested URL:

```javascript
// next.config.js
module.exports = {
  async redirects() {
    return [
      {
        source: '/jobs/dgft-recruitment-2026-notification-eligibility-vacancy-apply-online',
        destination: '/jobs/dgft-dgft-2026--2030',
        permanent: true, // HTTP 301 Permanent Redirect
      },
    ];
  },
};
```

---

## 3. Server Component Architecture (`page.tsx` Implementation)

```tsx
// app/jobs/[slug]/page.tsx
import { Metadata } from 'next';
import { notFound } from 'next/navigation';
import { getJobBySlug, getActiveCentralJobs } from '@/lib/db/jobs';
import { JobBreadcrumb } from '@/components/jobs/JobBreadcrumb';
import { ClosedApplicationBanner } from '@/components/jobs/ClosedApplicationBanner';
import { JobQuickFactsTable } from '@/components/jobs/JobQuickFactsTable';
import { SourceVerificationPanel } from '@/components/jobs/SourceVerificationPanel';
import { DynamicRelatedJobsWidget } from '@/components/jobs/DynamicRelatedJobsWidget';
import { AccessibleFAQAccordion } from '@/components/jobs/AccessibleFAQAccordion';

interface PageProps {
  params: { slug: string };
}

// 1. Static & Dynamic Metadata Generation
export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  const job = await getJobBySlug(params.slug);
  if (!job) return {};

  return {
    title: 'DGFT Recruitment 2026: 2 Posts, Eligibility & Last Date',
    description: 'DGFT Recruitment 2026: Check details of 2 reported posts, eligibility guidance, original 26 June deadline and official DGFT verification. Applications closed.',
    alternates: {
      canonical: 'https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030',
    },
    robots: {
      index: true,
      follow: true,
      googleBot: {
        index: true,
        follow: true,
        'max-snippet': -1,
        'max-image-preview': 'large',
      },
    },
    openGraph: {
      type: 'article',
      url: 'https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030',
      title: 'DGFT Recruitment 2026 — 2 Posts | Applications Closed',
      description: 'Review the archived DGFT recruitment summary, original last date, verification guidance and links to currently active government vacancies.',
      locale: 'en_IN',
      images: [
        {
          url: 'https://www.searchsarkarinaukri.com/images/jobs/dgft-recruitment-2026-banner.webp',
          width: 1200,
          height: 630,
          alt: 'DGFT Recruitment 2026 Overview',
        },
      ],
    },
  };
}

// 2. Main Page Server Component
export default async function DgftJobPage({ params }: PageProps) {
  const job = await getJobBySlug(params.slug);
  if (!job) notFound();

  // Query 3-6 verified active central jobs for dynamic widget
  const activeCentralJobs = await getActiveCentralJobs({ limit: 6, excludeId: job.id });

  // Safe WebPage + BreadcrumbList JSON-LD
  const jsonLd = {
    '@context': 'https://schema.org',
    '@graph': [
      {
        '@type': 'WebPage',
        '@id': 'https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030#webpage',
        url: 'https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030',
        name: 'DGFT Recruitment 2026: 2 Posts, Eligibility & Last Date',
        description: 'Historical DGFT 2026 recruitment listing reporting 2 posts and an original application deadline of 26 June 2026. Applications closed.',
        inLanguage: ['en-IN', 'mr-IN'],
        breadcrumb: { '@id': 'https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030#breadcrumb' },
      },
      {
        '@type': 'BreadcrumbList',
        '@id': 'https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030#breadcrumb',
        itemListElement: [
          { '@type': 'ListItem', position: 1, name: 'Home', item: 'https://www.searchsarkarinaukri.com/' },
          { '@type': 'ListItem', position: 2, name: 'Government Jobs', item: 'https://www.searchsarkarinaukri.com/jobs' },
          { '@type': 'ListItem', position: 3, name: 'DGFT Recruitment 2026', item: 'https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030' },
        ],
      },
    ],
  };

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
      />
      <main className="job-page-container max-w-5xl mx-auto px-4 py-8">
        {/* 1. Breadcrumbs */}
        <JobBreadcrumb
          items={[
            { label: 'Home', href: '/' },
            { label: 'Government Jobs', href: '/jobs' },
            { label: 'DGFT Recruitment 2026', href: '/jobs/dgft-dgft-2026--2030' },
          ]}
        />

        {/* 2. Hero Header & Closed Banner */}
        <header className="job-hero my-6">
          <h1 className="text-3xl md:text-4xl font-extrabold text-gray-900 leading-tight">
            DGFT Recruitment 2026 (DGFT भरती २०२६) — 2 Posts, Eligibility, Last Date & Official Updates
          </h1>
          <ClosedApplicationBanner
            lastDate="26 June 2026"
            currentStatus="Closed / Expired as of 18 October 2026"
          />
        </header>

        {/* 3. Quick Answer */}
        <section id="overview" className="quick-answer-card p-6 bg-slate-50 border rounded-xl my-6">
          <h2 className="text-xl font-bold mb-3">DGFT Recruitment 2026 — Quick Answer</h2>
          <p className="text-gray-700 leading-relaxed">
            The Search Sarkari Naukri DGFT Recruitment 2026 listing records <strong>2 vacancies</strong> and a last application date of <strong>26 June 2026</strong>. That application date has passed as of 18 October 2026. The archived listing remains available for reference; it is <strong>not an invitation to submit a new application</strong>.
          </p>
        </section>

        {/* 4. Quick Facts Table */}
        <JobQuickFactsTable record={job} />

        {/* 5. Marathi Summary */}
        <section className="marathi-summary-card p-6 bg-amber-50 border border-amber-200 rounded-xl my-6">
          <h2 className="text-xl font-bold text-amber-950 mb-3">DGFT भरती २०२६ — महत्त्वाची माहिती (Marathi Summary)</h2>
          <p className="text-amber-900 leading-relaxed">
            परराष्ट्र व्यापार महासंचालनालय (DGFT) संदर्भात Search Sarkari Naukri वरील २०२६ च्या भरती नोंदीमध्ये २ जागा आणि अर्जाची अंतिम तारीख २६ जून २०२६ अशी माहिती नमूद आहे. ही अंतिम तारीख आता संपलेली आहे.
          </p>
        </section>

        {/* 6. Source Verification Panel */}
        <SourceVerificationPanel officialUrl="https://www.dgft.gov.in/" />

        {/* 7. Action Buttons (Informational Only - No Apply Now) */}
        <div className="action-buttons-wrapper flex flex-wrap gap-4 my-8">
          <a
            href="https://www.dgft.gov.in/"
            target="_blank"
            rel="noopener noreferrer"
            className="px-6 py-3 rounded-lg font-semibold bg-gray-800 text-white hover:bg-gray-700 transition"
          >
            Visit DGFT Official Website
          </a>
          <a
            href="https://www.searchsarkarinaukri.com/"
            className="px-6 py-3 rounded-lg font-semibold bg-blue-600 text-white hover:bg-blue-500 transition"
          >
            Browse Active Government Jobs
          </a>
        </div>

        {/* 8. Dynamic Related Jobs Widget */}
        <DynamicRelatedJobsWidget jobs={activeCentralJobs} />

        {/* 9. 12 Accessible FAQs */}
        <AccessibleFAQAccordion />
      </main>
    </>
  );
}
```

---

## 4. Acceptance Criteria for Deployment

1. HTTP response code for `/jobs/dgft-dgft-2026--2030` is **200 OK**.
2. HTTP response code for `/jobs/dgft-recruitment-2026-notification-eligibility-vacancy-apply-online` is **301 Redirect**.
3. Zero instances of `JobPosting` schema in DOM head.
4. Active "Apply Now" button is completely absent.
5. Google Rich Results Test passes with zero critical errors.
