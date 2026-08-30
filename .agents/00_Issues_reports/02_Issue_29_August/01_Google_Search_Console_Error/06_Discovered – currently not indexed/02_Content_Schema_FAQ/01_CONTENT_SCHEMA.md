# Admit Card Detail Page â€” Content/Data Schema

Each record should supply as many of these fields as are actually known:

- id
- exam_name
- year
- status
- exam_date
- admit_card_release_date
- last_updated
- conducting_authority
- official_domain
- official_admit_card_url
- official_notification_url
- city_intimation_url
- exam_centre_info
- application_url
- credentials_required
- documents_required
- exam_instructions
- related_exam_slug
- related_result_slug
- related_job_slug
- related_admit_card_ids

### Content generation rule
Every section must be generated from the record. Missing fields should cause that section to be omitted or qualified, not filled with invented facts.

### Recommended section order
1. H1
2. Status summary
3. Important dates
4. How to download/check
5. Official source
6. What to keep ready
7. What appears on the admit card
8. Documents/items to carry
9. Exam-day instructions
10. Download troubleshooting
11. City intimation / exam centre (conditional)
12. Related updates
13. 10â€“15 FAQs
14. Verification note
15. Last updated
## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, site-wide layout, global styling, tracking setup, analytics setup, or shared components unless strictly required for admit-card indexing/content architecture. Do not mass-publish thin duplicate content just to make discovered URLs indexable.
