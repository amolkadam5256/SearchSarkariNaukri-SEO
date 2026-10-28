# 09 — Content Quality & E-E-A-T Audit

Output file: `outputs/final-reports/09-content-eeat-audit-REPORT.md`
E-E-A-T = Experience, Expertise, Authoritativeness, Trustworthiness — Google's
framework for evaluating content quality, especially critical for YMYL-adjacent
sites (job/career decisions affect people's livelihoods).

## A. Duplicate / Repeated Content Bug (verify the live finding first)
- [ ] Re-verify and root-cause the repeated identical entries spotted on the
  homepage (see `00-live-seed-findings.md` #1): "SBI CBO Result 2026" ×5,
  "MPSC Rajyaseva Result 2026" ×3, "MPSC Result 2026" ×2, "UPSC CSE Admit
  Card 2026" ×5. Confirm: is this a database duplicate (same row inserted
  multiple times), a template loop bug, or a caching issue? Document exact
  reproduction steps and affected page(s).
- [ ] Site-wide duplicate content scan (crawler "near duplicate content"
  report) — export all page pairs above 80% similarity

## B. Thin Content
- [ ] List every page under 150–200 words with no other substantial value
  (tables, schema, unique data)
- [ ] Assess whether expired/closed job listings degrade into thin
  "unavailable" pages that should be consolidated, redirected, or clearly
  archived instead of left as low-value indexable pages

## C. E-E-A-T Signals
- [ ] "About Us" page present, describes the organization, its purpose, and
  editorial/fact-checking process
- [ ] Author/editorial attribution present on content (even if just an
  "Editorial Team" byline with a bio page) — currently appears fully
  unattributed; flag as a trust gap
- [ ] Contact page with real contact information (email/phone/address) present
- [ ] Privacy Policy, Terms of Service, and a clear "not a government website"
  disclaimer present (disclaimer already spotted on homepage FAQ — verify it's
  also present prominently in the footer of every page, not just buried in FAQ)
- [ ] Source attribution present per job listing (link to official
  notification PDF/source — spot-check that links go to real, current
  official pages, not broken or generic homepage links)
- [ ] Fact accuracy spot-check: pick 10 random live job listings, compare
  vacancy count / dates / eligibility against the actual official notification
  — report any discrepancies found (accuracy is critical trust signal for this content type)

## D. Content Freshness & Maintenance
- [ ] Confirm "last updated" timestamps are real and automated, not static/fake
- [ ] Check for a visible content review/removal policy for expired
  opportunities (stale content harms trust and rankings)

## E. Readability
- [ ] Run a readability check (Flesch-Kincaid or similar) on sample pages —
  content should be clear and accessible given the broad candidate audience
  (10th-pass through graduate-level readers)
- [ ] Bilingual content reviewed for quality — confirm Marathi content is
  natural, not raw machine translation (spot-check with a native speaker or
  translation-quality tool)
