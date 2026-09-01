# Closing Soon Jobs Section

## Section Placement

Place this section after:

```text
06_EXAM_COUNTDOWN
```

and before:

```text
08_EXISTING_TALATHI_FEATURED_RECRUITMENT
```

---

## Section Goal

Show urgent government job vacancies with approaching application
deadlines. The section should help users quickly spot jobs ending today,
ending tomorrow, or closing soon.

Keep the section short, useful and action-focused.

---

## Final UI Content

Eyebrow:

```text
Last Date Ending Soon
```

Heading:

```text
Government Jobs Closing Soon
```

Description:

```text
Check government job vacancies with approaching application deadlines and apply before the last date.
```

Top CTA:

```text
View All Urgent Jobs
```

Top CTA link:

```text
/jobs?search=closing%20soon
```

Urgency notice:

```text
Apply before the deadline. These vacancies have approaching closing dates. Check the official recruitment notification before applying.
```

Trust notice:

```text
Application deadlines can change. Always verify the latest vacancy details and closing date in the official recruitment notification.
```

---

## Creative UI Format

Use this short visual structure:

```text
Last Date Ending Soon                    [View All Urgent Jobs]
Government Jobs Closing Soon
Short deadline-focused description

Apply before the deadline
Official notification check reminder

┌────────────────────┐ ┌────────────────────┐ ┌────────────────────┐
│ Ending Today       │ │ Ending Today       │ │ Closing Soon       │
│ URGENT             │ │ URGENT             │ │ Apply Fast         │
│ Organization       │ │ Organization       │ │ Organization       │
│ Job Title          │ │ Job Title          │ │ Job Title          │
│ Last Date          │ │ Last Date          │ │ Last Date          │
│ 0 days left        │ │ 1 day left         │ │ 3 days left        │
│ [View Job]         │ │ [View Job]         │ │ [View Job]         │
└────────────────────┘ └────────────────────┘ └────────────────────┘

Looking for more closing-soon vacancies? [View All Urgent Jobs]
```

Design direction:

- Use a clean urgency style, not a panic style.
- Use red only for "Ending Today" or "0 days left".
- Use orange for "Closing Soon" or "Apply Fast".
- Use dark navy for primary job buttons.
- Keep job cards compact and scannable.
- Show only 3 jobs on the homepage.
- Pull all jobs dynamically from the latest application deadline data.

---

## Job Card Content Fields

Each card should include:

```text
Deadline status
Urgency badge
Recruiting organization
Job title
Last date
Days left
View Job CTA
```

Recommended status labels:

```text
Ending Today
Ends Tomorrow
Closing Soon
Apply Fast
```

Recommended CTA:

```text
View Job
```

---

## Example Jobs From Current Source

Use these only as examples. In production, replace with live jobs from the
database.

Job 1:

```text
AWEIL Executive Finance Recruitment 2026 - Apply Offline for 9 Posts
Organization: Advanced Weapons & Equipment India Limited
Last Date: 31 Aug 2026
Status: Ending Today
```

Job 2:

```text
AWEIL Executive Finance Trainee Recruitment 2026 - Apply Offline for 3 Posts
Organization: Advanced Weapons & Equipment India Limited
Last Date: 31 Aug 2026
Status: Ending Today
```

Job 3:

```text
AWEIL Junior Executive Finance Trainee Recruitment 2026 - Apply Offline for 6 Posts
Organization: Advanced Weapons & Equipment India Limited
Last Date: 31 Aug 2026
Status: Ending Today
```

---

## Keyword Targeting

Primary keyword:

```text
government jobs closing soon
```

Secondary keywords:

```text
closing soon government jobs
last date government jobs
urgent government jobs
apply before last date jobs
Sarkari Naukri last date
latest government jobs deadline
today last date jobs
government vacancy closing date
railway jobs last date
Maharashtra government jobs last date
```

Use keywords naturally in:

- section heading
- description
- urgency notice
- CTA labels
- card status labels
- internal link titles
- aria labels

Do not repeat the same keyword in every card.

---

## Internal Link Strategy

Primary section link:

```text
/jobs?search=closing%20soon
```

Useful filtered links:

```text
/jobs?deadline=today
/jobs?deadline=tomorrow
/jobs?deadline=7-days
/jobs?state=maharashtra&deadline=7-days
/jobs?category=railway&deadline=7-days
```

Job cards must link to the real job detail pages.

---

## Scroll Animation Direction

Use subtle scroll reveal animation:

```text
Header appears first
Urgency notice appears second
Job card 1 appears third
Job card 2 appears fourth
Job card 3 appears fifth
Bottom CTA appears last
```

Motion rules:

- Slide elements upward by a small amount.
- Stagger card animation by 80-100ms.
- Add a small hover lift on job cards.
- Run the animation once only.
- Respect reduced-motion settings.

Do not use flashing urgency badges.

---

## Desktop UX

Desktop layout:

```text
Header row with CTA
Urgency notice full width
3 job cards in one row
Bottom CTA strip
Trust notice
```

Desktop rules:

- Keep card heights consistent.
- Clamp long organization names to two lines.
- Clamp long job titles to three lines.
- Keep all CTAs aligned at the bottom of cards.

---

## Mobile UX

Mobile layout:

```text
Eyebrow
Heading
Description
View All Urgent Jobs
Urgency notice
Job card 1
Job card 2
Job card 3
Bottom CTA
Trust notice
```

Mobile rules:

- Stack cards in one column.
- Make CTAs full width.
- Keep status and urgency badge on one row where possible.
- Avoid text overflow in long job titles.

---

## Data And Verification Rules

- Use live job data sorted by nearest application deadline.
- Exclude expired jobs unless the page intentionally supports expired listings.
- Show jobs with deadlines today, tomorrow or within the next 7 days.
- Always verify deadlines from the official recruitment notification.
- If no closing-soon jobs exist, show a fallback link to latest jobs.
- Do not show fake urgency labels.

---

## Quality Checklist

- [ ] Section is markdown-only guidance, not implementation code.
- [ ] Visible content stays short and keyword-focused.
- [ ] Homepage shows only 3 urgent jobs.
- [ ] Jobs are sorted by nearest deadline.
- [ ] Job links go to real detail pages.
- [ ] Deadlines match official notifications.
- [ ] Urgency style is clear but not aggressive.
- [ ] Scroll animation is subtle and accessible.
- [ ] Reduced-motion users are respected.
