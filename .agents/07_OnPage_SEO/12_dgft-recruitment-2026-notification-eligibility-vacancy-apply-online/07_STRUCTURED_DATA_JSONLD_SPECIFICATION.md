# 07 — STRUCTURED DATA & JSON-LD SPECIFICATION

**Target Canonical URL:** `https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030`  
**Structured Data Standard:** Schema.org via JSON-LD (`application/ld+json`)  
**Audit Date:** 18 October 2026 (IST)  
**Priority:** P0 Structured Data Integrity & Google Policy Compliance

---

## 1. Structured Data Policy: Current DGFT Page vs Verified Active Jobs

> ⚠️ **CRITICAL GOOGLE POLICY COMPLIANCE RULE:**  
> **DO NOT ENABLE `JobPosting` SCHEMA ON THIS DGFT PAGE AT PRESENT.**

### Why `JobPosting` Must Be Withheld on the Current Page:
1. **Google JobPosting Guidelines:** Google requires `JobPosting` structured data to represent an actual, single, actively hiring job opening with corroborated role specifics, verifiable compensation (if stated), and an official application pathway.
2. **Expired Status:** The application deadline for this listing was **26 June 2026**. Google Webmaster Guidelines strictly prohibit serving active `JobPosting` markup on expired listings without setting `validThrough` in the past, and actively penalize third-party aggregators that fabricate structured data.
3. **Unverified Role Specifics:** The reported 2 vacancies lack confirmed designations, salary scales, specific qualification clauses, and verified physical job locations. Inventing a dummy title (e.g. "Assistant") or dummy city to force a green check in a schema validator violates Google's Spam Policies.

### The Correct Implementation:
- Emit safe, compliant **`WebPage`** and **`BreadcrumbList`** structured data (Section 2 below).
- Use the production TypeScript engine (Section 3 below) **only** when a single, independently verified, active recruitment circular is published.

---

## 2. Safe Current Page JSON-LD (WebPage + BreadcrumbList)

Inject this exact JSON-LD block inside the `<head>` of `https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030`:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030#webpage",
      "url": "https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030",
      "name": "DGFT Recruitment 2026: 2 Posts, Eligibility & Last Date",
      "description": "Historical DGFT 2026 recruitment listing reporting 2 posts and an original application deadline of 26 June 2026. Applications closed.",
      "inLanguage": ["en-IN", "mr-IN"],
      "breadcrumb": {
        "@id": "https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030#breadcrumb"
      },
      "isPartOf": {
        "@type": "WebSite",
        "@id": "https://www.searchsarkarinaukri.com/#website",
        "url": "https://www.searchsarkarinaukri.com/",
        "name": "Search Sarkari Naukri",
        "publisher": {
          "@type": "Organization",
          "name": "Search Sarkari Naukri",
          "url": "https://www.searchsarkarinaukri.com/"
        }
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://www.searchsarkarinaukri.com/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Government Jobs",
          "item": "https://www.searchsarkarinaukri.com/jobs"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "DGFT Recruitment 2026",
          "item": "https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030"
        }
      ]
    }
  ]
}
</script>
```

---

## 3. Production TypeScript Engine for Verified Active JobPostings

The following TypeScript builder encapsulates all Google JobPosting guidelines. It is designed to be shared across all job pages, strictly returning `null` when a listing is unverified, expired, or represents multi-role aggregate figures:

```typescript
export type VerifiedJob = {
  canonicalUrl: string;
  jobId: string;
  title: string;                         // Specific designation, NOT an SEO keyword string
  descriptionHtml: string;              // Sanitized, complete HTML matching visible text
  datePosted: string;                   // Original employer publish date (ISO 8601)
  validThrough?: string;                // Real official closing date with timezone (ISO 8601)
  organizationName: string;
  organizationOfficialUrl?: string;
  organizationLogoUrl?: string;
  jobLocations?: Array<{
    locality?: string;
    region?: string;
    country: string;                    // "IN"
    postalCode?: string;
    streetAddress?: string;
  }>;
  employmentType?: 'FULL_TIME' | 'PART_TIME' | 'CONTRACTOR' | 'TEMPORARY' | 'INTERN';
  salary?: {
    min?: number;
    max?: number;
    value?: number;
    currency: string;                   // "INR"
    unitText: 'MONTH' | 'YEAR' | 'HOUR';
  };
  isRemote?: boolean;
  applicantLocationRequirements?: Array<{ type: string; name: string }>;
  directApply?: boolean;                // true ONLY if frictionless onsite apply exists
  isIndependentlyVerified: boolean;     // Primary verification flag
  singleSpecificJob: boolean;           // False if multi-post aggregate
  applicationOpen: boolean;             // False if past deadline
  officialNoticeUrl: string;            // Direct link to official recruitment PDF
};

export function buildJobPosting(job: VerifiedJob): Record<string, unknown> | null {
  // Strict Google Quality & Authenticity Guards
  if (!job.isIndependentlyVerified || !job.singleSpecificJob || !job.applicationOpen) {
    return null;
  }
  if (!job.title || !job.descriptionHtml || !job.datePosted || !job.organizationName || !job.officialNoticeUrl) {
    return null;
  }
  if (!job.isRemote && (!job.jobLocations || job.jobLocations.length === 0)) {
    return null; // Google requires Place address for non-remote roles
  }

  const schema: Record<string, unknown> = {
    '@context': 'https://schema.org',
    '@type': 'JobPosting',
    title: job.title,
    description: job.descriptionHtml,
    datePosted: job.datePosted,
    identifier: {
      '@type': 'PropertyValue',
      name: job.organizationName,
      value: job.jobId
    },
    hiringOrganization: {
      '@type': 'Organization',
      name: job.organizationName,
      ...(job.organizationOfficialUrl ? { sameAs: job.organizationOfficialUrl } : {}),
      ...(job.organizationLogoUrl ? { logo: job.organizationLogoUrl } : {})
    },
    ...(job.validThrough ? { validThrough: job.validThrough } : {}),
    ...(job.employmentType ? { employmentType: job.employmentType } : {}),
    ...(job.directApply === true ? { directApply: true } : {}),
    ...(job.jobLocations?.length ? {
      jobLocation: job.jobLocations.map(loc => ({
        '@type': 'Place',
        address: {
          '@type': 'PostalAddress',
          ...(loc.streetAddress ? { streetAddress: loc.streetAddress } : {}),
          ...(loc.locality ? { addressLocality: loc.locality } : {}),
          ...(loc.region ? { addressRegion: loc.region } : {}),
          ...(loc.postalCode ? { postalCode: loc.postalCode } : {}),
          addressCountry: loc.country
        }
      }))
    } : {}),
    ...(job.isRemote === true ? {
      jobLocationType: 'TELECOMMUTE',
      applicantLocationRequirements: job.applicantLocationRequirements?.map(req => ({
        '@type': req.type,
        name: req.name
      }))
    } : {}),
    ...(job.salary ? {
      baseSalary: {
        '@type': 'MonetaryAmount',
        currency: job.salary.currency,
        value: {
          '@type': 'QuantitativeValue',
          ...(job.salary.value != null ? { value: job.salary.value } : {}),
          ...(job.salary.min != null ? { minValue: job.salary.min } : {}),
          ...(job.salary.max != null ? { maxValue: job.salary.max } : {}),
          unitText: job.salary.unitText
        }
      }
    } : {})
  };

  return schema;
}
```

---

## 4. Production Engineering Adjustments & Rules

1. **Employer-Supplied Pay Only:**  
   Google limits `baseSalary` eligibility to figures directly authorized or published by the employer. Third-party aggregators should **normally omit `baseSalary`** unless quoting the official circular word-for-word. Never infer salary from 7th CPC matrices.
2. **`directApply` Integrity:**  
   `directApply: true` is allowed ONLY when the candidate can complete and submit the application in 2-3 clicks without navigating multiple landing pages. Linking to `dgft.gov.in` does NOT qualify.
3. **No Duplicate Schema Nodes:**  
   Ensure that SEO plugins (such as Yoast, RankMath, or custom Next.js layout heads) do not inject a conflicting secondary `JobPosting` or `BreadcrumbList` node. Validate output via Google Rich Results Test.
4. **FAQPage Schema Reality Check:**  
   Google's August 2023 update restricted FAQ rich snippets to authoritative government and healthcare websites. Third-party portals will not receive FAQ accordion snippets in SERPs. Do not rely on FAQPage schema for organic click growth; keep visible FAQs for AEO and user clarity.
