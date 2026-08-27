# SearchSarkariNaukri.com — Homepage Section 5: Government Jobs by Department & Exam Specification

**Section Name:** `05_Department_Exam`  
**Page:** Homepage `/` only  
**Section Position:** Immediately after `04_Qualification` and before `06_Maharashtra`  
**Purpose:** Provide structured navigation hubs into major Central & State Government departments, commissions, and competitive exams (UPSC, SSC, Banking, Railways, Defence, Police, PSU).  
**Status:** Ready for Implementation  

---

## 1. Scope & SEO Strategy

### Target Keywords
- `Sarkari Naukri by Department 2026`, `SSC Recruitment 2026`, `UPSC Government Jobs`, `Railway RRB Vacancy 2026`, `Bank Jobs IBPS SBI`, `Police Bharti 2026`, `Defence Recruitment NDA CDS`.

---

## 2. Department & Exam Categories

| Category | Key Exams / Boards | Hub URL Link |
|---|---|---|
| **Civil Services & State PSC** | UPSC, MPSC, BPSC, UPPSC, MPPSC | `/department/civil-services` |
| **Staff Selection Commission (SSC)** | SSC CGL, SSC CHSL, SSC GD Constable, SSC MTS | `/exams/ssc` |
| **Banking & Financial** | IBPS PO/Clerk, SBI PO, RBI Grade B, NABARD | `/exams/banking` |
| **Railways (RRB)** | RRB NTPC, RRB Group D, RRB ALP, RRB JE | `/exams/railway` |
| **Defence & Paramilitary** | NDA, CDS, AFCAT, CAPF, Army, Navy, Air Force | `/department/defence` |
| **Police & Home Guard** | State Police Sub-Inspector, Constable, Jail Warder | `/department/police` |
| **Engineering & PSU** | GATE PSU, ISRO, DRDO, ONGC, IOCL, NTPC, BHEL | `/department/psu` |
| **Teaching & Education** | CTET, State TET, UGC NET, KVS, NVS, Assistant Professor | `/department/teaching` |

---

## 3. UI/UX Wireframe Structure

```html
<section id="department-exam-jobs" class="section-dept-exam" aria-labelledby="dept-exam-heading">
  <div class="container">
    <div class="section-header">
      <h2 id="dept-exam-heading">Government Jobs by Department & Exam</h2>
      <p>Explore recruitment notifications categorized by top government sectors and competitive exam boards.</p>
    </div>

    <!-- 8-Card Grid Layout -->
    <div class="dept-exam-grid">
      <!-- Card: SSC -->
      <a href="/exams/ssc" class="dept-card">
        <div class="dept-icon"><img src="/icons/ssc.svg" alt="SSC Logo" width="40" height="40" loading="lazy"></div>
        <div class="dept-info">
          <h3>SSC Recruitment</h3>
          <span class="active-count">12 Active Notices</span>
        </div>
      </a>
      <!-- Additional category cards -->
    </div>
  </div>
</section>
```
