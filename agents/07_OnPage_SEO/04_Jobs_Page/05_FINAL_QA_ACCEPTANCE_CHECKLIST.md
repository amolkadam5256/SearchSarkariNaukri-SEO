# Final QA And Acceptance Checklist

Run this before considering the `/jobs` upgrade complete.

## Data Preservation

- [ ] Existing header unchanged
- [ ] Existing navbar unchanged
- [ ] Existing main navigation unchanged
- [ ] Existing footer unchanged
- [ ] No header/navbar/footer links added
- [ ] No header/navbar/footer links removed
- [ ] No header/navbar/footer labels renamed
- [ ] No header/navbar/footer menu order changed
- [ ] No header/navbar/footer layout redesigned
- [ ] No existing jobs deleted
- [ ] No existing job IDs changed
- [ ] No existing job URLs/slugs removed
- [ ] No existing indexed URLs removed
- [ ] No existing category URLs removed
- [ ] No existing district URLs removed
- [ ] No existing qualification URLs removed
- [ ] No existing exam URLs removed
- [ ] Existing FAQs preserved
- [ ] Existing internal links preserved or redirected
- [ ] Existing WhatsApp and Telegram channels preserved

## Job Accuracy

- [ ] Expired jobs are not displayed as active
- [ ] Closed jobs are retained as historical/closed where appropriate
- [ ] Closed jobs link to related active jobs
- [ ] Active count is accurate
- [ ] Displayed range is accurate
- [ ] Pagination count matches total results
- [ ] Vacancy formatting is normalized
- [ ] Location formatting is normalized
- [ ] Deadline formatting is normalized
- [ ] No negative countdowns
- [ ] No fake salary
- [ ] No fake vacancy
- [ ] No fake age limit
- [ ] No fake organization
- [ ] No fake deadline
- [ ] No fake application mode

## Search And Filters

- [ ] Search works by job title
- [ ] Search works by organization
- [ ] Search works by post/designation
- [ ] Search works by keyword
- [ ] Search works by location where supported
- [ ] Search works by qualification where supported
- [ ] Qualification filter works
- [ ] State filter works
- [ ] District filter works
- [ ] Department filter works
- [ ] Job type filter works
- [ ] Application mode filter works
- [ ] Exam filter works
- [ ] Deadline filter works
- [ ] Experience filter works where supported
- [ ] Filters preserve query state
- [ ] Pagination preserves query state
- [ ] Empty states are helpful and do not create thin SEO pages

## Page Sections

- [ ] Breadcrumb
- [ ] Correct H1
- [ ] Intro
- [ ] Dynamic statistics row
- [ ] Main search
- [ ] Advanced filters
- [ ] Quick search chips
- [ ] Popular searches
- [ ] Government Jobs Closing Today
- [ ] Government Jobs Closing Soon
- [ ] New Government Jobs Today
- [ ] Latest Government Jobs 2026
- [ ] Pagination
- [ ] Government Jobs by Qualification
- [ ] Government Jobs by State
- [ ] Government Jobs by District
- [ ] Government Jobs by City
- [ ] Government Jobs by Department
- [ ] Government Jobs by Exam
- [ ] Government Jobs by Organization
- [ ] Government Jobs by Type
- [ ] Government Jobs by Post / Designation
- [ ] Government Jobs for Freshers
- [ ] Government Jobs by Application Mode
- [ ] Government Jobs by Salary only if data supports it
- [ ] Central Government Jobs
- [ ] State Government Jobs
- [ ] Popular Government Job Categories
- [ ] Find Government Jobs by Deadline
- [ ] How to Find the Right Government Job
- [ ] How to Apply for Government Jobs
- [ ] Common Documents Required for Government Jobs
- [ ] Recruitment lifecycle links
- [ ] Useful Government Job Resources
- [ ] About Government Job Listings
- [ ] FAQ
- [ ] Job Alerts CTA
- [ ] Footer

## SEO

- [ ] SEO title implemented
- [ ] Meta description implemented
- [ ] `/jobs` canonical is correct
- [ ] Filtered page canonical/noindex strategy reviewed
- [ ] One H1 only
- [ ] H2/H3 hierarchy is clean
- [ ] BreadcrumbList structured data valid
- [ ] ItemList structured data valid where used
- [ ] FAQ schema used only if valid
- [ ] Individual job JobPosting schema accurate
- [ ] Expired jobs are not marked as active opportunities in schema
- [ ] Sitemap includes important job/landing pages
- [ ] Robots/noindex does not block valuable pages
- [ ] No broken internal links
- [ ] No orphan important pages
- [ ] No duplicate paragraphs
- [ ] No keyword stuffing
- [ ] No doorway/thin pages

## Internal Linking

- [ ] `/jobs` links to qualification pages
- [ ] `/jobs` links to state pages
- [ ] `/jobs` links to district pages
- [ ] `/jobs` links to city pages
- [ ] `/jobs` links to department/category pages
- [ ] `/jobs` links to exam pages
- [ ] `/jobs` links to organization pages where valid
- [ ] `/jobs` links to job-type pages where valid
- [ ] `/jobs` links to post/designation pages where valid
- [ ] Job cards link to relevant contextual pages where valid
- [ ] Individual jobs link back to relevant hubs
- [ ] Related jobs are contextual and dynamic
- [ ] Footer navigation remains intact and unchanged
- [ ] New internal links are placed inside page body sections, not global header/navbar/footer

## Accessibility

- [ ] Semantic HTML landmarks
- [ ] Breadcrumb has accessible label
- [ ] Search input has label
- [ ] Filter controls have labels
- [ ] Buttons have clear names
- [ ] Status badges are screen-reader friendly
- [ ] Keyboard navigation works
- [ ] Focus states are visible
- [ ] Color contrast is acceptable
- [ ] Mobile controls are thumb-friendly
- [ ] No horizontal overflow

## UX And Design

- [ ] Page feels like a professional government recruitment portal
- [ ] Jobs database remains the primary product
- [ ] Search is prominent
- [ ] Filters are easy to use
- [ ] Deadline is obvious on cards
- [ ] Cards are scannable
- [ ] Mobile layout is excellent
- [ ] Desktop layout is information-dense but readable
- [ ] No giant hero image
- [ ] No distracting animations
- [ ] No excessive gradients
- [ ] No long generic SEO paragraphs above listings

## Performance

- [ ] Server-side pagination where applicable
- [ ] Efficient queries
- [ ] Useful indexes for filter fields
- [ ] No rendering hundreds of unnecessary cards
- [ ] No loading all jobs into browser for filtering
- [ ] No duplicate API calls
- [ ] Non-critical content lazy-loaded where needed
- [ ] Core Web Vitals reviewed

## Final Acceptance

The upgrade is accepted only when `/jobs` is a complete Government Jobs discovery hub:

- Accurate
- Useful
- Fast
- Crawlable
- Mobile-friendly
- Accessible
- Internally connected
- Built around existing data
- Free of fake information
- Free of deleted existing SEO assets
- Free of header, navbar, main navigation, and footer changes
