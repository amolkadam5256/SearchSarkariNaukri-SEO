# SearchSarkariNaukri.com — Homepage Section 21: Trust, EEAT Authority & Disclaimer Specification

**Section Name:** `21_Trust`  
**Page:** Homepage `/` only  
**Section Position:** Final homepage section before standard site footer  
**Purpose:** Ensure strict Google Search Quality Rater & EEAT compliance through transparent editorial disclaimers, contact details, corrections policy, and trust badges.  
**Status:** Ready for Implementation  

---

## 1. Scope & Compliance Purpose

### Quality Rater & EEAT Pillars
1. **Clear Identity & Transparency:** Explicit disclosure that SearchSarkariNaukri is an informational aggregation portal, not a government body.
2. **Editorial Verification Standards:** Explaining how notices are sourced directly from verified government bodies.
3. **Editorial Contact & Corrections Policy:** Providing a direct email for users or government departments to request corrections or updates within 24 hours.

---

## 2. Disclaimer Content (Standardized)

> **Official Disclaimer:** SearchSarkariNaukri.com is an independent news and employment information platform. We are not associated with any central, state, or municipal government agency. All recruitment advertisements, dates, exam patterns, and qualification requirements are sourced from official government notifications (.gov.in / .nic.in). Candidates are strongly advised to cross-verify all details on the official recruitment website before submitting applications or fees.

---

## 3. UI/UX Wireframe Structure

```html
<section id="trust-authority" class="section-trust" aria-labelledby="trust-heading">
  <div class="container">
    <div class="trust-grid">
      <!-- Card 1: Editorial Policy -->
      <div class="trust-card">
        <div class="trust-icon">📋</div>
        <h3>Editorial Standards</h3>
        <p>Our team cross-references each job notification with authentic gazette releases and official department portals before publication.</p>
      </div>

      <!-- Card 2: 100% Free Public Service -->
      <div class="trust-card">
        <div class="trust-icon">🆓</div>
        <h3>100% Free Access</h3>
        <p>SearchSarkariNaukri does not charge candidates any application or processing fees. Beware of fraudulent agents.</p>
      </div>

      <!-- Card 3: Corrections & Contact -->
      <div class="trust-card">
        <div class="trust-icon">✉️</div>
        <h3>Corrections & Feedback</h3>
        <p>Noticed an error? Report discrepancies directly to our editorial desk at <a href="mailto:support@searchsarkarinaukri.com">support@searchsarkarinaukri.com</a>.</p>
      </div>
    </div>

    <div class="disclaimer-banner">
      <p><strong>Disclaimer:</strong> SearchSarkariNaukri.com is an independent career guidance and recruitment informational portal. We do not conduct recruitment or charge any fees. Always verify details on the respective official government portal.</p>
    </div>
  </div>
</section>
```
