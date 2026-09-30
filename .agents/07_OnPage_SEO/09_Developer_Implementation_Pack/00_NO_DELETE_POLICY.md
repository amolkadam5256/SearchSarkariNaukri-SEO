# Mandatory policy — do not delete anything

**Applies to:** All SearchSarkariNaukri SEO and on-page work (competitor gap, new hubs, homepage sections, jobs page, fixes).

**Effective:** 30 September 2026  
**Owner instruction:** TR — *do not delete any content, page, or section.*

---

## What you must NOT do

| Category | Forbidden |
|----------|-----------|
| **Pages / routes** | Removing URLs, unpublishing hubs, merging by deleting the old URL without 301, taking down expired job pages |
| **Homepage** | Removing or hiding sections (01–60 or newer 61–64), shortening by deleting blocks, “simplifying” by dropping FAQs or hubs |
| **Jobs / DB** | Deleting job records, slugs, or IDs to “clean SEO” |
| **Copy** | Stripping paragraphs, FAQs, Marathi/English blocks, trust disclaimers, or footer legal text |
| **Nav / footer** | Removing existing menu or footer links (only **add** links) |
| **Media** | Deleting images or PDF references on live pages |
| **Sitemap** | “Delete pages” via sitemap removal **as a substitute for deleting the live page** — exclude from sitemap only when the **page stays live** with intentional noindex |

---

## What you MAY do (allowed fixes)

- **Add** new pages, sections, links, metadata, schema, and copy blocks.  
- **Update** titles, descriptions, and body text **by expanding or correcting** — keep the old information unless it is factually wrong (then correct in place).  
- **301 redirect** only when two URLs are true duplicates and the **old URL must remain reachable** via redirect (content preserved on target).  
- **noindex,follow** on thin or duplicate URLs while **keeping the page live** for users.  
- **Fix** wrong data (dates, org names) on the same URL.  
- **Hide from sitemap** expired jobs while **keeping** the job detail page with “deadline passed” messaging.

---

## Competitor / SEO work

MySarkariNaukri gap work is **additive only**. New hubs (`/employment-news`, `/answer-keys`, etc.) and homepage sections 61–64 **sit beside** existing content — they do not replace it.

---

## Sign-off (developer)

Before deploy, confirm in PR notes:

- [ ] No routes removed from router  
- [ ] No homepage sections removed from render tree  
- [ ] No job rows deleted for indexation cleanup  
- [ ] No footer/nav links removed  
- [ ] Changelog lists **added/updated** items only  

If a stakeholder asks to delete for SEO, escalate — default answer is **noindex, redirect, or expand**, not delete.

---

**Read with:** `00_MASTER_DEVELOPER_HANDOFF.md`, `01_BRAND_MESSAGING_AND_VOICE.md`
