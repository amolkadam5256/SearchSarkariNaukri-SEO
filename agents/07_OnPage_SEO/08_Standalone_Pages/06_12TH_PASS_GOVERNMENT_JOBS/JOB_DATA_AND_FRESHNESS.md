# Job Data, Freshness and Recruitment Status Rules

## Fields to display when supported by verified records

- Job title and recruiting organization.
- Educational qualification and post-specific conditions.
- Actual posting/location coverage.
- Vacancy count only when officially specified.
- Notification publication date.
- Application opening date and deadline.
- Recruitment status.
- Official notification and application URLs.
- Last-verified date only when recorded by the system.

## Status definitions

- **Upcoming:** confirmed notice; applications have not opened.
- **Open:** applications are currently accepted according to verified notice dates and updates.
- **Closing soon:** verified deadline falls within the product's defined warning window, calculated in the correct timezone.
- **Closed:** deadline passed or authority closed applications.
- **Extended:** official extension verified; display the revised deadline and source.
- **Result/selection stage:** application is no longer the main action and recruitment has progressed.
- **Unverified:** record requires review; do not present it as active.

Respect corrections, extensions, timezone boundaries and cancellations. A database record's presence alone does not mean the vacancy is active. Never show an expired deadline with an active Apply action. Do not claim a state-specific vacancy merely because a state link is present; verify the posting location and eligibility from its notice.

## Required data audit

- [ ] Recalculate the reported 50 active openings from the actual records.
- [ ] Recheck each deadline reported as 27 October 2026 and all other displayed deadlines against later notices.
- [ ] Validate duplicate records, recruitment-cycle identifiers and status transitions.
- [ ] Verify the record's Class 12 eligibility; broad category labels are insufficient.
- [ ] Verify each official notification and application URL.
- [ ] Keep historical, closed and result-stage records clearly separated from current applications.
- [ ] Use useful empty/loading/error states when records are absent or unavailable.
