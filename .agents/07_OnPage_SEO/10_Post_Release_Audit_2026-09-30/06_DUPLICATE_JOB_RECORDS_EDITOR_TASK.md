# Editor task — duplicate job records (title collision)

**Not a dev title bug.** Six pages share titles because **two DB rows** describe the same recruitment.

---

## Pairs to resolve

| Pair | IDs | Issue | Action |
|------|-----|-------|--------|
| SBI duplicate A | **6147** / **6142** | Same posting entered twice, same apply link and date | Mark **one** as duplicate / unpublished; keep one canonical |
| SBI duplicate B | **6146** / **6144** | Same | Same |
| NMU Jalgaon | **6687** / **6280** | Same notice; different last date in DB | Reconcile dates from official PDF; mark one duplicate |

---

## Rules (from release PDF)

- **Do not delete** historical rows without editorial policy approval — prefer:
  - `status = duplicate` + `canonical_job_id` pointer, or  
  - unpublish duplicate + **301** to surviving job slug  
- After merge: re-run title scan — expect **0** duplicate title groups among published jobs

---

## Verification

- Both URLs should not appear as separate active listings on `/jobs`
- Sitemap should list only the surviving canonical job URL
