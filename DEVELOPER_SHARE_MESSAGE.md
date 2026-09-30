# Message to share with developer (copy below)

---

**Subject: SearchSarkariNaukri — competitor SEO implementation pack (add only, no deletes)**

Hi,

We added a full **MySarkariNaukri vs SearchSarkariNaukri** audit and step-by-step implementation docs in the repo **`SearchSarkariNaukri-SEO`**. Please read and implement from there.

**Start here (mandatory):**
1. `.agents/07_OnPage_SEO/09_Developer_Implementation_Pack/00_NO_DELETE_POLICY.md` — **do not delete any page, section, content, or nav link**; only add/update/fix.
2. `.agents/07_OnPage_SEO/09_Developer_Implementation_Pack/00_MASTER_DEVELOPER_HANDOFF.md` — build order and folder map.
3. `SEO_Audit_Review_2026-09-29/01_REGRESSION_FIX_IMPLEMENTATION_NO_DELETE.md` — **P0:** fix `/sitemap.xml` (currently 500), job URL slug must match page content, then resubmit GSC sitemap.

**New pages to build (human copy + semantic SEO in each folder):**
- `08_Standalone_Pages/01_EMPLOYMENT_NEWS_HUB/` → `/employment-news`
- `08_Standalone_Pages/02_ANSWER_KEYS_HUB/` → `/answer-keys`
- `08_Standalone_Pages/03_EXAM_SYLLABUS_PATTERNS_HUB/` → syllabus hub
- `08_Standalone_Pages/04_CANDIDATE_GUIDANCE_2026/` → guide page
- `08_Standalone_Pages/05_STATE_JOBS_DIRECTORY/` → `/state-government-jobs`

Each folder has **`DEVELOPER_INSTRUCTIONS.md`**, **`PAGE_COPY.md`**, **`SEMANTIC_HTML_AND_SCHEMA.md`**, **`04_QA_CHECKLIST.md`**.

**Homepage (additive sections only):** `01_Home_Page/61_*` through `64_*` — see each folder’s **`DEVELOPER_FULL_SPEC.md`**.

**Jobs page:** `04_Jobs_Page/06_STATE_DEPARTMENT_SEARCH_FILTER.md` and `07_JOB_CARD_MESSAGING_AND_LABELS.md`.

**Wire existing sections (no removal):** `09_Developer_Implementation_Pack/03_EXISTING_SECTIONS_WIRE_AND_COPY_UPDATES.md`  
**Nav/footer links to add:** `09_Developer_Implementation_Pack/02_NAV_AND_FOOTER_LINKS.md`

**Full comparison + sitemap audit:** `SEO_Audit_Review_2026-09-29/03_COMPETITOR_SITEMAP_AND_PAGES_AUDIT.md`  
**Index of all tasks:** `.agents/07_OnPage_SEO/00_Competitor_MySarkariNaukri/IMPLEMENTATION_INDEX.md`

Confirm when P0 is live (sitemap 200 + sample job URLs correct), then ship P1 pages.

Thanks.

---

## Short version (WhatsApp / Slack)

Added full MySarkariNaukri competitor SEO pack in repo **SearchSarkariNaukri-SEO**. **No deletes** — read `09_Developer_Implementation_Pack/00_NO_DELETE_POLICY.md` first. Implement from `00_MASTER_DEVELOPER_HANDOFF.md` + folders under `08_Standalone_Pages/` (Employment News, Answer Keys, Syllabus, Guide, State Jobs) and homepage `61–64`. **P0:** fix sitemap 500 + job slug/content bug (`SEO_Audit_Review_2026-09-29/01_REGRESSION_FIX_IMPLEMENTATION_NO_DELETE.md`). Details: `03_COMPETITOR_SITEMAP_AND_PAGES_AUDIT.md`.
