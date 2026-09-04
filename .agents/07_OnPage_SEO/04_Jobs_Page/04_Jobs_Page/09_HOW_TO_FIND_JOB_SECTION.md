# 09 — HOW TO FIND THE RIGHT GOVERNMENT JOB SECTION

**Section:** User Guidance / AEO Content  
**Priority:** P1  
**Type:** Additive (New content section)  
**Status:** Implementation Ready

---

## Ground Rules Reminder

> **Follow the ground rules in `01_ground_rules_do_not_delete_UPDATED.md`. This adds a new section without removing existing functionality.**

---

## Goal

Provide clear, actionable guidance for finding government jobs while creating AEO-optimized content that answers user questions directly.

---

## H2 Heading

```html
<h2>How to Find the Right Government Job</h2>
```

---

## Introduction Copy

```
Finding a suitable government job starts with matching your qualification, age, preferred location and eligibility requirements with the official recruitment notification.
```

---

## H3 Blocks with Actionable Guidance

### Check Your Qualification
**Copy:** Confirm the required educational qualification, subject, trade, degree or experience before applying. Some recruitments accept multiple qualification levels while others have specific requirements.

**AEO Format:** What qualification do I need for government jobs? → Check the educational requirements in the official notification. Each recruitment specifies the exact qualification needed, such as 10th pass, 12th pass, diploma, graduate or postgraduate.

### Check the Age Limit
**Copy:** Check the minimum and maximum age and any applicable relaxation in the official notification. Age relaxations may apply for reserved categories, ex-servicemen, or other eligible groups.

**AEO Format:** What is the age limit for government jobs? → Each recruitment notification specifies the age limit. Check the minimum and maximum age required and any applicable relaxation for your category before applying.

### Check the Job Location
**Copy:** Some recruitment is open across India, while other vacancies are limited to a state, district or organisation. Confirm the location eligibility before applying.

**AEO Format:** Are government jobs available in my location? → Some recruitments are open across India while others are state-specific or district-specific. Check the location requirement in the official notification to confirm eligibility.

### Check the Number of Vacancies
**Copy:** Review the post-wise vacancy table because eligibility and reservation can differ between posts. Some recruitments have multiple positions with different requirements.

**AEO Format:** How many vacancies are available? → Each recruitment notification includes a vacancy table showing the number of posts for each position. Check the vacancy details as eligibility may vary by post.

### Check the Application Dates
**Copy:** Confirm the application start date and last date. Do not rely only on a countdown shown on a third-party information page. Verify dates in the official notification.

**AEO Format:** What are the application dates for government jobs? → Each recruitment has specific application start and end dates. Always verify these dates in the official notification as recruiting organisations may modify deadlines.

### Check the Selection Process
**Copy:** Review whether selection involves a written examination, skill test, physical test, interview, document verification or another stage. Prepare accordingly for each stage.

**AEO Format:** What is the selection process for government jobs? → Selection processes vary by recruitment and may include written exams, skill tests, physical tests, interviews, or document verification. Check the official notification for the specific selection stages.

### Read the Official Notification
**Copy:** Always read the complete official notification for eligibility, fees, dates, selection process and application instructions. This is the authoritative source for recruitment information.

**AEO Format:** Where can I find the official notification? → The individual job page should provide the official notification PDF or link. Always read the complete official notification as it is the authoritative source for recruitment details.

### Apply Through the Official Channel
**Copy:** Use the official application portal or method specified by the recruiting organisation. Do not use unauthorised agents or payment methods.

**AEO Format:** How do I apply for government jobs? → Open the relevant recruitment details, check eligibility and dates, read the official notification, and submit the application through the official portal or method specified by the recruiting organisation.

---

## AEO Format Guidelines

### Question-Answer Structure
**Format:** Question → direct answer in first sentence → optional detail

**Example:**
- **Question:** How do I check government job eligibility?
- **Answer:** Check the qualification, age limit, location, and other requirements in the official notification. Each recruitment has specific eligibility criteria that must be met before applying.

**Implementation:**
- Keep answers short and direct
- Put the most important information first
- Avoid vague paragraphs
- Make answers work without clicking filters

---

## GEO Format Guidelines

### Entity Relationships
**Where facts are available, make relationships explicit:**

**Structure:**
- Organisation → Recruitment → Role → Location → Qualification → Vacancies → Dates → Application method → Official source

**Example:**
```
Organisation: Maharashtra Public Service Commission
Recruitment: State Services Examination 2026
Role: Various administrative positions
Location: Maharashtra
Qualification: Graduate
Vacancies: 200+
Dates: Application deadline 15 September 2026
Application method: Online through MPSC official portal
Official source: MPSC official website
```

**Benefit:** This creates clean entity relationships for search engines and AI systems to interpret.

---

## Implementation Steps

### Step 1: Create Section Structure
1. Add H2 heading after exam section
2. Add introduction copy
3. Create container for guidance blocks
4. Style to match existing design

### Step 2: Create H3 Guidance Blocks
1. Create blocks for each guidance topic
2. Add actionable copy for each
3. Implement AEO question-answer format
4. Add GEO entity structure where relevant

### Step 3: Add Visual Enhancements
1. Consider adding icons for each step
2. Use numbered steps for clarity
3. Add visual hierarchy
4. Ensure mobile readability

### Step 4: Link to Related Resources
1. Link to eligibility checker
2. Link to age calculator
3. Link to official notification examples
4. Link to application guides

### Step 5: Mobile Optimization
1. Test guidance blocks on mobile
2. Ensure readability on small screens
3. Optimize spacing and layout
4. Test scrolling behavior

---

## Validation Checklist

- [ ] H2 heading added after exam section
- [ ] Introduction copy added
- [ ] All H3 guidance blocks created
- [ ] AEO question-answer format implemented
- [ ] GEO entity structure added where relevant
- [ ] Actionable and practical guidance
- [ ] Links to related resources working
- [ ] Mobile layout tested
- [ ] Content is clear and scannable
- [ ] No existing functionality broken

---

## Developer Notes

1. **React Implementation:** Create reusable guidance block component
2. **Content Structure:** Use consistent formatting across all guidance blocks
3. **AEO Integration:** Consider adding schema markup for Q&A content
4. **Internal Links:** Link guidance to relevant tools and resources
5. **Performance:** Keep content lightweight, avoid heavy graphics

---

## Success Metrics

- [ ] Guidance section engagement increases
- [ ] Users complete application process more successfully
- [ ] Reduced application errors
- [ ] Positive user feedback on guidance clarity
- [ ] Improved understanding of application process
- [ ] Better resource utilization (eligibility checker, etc.)

---

## SEO Considerations

### Content Strategy
- Focus on practical, actionable guidance
- Use clear, simple language
- Address common user questions
- Provide step-by-step instructions
- Include relevant keywords naturally

### AEO Optimization
- Structure content as question-answer pairs
- Put direct answers first
- Make content self-contained where possible
- Use schema markup for Q&A where appropriate

### GEO Optimization
- Make entity relationships explicit
- Use structured data where relevant
- Connect related entities clearly
- Provide factual, verifiable information

---

**Last Updated:** 4 September 2026  
**Dependencies:** 08_BY_EXAM_SECTION.md  
**Blocks:** None (can be implemented independently)