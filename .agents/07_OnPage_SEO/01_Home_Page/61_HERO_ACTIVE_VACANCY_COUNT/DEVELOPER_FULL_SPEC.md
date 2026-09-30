# Section 61 — Hero active vacancy count (developer full spec)

## Where to add

Inside the **existing hero**, below the main H1 or the current subtitle — **do not replace** the H1 “Sarkari Naukri 2026…”.

## Dynamic data

```text
active_job_count = COUNT(jobs WHERE last_date >= TODAY AND status = active)
last_updated = MAX(jobs.updated_at) formatted for India locale
```

## Visible copy (template)

**Line 1 (keep existing hero headline as H1).**

**Line 2 (new paragraph or strong):**  
“Right now we show **[active_job_count] open government recruitments** you can still apply for — central and state. List refreshed **[last_updated]**.”

**Line 3 (trust, small text):**  
“Figures come from notices we track. Closing dates can change in the official PDF — always confirm there before you apply.”

## Semantic HTML

Wrap line 2 in `<p class="hero-lead">`. Wrap count in `<span data-job-count="…">` for optional analytics. Do not use `<h2>` in hero.

## SEO

- Do not stuff keywords in the count line.  
- Optional `dateModified` on WebPage from `last_updated`.

## Do not

- Hard-code “2,270” or competitor numbers.  
- Remove “Last updated” line already on homepage if present — merge into one clear date.

## QA

- [ ] Count matches `/jobs` filtered active set within tolerance  
- [ ] Shows 0 gracefully: “No open applications today — browse recent notices anyway”
