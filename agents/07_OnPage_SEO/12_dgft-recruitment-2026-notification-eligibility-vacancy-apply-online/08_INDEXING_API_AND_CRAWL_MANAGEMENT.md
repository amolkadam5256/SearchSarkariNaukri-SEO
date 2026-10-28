# 08 — INDEXING API & CRAWL MANAGEMENT SPECIFICATION

**Target Canonical URL:** `https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030`  
**Protocol:** Google Indexing API v3 & XML Sitemap Synchronization  
**Audit Date:** 18 October 2026 (IST)  
**Priority:** P1 Technical SEO & Crawl Governance

---

## 1. Google Indexing API Eligibility: Strict Rule for DGFT Page

> ⚠️ **CRITICAL GOOGLE COMPLIANCE RESTRICTION:**  
> **DO NOT SUBMIT THIS CURRENT DGFT HISTORICAL PAGE VIA THE GOOGLE INDEXING API.**

### Official Google Policy Scope:
Google's Indexing API is explicitly restricted to pages containing either:
1. `JobPosting` structured data for active employment opportunities.
2. `BroadcastEvent` structured data for live video streams.

Submitting pages that lack valid `JobPosting` markup—such as expired historical archives, category listings, blog posts, or generic informational pages—violates Google's API Terms of Service and can result in the revocation of API access across the entire SearchSarkariNaukri Google Cloud project.

### Crawl Request Procedure for the Current DGFT Archive:
- Rely on the standard **XML Sitemap** submission with an authentic `<lastmod>` timestamp.
- For immediate indexing checks, use the **Google Search Console URL Inspection Tool** to manually request a recrawl.

---

## 2. Infrastructure Setup for Verified Active Job Postings

For future, verified, actively hiring job postings that meet all criteria in `07_STRUCTURED_DATA_JSONLD_SPECIFICATION.md`, follow this production setup:

### Step 1: Google Cloud Project & Service Account Delegation
1. Create a dedicated Google Cloud Platform (GCP) project: `ssn-indexing-production`.
2. Enable the **Google Indexing API** in the GCP Console.
3. Generate a Service Account with a private JSON key stored securely in environment secrets (`GOOGLE_INDEXING_CREDENTIALS`).
4. In Google Search Console, navigate to **Settings > Users and permissions** and add the service account email as a **Delegated Owner** for `https://www.searchsarkarinaukri.com/`. (A standard "Full User" role will fail API authentication).

### Step 2: Automated Notification Service (Node.js / TypeScript)
```typescript
import { google } from 'googleapis';

const SCOPES = ['https://www.googleapis.com/auth/indexing'];

export async function notifyGoogleIndexing(
  url: string,
  action: 'URL_UPDATED' | 'URL_DELETED',
  jobId: string
): Promise<{ success: boolean; status?: number; error?: string }> {
  try {
    const auth = new google.auth.GoogleAuth({
      credentials: JSON.parse(process.env.GOOGLE_INDEXING_CREDENTIALS || '{}'),
      scopes: SCOPES,
    });

    const client = await auth.getClient();
    const endpoint = 'https://indexing.googleapis.com/v3/urlNotifications:publish';

    const response = await client.request({
      url: endpoint,
      method: 'POST',
      data: {
        url: url,
        type: action,
      },
    });

    // Log event in database audit table
    await logIndexingRequest({
      jobId,
      url,
      action,
      statusCode: response.status,
      timestamp: new Date().toISOString(),
    });

    return { success: response.status === 200, status: response.status };
  } catch (error: any) {
    console.error(`Indexing API failed for ${url}:`, error.message);
    return { success: false, error: error.message };
  }
}
```

---

## 3. Job Expiration & Lifecycle State Machine

When an active recruitment closes, adhere to this state machine to preserve search integrity:

```text
               [Active Job: OPEN]
                 │  - Emits valid JobPosting schema
                 │  - Dispatches URL_UPDATED via Indexing API
                 ▼
       [Application Deadline Reached]
                 │
                 ├── Retain Page as Historical Archive?
                 │     ├── YES:
                 │     │     1. Update visible UI: Display "Applications Closed".
                 │     │     2. Remove JobPosting JSON-LD (or set validThrough in past).
                 │     │     3. Render safe WebPage schema.
                 │     │     4. Update XML sitemap <lastmod>.
                 │     │     5. Send URL_UPDATED notification via Indexing API.
                 │     │     6. DO NOT use URL_DELETED (URL is still live!).
                 │     │
                 │     └── NO (Page Returns 404 / 410 Gone):
                 │           1. Issue HTTP 410 Gone header.
                 │           2. Send URL_DELETED notification via Indexing API.
                 │           3. Remove URL from XML sitemap.
```

---

## 4. XML Sitemap Governance

The canonical URL `https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030` must be present in `sitemap-jobs.xml`:

```xml
<url>
  <loc>https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030</loc>
  <lastmod>2026-10-18T18:17:11+05:30</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.6</priority>
</url>
```

### Truthful `<lastmod>` Rule:
- The `<lastmod>` tag must update **only** when a developer or editor publishes substantive modifications to the content, schema, or status.
- Avoid cron jobs that touch `<lastmod>` on every URL daily without actual changes. Googlebot detects and ignores synthetic lastmod dates.
