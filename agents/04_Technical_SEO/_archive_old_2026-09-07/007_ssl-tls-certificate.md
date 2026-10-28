# 7. SSL/TLS Certificate & CAA

**Priority: 🟠 Medium (renewal) / 🟢 Low (CAA)**

## The problem
| Item | Detail |
|---|---|
| Certificate issuer | Let's Encrypt (YE1) |
| Valid from → to | 3 Jul 2026 → 1 Oct 2026 |
| Validity window | ~90 days (standard for Let's Encrypt) |
| Days remaining (at report date) | ~54 days |
| DNS CAA record | Not present |

Let's Encrypt certificates are always short-lived by design, which is fine
**as long as renewal is automated** — but this needs explicit
confirmation, since a lapsed certificate would take the entire site
offline for both users and Googlebot.

## Fix 1 — Confirm/set up auto-renewal
If using **Certbot** (the standard Let's Encrypt client) on this Nginx/Ubuntu
server:
```bash
# Check if a renewal timer/cron job already exists
systemctl list-timers | grep certbot
# or
crontab -l | grep certbot

# If nothing is scheduled, set up the systemd timer (usually installed by default with certbot)
sudo systemctl enable --now certbot.timer

# Test that renewal works without actually renewing yet
sudo certbot renew --dry-run
```
- [ ] Confirm the dry run succeeds with no errors.
- [ ] Confirm Nginx is reloaded automatically after renewal (Certbot's
      default hooks usually handle this, but verify):
```bash
sudo cat /etc/letsencrypt/renewal/searchsarkarinaukri.com.conf | grep deploy_hook
```
  If no reload hook exists, add one:
```bash
sudo certbot renew --deploy-hook "systemctl reload nginx"
```
- [ ] Set a calendar reminder for ~2 weeks before expiry (mid-September
      2026) to manually verify the cert renewed, as a backup to automation.

## Fix 2 — Add a DNS CAA record (defense-in-depth, low priority)
A CAA (Certification Authority Authorization) record restricts which
Certificate Authorities are allowed to issue certificates for your domain,
preventing certificate mis-issuance by an unauthorized CA.

Add this DNS record at your DNS provider (wherever
`searchsarkarinaukri.com`'s DNS is managed):
```
searchsarkarinaukri.com.  IN  CAA  0 issue "letsencrypt.org"
searchsarkarinaukri.com.  IN  CAA  0 issuewild "letsencrypt.org"
searchsarkarinaukri.com.  IN  CAA  0 iodef "mailto:dmarc_rua@onsecureserver.net"
```
(Adjust the `iodef` contact to whichever mailbox should receive
mis-issuance reports — you already have one configured for DMARC
reporting, reuse it if appropriate.)

## Verification
```bash
# Confirm CAA record is live
dig CAA searchsarkarinaukri.com +short

# Re-check full chain and grade via SSL Labs
# https://www.ssllabs.com/ssltest/analyze.html?d=www.searchsarkarinaukri.com
```
- [ ] SSL Labs grade stays A (or improves) after changes.
- [ ] Certificate expiry date rolls forward automatically after the next
      renewal cycle without manual intervention.
