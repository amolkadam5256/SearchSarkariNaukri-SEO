# AI, AEO, GEO and SEO Ranking Requirements for Job Canonical Fix

## 1. AI / LLM Principle

LLMs and answer engines need one trusted URL per job. Do not split job facts across numeric URL, slug URL, query URL, and listing pages.

For job `862`, choose one canonical job URL and make every signal match: canonical tag, sitemap URL, internal links, BreadcrumbList URL, JobPosting URL, Open Graph URL, Twitter URL, and `llms.txt` entry if used.

## 2. llms.txt Recommendation

No workspace `llms.txt` was found in the earlier review. If production uses `llms.txt`, include only canonical indexable job URLs. Do not include `/jobs/862` if it redirects or is non-indexable.

## 3. AEO Requirements

If job `862` is indexable, add answer-friendly sections for what the recruitment is, last date, eligibility, age limit, selection process, how to apply, and official notification.

## 4. GEO Requirements

Expose labeled facts clearly: organization, post name, vacancy count, qualification, location, category, age limit, salary, deadline, official notification, official apply link, and verification/update date.

## 5. SEO Requirements

One canonical URL per job, one H1, unique title/meta description, JobPosting schema matching visible content, BreadcrumbList pointing to canonical job URL, no alternate route in sitemap, and no canonical to unrelated listing/district/department/homepage.

## 6. Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, site-wide layout, global styling, tracking setup, analytics setup, or shared components unless strictly required for this canonical fix.
