# Jobs page — card messaging and labels (human copy)

Use on `/jobs` and anywhere job cards render. **Do not change card layout** — only labels and link text.

## Card fields to show (when data exists)

| Label | Example |
|-------|---------|
| Recruiting body | “Recruiting body: Naval Dockyard Mumbai” |
| Location | “Location: Mumbai” |
| Vacancies | “Vacancies: 283” |
| Qualification | “Qualification: ITI (trade as per notification)” |
| Last date | “Last date to apply: 16 Oct 2026” |

## Buttons / links

| Control | Exact label | href |
|---------|-------------|------|
| Notification | Official PDF | `notification_url` |
| Application | Apply on official site | `application_url` |
| Detail | View vacancy details | internal job slug |

Never label our domain as “Apply online” if the form is external.

## Badges

- **Closing soon** — ≤ 7 days to last date  
- **New** — published within 48 hours (optional, only if true)  

## Empty states

If filters return zero jobs:

“No active jobs match this filter right now. Try a nearby state or qualification, or browse [all government jobs](/jobs). Some commissions publish in batches — check [Employment News](/employment-news) for the weekly list.”

## State / department filter helper text

Above filters:

“Pick a state or department to narrow results. For a full state list, open [state wise government jobs](/state-government-jobs).”

## Semantic note

Each card: `<article>` with `<h2>` or `<h3>` for title (match existing heading level on page — only one H1 on `/jobs`).
