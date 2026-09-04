# HTTP 400-499 Errors - Bing Site Scan

Bing reports 110 affected URLs. The supplied screen shows the first 25 visible URLs; this folder documents those and gives the developer the rule for the full 110 export.

## Visible URLs From Evidence

- `https://www.searchsarkarinaukri.com/jobs-in-lumding`
- `https://www.searchsarkarinaukri.com/districts/rangiya`
- `https://www.searchsarkarinaukri.com/jobs-in-chittaranjan`
- `https://www.searchsarkarinaukri.com/districts/across-jharkhand`
- `https://www.searchsarkarinaukri.com/jobs-in-across-jharkhand`
- `https://www.searchsarkarinaukri.com/jobs-in-yavatmal`
- `https://www.searchsarkarinaukri.com/districts/maharashtra`
- `https://www.searchsarkarinaukri.com/jobs-in-maharashtra-&-madhya-pradesh`
- `https://www.searchsarkarinaukri.com/districts/karnataka`
- `https://www.searchsarkarinaukri.com/districts/alipurduar`
- `https://www.searchsarkarinaukri.com/jobs-in-beed`
- `https://www.searchsarkarinaukri.com/districts/delhi`
- `https://www.searchsarkarinaukri.com/jobs/4198`
- `https://www.searchsarkarinaukri.com/jobs/4197`
- `https://www.searchsarkarinaukri.com/jobs/4278`
- `https://www.searchsarkarinaukri.com/jobs-in-ahmednagar`
- `https://www.searchsarkarinaukri.com/jobs-in-new-bongaigaon`
- `https://www.searchsarkarinaukri.com/districts/assam`
- `https://www.searchsarkarinaukri.com/jobs-in-neyveli`
- `https://www.searchsarkarinaukri.com/districts/rajasthan`
- `https://www.searchsarkarinaukri.com/districts/tinsukia`
- `https://www.searchsarkarinaukri.com/districts/punjab`
- `https://www.searchsarkarinaukri.com/districts/chennai`
- `https://www.searchsarkarinaukri.com/districts/goa`
- `https://www.searchsarkarinaukri.com/districts/odisha`

## Fix Logic

- Valid location/district page returning 4xx: restore 200 OK with useful content.
- Valid job page returning 4xx: restore job page or redirect to exact canonical job URL.
- Invalid/deleted page: keep 404 or 410 intentionally.
- Broken internal link: update contextual link to valid canonical URL.
- Sitemap URL returning 4xx: remove from sitemap immediately.

## Required Page Sections If Restored

- H1
- Clear summary
- Current jobs or useful recent/historical jobs
- Location/department/category context
- Related internal links
- FAQ section with 10-15 non-duplicate questions where the page is indexable
- Last updated
- Verification/source note

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Bing Webmaster Site Scan issue.
