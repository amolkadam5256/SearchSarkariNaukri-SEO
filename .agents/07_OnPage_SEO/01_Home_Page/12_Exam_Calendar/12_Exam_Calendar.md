# SearchSarkariNaukri.com — Homepage Section 12: Sarkari Exam Calendar Specification

**Section Name:** `12_Exam_Calendar`  
**Page:** Homepage `/` only  
**Section Position:** Immediately after `11_Results` and before `13_Tools`  
**Purpose:** Interactive chronological timeline and upcoming recruitment exam calendar, helping aspirants plan study and application schedules.  
**Status:** Ready for Implementation  

---

## 1. Scope & SEO Strategy

### Target Keywords
- `Sarkari Exam Calendar 2026`, `Upcoming Govt Exams Schedule`, `MPSC Exam Date 2026`, `SSC Exam Calendar PDF`, `UPSC Annual Time Table 2026`.

---

## 2. Calendar Features

1. **Monthly View Filter:** Filter by Current Month, Next Month, and Upcoming Quarter.
2. **Key Info per Event:**
   - Exam Date & Day
   - Commission / Exam Name
   - Tier / Phase (e.g., Prelims, Mains, Interview, Physical PET/PST)
   - Status Indicator (Upcoming / Postponed / Rescheduled)

---

## 3. UI/UX Wireframe Structure

```html
<section id="exam-calendar" class="section-calendar" aria-labelledby="calendar-heading">
  <div class="container">
    <div class="section-header">
      <h2 id="calendar-heading">Sarkari Exam Calendar 2026 (परीक्षेचे वेळापत्रक)</h2>
      <p>Stay ahead with official exam dates and annual recruitment schedules released by government commissions.</p>
    </div>

    <!-- Timeline Grid -->
    <div class="calendar-timeline">
      <div class="calendar-card">
        <div class="date-badge">
          <span class="month">OCT</span>
          <span class="day">12</span>
        </div>
        <div class="event-details">
          <h3>MPSC Combined Group B & C Prelims 2026</h3>
          <p>Phase: Preliminary Exam | Shifts: Morning & Afternoon</p>
        </div>
        <a href="/exams/mpsc-combined-2026" class="btn btn-sm btn-outline">View Details</a>
      </div>
    </div>

    <div class="calendar-footer">
      <a href="/exam-calendar" class="btn btn-primary">Download Annual Govt Exam Calendar 2026 PDF →</a>
    </div>
  </div>
</section>
```
