# SearchSarkariNaukri.com — Homepage Section 8: State-Wise Government Jobs Specification

**Section Name:** `08_State`  
**Page:** Homepage `/` only  
**Section Position:** Immediately after `07_District` and before `09_City`  
**Purpose:** Provide pan-India state-level faceted navigation hubs covering all 28 States and 8 Union Territories across India.  
**Status:** Ready for Implementation  

---

## 1. Scope & National SEO Strategy

### Target Keywords
- `State Govt Jobs 2026`, `UP Sarkari Naukri`, `Bihar Govt Jobs BSSC`, `Rajasthan Sarkari Vacancy`, `MP Govt Jobs`, `Delhi Govt Jobs DSSSB`, `Karnataka Govt Jobs KPSC`, `West Bengal Govt Jobs WBPSC`.

---

## 2. Priority State Aggregation Hubs

| Region | Featured States | Primary PSC / Boards |
|---|---|---|
| **North India** | Uttar Pradesh, Delhi (UT), Rajasthan, Haryana, Punjab, Himachal Pradesh | UPPSC, DSSSB, RPSC, HSSC |
| **Central & East** | Madhya Pradesh, Bihar, Jharkhand, West Bengal, Odisha | MPPSC, BPSC, JPSC, WBPSC |
| **West India** | Maharashtra, Gujarat, Goa | MPSC, GPSC, Goa PSC |
| **South India** | Karnataka, Tamil Nadu, Telangana, Andhra Pradesh, Kerala | KPSC, TNPSC, TSPSC, APPSC, KPSC |
| **Northeast** | Assam, Meghalaya, Tripura, Manipur, Nagaland, Arunachal Pradesh | APSC, MPSC, TPSC |

---

## 3. UI/UX Wireframe Structure

```html
<section id="state-wise-jobs" class="section-states" aria-labelledby="states-heading">
  <div class="container">
    <div class="section-header">
      <h2 id="states-heading">Pan-India Government Jobs by State & UT</h2>
      <p>Search state public service commissions, police departments, and educational boards across India.</p>
    </div>

    <!-- State Grid Cards with Map/Flag/Icon -->
    <div class="states-grid">
      <a href="/states/maharashtra" class="state-card featured">
        <h3>Maharashtra</h3>
        <span class="job-count">124 Vacancies</span>
      </a>
      <a href="/states/uttar-pradesh" class="state-card">
        <h3>Uttar Pradesh</h3>
        <span class="job-count">87 Vacancies</span>
      </a>
      <a href="/states/bihar" class="state-card">
        <h3>Bihar</h3>
        <span class="job-count">64 Vacancies</span>
      </a>
      <a href="/states/delhi" class="state-card">
        <h3>Delhi NCR</h3>
        <span class="job-count">52 Vacancies</span>
      </a>
      <a href="/states/rajasthan" class="state-card">
        <h3>Rajasthan</h3>
        <span class="job-count">41 Vacancies</span>
      </a>
      <a href="/states/madhya-pradesh" class="state-card">
        <h3>Madhya Pradesh</h3>
        <span class="job-count">39 Vacancies</span>
      </a>
    </div>

    <div class="states-view-all">
      <a href="/states" class="btn btn-outline">View All 28 States & 8 Union Territories →</a>
    </div>
  </div>
</section>
```
