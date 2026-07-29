# 20 — Security, Headers & Resilience

## 20.1 16-Point Security Audit Checklist

- [ ] 1. HTTPS enforced sitewide with automatic HTTP -> HTTPS 301 redirection.
- [ ] 2. SSL Certificate valid, 256-bit TLS 1.3 enforced, auto-renew active.
- [ ] 3. HSTS Preload header deployed (`Strict-Transport-Security: max-age=31536000; includeSubDomains; preload`).
- [ ] 4. Content-Security-Policy (CSP) header active blocking unauthorized scripts.
- [ ] 5. `X-Frame-Options: SAMEORIGIN` active preventing clickjacking attacks.
- [ ] 6. `X-Content-Type-Options: nosniff` active preventing MIME sniffing.
- [ ] 7. `Referrer-Policy: strict-origin-when-cross-origin` configured.
- [ ] 8. Cloudflare Web Application Firewall (WAF) rules active blocking malicious SQLi/XSS payloads.
- [ ] 9. Cloudflare Bot Management active (verifying Googlebot/Bingbot while blocking scrapers).
- [ ] 10. Automated daily malware and spam scanning via Cloudflare and Safe Browsing APIs.
- [ ] 11. Core CMS/Framework dependencies updated weekly (`npm audit` zero critical vulnerabilities).
- [ ] 12. Automated database snapshots executed every 6 hours and stored in multi-region backup storage.
- [ ] 13. Multi-Factor Authentication (2FA) enforced across all domain, hosting, and webmaster accounts.
- [ ] 14. Origin IP address hidden behind Cloudflare reverse proxy.
- [ ] 15. Server error logs monitored daily for unauthorized intrusion attempts.
- [ ] 16. Incident Response SOP documented and tested.

---

## 20.2 7-Step Incident Response SLA

1. **Detection:** Automated alert triggered via UptimeRobot / Sentry / GSC Security API (< 5 minutes).
2. **Triage:** Isolate compromised endpoints and assess severity (< 15 minutes).
3. **Containment:** Enable maintenance mode and block suspicious IPs on Cloudflare WAF (< 30 minutes).
4. **Eradication:** Patch vulnerability or restore clean server snapshot (< 1 hour).
5. **Verification:** Run comprehensive malware scan and verify 200-OK HTTP status.
6. **Recovery:** Re-enable public traffic and submit GSC review request if needed.
7. **Post-Mortem:** Document root cause, implement preventive rules, update SOPs within 24 hours.
