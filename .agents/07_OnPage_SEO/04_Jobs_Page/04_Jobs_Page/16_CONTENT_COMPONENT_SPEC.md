# 16 — CONTENT + UI COMPONENT SPECIFICATION

**Section:** UI/UX Implementation Guidelines  
**Priority:** P1  
**Type:** Developer Handoff  
**Status:** Implementation Ready

---

## Ground Rules Reminder

> **Follow the ground rules in `01_ground_rules_do_not_delete_UPDATED.md`. This provides UI/UX specifications without removing existing functionality.**

---

## Desktop Layout Recommendation

### Vertical Page Order
1. Breadcrumb
2. H1 + intro
3. Search
4. Filter bar
5. Popular searches
6. Closing Soon
7. Latest Jobs
8. Category discovery
9. How-to
10. Resources
11. Trust
12. FAQ
13. CTA

**Rule:** This maintains user-focused job discovery while adding SEO content below.

---

## Mobile Layout Recommendation

### Sticky or Easily Reachable Controls
**Primary mobile controls:**
- Search | Filters | Sort

**Job card mobile format:**
```
[Job title]
Organisation
Vacancies
Qualification
Location
Last Date
Status
[View Details]
```

**Rule:** Ensure touch targets are at least 44x44 pixels for thumb interaction.

---

## Component Rules

### Job Card Component
**HTML Structure:**
```html
<article class="job-card">
  <h3>Job Title</h3>
  <p>Organisation</p>
  <dl class="job-details">
    <dt>Location</dt><dd>...</dd>
    <dt>Qualification</dt><dd>...</dd>
    <dt>Vacancies</dt><dd>...</dd>
    <dt>Last Date</dt><dd>...</dd>
    <dt>Status</dt><dd>Open</dd>
  </dl>
  <a href="/jobs/example">View Job Details</a>
</article>
```

**Rules:**
- One `<article>` per card
- Title = `<h3>`
- Entire card must not be one giant link if it harms accessibility
- Use clear links/buttons for actions

### Filters Component
**Requirements:**
- Use real form controls
- Visible labels for each filter
- Keyboard accessible
- Clear focus states
- Screen-reader support

**Chips/Tags:**
- Use real anchors when they lead to indexable landing pages
- If a chip is only an in-page filter, it should not pretend to be an SEO landing page

### Closing Soon Component
**Requirements:**
- Dynamic inventory
- Show 6-10 high-value jobs
- Link to complete filtered inventory
- Urgency indicators where appropriate

### Category Blocks Component
**Requirements:**
- Prefer cards/links with one-sentence descriptions
- Consistent styling across categories
- Clear visual hierarchy
- Responsive layout

### FAQ Component
**Requirements:**
- Accordion is acceptable if text remains crawlable and accessible
- Keyboard accessible
- Screen-reader friendly
- Clear open/close states

---

## Copy Style Guidelines

### Language and Tone
- Simple English
- Indian search terminology where natural
- "Government Jobs" as primary entity
- "Sarkari Naukri" as supporting phrase
- Avoid repetitive keyword insertion
- Avoid unsupported superlatives

### Bilingual Content
**If Marathi and English are both important:**
- Decide whether /jobs is bilingual intentionally
- Maintain consistent labels
- Consider language-specific pages if content is substantial
- Do not randomly switch language within metadata or headings

---

## CTA Hierarchy

### Primary CTAs
**On /jobs page:**
- View Job Details

**On individual job page:**
- Apply Online

### Secondary CTAs
**On individual job page:**
- Check Official Notification

**Rule:** Avoid misleading "Apply Now" on listing card if click only opens details.

---

## Ad Placement Rules

### No Ads in Critical Areas
**Do not place ads:**
- Between H1 and search
- Between search and first job
- In a way that obscures deadline/action
- Above the fold in a way that delays job discovery

**Reserve ad space** to prevent CLS (Cumulative Layout Shift).

---

## Content Length Guidelines

### Target Content Volume
- **Static content:** 800–1,500 words across complete page
- **Excludes:** Dynamic job cards
- **Rule:** Do not add filler to hit a number
- **Focus:** User value over word count

---

## Developer Acceptance Test

### User Journey Verification
A new visitor should be able to:

- [ ] Understand the page
- [ ] Search for jobs
- [ ] Filter results
- [ ] Open a job detail
- [ ] Identify deadline
- [ ] Verify official source
- [ ] Find related jobs
- [ ] Navigate to exam/district/qualification pages
- [ ] Use resources (eligibility checker, etc.)
- [ ] Find answers in FAQ

**Without confusion or errors.**

---

## Component Implementation Steps

### Step 1: Job Card Component
1. Create semantic HTML structure
2. Add all required data fields
3. Implement responsive design
4. Test accessibility
5. Optimize performance

### Step 2: Filter Component
1. Implement all filter types
2. Add form validation
3. Ensure keyboard accessibility
4. Add clear labels
5. Test filter combinations

### Step 3: Category Component
1. Create consistent category blocks
2. Add descriptive content
3. Implement responsive layout
4. Add visual hierarchy
5. Test cross-linking

### Step 4: FAQ Component
1. Implement accordion functionality
2. Ensure crawlability
3. Add keyboard support
4. Test screen reader compatibility
5. Optimize performance

### Step 5: Mobile Optimization
1. Test all components on mobile
2. Optimize touch targets
3. Ensure responsive layout
4. Test horizontal scrolling
5. Validate performance

---

## Validation Checklist

### Desktop Layout
- [ ] All sections present in correct order
- [ ] H1 and intro visible above fold
- [ ] Search and filters accessible
- [ ] Job cards properly styled
- [ ] Category sections clear
- [ ] Internal links working
- [ ] Footer accessible

### Mobile Layout
- [ ] Sticky controls working
- [ ] Touch targets appropriate size
- [ ] Horizontal scrolling minimal
- [ ] Text readable without zooming
- [ ] Job cards compact but usable
- [ ] Filters accessible
- [ ] All CTAs thumb-friendly

### Components
- [ ] Job cards semantic HTML
- [ ] Filters use proper form controls
- [ ] Category blocks consistent
- [ ] FAQ accessible and crawlable
- [ ] Trust section clear
- [ ] Resource links working

### Content
- [ ] Copy style consistent
- [ ] No keyword stuffing
- [ ] Bilingual content intentional
- [ ] No unsupported claims
- [ ] Content length appropriate

### Performance
- [ ] No layout shifts
- [ ] Fast load times
- [ ] Smooth interactions
- [ ] Optimized images
- [ ] Efficient rendering

---

## Developer Notes

1. **React Implementation:** Create reusable components for consistency
2. **Styling:** Match existing design system, no visual redesign
3. **Performance:** Use code splitting, lazy loading where appropriate
4. **Accessibility:** Test with screen readers and keyboard navigation
5. **Testing:** Test on multiple devices and browsers

---

## Success Metrics

- [ ] Users complete key actions successfully
- [ ] Reduced bounce rate
- [ ] Increased engagement with new sections
- [ ] Improved mobile conversion
- [ ] Positive user feedback
- [ ] No accessibility complaints

---

## SEO Considerations

### Component Structure
- Use semantic HTML elements
- Maintain proper heading hierarchy
- Ensure content is crawlable
- Implement structured data where appropriate

### User Experience
- Prioritize job discovery
- Balance SEO content with UX
- Keep load times fast
- Ensure mobile optimization
- Provide clear navigation

---

**Last Updated:** 4 September 2026  
**Dependencies:** All section files  
**Blocks:** None (developer handoff)