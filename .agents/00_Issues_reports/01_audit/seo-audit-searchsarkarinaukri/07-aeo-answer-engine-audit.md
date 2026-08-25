# 07 — AEO (Answer Engine Optimization) Audit
### AEO = being surfaced as THE direct answer inside Google's own answer surfaces
(Featured Snippets, People Also Ask, Voice Search / Assistants, SGE/AI Overviews inline answer box)

Output file: `outputs/final-reports/07-aeo-answer-engine-audit-REPORT.md`

## A. Featured Snippet Opportunity Audit
- [ ] Pull GSC Performance report, filter queries currently ranking positions
  2–10 that are question-phrased ("how to apply for...", "what is the age
  limit for...", "is X a government job") — export list with impressions
- [ ] For each opportunity query, check if the page currently answers it in a
  **snippet-extractable format** in the first 100–150 words: direct answer
  sentence, ordered list, or table
- [ ] Check current featured snippet holder (who owns it now) for each query —
  is it a competitor or already this site?

## B. Question-Answer Content Structure
- [ ] Confirm each FAQ question on the homepage/category pages is phrased the
  way real users search (match to GSC query data, not guessed phrasing)
- [ ] Confirm each FAQ answer leads with a **direct, self-contained answer** in
  the first sentence (definition-style: "X is..." / "Yes/No, ...") before
  elaboration — this is required for snippet extraction
- [ ] Check answer length: ideal 40–60 words for paragraph snippets, 5–8 items
  for list snippets, 2–4 columns for table snippets

## C. Voice Search Readiness
- [ ] Check for natural-language, conversational phrasing on key
  informational pages (voice queries are longer and more conversational than
  typed queries — e.g. "when is the last date to apply for talathi bharti"
  vs typed "talathi bharti last date")
- [ ] Confirm local/time-sensitive facts (dates, deadlines, districts) are
  stated in plain unambiguous sentences a voice assistant/AI Overview can
  extract confidently (avoid ambiguous relative dates like "next week" —
  always state the actual date)

## D. "People Also Ask" (PAA) Opportunity Mapping
- [ ] For top 20 target queries, pull the current PAA box questions (manual
  SERP check or tool like Ahrefs/Semrush "Also Ask")
  and check whether the site's content answers each PAA question anywhere on
  the relevant page — flag gaps to add

## E. AI Overview (Google SGE) Presence Check
- [ ] For top 20 target queries, manually check (logged-in India SERP) whether
  an AI Overview box appears, and if so:
  - Is this site cited as a source? (Y/N)
  - Which competitor domains ARE cited?
  - What content format/structure do the cited sources use that this site
    currently lacks?

## F. Technical Enablers for AEO
- [ ] Confirm `max-snippet:-1` is set in meta robots (already confirmed present
  on homepage — verify site-wide, since a restrictive `max-snippet` value
  blocks snippet eligibility)
- [ ] Confirm `FAQPage` / `HowTo` / `QAPage` schema implemented where content
  format matches (cross-ref file `04`)
- [ ] Confirm page speed/CWV isn't disqualifying otherwise-eligible content
  (cross-ref file `06` — slow pages are deprioritized for snippet eligibility)
