# 6. Security Headers — Content-Security-Policy (CSP)

**Priority: 🟠 Medium**

## The problem
Current header status:
| Header | Status |
|---|---|
| Strict-Transport-Security | ✅ Present |
| X-Content-Type-Options | ✅ Present |
| X-Frame-Options | ✅ Present |
| Referrer-Policy | ✅ Present |
| Permissions-Policy | ✅ Present |
| **Content-Security-Policy** | ❌ **Missing** |

This was also flagged independently by PageSpeed Insights' Best Practices
audit ("Ensure CSP is effective against XSS attacks", "Mitigate DOM-based
XSS with trusted types"). Without a CSP, the site has no browser-enforced
allowlist for what scripts/styles/frames are permitted to run — a
mitigating control against cross-site scripting (XSS) attacks.

## The fix
Because this site loads many third-party scripts (Google Tag Manager,
Google Analytics, AdSense, Microsoft Clarity, Ahrefs Analytics), the CSP
needs to explicitly allowlist each of them. Start in **report-only** mode
first so you can see what would be blocked before enforcing it.

### Step 1 — Report-only CSP (safe, doesn't block anything yet)
Add this response header (e.g. in Nginx, or in your app's HTML `<meta>`
if you can't set response headers):
```nginx
add_header Content-Security-Policy-Report-Only "
  default-src 'self';
  script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://www.google-analytics.com https://pagead2.googlesyndication.com https://www.clarity.ms https://analytics.ahrefs.com;
  style-src 'self' 'unsafe-inline';
  img-src 'self' data: https:;
  font-src 'self' data:;
  connect-src 'self' https://www.google-analytics.com https://analytics.ahrefs.com https://www.clarity.ms;
  frame-src https://www.googletagmanager.com https://pagead2.googlesyndication.com https://googleads.g.doubleclick.net;
  object-src 'none';
  base-uri 'self';
  report-uri /csp-violation-report;
" always;
```
Monitor `/csp-violation-report` (or your browser console — CSP-Report-Only
violations show up there too) for a week to catch anything the policy
would incorrectly block (e.g. an AdSense sub-domain not yet allowlisted).

### Step 2 — Switch to enforcing mode
Once the report-only policy runs clean for ~1–2 weeks with no unexpected
violations, change the header name to enforce it:
```nginx
add_header Content-Security-Policy "
  default-src 'self';
  script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://www.google-analytics.com https://pagead2.googlesyndication.com https://www.clarity.ms https://analytics.ahrefs.com;
  style-src 'self' 'unsafe-inline';
  img-src 'self' data: https:;
  font-src 'self' data:;
  connect-src 'self' https://www.google-analytics.com https://analytics.ahrefs.com https://www.clarity.ms;
  frame-src https://www.googletagmanager.com https://pagead2.googlesyndication.com https://googleads.g.doubleclick.net;
  object-src 'none';
  base-uri 'self';
" always;
```

### Notes specific to your stack
- `'unsafe-inline'` is included for `script-src`/`style-src` because your
  GTM snippet and (per the audit) some inline styles run inline. This
  weakens the XSS protection somewhat — the stronger long-term approach is
  to migrate to **nonce-based** or **hash-based** CSP (generate a random
  nonce per request, add `nonce="..."` to your inline `<script>` tags, and
  use `script-src 'self' 'nonce-<value>'` instead of `'unsafe-inline'`).
  This requires server-side templating support to inject a fresh nonce per
  request — worth doing once file 01 (SSR) is in place, since a
  server-rendering setup makes per-request nonces easy to add.
- AdSense in particular loads scripts from several Google ad domains
  (`googlesyndication.com`, `doubleclick.net`, `googleadservices.com`) —
  test thoroughly in report-only mode, as ad networks are the most common
  source of CSP breakage.

## Also address (Best Practices audit)
- [ ] **Trusted Types for DOM XSS mitigation** — add
  `require-trusted-types-for 'script';` to the CSP once the main policy is
  stable; this requires auditing any code that writes to `innerHTML` /
  `document.write` and wrapping it in a Trusted Types policy. Do this as a
  follow-up after the base CSP is live, not in the same deploy.
- [ ] **Strengthen HSTS** — current header is
  `max-age=31536000; includeSubDomains`. Consider adding `preload` once
  you're confident all subdomains (including `api.searchsarkarinaukri.com`,
  which is in your certificate's Subject Alternative Names) are
  HTTPS-only, then submit to https://hstspreload.org/:
  ```nginx
  add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
  ```

## Verification
- [ ] Re-scan with securityheaders.com after deployment — target grade A.
- [ ] Re-run PageSpeed Insights Best Practices audit — the CSP and
      Trusted Types findings should clear.
- [ ] Manually click through the site (job apply flow, ads visible,
      analytics firing in GA4 real-time report) to confirm nothing broke.
