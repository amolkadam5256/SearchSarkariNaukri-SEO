# 01 — HERO / H1 / INTRO / BREADCRUMB + METADATA

**Section:** Hero Section with Metadata  
**Priority:** P0  
**Type:** Approved Edit Exception (H1, title, meta) + Additive (breadcrumb, intro)  
**Status:** Implementation Ready

---

## Ground Rules Reminder

> **Follow the ground rules in `01_ground_rules_do_not_delete_UPDATED.md`. Nothing here removes existing filters, cards, or components — this only updates approved metadata and adds breadcrumb/intro content.**

---

## Goal

Make the page immediately understandable to both users and search engines while maintaining the existing visual design and layout.

---

## Visible Structure

```html
<!-- Breadcrumb Navigation (NEW ADDITION) -->
<nav aria-label="Breadcrumb">
  <a href="/">Home</a> → <span>Government Jobs</span>
</nav>

<!-- Existing Header Structure with APPROVED EDITS -->
<header>
  <!-- APPROVED EDIT: Update H1 -->
  <h1>Government Jobs 2026 – Latest Active Sarkari Naukri</h1>
  
  <!-- NEW ADDITION: Intro paragraph -->
  <p>Find the latest active Government Jobs 2026 and Sarkari Naukri across India. Search and filter government vacancies by qualification, department, state, district, exam and application deadline. Check the recruitment details and official notification before applying.</p>
  
  <!-- NEW ADDITION: Dynamic inventory line -->
  <div>{{active_job_count}} active government jobs found · Updated {{last_updated_date}}</div>
  
  <!-- NEW ADDITION: Trust strip -->
  <div>Active Vacancies · Application Deadlines · Official Notification Links</div>
</header>
```

---

## Approved Metadata Changes

### Title Tag (APPROVED EDIT)
**Current:** (Likely homepage-oriented)  
**Update to:**
```html
<title>Government Jobs 2026 – Latest Sarkari Naukri & Govt Jobs</title>
```

**Character Count:** 58 characters (Optimized for SERP display)  
**Primary Keywords:** Government Jobs 2026, Sarkari Naukri, Govt Jobs

### Meta Description (APPROVED EDIT)
**Current:** (Likely homepage-oriented)  
**Update to:**
```html
<meta name="description" content="Find the latest Government Jobs 2026 and Sarkari Naukri in India. Browse active govt vacancies by qualification, department, state, district and exam.">
```

**Character Count:** 147 characters  
**Keywords:** Government Jobs 2026, Sarkari Naukri, govt vacancies, qualification, department, state, district, exam

### Canonical Tag (NEW ADDITION)
```html
<link rel="canonical" href="https://www.searchsarkarinaukri.com/jobs">
```

---

## H1 Specification (APPROVED EDIT)

### Current H1
```
All Active Government Jobs
```

### Update to
```
Government Jobs 2026 – Latest Active Sarkari Naukri
```

**Rules:**
- Use this H1 **only once** on the page
- Do not create multiple H1s
- This is the **only approved H1 change** per ground rules

---

## Intro Paragraph (NEW ADDITION)

### Copy
```
Find the latest active Government Jobs 2026 and Sarkari Naukri across India. Search and filter government vacancies by qualification, department, state, district, exam and application deadline. Check the recruitment details and official notification before applying.
```

**Length:** 40-60 words (optimized for UX and SEO)  
**Keywords:** Government Jobs 2026, Sarkari Naukri, government vacancies, qualification, department, state, district, exam, application deadline

---

## Dynamic Inventory Line (NEW ADDITION)

### Template
```
{{active_job_count}} active government jobs found · Updated {{last_updated_date}}
```

**Rules:**
- Never hardcode the number or date
- Use dynamic variables from your backend
- Update automatically when inventory changes
- Format: "200 active government jobs found · Updated 4 September 2026"

---

## Trust Strip (NEW ADDITION)

### Content
```
Active Vacancies · Application Deadlines · Official Notification Links
```

**Alternative (if verification workflow exists):**
```
Active Vacancies · Verified Job Information · Application Deadlines · Official Notification Links
```

**Rules:**
- Only use "Verified" if you have an actual editorial verification workflow
- Do not make claims you cannot substantiate
- Keep it concise and factual

---

## Breadcrumb Navigation (NEW ADDITION)

### HTML Structure
```html
<nav aria-label="Breadcrumb">
  <a href="/">Home</a> → <span>Government Jobs</span>
</nav>
```

### Placement
- Above H1
- Below main navigation
- Visible on both desktop and mobile

### BreadcrumbList Structured Data (NEW ADDITION)
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://www.searchsarkarinaukri.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Government Jobs",
      "item": "https://www.searchsarkarinaukri.com/jobs"
    }
  ]
}
```

---

## Keyword Placement Strategy

### Primary Keyword Placement
- **Title:** "Government Jobs 2026"
- **H1:** "Government Jobs 2026"
- **First 100 words:** Intro paragraph
- **One later relevant heading:** Government Jobs by [Category]

### Secondary Keywords
- Sarkari Naukri (H1, intro, body)
- Government Jobs in India (intro)
- Latest Government Jobs (section heading)
- Government Job Vacancies (body copy)

---

## UX Rules

1. **Search box visibility:** Search should be visible without scrolling on desktop and mobile
2. **No ad placement:** Do not place ads between H1 and search
3. **Intro length:** Keep intro to 40-60 words maximum
4. **Hero image:** Avoid giant hero images that delay LCP
5. **Mobile optimization:** Ensure breadcrumb and intro are readable on mobile

---

## Implementation Steps

### Step 1: Update Metadata (APPROVED EDIT)
1. Update `<title>` tag in the `/jobs` route/component
2. Update `<meta name="description">` 
3. Add `<link rel="canonical">` if not present
4. Verify no other metadata conflicts

### Step 2: Update H1 (APPROVED EDIT)
1. Locate existing H1 in `/jobs` component
2. Replace "All Active Government Jobs" with "Government Jobs 2026 – Latest Active Sarkari Naukri"
3. Ensure no other H1s exist on the page
4. Test heading hierarchy with accessibility tools

### Step 3: Add Breadcrumb (NEW ADDITION)
1. Add breadcrumb navigation above H1
2. Implement BreadcrumbList structured data
3. Style to match existing design
4. Test on mobile and desktop

### Step 4: Add Intro Paragraph (NEW ADDITION)
1. Add intro paragraph below H1
2. Keep within 40-60 words
3. Style to match existing typography
4. Ensure it doesn't push search too far down

### Step 5: Add Dynamic Inventory Line (NEW ADDITION)
1. Add dynamic count variable from backend
2. Add dynamic date variable from backend
3. Format as: "X active government jobs found · Updated DD Month YYYY"
4. Ensure automatic updates

### Step 6: Add Trust Strip (NEW ADDITION)
1. Add trust indicators below intro
2. Use only substantiated claims
3. Style as subtle badges or text
4. Consider adding icons if available

---

## Validation Checklist

- [ ] Title tag updated correctly
- [ ] Meta description updated correctly  
- [ ] Canonical tag added (if not present)
- [ ] H1 updated and is the only H1 on page
- [ ] Breadcrumb navigation added and functional
- [ ] BreadcrumbList structured data implemented
- [ ] Intro paragraph added and properly styled
- [ ] Dynamic inventory line shows real data
- [ ] Trust strip added with accurate claims
- [ ] No existing visual design changes
- [ ] No existing functionality broken
- [ ] Mobile layout tested
- [ ] Accessibility tested (screen readers, keyboard nav)
- [ ] Core Web Vitals not negatively impacted

---

## Developer Notes

1. **React Implementation:** Update the `/jobs` route component's metadata using your framework's head management (Next.js `metadata`, React Helmet, etc.)
2. **Dynamic Data:** Ensure backend provides accurate job count and last updated timestamp
3. **Styling:** Match existing design system - no visual redesign
4. **Testing:** Test in staging environment before production
5. **Rollback:** Keep previous metadata handy in case of issues

---

## Success Metrics

- [ ] Google Search Console shows improved click-through rate
- [ ] Users can understand page purpose within 3 seconds
- [ ] Breadcrumb navigation works correctly
- [ ] Dynamic inventory updates automatically
- [ ] No negative impact on user engagement metrics
- [ ] Accessibility audit passes

---

**Last Updated:** 4 September 2026  
**Dependencies:** None (can be implemented independently)  
**Blocks:** None (but should be done before other content sections)