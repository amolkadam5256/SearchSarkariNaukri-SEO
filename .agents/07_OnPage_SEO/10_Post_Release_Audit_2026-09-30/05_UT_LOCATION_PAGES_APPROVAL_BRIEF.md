# Approval brief — 5 union territory location pages

**Context:** `/state-government-jobs` lists these UTs **without links** (correct per spec: do not remove from grid):

- Andaman and Nicobar Islands  
- Dadra and Nagar Haveli and Daman and Diu  
- Ladakh  
- Lakshadweep  
- Puducherry  

**Already have UT pages (examples):** Delhi, Chandigarh, Jammu and Kashmir.

---

## Proposed routes (match existing state pattern)

| UT | Suggested slug | Notes |
|----|----------------|-------|
| Andaman and Nicobar | `/state/andaman-and-nicobar` or `/location/andaman-and-nicobar` | Follow existing state URL convention in codebase |
| Dadra & Nagar Haveli and Daman & Diu | `/state/dadra-nagar-haveli-daman-diu` | Single UT since merger |
| Ladakh | `/state/ladakh` | |
| Lakshadweep | `/state/lakshadweep` | |
| Puducherry | `/state/puducherry` | |

**Confirm** actual route pattern with dev (grep live `/state/delhi` etc.).

---

## Minimum page template (same as other states)

- H1: `{UT} Government Jobs 2026`
- Dynamic job count from DB (can be zero)
- Link to `/jobs` with location filter when available
- 2–3 sentences on central vs UT recruitment
- Link back to `/state-government-jobs`
- No invented vacancies

---

## Data work

- Add location records / tags so jobs can filter to these UTs  
- Low job count is OK — page still indexable with honest “0 active” + browse all jobs CTA

---

## Approval checklist

- [ ] Approve creating 5 location pages  
- [ ] Confirm URL pattern with dev  
- [ ] Assign who adds location metadata to existing jobs (data/editor)

**After approval:** Implement using `05_districts_Job_Page` or state page template from production repo.
