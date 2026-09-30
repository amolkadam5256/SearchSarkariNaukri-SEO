# Section 63 — Urgent alerts strip (developer full spec)

## Placement

Above or directly under “Ending Soon” (`07_CLOSING_SOON_JOBS`) — **both stay live**.

## H2

Urgent Sarkari alerts

## Intro line

“Time-sensitive notices and high-vacancy recruitments — verify last date on the official notification.”

## List content (max 10 items, `[DYNAMIC]`)

Mix sources in this order:

1. **Latest Employment News issue** — title from DB, link to `/employment-news` and external official issue URL.  
2. **Jobs** where `vacancies >= 100` OR `urgent_flag = true` OR last date within 5 days.  
3. Static fallback if empty: link to `/employment-news` + `/jobs`.

## Row format (semantic)

```html
<article>
  <h3><a href="job_url">[Post title — org — year]</a></h3>
  <p><span>Last date:</span> <time datetime="…">…</time> · [vacancies] posts · [city optional]</p>
</article>
```

## Badge copy

- “Closing soon” if ≤ 7 days  
- “High vacancies” if ≥ 100 posts  

## Messaging

- Employment News row label: “Employment News — [issue label]”  
- Do not say “apply here on SearchSarkariNaukri”

## Internal links footer

“All job alerts → `/job-updates`” · “Employment News hub → `/employment-news`”

## QA

- [ ] Job URLs pass slug/ID integrity check (P0 regression)  
- [ ] EN link uses official domain  
