# Section 64 - Featured High-Vacancy Openings

**Competitor:** MSN “Featured Sarkari Openings 2026” (PRL, NaBFID, Ministry of Culture + “View All Central Jobs”)  
**Priority:** P2  

## Selection rule

- Query jobs with `vacancies >= 50` OR top 4 by vacancy count nationally (exclude expired).  
- Prefer central recruitments (UPSC, SSC, RRB, PSU) for parity with MSN; **include** Maharashtra mega posts when in top N.

## Card fields (match MSN SEO signals)

- City / location  
- Vacancy count badge  
- H3 title (org + post + year)  
- 1-line “Recruiting Body” teaser  
- Last date  
- **PDF** → official notification URL (label “Official PDF”)  
- **View & Apply** → official application URL  

## Section copy

- H2: `Featured Sarkari Openings 2026`  
- Subtext: `Prominent national recruitments with high vacancies`  
- Footer link: `View all central government jobs →` → `/central-government-jobs` or `/category/...` if live  

## Schema

- ItemList of ListItem → job URLs; JobPosting remains on detail pages only.

## Guardrail

Same card component as `/jobs` if possible — **no new visual design system**.
