# 09 — DATA MODEL & DATABASE SCHEMA SPECIFICATION

**Target Canonical URL:** `https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030`  
**Data Architecture:** PostgreSQL / Prisma / TypeScript ORM Layer  
**Audit Date:** 18 October 2026 (IST)  
**Priority:** P1 Backend Data Architecture & Source Provenance

---

## 1. Master TypeScript Type Definition: `RecruitmentRecord`

To eliminate data ambiguity, prevent synthetic schema errors, and track field-by-field verification sources, all recruitment records in SearchSarkariNaukri must adhere to this unified TypeScript interface:

```typescript
export interface RecruitmentRecord {
  id: string;                                // e.g. "dgft-dgft-2026--2030"
  slug: string;                              // e.g. "dgft-dgft-2026--2030"
  canonicalUrl: string;                      // Full canonical URL
  pageStatus: 'OPEN' | 'CLOSED' | 'CANCELLED' | 'UNKNOWN';
  
  // Display Titles
  titleDisplayMr: string;                    // e.g. "२ पदांकरिता DGFT भरती अपडेट २०२६ — DGFT"
  titleDisplayEn?: string;                   // e.g. "DGFT Recruitment 2026: 2 Posts, Eligibility & Last Date"
  
  // Employer & Authority
  employerName: string;                      // "Directorate General of Foreign Trade (DGFT)"
  employerOfficialUrl: string;               // "https://www.dgft.gov.in/"
  
  // Primary Notification Metadata
  notificationPdfUrl?: string;               // Direct link to official PDF circular
  notificationNumber?: string;               // e.g. "01/2026/DGFT/HR"
  notificationDate?: string;                 // Date on circular (ISO 8601)
  employerDatePosted?: string;               // Initial publishing date (ISO 8601)
  
  // Timeline & Application Window
  applicationStartDate?: string;             // ISO 8601
  applicationEndDate?: string;               // ISO 8601 (e.g. "2026-06-26")
  deadlineTimeZone?: string;                 // "Asia/Kolkata" (IST)
  deadlineExtensionUrl?: string;             // Corrigendum link if extended
  
  // Vacancy & Post Breakdown
  reportedVacancies?: number;                // 2
  postBreakdown?: Array<{
    designation: string;
    count?: number;
    education?: string;
    experience?: string;
    ageLimit?: string;
    selection?: string;
    compensation?: string;
    location?: string;
  }>;
  
  // Source Verification & E-E-A-T Audit Trail
  sourceVerified: boolean;                   // false for current unverified record
  sourceVerifiedAt?: string;                 // ISO 8601
  sourceVerifiedBy?: string;                 // Editor ID / Name
  fieldProvenance: Record<string, {
    url: string;
    pageOrClause?: string;
    verifiedAt: string;
  }>;
  
  // Editorial Timestamps
  editorialPublishedAt: string;              // Initial SSN import timestamp
  editorialModifiedAt: string;               // Substantive update timestamp
  lastEditorialReviewAt?: string;            // Last manual review timestamp
  
  // Application Pathway
  activeApplicationUrl?: string;             // Null if closed or unverified
  
  // Content & Changelog
  articleBodyMd: string;                     // Markdown source for SSR
  legacySummary?: string;                    // Original legacy text
  updateLog: Array<{
    timestamp: string;
    change: string;
    evidenceUrl?: string;
  }>;
}
```

---

## 2. Field Hierarchy & Resolution Precedence

When conflicting values exist across different sources, the database and publishing engine must resolve values according to this strict hierarchy:

```text
1. Authentic Primary Circular PDF (Official Government Department) [HIGHEST]
    │
    ▼
2. Official Corrigendum / Addendum Published on Official Domain (.gov.in / .nic.in)
    │
    ▼
3. Official Department Recruitment Portal / Online Application System
    │
    ▼
4. SearchSarkariNaukri Historical Database Record
    │
    ▼
5. Third-Party Job Aggregators / Unofficial Forums [LOWEST - REJECT AS SOURCE]
```

### Precedence Rules:
- **Deadline Overrides:** An official dated corrigendum overrides the original deadline **only when** accompanied by an entry in the `updateLog` linking the corrigendum URL. Silent deadline overwrites are forbidden.
- **Unknown ≠ False:** An unverified qualification clause must be marked `UNKNOWN / NOT VERIFIED`. Never assume standard 10th or 12th pass rules apply by default.

---

## 3. Production Publishing Control Gate

The publishing engine must evaluate this boolean condition before allowing the emission of Google `JobPosting` structured data:

```typescript
export function canRenderJobPosting(record: RecruitmentRecord): boolean {
  const isSingleRealRole = record.postBreakdown?.length === 1 && Boolean(record.postBreakdown[0].designation);
  const completeJobDetails = Boolean(
    record.employerName &&
    record.notificationPdfUrl &&
    record.employerDatePosted &&
    record.articleBodyMd
  );
  const validThroughValid = record.applicationEndDate 
    ? new Date(record.applicationEndDate) >= new Date() 
    : false;

  return (
    record.sourceVerified === true &&
    record.pageStatus === 'OPEN' &&
    isSingleRealRole &&
    completeJobDetails &&
    validThroughValid
  );
}
```

### Status for DGFT Record `dgft-dgft-2026--2030`:
```typescript
canRenderJobPosting(dgftRecord) === false; // JobPosting is suppressed
```

---

## 4. PostgreSQL Database Schema Migration (DDL)

```sql
-- Migration: Add E-E-A-T Source Provenance & Audit Fields to Job Records
ALTER TABLE recruitment_records
  ADD COLUMN IF NOT EXISTS source_verified BOOLEAN DEFAULT FALSE,
  ADD COLUMN IF NOT EXISTS source_verified_at TIMESTAMP WITH TIME ZONE,
  ADD COLUMN IF NOT EXISTS source_verified_by VARCHAR(255),
  ADD COLUMN IF NOT EXISTS field_provenance JSONB DEFAULT '{}'::jsonb,
  ADD COLUMN IF NOT EXISTS update_log JSONB DEFAULT '[]'::jsonb,
  ADD COLUMN IF NOT EXISTS notification_number VARCHAR(255),
  ADD COLUMN IF NOT EXISTS notification_pdf_url TEXT,
  ADD COLUMN IF NOT EXISTS deadline_timezone VARCHAR(50) DEFAULT 'Asia/Kolkata',
  ADD COLUMN IF NOT EXISTS last_editorial_review_at TIMESTAMP WITH TIME ZONE;

-- Index for Dynamic Active Job Queries
CREATE INDEX IF NOT EXISTS idx_recruitment_open_verified
  ON recruitment_records (category_or_type, application_status, application_end_date)
  WHERE application_status = 'OPEN' AND source_verified = TRUE;
```
