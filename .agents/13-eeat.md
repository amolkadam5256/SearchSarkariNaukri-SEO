# 13 — E-E-A-T & Trust Infrastructure

## 13.1 Mandated Trust Pages & Content Requirements

| Page Title | Target URL | Mandatory Content Requirements |
|------------|------------|--------------------------------|
| **About Us** | `/about-us` | Company mission statement, history, team overview, founding year, physical address |
| **Contact Us** | `/contact-us` | Office address, official contact email, support form, 24-hour response SLA |
| **Privacy Policy** | `/privacy-policy` | GDPR & Indian IT Act compliant policy detailing cookie usage and data protection |
| **Terms of Service** | `/terms-of-service` | User terms, intellectual property, service agreements, liability disclaimers |
| **Disclaimer** | `/disclaimer` | Clear notice: *"SearchSarkariNaukri.com is an independent news portal and is not affiliated with any government department."* |
| **Editorial Policy** | `/editorial-policy` | How job listings are sourced, verified, written, and published |
| **Fact-Check Policy** | `/fact-check-policy` | Multi-step verification against official `.gov.in` PDFs before publication |
| **Corrections Policy** | `/corrections-policy` | Procedure for reporting, correcting, and logging factual updates |

---

## 13.2 Author Profile & Byline Standards

Every published article and job listing MUST feature an Author Byline linking to a dedicated Author Profile page (`/author/[author-name]`):

```html
<!-- Author Byline HTML Component -->
<div class="author-byline">
  <img src="/images/authors/author-headshot.webp" alt="Author Full Name" width="60" height="60" loading="lazy" />
  <div class="author-meta">
    <span>Written by <a href="/author/author-name"><strong>Author Full Name</strong></a></span>
    <p>Government Recruitment Specialist | Updated: July 23, 2026</p>
  </div>
</div>
```

### Author Profile Page Requirements
- Full legal name (no anonymous aliases).
- High-resolution professional headshot.
- 150-word bio detailing recruitment domain expertise and educational background.
- Social profile links (LinkedIn, X/Twitter).
- List of articles written by this author.
- `Person` schema markup.

---

## 13.3 12-Point E-E-A-T Quality Checklist

- [ ] 1. Dedicated About Us page is live and accessible via footer.
- [ ] 2. Dedicated Contact Us page displays real contact details.
- [ ] 3. Disclaimer banner prominently displayed on every job page ("Not an official government website").
- [ ] 4. All job listings cite and link directly to official government PDF notifications.
- [ ] 5. Every post features a named author with a verified profile page.
- [ ] 6. Editorial, Fact-Check, and Corrections policies published.
- [ ] 7. "Last Updated" date visible on all content pages.
- [ ] 8. HTTPS enforced sitewide with valid SSL certificate.
- [ ] 9. Privacy Policy and Terms of Service updated for 2026.
- [ ] 10. No misleading clickbait titles or deceptive ad placements.
- [ ] 11. Content verified against primary government sources prior to publishing.
- [ ] 12. Author profile pages include `Person` schema markup.
