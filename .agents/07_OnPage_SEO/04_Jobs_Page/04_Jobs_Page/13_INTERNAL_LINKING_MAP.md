# 13 — INTERNAL LINKING MAP

**Section:** Internal Linking Strategy  
**Priority:** P1  
**Type:** Strategic Documentation  
**Status:** Implementation Ready

---

## Ground Rules Reminder

> **Follow the ground rules in `01_ground_rules_do_not_delete_UPDATED.md`. This provides internal linking strategy without removing existing functionality.**

---

## Goal

Build a connected internal link graph rather than isolated pages, using contextual links inside the page content rather than only footer links.

---

## Internal Linking Principle

Use contextual links inside the page, not only footer links. Every important supporting page should receive relevant anchor text from /jobs.

---

## Priority Internal Links from /jobs

### High Priority (P0)
| Anchor | Destination | Section | Priority |
|---|---|---|---|
| Government Jobs by District | /districts | State | P0 |
| Latest Government Job Updates | /job-updates | Resources | P0 |
| UPSC Jobs | /exams/upsc-cse | Exam | P0 |
| MPSC Jobs | /exams/mpsc-rajyaseva | Exam | P0 |
| SSC Jobs | /exams/ssc-cgl | Exam | P0 |
| Banking Exams | /exams/sbi-po-clerk | Exam | P0 |
| Railway Exams | /exams/rrb-ntpc | Exam | P0 |
| Police Recruitment | /exams/maharashtra-police-bharti | Exam | P0 |
| Government Admit Cards | /admit-cards | Resources | P0 |
| Government Exam Results | /results | Resources | P0 |
| Government Exam Calendar | /exam-calendar | Resources | P0 |
| Government Job Eligibility Checker | /eligibility-checker | Resources | P0 |

### Medium Priority (P1)
| Anchor | Destination | Section | Priority |
|---|---|---|---|
| CTET / TET | /exams/ctet | Exam | P1 |
| Government Job Age Calculator | /age-calculator | Resources | P1 |
| Current Affairs | /current-affairs | Resources | P1 |
| Daily Quiz | /quiz | Resources | P1 |
| Career Guidance | /career-guidance | Resources | P1 |
| Editorial Policy | /editorial-policy | Trust | P1 |

---

## Category Landing Page Links

### Qualification Landing Pages
- `/government-jobs/10th-pass`
- `/government-jobs/12th-pass`
- `/government-jobs/iti`
- `/government-jobs/diploma`
- `/government-jobs/graduate`
- `/government-jobs/engineering`
- `/government-jobs/post-graduate`

### Location Landing Pages
- `/government-jobs/maharashtra`
- `/government-jobs/maharashtra/pune`
- `/government-jobs/maharashtra/mumbai`
- `/government-jobs/maharashtra/nagpur`
- `/government-jobs/maharashtra/nashik`
- `/government-jobs/maharashtra/thane`
- `/government-jobs/maharashtra/solapur`

### Department Landing Pages
- `/government-jobs/railway`
- `/government-jobs/banking`
- `/government-jobs/police`
- `/government-jobs/teaching`
- `/government-jobs/defence`
- `/government-jobs/healthcare`
- `/government-jobs/engineering`
- `/government-jobs/forest`
- `/government-jobs/psu`

---

## Anchor Text Rules

### Prefer Descriptive Anchors
**Good Examples:**
- Latest Government Jobs
- Maharashtra Government Jobs
- 12th Pass Government Jobs
- Government Jobs by District
- Government Job Eligibility Checker

**Avoid Excessive Repetition**
- Don't use the exact same anchor in every block
- Vary anchor text while maintaining relevance
- Use context-specific variations

**Weak Examples to Avoid:**
- Click Here
- Read More
- View
- Learn More

---

## Contextual Linking Formula

### Job Card → Related Pages
- Job card → related qualification page
- Job card → related location page
- Job card → related department page

### Job Detail → Hub Pages
- Job detail → /jobs
- Job detail → related jobs
- Job detail → exam pages
- Job detail → admit cards/results

### Cross-Page Linking
- Exam page → current matching jobs
- District page → jobs in district
- Qualification page → active jobs
- Department page → relevant recruitments

---

## Link Equity Objective

Build a connected graph rather than isolated pages:

```
/jobs (broad hub)
├── Qualification pages (focused spokes)
├── Location pages (focused spokes)
├── Department pages (focused spokes)
├── Exam pages (focused spokes)
└── Resource pages (supporting content)
```

**Implementation:** /jobs is the broad hub, qualification/state/department/exam pages are focused spokes.

---

## Implementation Steps

### Step 1: Audit Existing Links
1. Review current internal linking structure
2. Identify missing high-priority links
3. Check anchor text quality
4. Map existing link graph

### Step 2: Add High-Priority Links
1. Add P0 links from /jobs to key destinations
2. Ensure descriptive anchor text
3. Place links in relevant sections
4. Test link functionality

### Step 3: Create Category Landing Links
1. Add qualification landing page links
2. Add location landing page links
3. Add department landing page links
4. Ensure proper internal linking

### Step 4: Implement Contextual Linking
1. Add job card to related page links
2. Add job detail to hub page links
3. Implement cross-page linking
4. Test user journeys

### Step 5: Optimize Anchor Text
1. Review all anchor text for descriptiveness
2. Remove generic "click here" links
3. Add keyword-rich descriptive anchors
4. Ensure natural language

---

## Validation Checklist

- [ ] All P0 internal links added
- [ ] Descriptive anchor text used
- [ ] Links placed in relevant sections
- [ ] Category landing pages linked
- [ ] Contextual linking implemented
- [ ] Link graph structure optimized
- [ ] No broken internal links
- [ ] Anchor text naturally varied
- [ ] User journeys tested
- [ ] No existing functionality broken

---

## Developer Notes

1. **React Implementation:** Use internal link components, avoid hardcoded URLs
2. **Link Management:** Consider creating a link configuration system
3. **Anchor Text:** Use descriptive, keyword-rich anchors naturally
4. **Testing:** Test all internal links after changes
5. **Performance:** Internal links should not impact page load

---

## Success Metrics

- [ ] Internal link graph strength improves
- [ ] Users discover related content more easily
- [ ] Reduced bounce rate
- [ ] Increased page views per session
- [ ] Better topical authority signals
- [ ] Improved crawling efficiency

---

## SEO Considerations

### Internal Linking Strategy
- Use descriptive, keyword-rich anchor text
- Link from high-authority pages to important pages
- Create contextual links based on content relevance
- Build topic clusters through internal linking

### Link Equity Distribution
- Distribute link equity from /jobs to key pages
- Ensure important pages receive sufficient internal links
- Create logical link hierarchies
- Avoid orphan pages

---

**Last Updated:** 4 September 2026  
**Dependencies:** All section files  
**Blocks:** None (strategic documentation)