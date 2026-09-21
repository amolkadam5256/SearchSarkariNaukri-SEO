# 02 - EXAM DIRECTORY AND CARD SPEC

**Purpose:** Standardize all exam cards and build the full directory.

---

## Reusable ExamCard Requirements

Every exam card must contain:

- Exam name
- Marathi/local name where relevant
- Conducting body
- Exam level: Central / State / Banking / Railway / Defence etc.
- Location / coverage: All India, Maharashtra, railway zones, etc.
- Minimum qualification
- Age: exact if stable, otherwise `Varies by post/notification`
- Major posts, 2-4 examples
- Selection stages
- Next important event, only if valid data exists
- CTA: `View Syllabus, Pattern & Eligibility`

## Do Not Put Entire Card Inside One Link

Preferred HTML:

```html
<article class="exam-card">
  <h3>
    <a href="/exams/mpsc-rajyaseva">MPSC Rajyaseva</a>
  </h3>
  <p>Maharashtra Public Service Commission</p>
  <ul>
    <li>Maharashtra</li>
    <li>Graduate</li>
    <li>State Government</li>
  </ul>
  <a href="/exams/mpsc-rajyaseva">View exam details</a>
</article>
```

This is better for accessibility and scanning than making the whole card one giant anchor.

## Directory Groups

### A. MPSC & Maharashtra State Exams

Include:

- MPSC Rajyaseva
- MPSC PSI / STI / ASO Combined
- MPSC Group B
- MPSC Group C
- Maharashtra Engineering Services
- Maharashtra Agriculture Services
- Maharashtra Forest Services
- MPSC Subordinate Services
- Maharashtra Police Bharti
- Talathi Recruitment, if maintained
- Zilla Parishad Recruitment, if maintained
- Maharashtra Teacher Recruitment, if maintained
- CDPO / Women & Child Development exams, if maintained

### B. UPSC Exams

Include where content is maintained:

- UPSC Civil Services Examination
- UPSC NDA
- UPSC CDS
- UPSC CAPF AC
- UPSC Engineering Services
- UPSC Combined Medical Services
- UPSC Indian Economic Service / Indian Statistical Service
- UPSC EPFO recruitment/examinations, where applicable

### C. SSC Exams

Include:

- SSC CGL
- SSC CHSL
- SSC MTS
- SSC GD Constable
- SSC CPO
- SSC JE
- SSC Stenographer
- SSC Selection Post

### D. Banking Exams

Include:

- IBPS PO
- IBPS Clerk / CSA
- IBPS SO
- IBPS RRB Officer
- IBPS RRB Office Assistant
- SBI PO
- SBI Clerk
- SBI SO
- RBI Grade B
- RBI Assistant
- NABARD Grade A

### E. Railway Exams

Include:

- RRB NTPC
- RRB Group D
- RRB ALP
- RRB Technician
- RRB JE
- RPF Constable
- RPF Sub-Inspector

### F. Defence Exams

Include:

- NDA
- CDS
- AFCAT
- Army Agniveer
- Navy Agniveer
- Air Force Agniveervayu
- Indian Coast Guard

Distinguish officer-entry exams from other-rank recruitment.

### G. Police / Uniformed Services

Include:

- Maharashtra Police Bharti
- SSC GD
- SSC CPO
- RPF Constable
- RPF SI
- CAPF AC
- State Police exams where maintained

### H. Teaching Exams

Include:

- CTET
- MAHA TET
- State TET exams where maintained
- KVS recruitment
- NVS recruitment
- UGC NET
- CSIR NET

Separate eligibility tests such as TET/NET from direct recruitment exams.

### I. Engineering / Technical Exams

Include:

- UPSC Engineering Services
- SSC JE
- RRB JE
- MPSC Engineering Services
- PSU technical recruitment where maintained

### J. Agriculture & Forest Exams

Include:

- MPSC Agriculture Services
- MPSC Forest Services
- State Agriculture Officer exams where maintained
- Forest Department recruitment where maintained

### K. Women & Child Development / CDPO

Include:

- CDPO / Child Development Project Officer
- Supervisor / Women & Child Development recruitment
- State-specific WCD examinations where maintained

## Example Card

```text
UPSC Civil Services Examination
Conducting Body: Union Public Service Commission
Level: Central Government
Coverage: All India
Qualification: Graduate degree
Major Services: IAS, IPS, IFS, IRS and other services
Selection Process: Preliminary Examination -> Main Examination -> Personality Test
Explore: Syllabus, Exam Pattern, Eligibility, Preparation, Important Dates
```

---

**Last Updated:** 21 September 2026
