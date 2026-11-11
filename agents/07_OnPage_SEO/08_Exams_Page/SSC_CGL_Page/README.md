# SSC CGL Exam Page Package

**Permanent route:** `/exams/ssc-cgl`  
**Page type:** Maintained exam reference hub  
**Status:** Implementation-ready content and technical handoff; application source code is not present in this repository.  
**Cycle checked:** 12 November 2026  
**Latest verified vacancy count:** 10,731 tentative (SSC list dated 24 September 2026)  
**Historical cutoff data:** SSC 2025 Tier I shortlisting cutoffs included, with normalized score labels

## Files

- `01_COMPLETE_PAGE_CONTENT.md` — Page copy and structured, cycle-aware data for the exam hub.
- `02_SEMANTIC_HTML_STRUCTURE.md` — Heading map, section IDs and responsive component behavior.
- `03_IMPLEMENTATION_SEO_DATA_QA.md` — Design, data contracts, official sources, SEO/schema, release priorities and QA.

## Page role

Keep the existing `/exams/ssc-cgl` URL. Make it a national SSC CGL exam reference page, not another duplicate CGL blog post. Link out to focused preparation guides where they add depth.

## Scope boundary

This repository contains SEO documentation and mock/template material, not the website application or its exam data service. This package is a developer handoff. The live route cannot be changed from this checkout; implement these specifications in the website application repository and connect cycle updates to its verified data source.
