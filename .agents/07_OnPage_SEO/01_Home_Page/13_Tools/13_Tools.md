# SearchSarkariNaukri.com — Homepage Section 13: Free Sarkari Career & Eligibility Tools Specification

**Section Name:** `13_Tools`  
**Page:** Homepage `/` only  
**Section Position:** Immediately after `12_Exam_Calendar` and before `14_Study_Material`  
**Purpose:** Provide interactive self-service utility tools designed to resolve user blockers during government job applications and capture high-intent non-branded search traffic.  
**Status:** Ready for Implementation  

---

## 1. Scope & SEO Strategy

### Target Keywords
- `Sarkari Age Calculator for Govt Jobs`, `Govt Job Salary Calculator 7th Pay Commission`, `Photo & Signature Resizer for Online Form`, `Govt Job Eligibility Checker`, `Typing Speed Test for Clerk Jobs`.

---

## 2. Core Interactive Utilities Included

| Tool Name | Purpose | Target URL |
|---|---|---|
| 🧮 **Age Calculator for Govt Jobs** | Calculate exact age on cutoff date with category-wise relaxation (SC/ST/OBC/EWS/PwD) | `/tools/age-calculator` |
| 💰 **7th Pay Commission Salary Estimator** | Calculate In-Hand, Basic Pay, DA, HRA & Deductions by Pay Level (Level 1 to 14) | `/tools/salary-calculator` |
| 🖼️ **Photo & Signature Resizer & Compressor** | Compress and resize application photos (20KB - 50KB) and signatures to exact pixel specifications | `/tools/photo-resizer` |
| 🎯 **Eligibility Matcher** | Input qualification, age, and state to get tailored eligible Sarkari Naukri listings | `/eligibility-checker` |
| ⌨️ **English & Marathi Typing Speed Test** | Practice 30 WPM & 40 WPM GCC-TBC typing tests for government clerk/steno exams | `/tools/typing-test` |

---

## 3. UI/UX Wireframe Structure

```html
<section id="career-tools" class="section-tools" aria-labelledby="tools-heading">
  <div class="container">
    <div class="section-header">
      <h2 id="tools-heading">Free Sarkari Career & Application Tools</h2>
      <p>Instant online tools to calculate eligibility, age relaxation, in-hand salary, and resize application documents.</p>
    </div>

    <div class="tools-grid">
      <a href="/tools/age-calculator" class="tool-card">
        <div class="tool-icon">🧮</div>
        <h3>Age Calculator</h3>
        <p>Check cutoff date eligibility with SC/ST/OBC/EWS relaxation rules.</p>
        <span class="tool-cta">Calculate Now →</span>
      </a>

      <a href="/tools/salary-calculator" class="tool-card">
        <div class="tool-icon">💰</div>
        <h3>7th CPC Salary Calculator</h3>
        <p>Estimate in-hand monthly salary with DA, HRA, and allowances.</p>
        <span class="tool-cta">Estimate Salary →</span>
      </a>

      <a href="/tools/photo-resizer" class="tool-card">
        <div class="tool-icon">🖼️</div>
        <h3>Photo & Sign Resizer</h3>
        <p>Resize images to 20KB–50KB and exact dimensions for MPSC/SSC/UPSC forms.</p>
        <span class="tool-cta">Resize Free →</span>
      </a>

      <a href="/eligibility-checker" class="tool-card">
        <div class="tool-icon">🎯</div>
        <h3>Job Eligibility Checker</h3>
        <p>Match your age & qualification with hundreds of open government vacancies.</p>
        <span class="tool-cta">Check Matching Jobs →</span>
      </a>
    </div>
  </div>
</section>
```
