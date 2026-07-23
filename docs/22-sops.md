# 22 — Standard Operating Procedures (SOPs)

## SOP 1: Publishing a New Job Notification
```
TRIGGER: Official recruitment notification PDF released by government portal (.gov.in / .nic.in)

STEP 1: SOURCE VERIFICATION
- Download official PDF notification directly from official government domain.
- Verify dates, vacancy breakdown, eligibility criteria, age relaxation rules, and fee structure.
- Note official notification number.

STEP 2: CONTENT CREATION & FORMATTING
- Create new page in CMS using Job Notification Template.
- Add structured summary table, important dates table, category-wise vacancy table, eligibility list, fee details, and step-by-step apply guide.
- Upload official notification PDF link and direct official application URL.

STEP 3: ON-PAGE SEO & STRUCTURED DATA
- Write SEO Title (≤ 60 chars) and Meta Description (140-160 chars) with CTA.
- Add 3–5 contextual internal links to parent State, Qualification, and Department hubs.
- Inject JobPosting, BreadcrumbList, and FAQPage JSON-LD schema blocks.

STEP 4: PUBLISH & INSTANT INDEXING API PUSH
- Publish live URL.
- Trigger automated POST request to Google Indexing API and IndexNow API (Bing).
- Trigger instant broadcast to Telegram and WhatsApp channels.
```

---

## SOP 2: Updating an Existing Page (Dates / Cutoffs / Results)
```
TRIGGER: Official update announced (application deadline extended, admit card released, answer key published)

STEP 1: IDENTIFY & VERIFY
- Verify update against official government PDF release.

STEP 2: UPDATE CONTENT
- Update target sections (Important Dates, Result Links, Admit Card Links).
- Prominently update "Last Updated: [Date]" header.
- Update meta description if deadline or key detail changed.

STEP 3: RE-INDEXATION
- Push updated URL to Google Indexing API and IndexNow API.
```

---

## SOP 3: Refreshing Stale Content (> 90 Days Old)
```
TRIGGER: Content flagged as older than 90 days with declining traffic in GSC

STEP 1: CONTENT AUDIT
- Check GSC search impressions and ranking position.
- Audit page for outdated dates, broken links, or missing FAQ questions.

STEP 2: CONTENT ENHANCEMENT
- Update all dates, facts, and syllabus details.
- Add 3–5 new internal links to recent job notifications.
- Update FAQ section targeting current "People Also Ask" questions.

STEP 3: RE-SUBMISSION
- Update "Last Updated" timestamp and submit to Google Indexing API.
```

---

## SOP 4: Handling Redirects & Expired Listings
```
TRIGGER: URL structure change, page consolidation, or expired job listing (> 180 days)

STEP 1: DETERMINE RESPONSE
- Permanent URL Move -> 301 Permanent Redirect.
- Expired Job (> 180 days with zero traffic) -> Apply "Applications Closed" banner OR issue 410 Gone response.

STEP 2: IMPLEMENTATION
- Configure 301 redirect in Cloudflare/CMS config (max 1 hop; no redirect chains).
- Update internal links pointing to old URL.
```

---

## SOP 5: Fixing Search Console Indexing Issues
```
TRIGGER: GSC Page Indexing report flags errors or "Crawled - currently not indexed" URLs

STEP 1: DIAGNOSE
- Run URL Inspection tool on affected sample URLs.
- Identify if issue is technical (404/5xx), thin content, soft 404, or canonical conflict.

STEP 2: RESOLUTION
- Thin / Zero-Job Page: Inject dynamic `noindex, follow` tag.
- Soft 404: Improve content depth or issue clean 404/410 status code.
- Canonical Conflict: Fix canonical tag to match primary URL.

STEP 3: VALIDATION
- Click "Validate Fix" in Search Console and monitor resolution status.
```
