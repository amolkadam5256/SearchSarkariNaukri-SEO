# 21 — Monitoring, CRO & Operational Cadence

## 21.1 Conversion Rate Optimization (CRO) Guidelines

```
Candidate Visits Page (100%)
    │
    ├── Reads Eligibility & Fee Details (80% target)
    │       │
    │       ├── Clicks "Apply Online" (15–20% target) ───> Primary Goal: Outbound Conversion
    │       │
    │       ├── Subscribes to Job Alerts (8–12% target) ──> Secondary Goal: Retention
    │       │
    │       └── Shares Job via WhatsApp (3–5% target) ───> Viral Growth
    │
    └── Bounce Rate (< 25% target)
```

### Call-to-Action (CTA) Placement Rules
- **Top CTA Banner:** High-contrast "Apply Online — Last Date: [Date]" button placed above the fold on mobile and desktop.
- **Mobile Sticky Bar:** Fixed bottom bar on mobile screens featuring 1-click "Apply Now" and "Join Telegram Channel" buttons.
- **Inline Alert Injections:** Telegram/WhatsApp subscription banners injected immediately below the main Vacancy Table.

---

## 21.2 Operational Cadence Schedule

| Cadence | Responsible Role | Scope of Tasks | Target SLA |
|---------|------------------|----------------|------------|
| **Daily** | Dev Ops / SEO Tech | Monitor Uptime (UptimeRobot), TTFB (< 200ms), Instant Indexing API pushes, 5xx server log errors | Uptime > 99.9% |
| **Weekly** | SEO Lead | Inspect GSC Page Indexing errors, review GA4 `apply_click` conversion rates, triage CTR for positions 3–10 | Fix errors < 48h |
| **Monthly** | SEO & Content Team | Execute full site crawl (Screaming Frog), backlink audit & disavow update, audit stale content (> 90 days) | 100% stale content updated |
| **Quarterly** | Management & SEO Lead | Full E-E-A-T audit, competitor gap analysis, strategy review, 90-day roadmap adjustment | Executive sign-off |
