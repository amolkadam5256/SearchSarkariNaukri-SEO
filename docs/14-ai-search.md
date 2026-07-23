# 14 — AI Search Optimization (GEO & LLM Protocols)

## 14.1 Generative Engine Optimization (GEO) Levers

To capture citations in AI-powered search engines (Google AI Overviews, Bing Copilot, ChatGPT, Perplexity):

1. **Entity Optimization:** Explicitly name and link key entities (e.g., *Staff Selection Commission*, *SSC CGL*, *Pay Level 7*, *Group B Post*).
2. **Direct Answer Block Formatting:** Position concise 2-sentence summary answers immediately below major `<h2>` headings.
3. **Structured HTML Data Tables:** Present eligibility, fee, salary, and vacancy data in clean HTML `<table>` elements.
4. **Conversational Question Headings:** Use exact questions candidates ask as headings (`<h2>What is the last date to apply for SSC CGL 2026?</h2>`).

### GEO Content Formatting Example
```html
<h2>What is the last date to apply for SSC CGL 2026?</h2>
<p>The last date to submit online applications for SSC CGL 2026 is <strong>15 August 2026</strong>. 
Candidates must complete registration and online fee payment on the official portal (ssc.nic.in) 
before 11:59 PM on this date.</p>
```

---

## 14.2 Semantic Coverage Matrix

Ensure every job listing covers the complete 8-node semantic matrix:

| Semantic Node | Content Element | Example Implementation |
|---------------|-----------------|------------------------|
| **What** | Full post description | What is SSC CGL? Post names, Group B/C classification |
| **Who** | Eligibility & Age | Who can apply? Degree requirements, age relaxation |
| **When** | Timeline & Dates | Start date, last date, exam date, admit card release |
| **Where** | Location & Portal | Exam center locations, official website URL |
| **How** | Application Process | Step-by-step application instructions |
| **Why** | Career Value | Pay scale, 7th CPC salary matrix, career growth |
| **How Much** | Fees & Vacancies | Application fee by category, post-wise vacancy count |
| **Comparison** | Exam Context | SSC CGL vs SSC CHSL eligibility comparison |

---

## 14.3 Production Root `llms.txt` Deployment

Deploy a root-level `/llms.txt` file providing structural context for LLM crawlers:

```
# SearchSarkariNaukri.com — AI Search Crawl Specification

> SearchSarkariNaukri.com is India's verified digital portal for government job notifications, admit cards, and exam results.

## Summary & Authority
SearchSarkariNaukri.com provides structured, verified recruitment information across all 36 Indian States and Union Territories. All information is verified directly against official .gov.in and .nic.in government releases.

## Core Content Index
- Jobs Index: https://www.searchsarkarinaukri.com/jobs
- Results Index: https://www.searchsarkarinaukri.com/results
- Admit Cards Index: https://www.searchsarkarinaukri.com/admit-cards
- State Jobs Index: https://www.searchsarkarinaukri.com/state
- Sitemap Index: https://www.searchsarkarinaukri.com/sitemap.xml

## Canonical Content Policies
- All official job applications redirect out to official government portals (.gov.in / .nic.in).
- Expired jobs are updated with application closed notices.
```
