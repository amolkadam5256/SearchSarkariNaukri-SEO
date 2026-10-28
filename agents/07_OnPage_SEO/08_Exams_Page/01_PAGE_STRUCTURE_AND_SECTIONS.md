# 01 - PAGE STRUCTURE AND SECTIONS

**Page:** `/exams`  
**Purpose:** Complete section-by-section implementation specification

---

## 1. Breadcrumb

Add above the H1:

```html
<nav aria-label="Breadcrumb">
  <a href="/">Home</a>
  <span aria-hidden="true">›</span>
  <span aria-current="page">Government Exams</span>
</nav>
```

Schema must match visible breadcrumb.

## 2. Hero

H1:

```text
Government Exams 2026 - UPSC, SSC, MPSC, Banking, Railway & More
```

Intro:

```text
Explore major central and state government exams in India. Compare eligibility, qualification, selection stages, syllabus, exam pattern, job location and major posts before choosing an exam.
```

Primary CTAs:

- Find an Exam
- Exam Calendar
- Check Eligibility

## 3. Exam Finder

Heading:

```text
Find the Right Government Exam
```

Controls:

- Search exam input: `Search UPSC, SSC, Railway, MPSC...`
- Qualification chips: 10th, 12th, Graduate, Engineering, Diploma, Postgraduate
- Location chips: All India, Maharashtra, State Government
- Career chips: Administrative, Police, Banking, Railway, Defence, Teaching, Engineering

Rules:

- Use real exam data.
- Search input must have label.
- Filter chips should be crawlable links where they navigate.
- Do not require JavaScript for core discovery links.

## 4. Popular Government Exams

Show 10-12 major exams before the full directory:

- UPSC Civil Services
- MPSC Rajyaseva
- SSC CGL
- SSC CHSL
- RRB NTPC
- RRB Group D
- IBPS PO
- SBI PO
- Maharashtra Police Bharti
- CTET
- NDA
- CDS

Each card should contain:

- Exam name
- Conducting body
- Qualification
- Coverage/location
- CTA: `Explore`

## 5. All Government Exams Directory

This is the core page section. Use category groups:

- MPSC & Maharashtra State Exams
- UPSC Exams
- SSC Exams
- Banking Exams
- Railway Exams
- Defence Exams
- Police / Uniformed Services
- Teaching Exams
- Engineering / Technical Exams
- Agriculture & Forest Exams
- Women & Child Development / CDPO

## 6. Exams by Location

Heading:

```text
Government Exams by Location
```

Groups:

- All India / Central Government
- Maharashtra Government
- Other states as coverage grows

Do not create hundreds of state sections until there is useful maintained content.

## 7. Exams by Qualification

Heading:

```text
Government Exams by Qualification
```

Groups:

- 10th Pass
- 12th Pass
- Graduate
- Engineering
- Diploma
- Postgraduate
- Agriculture

Always include:

```text
Exact qualification varies by post and notification.
```

## 8. Exams by Career Goal

Heading:

```text
Choose an Exam by Career
```

Groups:

- Civil Services
- Police & Uniformed Services
- Banking
- Railways
- Defence
- Teaching
- Engineering
- Agriculture & Forest

## 9. Upcoming Government Exam Dates

Table fields:

- Exam
- Event
- Date
- Status
- Details

Rules:

- Use Exam Calendar data.
- Never fabricate expected dates.
- Link to full Exam Calendar.

## 10. Latest Exam Notifications

Show 5-10 latest updates:

- New notification
- Application started
- Application deadline
- Exam date announced
- Correction window
- Schedule changed

Fields:

- Exam
- Authority
- Update type
- Date
- View details

## 11. Admit Cards / Results / Cutoffs / Calendar

Compact card block linking to:

- Admit Cards
- Results
- Cutoffs, if available
- Exam Calendar

## 12. Compare Popular Government Exams

Comparison table:

- Exam
- Qualification
- Level
- Career
- Selection

Do not rank exams as "best". Keep it factual.

## 13. Preparation Resources

Cards:

- Current Affairs
- Daily Quiz
- Daily Assessment
- Battle Arena
- Digital Library
- Eligibility Checker
- Age Calculator
- Career Guidance

## 14. How to Choose the Right Government Exam

Short ordered list:

1. Check your qualification.
2. Check age and category rules.
3. Decide between central and state careers.
4. Choose the role type.
5. Compare syllabus and selection stages.
6. Check current notifications on the official authority website.

CTAs:

- Check Eligibility
- Career Guidance

## 15. Official Exam Authorities

Keep compact. Include only major authorities:

- UPSC
- Staff Selection Commission
- Railway Recruitment Boards
- IBPS
- SBI Careers
- RBI
- MPSC
- National Testing Agency where relevant

## 16. FAQ

Add 8-10 useful questions only.

## 17. Verification / Disclaimer

Add page-body statement:

```text
Search Sarkari Naukri is an independent information platform and is not affiliated with any government authority. Exam eligibility, age limits, dates, vacancies, syllabus and selection procedures can change. Always confirm the latest information from the official notification and conducting authority before applying.
```

---

**Last Updated:** 21 September 2026
