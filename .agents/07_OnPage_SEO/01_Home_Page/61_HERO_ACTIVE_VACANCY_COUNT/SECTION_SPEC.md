# Section 61 - Hero Active Vacancy Count

**Competitor:** MSN hero “Explore over **2,270** active central and state vacancies”  
**Placement:** Immediately under or within existing H1 block — **do not remove** current hero text.  
**Priority:** P2  

## Copy pattern

- “Explore **{active_job_count}** active government vacancies (central & state). Updated {last_updated_date}.”  
- Count = DB query: jobs where application deadline ≥ today and status = active. **Never hard-code or inflate.**

## SEO

- Visible text only; optional `numberOfItems` in ItemList elsewhere — do not fake JobPosting aggregate counts.

## Rules

- If count < 100, still show real number.  
- Marathi/English: optional secondary line — keep existing bilingual hero.

## Guardrail

Audit existing hero first; patch, do not rebuild.
