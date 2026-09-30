# Semantic HTML and schema — Employment News

## Outline

```html
<main id="main-content">
  <nav aria-label="Breadcrumb">…</nav>
  <article>
    <header><h1>…</h1><p>intro</p></header>
    <section aria-labelledby="quick-answer">
      <h2 id="quick-answer">Quick answer: what is Employment News?</h2>
      …
    </section>
    <section aria-labelledby="latest-issues">
      <h2 id="latest-issues">Latest Employment News issues</h2>
      <table>…</table>
    </section>
    <section aria-labelledby="how-to-use">…</section>
    <section aria-labelledby="faq">
      <h2 id="faq">Frequently asked questions</h2>
      <!-- each Q as h3 -->
    </section>
  </article>
</main>
```

## JSON-LD (single script block)

- `BreadcrumbList`  
- `WebPage` with `name`, `description`, `url`, `dateModified`  
- `FAQPage` — only questions visible in `PAGE_COPY.md`  
- `Organization` publisher: SearchSarkariNaukri (reuse site-wide `@id`)  

Do **not** claim `GovernmentOrganization` for our site.

## Open Graph

- `og:type` = website  
- `og:title` / `og:description` match meta  
- `og:url` = canonical  
