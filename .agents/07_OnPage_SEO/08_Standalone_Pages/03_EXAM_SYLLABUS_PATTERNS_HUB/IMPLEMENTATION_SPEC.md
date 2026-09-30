# Exam Syllabus & Patterns Hub

**Competitor reference:** MSN nav “Exam Syllabus & Patterns” + homepage tile  
**Existing overlap:** `01_Home_Page/51_EXAM_PREPARATION_HUB/`, `/exams`, study material  
**Priority:** P1  

## Route options (pick one — do not duplicate thin URLs)

**Recommended:** Enhance existing `/exams` index with this spec **or** add alias `/exam-syllabus-patterns` → **301** to `/exams` if content lives there.

If separate hub needed:

- **Canonical:** `https://www.searchsarkarinaukri.com/exam-syllabus-patterns`

## Purpose

Rank for *SSC CGL syllabus 2026*, *RRB NTPC exam pattern*, *MPSC Rajyaseva syllabus*.

## Sections

1. H1: Government Exam Syllabus & Exam Pattern 2026  
2. Commission grid (same 8 sectors as MSN): UPSC, SSC, RRB, Banking, Police, Teaching, PSU, Medical — each links to `/exams/[slug]` or `/department/[slug]`  
3. For each exam stub: pattern (prelims/mains), marks, negative marking, syllabus PDF **official link only**  
4. Link `/free-study-material`, `/government-exam-calendar`, `/daily-assessment`  
5. ItemList schema for exam links  

## Update existing

- **UPDATE** `51_EXAM_PREPARATION_HUB/SECTION_SPEC.md` implementation on homepage to link “Syllabus & Pattern” → this hub.  
- **Do not delete** individual exam pages.
