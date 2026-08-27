# SearchSarkariNaukri.com — Homepage Section 16: How It Works Specification

**Section Name:** `16_How_It_Works`  
**Page:** Homepage `/` only  
**Section Position:** Immediately after `15_Alerts` and before `17_Verification`  
**Purpose:** Provide transparent 3-step onboarding for first-time aspirants, establishing confidence, clear user flow, and reducing bounce rates.  
**Status:** Ready for Implementation  

---

## 1. Scope & UX Purpose

### Target Keywords & User Questions
- `How to find government jobs online`, `How SearchSarkariNaukri works`, `How to apply for Sarkari Naukri online step by step`.

---

## 2. The 3-Step Candidate Journey

1. **Step 1: Search & Filter** — Filter by your qualification (10th/12th/Graduate), location (Maharashtra/District), or exam type.
2. **Step 2: Verify Official Notification** — Review eligibility, age relaxation, salary scale, and download the official government gazette PDF.
3. **Step 3: Direct Official Application** — Follow step-by-step guides and click directly to the official government portal to apply securely.

---

## 3. UI/UX Wireframe Structure

```html
<section id="how-it-works" class="section-how" aria-labelledby="how-heading">
  <div class="container">
    <div class="section-header">
      <h2 id="how-heading">How SearchSarkariNaukri Works — 3 Simple Steps</h2>
      <p>Your transparent guide from discovering a vacancy to submitting your official application.</p>
    </div>

    <div class="how-steps-grid">
      <!-- Step 1 -->
      <div class="step-card">
        <div class="step-number">01</div>
        <h3>Search & Filter</h3>
        <p>Find matching vacancies by selecting your education, district, department, or preferred exam.</p>
      </div>

      <!-- Step 2 -->
      <div class="step-card">
        <div class="step-number">02</div>
        <h3>Verify Details</h3>
        <p>Cross-check age limits, syllabus, vacancy counts, and download the official PDF advertisement.</p>
      </div>

      <!-- Step 3 -->
      <div class="step-card">
        <div class="step-number">03</div>
        <h3>Apply on Official Site</h3>
        <p>Use our direct verified portal links to submit your application form accurately and safely.</p>
      </div>
    </div>
  </div>
</section>
```
