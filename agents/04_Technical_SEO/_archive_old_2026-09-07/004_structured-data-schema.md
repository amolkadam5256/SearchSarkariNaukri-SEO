# 4. Structured Data (JobPosting Schema)

**Priority: 🟠 Medium**

## The problem
Search Console detected 3 valid JobPosting items but flagged 4
"improve item appearance" issues (each affecting all 3 items):
- Missing field `streetAddress` (in `jobLocation.address`)
- Missing field `postalCode` (in `jobLocation.address`)
- Invalid enum value in field `credentialCategory` (in `educationRequirements`)
- Missing field `baseSalary`

These don't break the rich result, but Google downgrades the listing's
eligibility for enhanced job-search features without them.

## The fix — corrected JSON-LD template
Add/update this block (server-rendered — see file 01, not injected only
by client-side JS) on every job posting page:

```json
{
  "@context": "https://schema.org/",
  "@type": "JobPosting",
  "title": "Trade Apprentice – Data Entry Operator",
  "description": "<full job description, HTML allowed>",
  "identifier": {
    "@type": "PropertyValue",
    "name": "Indian Oil Corporation Limited",
    "value": "IOCL-2026-DEO-001"
  },
  "datePosted": "2026-08-01",
  "validThrough": "2026-08-31T23:59:59+05:30",
  "employmentType": "OTHER",
  "hiringOrganization": {
    "@type": "Organization",
    "name": "Indian Oil Corporation Limited",
    "sameAs": "https://iocl.com",
    "logo": "https://www.searchsarkarinaukri.com/logos/iocl.png"
  },
  "jobLocation": {
    "@type": "Place",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Panipat Refinery & Petrochemical Complex",
      "addressLocality": "Panipat",
      "addressRegion": "Haryana",
      "postalCode": "132140",
      "addressCountry": "IN"
    }
  },
  "baseSalary": {
    "@type": "MonetaryAmount",
    "currency": "INR",
    "value": {
      "@type": "QuantitativeValue",
      "value": 25000,
      "unitText": "MONTH"
    }
  },
  "educationRequirements": {
    "@type": "EducationalOccupationalCredential",
    "credentialCategory": "highschool"
  }
}
```

### Field-by-field fix notes
- **`streetAddress` / `postalCode`** — you likely already store a city or
  district per posting. Where you don't have a precise street address
  (common for government postings that just say "at the regional office"),
  use the organisation's known official address for that location, or at
  minimum the district office address — Google requires the field to be
  present and non-empty, even if approximate.
- **`baseSalary`** — many government postings publish a pay scale/pay band
  rather than a single figure. Use the minimum of the published pay
  scale/level as `value`, or a `MonetaryAmountDistribution`-style range if
  your data model supports it:
  ```json
  "baseSalary": {
    "@type": "MonetaryAmount",
    "currency": "INR",
    "value": {
      "@type": "QuantitativeValue",
      "minValue": 21700,
      "maxValue": 69100,
      "unitText": "MONTH"
    }
  }
  ```
  If a posting genuinely has no published salary, it's better to omit the
  whole `baseSalary` block than to send a guessed/incorrect value —
  omitting loses the enhancement but avoids a data-quality penalty;
  guessing risks manual action for misleading structured data.
- **`credentialCategory`** — must be one of Google's accepted enum values:
  `"high school"`, `"associate degree"`, `"bachelor degree"`,
  `"professional certificate"`, `"postgraduate degree"`. Whatever value
  is currently being sent (likely a free-text Indian qualification like
  "10th Pass" or "Graduate") needs mapping to the closest accepted value,
  e.g.:
  | Your current data | Correct schema.org value |
  |---|---|
  | 10th Pass / SSC | `high school` |
  | 12th Pass / HSC | `high school` |
  | Diploma/ITI | `associate degree` |
  | Graduate/Bachelor's | `bachelor degree` |
  | Post-graduate/Master's | `postgraduate degree` |

## Implementation checklist
- [ ] Update the JobPosting schema generator (backend template/component)
      to always emit `streetAddress`, `postalCode`, and a mapped
      `credentialCategory`.
- [ ] Add `baseSalary` wherever a pay scale is available in your job data;
      leave it out entirely when not available (don't fabricate).
- [ ] Re-test each fixed template with the [Rich Results
      Test](https://search.google.com/test/rich-results) before deploying
      site-wide.
- [ ] After deploy, check Search Console → Enhancements → Job Postings
      weekly — the 4 warning counts (currently "3" each) should drop to 0
      within a few crawl cycles.
- [ ] Also verify `datePosted` and `validThrough` are always present and
      accurate — Google removes/deprioritises job postings whose
      `validThrough` date has passed, so make sure this field updates
      automatically when a vacancy closes (ties into Fix 2 in file 03 —
      soft 404 handling for expired postings).
