# SearchSarkariNaukri.com — Homepage Section 11: Sarkari Exam Results Specification

**Section Name:** `11_Results`  
**Page:** Homepage `/` only  
**Section Position:** Immediately after `10_Admit_Cards` and before `12_Exam_Calendar`  
**Purpose:** Provide real-time published exam results, official merit lists, category-wise cut-off marks, and scorecard download links.  
**Status:** Ready for Implementation  

---

## 1. Scope & SEO Strategy

### Target Keywords
- `Sarkari Result 2026`, `Latest Exam Results`, `MPSC Result 2026 Merit List`, `SSC Result Cut Off Marks`, `Railway RRB Scorecard`, `Police Bharti Final Selection List`.

---

## 2. Dynamic Component Requirements

1. **Category Tabs:** `All Results`, `Central Exams`, `Maharashtra & State PSC`, `Police & Defence`, `Banking & Railways`.
2. **Metadata per Result Entry:**
   - Exam Name & Year
   - Declaration Date
   - Direct PDF Merit List / Roll Number Search Link
   - Official Cut-off Score Breakdown

---

## 3. UI/UX Wireframe Structure

```html
<section id="exam-results" class="section-results" aria-labelledby="results-heading">
  <div class="container">
    <div class="section-header">
      <h2 id="results-heading">Latest Sarkari Exam Results & Merit Lists (निकाल २०२६)</h2>
      <p>Check declared written test results, selection lists, and official cut-off marks.</p>
    </div>

    <div class="results-table-wrapper">
      <table class="results-table" aria-label="Latest Results Table">
        <thead>
          <tr>
            <th>Exam / Recruitment</th>
            <th>Conducting Authority</th>
            <th>Declaration Date</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Maharashtra Police Constable Final Merit List 2026</strong></td>
            <td>Maharashtra Police Department</td>
            <td>Declared Today</td>
            <td><a href="/results/mh-police-constable-2026" class="btn btn-sm btn-success">Check Result & Cut-off</a></td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="results-footer-cta">
      <a href="/results" class="btn btn-outline">Browse All Sarkari Results Archive →</a>
    </div>
  </div>
</section>
```
