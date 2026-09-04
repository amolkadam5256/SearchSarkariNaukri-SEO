# Production Server Read-Only Evidence — Withheld From Public Repository

This evidence file exists in the full audit package but is **not published in this repository**.

The repository is public. The original file documents production infrastructure detail —
Nginx document root, the internal prerender upstream port, the PM2 process name, and the
current response-header configuration including which security headers are and are not set.
Publishing that detail on the public web serves no SEO purpose and gives unnecessary
information to anyone probing the server.

## What it covered

The file recorded a read-only SSH inspection performed on 25 August 2026. Nothing on the
server was changed. Its findings were used as evidence for the following audit conclusions,
which are fully stated in the published reports:

- TLS, HTTP/2, gzip, and static-asset caching behavior (`01-technical-seo-audit-REPORT.md`).
- Apex-to-`www` 301 canonicalization and trailing-slash handling.
- Bot prerender coverage, including which crawler and AI user-agents are recognized.
- The analytics-tag difference between prerendered bot HTML and ordinary browser HTML
  (`13-analytics-tracking-audit-REPORT.md`).
- Access-log format limitations that prevent per-host historic bot-hit separation.

## How to get it

The unredacted file is held with the developer copy of the audit package. Request it from the
development team through a private channel if it is needed for verification.
