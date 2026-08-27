# SearchSarkariNaukri.com — Homepage Section 9: City-Wise Government Jobs Specification

**Section Name:** `09_City`  
**Page:** Homepage `/` only  
**Section Position:** Immediately after `08_State` and before `10_Admit_Cards`  
**Purpose:** Direct navigation hub for major Tier-1 Metro and Tier-2 urban city municipal corporations, public utilities, metro rail corporations, and local cantonment boards.  
**Status:** Ready for Implementation  

---

## 1. Scope & Urban Geo-SEO Strategy

### Target Keywords
- `Govt Jobs in Pune City`, `Mumbai Municipal Corporation BMC Jobs`, `Delhi Govt Vacancies`, `Bangalore Metro BMRCL Jobs`, `Hyderabad Govt Jobs`, `Chennai Corporation Recruitment`, `Kolkata Municipal Jobs`.

---

## 2. Featured Urban & Metro Cities

1. **Tier-1 Metros:** Mumbai, Delhi, Bengaluru, Hyderabad, Chennai, Kolkata, Pune, Ahmedabad.
2. **Key Tier-2 Hubs:** Nagpur, Nashik, Lucknow, Patna, Jaipur, Bhopal, Chandigarh, Indore, Surat, Visakhapatnam.
3. **Target Municipal & Urban Employers:**
   - Municipal Corporations (BMC, PMC, PCMC, BBMP, GHMC, GCC, KMC)
   - Metro Rail Corporations (Maha Metro, DMRC, BMRCL, CMRL, MMRDA)
   - Urban Development Authorities (CIDCO, PMRDA, DDA, BDA, HUDA)
   - Cantonment Boards & Port Trusts

---

## 3. UI/UX Wireframe Structure

```html
<section id="city-wise-jobs" class="section-cities" aria-labelledby="cities-heading">
  <div class="container">
    <div class="section-header">
      <h2 id="cities-heading">Government Jobs in Top Indian Cities</h2>
      <p>Search municipal corporation, metro rail, urban development, and local departmental jobs in top cities.</p>
    </div>

    <!-- City Card Quick-Grid -->
    <div class="cities-grid">
      <a href="/city/mumbai" class="city-card">
        <div class="city-name">Mumbai</div>
        <div class="city-meta">BMC, MMRDA & Naval Dockyard</div>
      </a>
      <a href="/city/pune" class="city-card">
        <div class="city-name">Pune</div>
        <div class="city-meta">PMC, PCMC, Pune Metro & DRDO</div>
      </a>
      <a href="/city/delhi" class="city-card">
        <div class="city-name">Delhi NCR</div>
        <div class="city-meta">DMRC, MCD, DSSSB & Ministries</div>
      </a>
      <a href="/city/nagpur" class="city-card">
        <div class="city-name">Nagpur</div>
        <div class="city-meta">NMC, Maha Metro & Ordinance Factory</div>
      </a>
    </div>

    <div class="city-browse-more">
      <a href="/city" class="btn btn-outline">Explore All City Government Jobs →</a>
    </div>
  </div>
</section>
```
