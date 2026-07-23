# 11 — Programmatic SEO & Scale Governance

## 11.1 Programmatic Matrix & Estimated Page Volume

| Combination Type | Example URL Pattern | Example Page Title | Est. URL Count |
|------------------|---------------------|--------------------|----------------|
| **State × Qualification** | `/jobs/uttar-pradesh/graduate` | `Graduate Govt Jobs in Uttar Pradesh 2026` | ~700 |
| **State × Department** | `/jobs/uttar-pradesh/railway` | `Railway Jobs in Uttar Pradesh 2026` | ~1,800 |
| **Department × Qualification** | `/jobs/railway/10th-pass` | `10th Pass Railway Jobs 2026` | ~500 |
| **District × Qualification** | `/jobs/lucknow/graduate` | `Graduate Govt Jobs in Lucknow 2026` | ~5,000 |
| **State × Category** | `/jobs/bihar/walk-in` | `Walk-in Govt Jobs in Bihar 2026` | ~200 |
| **Total Programmatic Scope** | | | **~8,200 Pages** |

---

## 11.2 9 Quality Control Governance Rules

> [!CAUTION]
> Programmatic pages that simply swap variable tags without offering real value will trigger Google doorway page penalties. Enforce all 9 rules programmatically.

1. **Active Job Threshold:** Pages are generated and submitted ONLY when dynamic active job count is **>= 3**.
2. **Zero-Job Route Handling:** If active job count = 0, inject `<meta name="robots" content="noindex, follow">` while retaining crawl links.
3. **Unique Intro Copy:** Programmatically inject a unique 150-word intro paragraph tailored to the combination (mentioning state name, qualification, and active vacancy counts).
4. **Tailored FAQ Injections:** Inject 3–5 dynamic FAQ items addressing specific eligibility and salary queries for that exact combination.
5. **Self-Referencing Canonical:** Enforce self-referencing canonical tag matching clean URL pattern.
6. **Unique Meta Titles & Descriptions:** Ensure no duplicate titles exist across combination variations.
7. **Breadcrumb Integration:** Full `BreadcrumbList` JSON-LD schema on 100% of programmatic routes.
8. **Internal Link Equity Flow:** Link programmatic pages back to parent State and Qualification hub pages.
9. **Monthly Indexing Audits:** Audit GSC indexation status of programmatic URLs monthly to prune soft 404s.

---

## 11.3 Programmatic Landing Page Layout Code Structure

```html
<!-- Programmatic Combination Layout -->
<article class="programmatic-page">
  <header>
    <nav class="breadcrumbs">[Breadcrumb Navigation]</nav>
    <h1>[Qualification] Govt Jobs in [State Name] 2026</h1>
  </header>

  <section class="unique-intro">
    <p>Find the latest [Qualification] government job opportunities across [State Name]. Currently, there are <strong>[Active Job Count]</strong> active recruitment notifications available for candidates with [Qualification] qualification in [State Name] departments.</p>
  </section>

  <section class="listings-table">
    <h2>Active [Qualification] Vacancies in [State Name]</h2>
    [Dynamic Active Jobs Table with Direct Apply Links]
  </section>

  <section class="combination-guide">
    <h2>About [Qualification] Recruitment in [State Name]</h2>
    <p>[Unique 200-word contextual guide detailing major state recruiting bodies like State PSC, Subordinate Selection Board, and Police Recruitment Board].</p>
  </section>

  <section class="faqs">
    <h2>Frequently Asked Questions</h2>
    [Dynamic FAQ Accordion with FAQPage JSON-LD Schema]
  </section>
</article>
```
