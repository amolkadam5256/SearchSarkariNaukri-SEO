# 11 — ABOUT / TRUST / E-E-A-T SECTION

**Section:** Trust Signals and Editorial Information  
**Priority:** P1  
**Type:** Additive (New content section)  
**Status:** Implementation Ready

---

## Ground Rules Reminder

> **Follow the ground rules in `01_ground_rules_do_not_delete_UPDATED.md`. This adds a new section without removing existing functionality.**

---

## Goal

Establish trust and credibility by clearly communicating who publishes the information, where it comes from, when it was updated, and where users can verify it.

---

## H2 Heading

```html
<h2>About These Government Job Listings</h2>
```

---

## Main Copy

```
Search Sarkari Naukri brings government recruitment information together in one place to help candidates discover relevant job opportunities. Listings may include vacancies, qualifications, locations, application deadlines and other recruitment information.

Search Sarkari Naukri is an information platform and is not affiliated with any government body. The recruiting organisation named in each listing is the source of the recruitment notification. Candidates should read the official notification and verify important details before applying.
```

---

## Dynamic Trust Information

### Last Updated Display
**Template:** `Last updated: {{actual_inventory_update}}`

**Implementation:** Only show a date generated from the real system when inventory actually changes.

**Example:** `Last updated: 4 September 2026`

### Optional Editorial Credit
**Copy:** Reviewed by Search Sarkari Naukri Editorial Team

**Implementation:** Only use this if an actual editorial review process exists.

**Rule:** Do not add editorial credit if there's no real review workflow.

---

## Editorial Policy Link

### Anchor and Destination
**Anchor:** Editorial Policy  
**Destination:** `/editorial-policy`

**Copy:** Learn how Search Sarkari Naukri researches and updates recruitment information in our Editorial Policy.

**Implementation:** The existing footer already links to `/editorial-policy`. This provides contextual access.

---

## Trust Architecture for Individual Job Pages

### Every Recruitment Page Should Identify

**Required Information:**
- Recruiting organisation
- Official notification
- Official website/application portal
- Published date
- Updated date
- Last date
- Eligibility
- Source

**Implementation:** This information should be clearly visible on individual job detail pages.

---

## Claims to Avoid

### Do NOT Claim
- "100% verified" (unless you have actual verification workflow)
- "official government website" (unless you actually are the official site)
- "government-approved" (unless specifically approved)
- "guaranteed government job" (never guarantee jobs)

### Only Use When Objectively True
- "Verified Job Information" (only with real verification process)
- "Official Source" (when linking to actual official sources)
- "Updated Regularly" (when actually updated regularly)

---

## Existing Legal/Disclaimer Links

### Keep Accessible
- Disclaimer
- Privacy Policy
- Terms & Conditions
- Cookie Policy
- Refund / No-Payment Policy
- Editorial Policy

**Implementation:** Ensure these remain accessible from this section or footer.

---

## E-E-A-T Objectives

### Make It Obvious
**Who publishes?** → Search Sarkari Naukri  
**Where does information come from?** → Official recruitment notifications  
**When was it updated?** → Dynamic last updated date  
**Where can candidates verify?** → Official notification links

---

## Implementation Steps

### Step 1: Create Section Structure
1. Add H2 heading after resources section
2. Add main copy about the platform
3. Add disclaimer about non-affiliation
4. Style to match existing design

### Step 2: Add Dynamic Trust Information
1. Implement last updated date display
2. Add optional editorial credit (if applicable)
3. Ensure dates are dynamically generated
4. Add source attribution where relevant

### Step 3: Add Editorial Policy Link
1. Add contextual link to editorial policy
2. Add explanatory copy
3. Ensure link is working
4. Test on mobile and desktop

### Step 4: Add Legal/Disclaimer Links
1. Ensure all legal links are accessible
2. Add context for each link
3. Maintain existing footer links
4. Test link functionality

### Step 5: Mobile Optimization
1. Test trust section on mobile
2. Ensure readability on small screens
3. Optimize spacing and layout
4. Test link accessibility

---

## Validation Checklist

- [ ] H2 heading added after resources section
- [ ] Main copy about platform added
- [ ] Non-affiliation disclaimer included
- [ ] Dynamic last updated date working
- [ ] Editorial credit added (if applicable)
- [ ] Editorial policy link working
- [ ] Legal/disclaimer links accessible
- [ ] No unsupported claims made
- [ ] Mobile layout tested
- [ ] Trust signals clearly visible
- [ ] Source attribution clear
- [ ] No existing functionality broken

---

## Developer Notes

1. **React Implementation:** Create trust section component with dynamic date
2. **Dynamic Data:** Ensure last updated date comes from real system updates
3. **Content Accuracy:** Review all claims for accuracy and substantiation
4. **Legal Compliance:** Ensure all required legal links are present
5. **Performance:** Keep trust section lightweight

---

## Success Metrics

- [ ] User trust indicators improve (user feedback)
- [ ] Reduced complaints about information accuracy
- [ ] Increased usage of official verification links
- [ ] Better understanding of platform role
- [ ] Positive user feedback on transparency
- [ ] Improved editorial policy page visits

---

## SEO Considerations

### E-E-A-T Signals
- Clear author/publisher information
- Transparent sourcing
- Regular updates
- Editorial oversight
- Legal compliance

### Content Strategy
- Be transparent about platform role
- Emphasize official sources
- Provide verification guidance
- Maintain accurate information
- Build user trust through clarity

---

## AEO Enhancement

### Question-Answer Format

**Question:** Who publishes these government job listings?

**Answer:** Search Sarkari Naukri publishes these government job listings as an information platform. The platform is not affiliated with any government body. All recruitment information is sourced from official notifications published by recruiting organisations.

**Implementation:** Add to trust section and FAQ.

---

**Last Updated:** 4 September 2026  
**Dependencies:** 10_RESOURCES_SECTION.md  
**Blocks:** None (can be implemented independently)