# 10 — GEO / AEO: Optimizing for AI Answer Engines (Additive Only)

> GEO (Generative Engine Optimization) and AEO (Answer Engine Optimization) means making pages easy for AI systems — Google AI Overviews, ChatGPT, Perplexity, Copilot — to extract clean, quotable, trustworthy answers. These are all additions layered on top of the traditional SEO work in files 02–09; nothing here changes existing UI.

## 1. Add a `/llms.txt` file at the site root (new file, doesn't affect anything else)

A plain-text file some AI crawlers use to understand site structure and priority content. This does not replace `robots.txt` or `sitemap.xml` — it's an additional, optional signal file.

```
# llms.txt for searchsarkarinaukri.com

## About
SearchSarkariNaukri is an independent government job information portal
covering Sarkari Naukri, MPSC, SSC, Railway, Banking, Police Bharti and
other Indian government recruitment, primarily focused on Maharashtra.

## Key pages
- Latest Government Jobs: https://www.searchsarkarinaukri.com/jobs
- Maharashtra Government Jobs: https://www.searchsarkarinaukri.com/maharashtra-government-jobs
- Government Jobs by Qualification: https://www.searchsarkarinaukri.com/qualification/
- Government Jobs by Category: https://www.searchsarkarinaukri.com/category/
- FAQs: see FAQPage schema on /jobs

## Disclaimer
SearchSarkariNaukri is not affiliated with any government department.
Always verify details on the official recruitment notification.
```

## 2. Write answer-first content blocks (additive text pattern, not a structural rewrite)

For each FAQ answer (files 03 and 04) and each landing-page intro (file 07), lead with a direct, self-contained 1–2 sentence answer before any elaboration. This is the format both Google's featured snippets and LLM answer engines extract most reliably.

```
Q: Which government jobs are available for 12th-pass candidates in Maharashtra?
A: 12th-pass candidates can apply for government jobs in Police Bharti, Talathi,
Railway Group D, Forest Guard and various clerical posts across Maharashtra
government departments. [then 2–3 sentences of supporting detail]
```

## 3. Keep FAQPage schema text identical to visible text (already required in file 05/06)

AI answer engines and Google both cross-check visible content against structured data; mismatched schema is a trust/quality signal problem, not just an SEO nicety.

## 4. Strengthen E-E-A-T signals (additive, no redesign)

- Add an "About Us" / "How We Verify Jobs" page if one doesn't exist, explaining the editorial/verification process (ties to the "Source: Official Notification · Verified: {date}" block in file 04).
- Add the disclaimer (file 03) consistently across `/jobs`, category pages, and individual job pages — AI systems weight clear, consistent trust disclosures when deciding whether to surface a source.
- Where possible, attribute content review to a named editorial process/team rather than leaving it anonymous.

## 5. Structured, extractable data tables

Wherever a job/qualification/category page lists facts (vacancy count, last date, eligibility), keep them as actual `<table>` or definition-list markup rather than only prose — both Google's AI Overviews and LLM crawlers parse tables more reliably than paragraph text for structured facts. File 04's Quick Information table already does this; extend the same pattern to qualification/category landing pages.

## 6. Keep content genuinely original (ties to file 09)

Both Google's ranking systems and most LLM retrieval layers now down-weight or ignore templated/boilerplate pages with near-duplicate content. The original 2–4 sentence per-job overviews required in file 04 aren't just for classic SEO — they're what makes a page worth an AI system citing over a competitor's near-identical listing.

## 7. Add `dateModified`/`datePosted` consistently

Freshness fields already specified in file 06's JobPosting schema (`datePosted`, `validThrough`) and file 04's "Last Updated" badge double as GEO signals — AI answer engines favor demonstrably current sources for time-sensitive queries like recruitment deadlines.

## Checklist for this file

- [ ] `/llms.txt` added at site root
- [ ] FAQ and landing-page intros rewritten in answer-first format
- [ ] FAQPage schema text kept in sync with visible text
- [ ] "How We Verify Jobs" / About page added or linked from disclaimer
- [ ] Disclaimer present consistently across `/jobs`, category, and job pages
- [ ] Structured facts kept in tables, not buried in prose only
- [ ] Freshness fields (`datePosted`, `validThrough`, Last Updated) populated everywhere applicable
