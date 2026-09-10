# 12 — FRESHNESS SECTION SPECIFICATION

**Section:** Dynamic Freshness Implementation  
**Priority:** P1  
**Type:** Technical Content  
**Status:** Implementation Ready

---

## CONTENT EDITING RULES

**IMPORTANT:** When updating or creating any content based on this specification, follow these human editing guidelines:

### Primary Objective
Transform draft content into natural, original, reader-first writing while preserving factual meaning, important facts, numbers, dates, names, terminology, search intent, primary topic, important keywords, useful supporting information, intended audience, actual purpose of the page, and legitimate claims supported by source material.

### Key Requirements
1. **Remove generic AI-style openings** - Avoid predictable openings like "In today's digital world...", "In this comprehensive guide...", "Let's dive in...". Start with direct, useful information.
2. **Remove repetition** - Check for repeated ideas, keywords, conclusions, explanations, adjectives, sentence structures, headings, and calls to action.
3. **Vary sentence structure** - Mix short, medium, and long sentences. Avoid predictable grammatical patterns.
4. **Improve paragraph flow** - Use transitions only when genuinely helpful. Avoid excessive use of "Furthermore", "Moreover", "Additionally", etc.
5. **Remove formulaic "rule of three" writing** - Avoid unnecessary lists of three similar adjectives unless they provide genuinely different information.
6. **Remove filler** - Delete unnecessary phrases like "It is worth mentioning that", "It should be noted that", "Needless to say", etc.
7. **Use specific language** - Replace vague statements with precise information. Do not add unsupported facts.
8. **Preserve factual accuracy** - Never change dates, statistics, percentages, names, official terminology, URLs, product names, organization names, exam names, job titles, application requirements, eligibility conditions, fees, or deadlines.
9. **Make writing contextual** - Write according to the actual subject (informational, SEO, product, news, educational, job/exam content).
10. **SEO requirements** - Maintain important target keywords naturally. Never stuff keywords or sacrifice readability for SEO.
11. **Heading structure** - Keep logical hierarchy (H1, H2, H3). Use descriptive headings, not generic ones like "Introduction" or "Conclusion".
12. **Lists and tables** - Use bullet points when information is easier to scan as a list. Use tables for structured comparisons.
13. **Remove robotic phrases** - Rewrite templated or generic phrases naturally.
14. **Do not over-humanize** - Do not add random typos, grammar mistakes, excessive slang, fake personal stories, or fake opinions.
15. **Add human-like specificity** - Prefer concrete explanations over generic claims when supported by source material.
16. **Control tone** - Use professional, clear, direct, helpful, natural, confident tone without exaggeration.
17. **Readability** - Make content easy to scan with short paragraphs, clear headings, direct sentences, useful lists, concrete explanations, and logical ordering.
18. **Preserve author's intent** - Do not change the message simply because of personal style preference.
19. **Originality** - Perform genuine rewriting, not superficial synonym replacement. Understand the idea, identify purpose, reorganize wording, rewrite sentence structures, combine repetitive statements, improve clarity, add specificity only when supported, preserve important terminology, and produce genuinely original phrasing.
20. **Final quality check** - Verify content (meaning preserved, no important info removed, no unsupported claims, no changed facts), writing (natural, varied sentences, purposeful paragraphs, no repetition, appropriate formality, no templates), SEO (search intent satisfied, keywords natural, no stuffing, useful headings, crawlable structure), readability (quick understanding, broken long sentences, reasonable paragraph sizes, useful lists), and quality (precise wording, qualified claims, genuinely useful, valuable sections).

### Output Rule
Return ONLY the rewritten content unless explicitly asked for explanation or audit. Do not mention AI detection, humanization, or bypassing detectors. The objective is high-quality human-readable content, not detector manipulation.

---

## Freshness Strategy

### Why Freshness Matters
This niche is highly freshness-dependent. Government recruitment notifications are issued throughout the year, and job seekers need current information.

### Competitive Benchmark
Competitors like FreeJobAlert emphasize:
- Daily updates
- Current vacancies
- Closing-soon listings
- Today's updates
- New updates

### Adaptation Strategy
Adapt this model (not copy) for competitive advantage:
- Emphasize daily updates
- Show current vacancies
- Display closing-soon listings
- Highlight today's updates
- Show new updates

---

## Dynamic Freshness Sections

### 1. Latest Government Job Alerts
**Section:** Latest Government Job Alerts  
**Content:** Dynamic job listings from database  
**Update Frequency:** Daily  
**Data Source:** Database/API  
**Columns:** Job, Organization, Qualification, Last Date, Details

**Implementation:**
```html
<section id="latest-job-alerts">
  <h2>Latest Government Job Alerts</h2>
  <p>Looking for the latest Sarkari Naukri? Search Sarkari Naukri publishes new government recruitment updates from central and state departments. Check the latest vacancies, eligibility, important dates and official application information before applying.</p>
  
  <table>
    <thead>
      <tr>
        <th>Job</th>
        <th>Organization</th>
        <th>Qualification</th>
        <th>Last Date</th>
        <th>Details</th>
      </tr>
    </thead>
    <tbody>
      <!-- Dynamic job rows from database -->
    </tbody>
  </table>
</section>
```

**Requirements:**
- Must use real job data from database
- Do not hardcode job listings
- Update daily
- Remove expired jobs
- Show most recent jobs first

---

### 2. Government Jobs Closing Soon
**Section:** Government Jobs Closing Soon  
**Content:** Dynamic closing-soon job listings from database  
**Update Frequency:** Daily  
**Data Source:** Database/API  
**Columns:** Job, Department, Qualification, Last Date, Days Remaining, Apply/View

**Implementation:**
```html
<section id="closing-soon">
  <h2>Government Jobs Closing Soon</h2>
  <table>
    <thead>
      <tr>
        <th>Job</th>
        <th>Department</th>
        <th>Qualification</th>
        <th>Last Date</th>
        <th>Days Remaining</th>
        <th>Apply/View</th>
      </tr>
    </thead>
    <tbody>
      <!-- Dynamic closing-soon job rows from database -->
    </tbody>
  </table>
</section>
```

**Requirements:**
- Must use real job data from database
- Do not hardcode job listings
- Update daily
- Show jobs closing within 7-30 days
- Calculate days remaining dynamically
- Remove jobs after last date

---

## Automatic Updates

### What Should Update Automatically
1. Today / Latest updates
2. Newly added jobs
3. Last-date changes
4. Closing soon listings
5. Admit card updates
6. Results
7. Important recruitment notices

### Update Frequency
- **Latest jobs:** Daily
- **Closing soon:** Daily
- **Last date changes:** Real-time
- **Admit card updates:** As published
- **Results:** As published
- **Important notices:** As published

---

## Technical Implementation

### Database Queries
Query database for:
- Latest jobs (ORDER BY last_date DESC, published_date DESC)
- Closing soon (WHERE last_date BETWEEN NOW() AND NOW() + INTERVAL 30 DAY)
- Today's updates (WHERE published_date = CURRENT_DATE)
- New updates (WHERE published_date >= CURRENT_DATE - INTERVAL 7 DAY)

### Caching Strategy
- Cache latest jobs for 1 hour
- Cache closing soon for 1 hour
- Invalidate cache when new jobs are added
- Invalidate cache when last dates change

### API Integration
If using external API:
- Implement rate limiting
- Handle API failures gracefully
- Show cached data if API is down
- Implement retry logic

---

## Freshness Signals

### Schema Markup
Update schema dates dynamically:
- `dateModified`: Update when content changes
- `lastReviewed`: Update when content is reviewed
- Keep schema in sync with visible content

### Last Updated Date
Display last updated date in Verify Recruitment Information section:
```html
<p><strong>Last Updated:</strong> [dynamic date]</p>
```

### HTTP Headers
Set appropriate HTTP headers:
- `Last-Modified`: When content was last modified
- `Cache-Control`: Appropriate caching strategy
- `ETag`: For content validation

---

## Data Quality

### Remove Expired Jobs
- Remove jobs after last date from "latest" section
- Move expired jobs to archive (if needed)
- Do not show expired jobs as "current"

### Validate Job Data
- Verify job titles are accurate
- Verify organization names are correct
- Verify qualification data is accurate
- Verify last dates are correct
- Verify job URLs are valid

### Handle Missing Data
- Show placeholder for missing qualification
- Show "TBD" for missing last date
- Show "N/A" for missing organization
- Do not show jobs with missing critical data

---

## Performance Optimization

### Database Optimization
- Index on `published_date`
- Index on `last_date`
- Index on `qualification`
- Use appropriate query limits
- Implement pagination if needed

### Page Load Optimization
- Lazy load job tables
- Implement infinite scroll or pagination
- Optimize table rendering
- Minimize database queries per page load

---

**Implementation Priority:** P1  
**Update Frequency:** Daily  
**Data Source:** Database/API  
**Cache Strategy:** 1-hour cache
