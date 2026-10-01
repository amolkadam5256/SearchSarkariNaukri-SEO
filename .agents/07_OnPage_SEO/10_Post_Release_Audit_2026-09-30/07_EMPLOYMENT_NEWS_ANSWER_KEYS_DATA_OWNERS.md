# Data owners — Employment News & Answer Keys hubs

**Status:** Spec ready in repo; **not live** (30 Sep release explicitly skipped broken links).

| Hub | Route | Spec folder | Blocker |
|-----|-------|-------------|---------|
| Employment News | `/employment-news` | `08_Standalone_Pages/01_EMPLOYMENT_NEWS_HUB/` | Official EN feed / curation owner |
| Answer Keys | `/answer-keys` | `08_Standalone_Pages/02_ANSWER_KEYS_HUB/` | Source for provisional/final keys per exam |

---

## Employment News — what “data owner” must provide

- Update frequency (weekly PDF vs daily HTML on employmentnews.gov.in)
- Which fields to store: issue date, post title, org, link to PDF, page reference
- Legal: link out to official EN; do not republish full PDF without permission policy check
- Homepage **§63 urgent strip** depends on this feed (`63_URGENT_ALERTS_EMPLOYMENT_NEWS`)

---

## Answer Keys — what “data owner” must provide

- Per-exam rows: commission, exam name, provisional/final key URL, objection window
- Rule: only link **official** `.gov.in` / `.nic.in` key pages
- Guide page currently says “commission website” — correct until hub exists

---

## Interim (live today)

- Guide → editorial policy for verification  
- Answer key step → official commission sites  
- Do **not** add `/answer-keys` or `/employment-news` to nav until pages return 200

---

## Assign

| Role | Name | Hub |
|------|------|-----|
| Employment News owner | _TBD_ | EN |
| Answer Keys owner | _TBD_ | AK |
| Dev implementer | _TBD_ | Both after data pipeline defined |
