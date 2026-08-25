# 08 — GEO (Generative Engine Optimization) Audit
### GEO = being cited/quoted as a SOURCE inside AI chatbot answers
(ChatGPT, Perplexity, Google Gemini, Microsoft Copilot, Claude) when users ask
government-job-related questions conversationally. This is DISTINCT from AEO
(file 07) — GEO targets AI chat products, not Google's own SERP answer boxes.
This section was explicitly requested by the client — do not skip or merge with file 07.

Output file: `outputs/final-reports/08-geo-generative-engine-audit-REPORT.md`

## A. Current AI-Citation Baseline (manual test — run and screenshot each)
Ask each of the following tools these exact test prompts, and log verbatim
whether searchsarkarinaukri.com is cited, ranked, or mentioned at all:
- [ ] ChatGPT (with browsing/search enabled): "What are the latest MPSC Rajyaseva
  2026 government job openings in Maharashtra?"
- [ ] Perplexity: "Talathi Bharti 2026 last date to apply"
- [ ] Google Gemini: "Police Bharti Maharashtra 2026 eligibility criteria"
- [ ] Microsoft Copilot: "Railway RRB NTPC 2026 admit card"
- [ ] Claude (with web search): "Which sites list daily updated Sarkari Naukri
  for Maharashtra government jobs?"

For each: record (1) was the domain cited at all, (2) position in the citation
list, (3) what snippet/claim was pulled from the site (if any), (4) which
competitor domains were cited instead and why (their content structure/authority).

## B. Content Structure for LLM Extractability
Generative engines favor content that's easy to parse into discrete facts.
- [ ] Check whether key facts per job listing (organization, post name,
  vacancy count, qualification, age limit, last date, application link) are
  presented as **structured, labeled data** (definition list / table) rather
  than buried in narrative prose — this is the single biggest GEO lever for a
  jobs site
- [ ] Check for a clear, quotable one-sentence summary near the top of each
  page (LLMs frequently extract the first clear declarative sentence)
- [ ] Check heading structure maps to likely LLM sub-queries ("Eligibility",
  "Important Dates", "How to Apply", "Selection Process" as actual H2/H3s)

## C. Machine-Readability & Access Signals
- [ ] Check whether `robots.txt` explicitly allows or blocks known AI
  crawlers: `GPTBot` (OpenAI), `PerplexityBot`, `Google-Extended` (Gemini/AI
  Overviews training+grounding), `ClaudeBot`/`anthropic-ai`, `CCBot` (Common
  Crawl, feeds many LLMs), `Bingbot`/`Applebot-Extended` — report current
  allow/block status for each, and flag if any are unintentionally blocked
  (since blocking them removes eligibility for citation in that AI product)
- [ ] Confirm content is server-rendered/crawlable without JS execution
  (many AI crawlers do not execute JavaScript — cross-ref file `01` section I)
- [ ] Check page load reliability (AI crawlers often have short timeouts —
  slow pages, per file `06`, may simply fail to be ingested)

## D. Authority & Corroboration Signals (LLMs cross-check facts across sources)
- [ ] Check whether facts (deadlines, vacancy counts) on the site match the
  **official government notification** exactly — any discrepancy reduces
  trust/citation likelihood when an LLM cross-references multiple sources
- [ ] Check whether the site is cited/mentioned on other reputable sources
  (news sites, Wikipedia, government-adjacent directories) — external
  corroboration increases LLM citation confidence (cross-ref file `10`)
- [ ] Check freshness signals are unambiguous: exact publish/update
  datestamps visible in raw HTML, not just relative ("2 days ago") text that
  a crawler snapshot can't resolve to an absolute date

## E. Brand & Entity Clarity
- [ ] Confirm consistent brand naming across the site (cross-ref
  `00-live-seed-findings.md` #8) — inconsistent naming ("SearchSarkariNaukri"
  vs "Search Sarkari Naukri" vs "SearchSarkariNaukri.com") fragments entity
  recognition and can reduce how confidently an LLM attributes/cites the source
- [ ] Check for a clear "About" page describing what the site is, who runs it,
  and its editorial/verification process — LLMs and their safety layers favor
  citing sources with clear provenance, especially for something as
  consequential as government job application deadlines

## F. Recommendations Log
- [ ] For every gap found above, log a specific, actionable GEO fix (e.g.
  "Add labeled fact table to job listing template", "Unblock GPTBot and
  Google-Extended in robots.txt", "Add absolute datePosted stamp visible in raw HTML")
