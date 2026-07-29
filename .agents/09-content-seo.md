# 09 — Content Strategy, Page Templates & Editorial SOPs

## 9.1 Master Page Templates

### 1. Job Notification Page Layout Template
```markdown
# [Organization Name] Recruitment 2026 — [Post Count] Vacancies | Apply Online

## Quick Summary Table
| Field | Details |
|---|---|
| Organization | [Official Name] |
| Post Name | [Post Names] |
| Total Vacancies | [Count] |
| Qualification | [10th/12th/Graduate/etc.] |
| Last Date to Apply | [Date] |
| Application Mode | Online |
| Official Portal | [Official .gov.in URL] |

## Important Dates
| Event | Date |
|---|---|
| Notification Release | [Date] |
| Start Date to Apply | [Date] |
| Last Date to Apply | [Date] |
| Exam Date | [Date / To be notified] |

## Vacancy Breakdown
[Category-wise table: General, OBC, SC, ST, EWS, PH]

## Eligibility Criteria
- **Age Limit:** [Min Age] to [Max Age] years (Age relaxation applicable as per rules).
- **Educational Qualification:** [Detailed degree/diploma requirement].

## Application Fee & Pay Scale
- **Fee:** General/OBC: ₹[X] | SC/ST/Female: ₹[Y]
- **Salary:** Pay Level [X] (₹[Min] - ₹[Max] per month as per 7th CPC).

## How to Apply Step-by-Step
1. Visit official website [linked].
2. Click "Apply Online" for [Post Name].
3. Fill registration details and upload documents.
4. Pay fee and submit form.

## Important Links
| Link Type | Direct URL |
|---|---|
| Official Notification PDF | [Link] |
| Apply Online Portal | [Link] |

## Frequently Asked Questions (FAQs)
[5+ structured Q&A blocks marked up with FAQPage JSON-LD schema]
```

---

### 2. Result Page Layout Template
```markdown
# [Exam Name] Result 2026 — Download Scorecard & Cutoff

## Result Highlights
| Field | Details |
|---|---|
| Conducting Body | [Organization Name] |
| Exam Name | [Exam Name] |
| Result Release Date | [Date] |
| Official Website | [Official URL] |

## How to Check [Exam Name] Result 2026
1. Click direct result link below.
2. Enter Roll Number / Registration ID and Date of Birth.
3. View and download scorecard PDF.

## Category Wise Cutoff Marks
[Table: General, OBC, SC, ST, EWS cutoff marks]
```

---

## 9.2 Content Types Matrix & Publishing Targets

| Content Type | Target Quantity (Year 1) | Publishing / Update Cadence | SEO Value | Priority |
|--------------|--------------------------|-----------------------------|-----------|----------|
| **Job Notifications** | 2,000 – 5,000 | Daily / Real-time | Very High | P0 |
| **State Hub Pages** | 36 (All States/UTs) | Weekly updates | Very High | P0 |
| **Department Hubs** | 30 – 50 | Weekly updates | Very High | P0 |
| **Qualification Hubs** | 15 – 20 | Weekly updates | Very High | P0 |
| **Cross-Filter Pages** | 1,000 – 5,000 | Weekly updates (Auto) | High | P1 |
| **Result Pages** | 500 – 1,000 | Immediate upon release | Very High | P0 |
| **Admit Card Pages** | 500 – 1,000 | Immediate upon release | Very High | P0 |
| **News Articles** | 200 – 500 | Daily | Medium-High | P1 |
| **Blog / Guide Posts** | 100 – 200 | Monthly refresh | High | P1 |

---

## 9.3 Content Refresh & Pruning Decision SOP

```
                          [Evaluate Page Age & Traffic]
                                       │
                 ┌─────────────────────┴─────────────────────┐
         Age < 90 Days                              Age > 90 Days
                 │                                           │
         [No action required]                    [Check GSC Organic Clicks]
                                                             │
                                          ┌──────────────────┴──────────────────┐
                                   Clicks >= 10 Clicks                     Clicks < 10 Clicks
                                          │                                     │
                                [Content Refresh SOP]                [Evaluate Relevancy]
                                ├── Update facts & dates                       │
                                ├── Add 3-5 new internal links       ┌─────────┴─────────┐
                                └── Submit Indexing API              │                   │
                                                             [Has Active Sub?]   [No Replacement]
                                                                     │                   │
                                                             [301 Redirect]      [410 Gone Response]
```
