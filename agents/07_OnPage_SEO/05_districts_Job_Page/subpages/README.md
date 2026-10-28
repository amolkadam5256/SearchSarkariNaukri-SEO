# District Recruitment Subpages — Developer Audit Package

Use this package for district-specific recruitment routes such as `/districts/nanded/talathi`. Keep the district landing-page package at the parent level; store each focused recruitment page in its own district/topic folder.

## Structure

```text
subpages/
├── README.md
├── 00_DISTRICT_SUBPAGE_AUDIT_AND_IMPLEMENTATION_TEMPLATE.md
└── nanded/
    └── talathi/
        ├── README.md
        ├── 00_COMPLETE_PAGE_IMPLEMENTATION_BRIEF.md
        ├── 01_PAGE_CONTENT_AND_15_SECTION_LAYOUT.md
        ├── 02_SEO_GEO_AEO_KEYWORD_AND_SCHEMA.md
        ├── 03_FAQ_15_QUESTIONS_AND_ANSWERS.md
        ├── 04_INTERNAL_EXTERNAL_LINKS_AND_SOURCES.md
        ├── 05_UI_UX_ACCESSIBILITY_AND_RESPONSIVE.md
        ├── 06_INDEXING_AND_NOindex_AUDIT.md
        ├── 07_DEVELOPER_IMPLEMENTATION_AND_TWO_PASS_QA.md
        └── 08_FINDINGS_AND_VERIFICATION_LOG.md
```

Folder names use the district slug and topic slug. Do not move or rename existing district package files as part of this addition.

## Reusable instructions

- [District subpage audit and implementation template](00_DISTRICT_SUBPAGE_AUDIT_AND_IMPLEMENTATION_TEMPLATE.md)
- [Nanded Talathi page checklist package](nanded/talathi/README.md)

## Rules for related district pages

- Use the reusable template for other district/topic routes, then create a district/topic folder only when a page-specific brief or implementation is needed.
- Reuse shared components and instructions, but verify each route's content, job data, sources, metadata and indexing policy independently.
- Do not clone Nanded facts, recruitment records, FAQs, keywords, vacancy counts or source links onto another district page.
- Preserve existing Markdown files and links. This package adds an organized subpage layer without changing the parent district documentation.
- Every route checklist requires two passes and recorded evidence. The screenshot's 909 noindex URLs are sitewide evidence only; it does not prove that any particular district subpage is affected.
