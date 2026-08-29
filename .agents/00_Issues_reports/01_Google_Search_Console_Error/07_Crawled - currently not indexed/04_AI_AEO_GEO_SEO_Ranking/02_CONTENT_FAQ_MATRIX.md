# Content Sections And FAQ Matrix By Page Type

Date: 2026-08-29
Issue: Crawled - currently not indexed

## Goal

For every URL selected for indexing, add useful page-specific content sections. Do not add the same generic FAQ block to every page.

## Required Sections By Page Type

Job detail pages need: H1, current status, organization, post name, vacancy count, location, qualification, age limit, salary, application mode, dates, fee, selection process, how to apply, documents, official links, related jobs, last updated, verification note, and 10-15 job-specific FAQs.

Result pages need: H1, result status, result date, authority, exam date, how to check result, roll/registration requirements, merit list/cutoff note, next step, official source, related links, last updated, and 10-15 result-specific FAQs.

District/topic pages need: H1, active job count, latest jobs, recent closed jobs, recruiting departments, qualification links, category links, nearby district links, eligibility/application guidance, last updated, and 10-15 location/topic FAQs.

Department pages need: H1, department overview, latest jobs, closed recruitments, common posts, eligibility patterns, selection process patterns, official source, related departments/categories, last updated, and 10-15 department FAQs.

Qualification/location pages need: H1, active job count, latest jobs, recent closed jobs, departments hiring this qualification, application tips, related locations, related qualifications, related categories, last updated, and 10-15 specific FAQs.

Filter URLs like `/jobs?category=banking` should not be indexed by default. Use a clean static canonical page such as `/jobs/banking`, or keep the parameter URL functional and noindex/canonicalize it.

## FAQ Rules To Avoid Duplication

- Generate questions from page type and actual record data.
- Include organization, location, exam, post, and year only when known.
- Do not use the same 10 questions in the same order across all pages.
- Do not fabricate missing dates, salary, eligibility, result status, or source links.
- If data is missing, use a verification note and official-source instruction.
- Keep answers short, factual, and user-first.

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue.
