# 8. Email Authentication — SPF (DMARC already present)

**Priority: 🟠 Medium**

## The problem
| Record | Status |
|---|---|
| DMARC | ✅ Present — `v=DMARC1; p=quarantine; adkim=r; aspf=r; rua=mailto:dmarc_rua@onsecureserver.net;` |
| SPF | ❌ **Missing** |

Having DMARC set to `p=quarantine` **without** a matching SPF record
undermines the DMARC policy itself — SPF alignment is one of the two
mechanisms (the other is DKIM) that DMARC checks to decide whether an
email is legitimate. Without SPF, you're relying on DKIM alone, and any
mail sent without DKIM signing (or with DKIM broken by a relay) has no
fallback authentication — increasing the chance your legitimate mail
(contact-form notifications, job-alert emails, transactional mail) lands
in spam, and doing less to stop attackers from spoofing your domain.

## The fix
1. **Identify every legitimate sender for `searchsarkarinaukri.com`**
   email — e.g.:
   - Your own mail server / hosting provider's outbound mail
   - Any transactional email service (SendGrid, Mailgun, Amazon SES,
     Brevo, etc.) if used for job-alert or contact-form emails
   - Google Workspace, if used for `@searchsarkarinaukri.com` mailboxes

2. **Publish one SPF TXT record** at the domain apex (only one SPF record
   is allowed per domain — merge all senders into a single record using
   `include:`):
```
searchsarkarinaukri.com.  IN  TXT  "v=spf1 include:_spf.google.com include:sendgrid.net ~all"
```
   (Replace `include:_spf.google.com` / `include:sendgrid.net` with
   whichever services you actually use — remove ones that don't apply,
   add others as needed. Common includes:
   - Google Workspace → `include:_spf.google.com`
   - SendGrid → `include:sendgrid.net`
   - Mailgun → `include:mailgun.org`
   - Amazon SES → `include:amazonses.com`
   - cPanel/shared hosting's own mail → usually just the server's own IP,
     e.g. `ip4:157.245.102.177`)

3. Use `~all` (soft fail) initially rather than `-all` (hard fail) while
   you confirm every real sender is captured — hard-fail can cause
   legitimate mail to be rejected if you missed an `include`.

## Verification
```bash
dig TXT searchsarkarinaukri.com +short | grep spf1
```
- [ ] Send a test email from each real sending source (contact form,
      job-alert system, any Google Workspace mailbox) to
      https://www.mail-tester.com/ or a Gmail account, and check the
      "Authentication-Results" header shows `spf=pass`.
- [ ] After ~2–4 weeks of clean SPF+DKIM alignment with no legitimate mail
      failing, consider tightening DMARC from `p=quarantine` toward
      `p=reject` for maximum anti-spoofing protection — only do this once
      you're confident every legitimate sender passes SPF or DKIM.
- [ ] Check the DMARC aggregate reports (sent to
      `dmarc_rua@onsecureserver.net`) after SPF is live — they'll show
      pass/fail rates across real-world mail flows and confirm nothing is
      being incorrectly blocked.
