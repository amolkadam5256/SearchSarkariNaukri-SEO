# 03 - SCHEMA, INTERNAL LINKING AND QA

**Route:** `/exams/upsc-cse`  
**Status:** Required before deployment

---

## Schema

Use:

- `WebPage`
- `BreadcrumbList`
- `FAQPage`, only for visible FAQ content
- `ItemList`, optional for preparation guide links

Do not use:

- `JobPosting`
- Fake `Course` schema
- Hidden FAQ schema

## WebPage Schema

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "UPSC Civil Services Examination 2026 - Eligibility, Syllabus, Pattern & Dates",
  "description": "Check UPSC Civil Services Examination 2026 eligibility, age limit, attempts, important dates, Prelims and Mains pattern, syllabus, optional subjects, previous papers, results, cut-offs and official UPSC links.",
  "url": "https://www.searchsarkarinaukri.com/exams/upsc-cse",
  "dateModified": "2026-09-22",
  "isPartOf": {
    "@type": "WebSite",
    "name": "Search Sarkari Naukri",
    "url": "https://www.searchsarkarinaukri.com"
  }
}
```

`dateModified` must reflect real review/content changes, not current render time.

## Breadcrumb Schema

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://www.searchsarkarinaukri.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Government Exams",
      "item": "https://www.searchsarkarinaukri.com/exams"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "UPSC Civil Services Examination",
      "item": "https://www.searchsarkarinaukri.com/exams/upsc-cse"
    }
  ]
}
```

## Internal Linking Priority

P0 internal links:

- `/exams`
- `/exams/upsc-cse/guide/syllabus`
- `/exams/upsc-cse/guide/subject-preparation`
- `/exams/upsc-cse/guide/books`
- `/exams/upsc-cse/guide/answer-writing`
- `/exams/upsc-cse/guide/important-topics`
- `/exams/upsc-cse/guide/marking-system`

P1 internal links:

- `/current-affairs`
- `/daily-assessment`
- `/quiz`
- `/digital-library`
- `/exam-calendar`
- `/age-calculator`

P2 links:

- `/battle`
- `/career-guidance`
- `/admit-cards`
- `/results`
- UPSC beginner blog

## Recommended Link Placement

| Section | Link |
| --- | --- |
| Breadcrumb | `/exams` |
| Hero quick links | syllabus guide, dates anchor, eligibility anchor, preparation strategy |
| Current status | `/exam-calendar` |
| Quick facts | `/exams` |
| Overview | UPSC beginner blog |
| Services | `/career-guidance` |
| Important dates | `/exam-calendar` |
| Age limit | `/age-calculator` |
| Age relaxation | marking-system guide |
| Attempts | marking-system guide |
| Selection process | syllabus guide |
| Prelims pattern | syllabus guide, daily assessment |
| Prelims syllabus | subject preparation, books, important topics, current affairs |
| Mains pattern | syllabus guide, answer writing |
| Mains syllabus | subject preparation, important topics, books, answer writing |
| Optional subjects | subject preparation |
| Interview | marking-system guide |
| Final merit | marking-system guide |
| Previous papers | important topics guide |
| Results and cut-offs | marking-system guide, `/results` |
| Application process | `/exam-calendar` |
| Preparation guides | six UPSC child guide pages |
| Daily practice | current affairs, daily assessment, quiz, battle, digital library |
| Related exams | existing exam pages or `/exams` |

## Anchor Text Rules

Good anchor examples:

- UPSC CSE syllabus and exam pattern
- UPSC Mains answer-writing strategy
- UPSC attempts and cut-off guide
- UPSC subject-wise preparation strategy
- Daily UPSC current affairs
- Free UPSC study resources

Avoid:

- Click here
- Read more
- Learn more
- View

## Official Sources

Use these as external official references:

- UPSC official website: `https://www.upsc.gov.in`
- Civil Services Preliminary Examination 2026 official page
- Civil Services Main Examination 2026 official page
- Active examinations page
- Previous question papers page
- UPSC online application portal: `https://upsconline.nic.in`

## QA Checklist

### Technical SEO

- [ ] URL returns HTTP 200.
- [ ] Canonical is `https://www.searchsarkarinaukri.com/exams/upsc-cse`.
- [ ] Robots is `index,follow`.
- [ ] One H1 only.
- [ ] Title and meta description are unique.
- [ ] Breadcrumb visible and schema valid.
- [ ] Page is in sitemap.
- [ ] Sitemap lastmod reflects real content review.

### Content

- [ ] All sections from README are present.
- [ ] Current UPSC CSE 2026 status is accurate.
- [ ] No `Apply Now` CTA appears when applications are closed.
- [ ] Quick facts table present.
- [ ] Table of contents present.
- [ ] Eligibility subsections present.
- [ ] Age and attempts sections are not generic guesses.
- [ ] Prelims and Mains sections are separated.
- [ ] Optional subjects section does not link to empty pages.
- [ ] Official UPSC links present.
- [ ] FAQ has 10-12 useful questions.
- [ ] Verification note visible.

### Data Accuracy

- [ ] Dates are sourced from official UPSC data.
- [ ] Fees are dynamic from current notification.
- [ ] Age relaxation is dynamic from current notification.
- [ ] Attempts are dynamic from current notification.
- [ ] Services list comes from current notification data.
- [ ] No fabricated interview criteria.
- [ ] No exam centre listed as job location.

### Internal Links

- [ ] Six UPSC guide pages linked.
- [ ] `/exams` linked.
- [ ] `/exam-calendar` linked.
- [ ] `/age-calculator` linked once in age context.
- [ ] `/current-affairs` linked in preparation context.
- [ ] `/daily-assessment` linked in practice context.
- [ ] `/digital-library` linked in resources context.
- [ ] No broken internal links.
- [ ] Anchor text is descriptive.

### Accessibility and Semantics

- [ ] H1-H6 hierarchy follows `02_SEMANTIC_HTML_STRUCTURE.md`.
- [ ] Tables have headers.
- [ ] TOC works by keyboard.
- [ ] Focus states visible.
- [ ] Link text is meaningful.
- [ ] No giant card anchor.
- [ ] Mobile table layout does not break page width.

### Performance

- [ ] LCP <= 2.5 seconds.
- [ ] INP < 200 ms.
- [ ] CLS < 0.1.
- [ ] No unnecessary heavy images.
- [ ] Core content server-rendered or prerendered where practical.
- [ ] No API failure turns the page into thin content.

---

**Last Updated:** 22 September 2026
