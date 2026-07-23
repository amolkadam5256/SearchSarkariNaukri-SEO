# 08 — On-Page SEO & Content Formatting Standards

## 8.1 On-Page Optimization Guidelines

### Title Tag Formatting Rules
- **Length:** 50–60 characters (front-load primary keyword).
- **Format Templates by Page Type:**
  - *Job Notifications:* `[Organization] [Post Name] Recruitment 2026 — [Vacancies] Posts | Apply Online`
  - *State Pages:* `[State Name] Government Jobs 2026 — Latest Sarkari Naukri`
  - *Department Pages:* `[Department Name] Recruitment 2026 — Latest [Department] Bharti`
  - *Qualification Pages:* `[Qualification] Govt Jobs 2026 — Sarkari Naukri for [Qualification]`
  - *Result Pages:* `[Exam Name] Result 2026 — Download Scorecard & Cutoff`
  - *Admit Card Pages:* `[Exam Name] Admit Card 2026 — Download Hall Ticket`

### Meta Description Formatting Rules
- **Length:** 140–160 characters (must include a direct CTA like "Apply Online" or "Download Here").
- **Format Templates by Page Type:**
  - *Job Notifications:* `[Organization] has released [Post Name] recruitment 2026 for [Count] vacancies. Last date: [Date]. Check eligibility, age limit, fee, salary, and apply online.`
  - *State Pages:* `Find latest [State Name] government jobs 2026. Browse [Count]+ active sarkari naukri vacancies across [State Name] departments. Updated daily.`

---

## 8.2 Image Optimization Standards

| Optimization Element | Technical Standard | Example |
|----------------------|--------------------|---------|
| **File Naming** | Lowercase, hyphenated, keyword-rich | `ssc-cgl-2026-vacancy-details.webp` |
| **ALT Text** | Descriptive explanation including target keyword | `SSC CGL 2026 category wise vacancy breakdown table` |
| **File Format** | WebP primary format (AVIF where supported) | Use `<picture>` element with WebP source |
| **Dimensions** | Explicit `width` and `height` attributes | `<img src="..." width="800" height="450" alt="...">` |
| **Max File Size** | < 100KB for content images; < 150KB for hero images | Compressed via Sharp / Squoosh pipeline |
| **Lazy Loading** | `loading="lazy"` on all below-fold images | Native browser lazy loading |

---

## 8.3 On-Page SEO Checklist (18-Point Verification per Page)

- [ ] 1. Unique, keyword-optimized `<title>` tag (≤ 60 characters).
- [ ] 2. Compelling `<meta description>` (140–160 characters) with clear Call to Action.
- [ ] 3. Single `<h1>` tag matching target search query closely.
- [ ] 4. Primary keyword placed within first 100 words of body content.
- [ ] 5. Heading hierarchy follows logical structure (`<h1>` -> `<h2>` -> `<h3>`).
- [ ] 6. Heading tags include secondary and long-tail keywords naturally.
- [ ] 7. Minimum 3–5 contextual internal links to related state, department, or qualification hubs.
- [ ] 8. At least 1 explicit outbound link to official government domain (`.gov.in` / `.nic.in`).
- [ ] 9. Descriptive, keyword-relevant anchor text used for all internal links (no "click here").
- [ ] 10. All images use WebP format with explicit `width` and `height` attributes.
- [ ] 11. All images have descriptive, keyword-relevant `alt` text.
- [ ] 12. Below-the-fold images use `loading="lazy"`.
- [ ] 13. LCP hero image uses `fetchpriority="high"`.
- [ ] 14. Content is 100% original, accurate, and verified against official PDF notifications.
- [ ] 15. FAQ section included with `FAQPage` structured data JSON-LD.
- [ ] 16. Self-referencing canonical tag present and matches primary URL.
- [ ] 17. Open Graph and Twitter Card social meta tags present.
- [ ] 18. Mobile-friendly formatting (short 2-sentence paragraphs, bullet points, clean tables).
