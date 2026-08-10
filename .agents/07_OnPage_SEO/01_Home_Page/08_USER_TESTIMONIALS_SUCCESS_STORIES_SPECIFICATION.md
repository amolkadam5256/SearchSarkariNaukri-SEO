# ⭐ User Testimonials / Success Stories Section Specification

**Page:** Home Page (`https://www.searchsarkarinaukri.com/`)\
**Section Name:** `What Job Seekers Say / उमेदवारांचे अनुभव`\
**Alternative Section:** `Success Stories / यशोगाथा`\
**Purpose:** Build user trust, improve conversion, demonstrate
real-world usefulness, and provide authentic social proof.

---

## ⚠️ Critical Trust & Content Rule

**DO NOT create fake testimonials, fake names, fake candidates, fake job
selections, fake screenshots, fake ratings, or fabricated success
stories.**

Testimonials must come only from:

- Real SearchSarkariNaukri users.
- Real candidates who voluntarily submitted feedback.
- Genuine WhatsApp or other user messages, where permission has been
  obtained.
- Genuine feedback forms or surveys.
- Real success stories that can be verified internally.
- Real screenshots supplied by users, with personal information
  removed or consent obtained.

If there are currently **no genuine testimonials**, do **not** add
placeholder reviews that look real.

Instead, either:

1.  Hide the testimonial section until genuine feedback is collected, or
2.  Display a simple trust message such as:

> We are building our community of job seekers. Genuine candidate
> experiences and success stories will be featured here as more users
> share their feedback.

---

# 📌 Section Placement Directive

Recommended homepage placement:

```text
Main Homepage Content
        ↓
Government Job Categories
        ↓
Useful Tools / Features
        ↓
User Testimonials / Success Stories
        ↓
FAQ Section
        ↓
Footer
```

The testimonial section should preferably appear **before the FAQ
section and directly after the major product/value sections**.

---

# 🏷️ Recommended Section Heading

### Primary Heading

```text
What Job Seekers Say
```

### Bilingual Heading

```text
What Job Seekers Say / उमेदवारांचे अनुभव
```

### Alternative

```text
Success Stories / यशोगाथा
```

### Recommended `<h2>`

```html
<h2>What Job Seekers Say / उमेदवारांचे अनुभव</h2>
```

---

# 🎯 Main Objectives

The section should help visitors understand:

- Whether real candidates find the platform useful.
- How SearchSarkariNaukri helps users discover government jobs.
- Whether users find the job information easy to understand.
- Whether qualification and location filters are useful.
- Whether users find official application links useful.
- Whether job alerts help users discover new opportunities.
- Whether users have successfully applied for jobs discovered through
  the platform.

The section should support **trust and conversion**, not be treated as a
keyword-stuffing section.

---

# 📝 Testimonial Content Structure

Each genuine testimonial should ideally contain:

```text
Candidate First Name / Approved Display Name
Location
Qualification
Optional: Job Category
Short Genuine Feedback
Optional: Result / Outcome
```

Example structure:

```text
Name:
Rahul

Location:
Pune, Maharashtra

Qualification:
Graduate

Feedback:
"SearchSarkariNaukri helped me find government job notifications
according to my qualification. The official application links
made it easier for me to check the recruitment details."

Outcome:
Applied for a relevant government recruitment.
```

**Important:** This is only a content structure example. Do not publish
it as a real testimonial unless it comes from an actual user.

---

# ⭐ Testimonial Card Specification

Each testimonial card should contain:

### 1. Candidate Name

Use the real name only with permission.

If the candidate requests privacy:

```text
Rahul K.
```

or:

```text
Verified Candidate
```

Do not invent a name.

---

### 2. Location

Only display location when the candidate has consented.

Example:

```text
Pune, Maharashtra
```

---

### 3. Qualification

Only include it if provided voluntarily and appropriate.

Examples:

```text
Graduate
12th Pass
ITI
Diploma
Engineering
```

---

### 4. Genuine Feedback

Use the candidate's actual words where permission exists.

Do not rewrite the testimonial into a stronger claim that the candidate
did not make.

---

### 5. Outcome

Only include a success outcome if it is genuinely reported or verified.

Possible outcomes:

```text
Found a relevant vacancy
Applied for a government job
Discovered an important notification
Received a job alert
Cleared an examination
Received an interview/call
Joined a government department
```

Do not claim:

```text
Got a government job because of SearchSarkariNaukri
```

unless the candidate genuinely states this and the claim is supportable.

---

# 🧩 Recommended Testimonial Card UI

```text
┌──────────────────────────────────────────┐
│ ★★★★★                                   │
│                                          │
│ "Actual candidate feedback goes here."   │
│                                          │
│ Rahul K.                                 │
│ Pune, Maharashtra                        │
│ Graduate                                 │
│                                          │
│ Government Job Search                    │
└──────────────────────────────────────────┘
```

### Design Requirements

- Clean card layout.
- High readability.
- Mobile responsive.
- Avoid excessive animations.
- Do not use fake star ratings.
- Do not show 5-star ratings unless they were genuinely submitted.
- Do not use stock photos as if they are the candidates.
- Do not use AI-generated candidate portraits.
- Use initials/avatar only if the candidate's identity should remain
  private.
- Keep testimonials short enough to scan easily.

---

# 📱 Recommended Homepage Layout

Desktop:

```text
             What Job Seekers Say
             उमेदवारांचे अनुभव

        Real experiences from our users

┌────────────────┐ ┌────────────────┐ ┌────────────────┐
│ ★★★★★          │ │ ★★★★★          │ │ ★★★★★          │
│                │ │                │ │                │
│ Feedback       │ │ Feedback       │ │ Feedback       │
│                │ │                │ │                │
│ Candidate      │ │ Candidate      │ │ Candidate      │
│ Location       │ │ Location       │ │ Location       │
└────────────────┘ └────────────────┘ └────────────────┘
```

Mobile:

```text
What Job Seekers Say
उमेदवारांचे अनुभव

[ Testimonial Card ]

[ Testimonial Card ]

[ Testimonial Card ]
```

Use a horizontal carousel on mobile only if there are enough genuine
testimonials.

---

# 🇮🇳 Mixed English + Marathi Testimonial Strategy

Do not translate every testimonial into two separate versions.

Keep the language natural based on the actual user feedback.

Example of a genuine mixed-language testimonial format:

> "SearchSarkariNaukri वर माझ्या qualification नुसार government jobs शोधणे
> खूप सोपे झाले. Official notification आणि apply link एकाच ठिकाणी मिळाल्यामुळे
> मला recruitment details check करायला मदत झाली."

This is an example of the **style**, not a real testimonial.

Only publish actual user feedback.

---

# 🏆 Success Stories Section

If genuine success stories are available, create a separate subsection.

### Heading

```text
Success Stories / यशोगाथा
```

### Purpose

Show real examples of how candidates used the platform.

A success story should answer:

```text
Who was the candidate?
        ↓
What were they looking for?
        ↓
How did they use SearchSarkariNaukri?
        ↓
What did they discover?
        ↓
What happened afterward?
```

---

# 📖 Success Story Template

```text
## [Candidate Story Title]

Candidate:
[Real approved name]

Location:
[Location, if permitted]

Qualification:
[Qualification]

Looking For:
[Type of government job]

How SearchSarkariNaukri Helped:
[Actual experience]

Outcome:
[Actual outcome]

Candidate Quote:
"[Genuine quote]"
```

---

# Example Success Story Structure

**Important: The following is a TEMPLATE, not a real success story.**

```text
### From Job Search to Application

Candidate:
[Real Candidate Name]

Location:
Pune, Maharashtra

Qualification:
Graduate

Looking For:
Government jobs matching graduation qualification

How SearchSarkariNaukri Helped:
The candidate used the qualification and job-category
sections to discover relevant recruitment notifications
and then checked the official notification before applying.

Outcome:
Applied for a relevant government recruitment.

Candidate Quote:
"[Insert genuine candidate quote after receiving permission.]"
```

---

# 🔐 Privacy & Consent Requirements

Before publishing a testimonial, obtain permission to use:

- Candidate name.
- Location.
- Qualification.
- Photograph, if applicable.
- Screenshot, if applicable.
- WhatsApp message, if applicable.
- Quote.
- Success outcome.
- Any personal information contained in the feedback.

Never publish:

- Phone numbers.
- Email addresses.
- Application numbers.
- Aadhaar numbers.
- PAN details.
- Registration IDs.
- Login credentials.
- Personal documents.
- Private WhatsApp information.
- Sensitive personal information.

Redact personal information from screenshots before publication.

---

# 📸 Testimonial Screenshot Rules

If a genuine candidate sends feedback through WhatsApp:

```text
Original Screenshot
        ↓
Obtain Permission
        ↓
Remove Phone Number
        ↓
Remove Profile Photo if Necessary
        ↓
Remove Private Conversation Details
        ↓
Keep Relevant Feedback
        ↓
Publish
```

Do not create artificial WhatsApp screenshots.

Do not edit a candidate's message in a way that changes its meaning.

---

# ⭐ Star Rating Rules

Only show star ratings when there is a genuine rating system.

### If genuine rating exists:

```text
★★★★★ 5/5
```

### If no rating exists:

Do not display:

```text
★★★★★
```

simply to make the testimonial appear more trustworthy.

Use:

```text
Candidate Feedback
```

instead.

---

# 📊 Recommended Testimonial Database Structure

If testimonials are managed dynamically, use fields such as:

```text
id
candidate_name
display_name
location
qualification
job_category
testimonial_text
outcome
rating
source
consent_status
consent_date
photo_url
screenshot_url
is_verified
is_published
created_at
updated_at
```

### Suggested status values

```text
pending
approved
rejected
archived
```

Only:

```text
approved + consent_status = approved + is_published = true
```

should appear publicly.

---

# 🔎 SEO Considerations

Testimonials are primarily a **trust and conversion feature**, not a
keyword-stuffing mechanism.

Do not force keywords into testimonials.

Bad:

```text
"I found the best latest government jobs today through
SearchSarkariNaukri government jobs Maharashtra..."
```

Good:

```text
"I was looking for government jobs in Maharashtra and
found the qualification filter useful."
```

The second is more natural and credible.

---

# 🤖 AI Search / Semantic SEO Value

Real testimonials can provide useful contextual signals about:

- Government job discovery.
- Qualification-based search.
- Maharashtra recruitment.
- Job notification discovery.
- Application information.
- Job alerts.
- Candidate experience.

However:

**Testimonials should not be written solely for AI SEO.**

The primary purpose is genuine user trust.

---

# 🧠 E-E-A-T / Trust Guidance

Use testimonials to demonstrate real user experience, but do not present
testimonials as proof that SearchSarkariNaukri is an official government
authority.

Always maintain the distinction:

```text
SearchSarkariNaukri
        ↓
Independent career information platform
        ↓
Helps users discover recruitment information
        ↓
Official government notification
        ↓
Official recruitment authority
```

The official recruitment authority remains the authoritative source for:

- Eligibility.
- Vacancy.
- Dates.
- Fees.
- Selection process.
- Application requirements.
- Results.
- Recruitment decisions.

---

# ❌ Do Not Do This

Never create testimonials such as:

```text
"SearchSarkariNaukri helped me get my dream government job."
- Amit, Pune
```

unless Amit is a real user and this statement was genuinely provided.

Never create:

- Fake candidate profiles.
- Fake government-job selections.
- Fake salary claims.
- Fake application success rates.
- Fake review counts.
- Fake Google reviews.
- Fake screenshots.
- Fake WhatsApp conversations.
- AI-generated candidate photos presented as real people.
- Invented 5-star ratings.
- Invented success percentages.

---

# 🟡 If There Are Currently No Testimonials

Use a temporary trust section rather than fake reviews.

### Heading

```text
What Job Seekers Say / उमेदवारांचे अनुभव
```

### Temporary Copy

```text
We are building our community of job seekers and collecting
genuine feedback from users who use SearchSarkariNaukri to
discover recruitment opportunities.

तुमचा अनुभव आमच्यासाठी महत्त्वाचा आहे. SearchSarkariNaukri
वापरून सरकारी नोकरीची माहिती शोधली असल्यास तुमचा genuine
feedback आमच्यासोबत share करा.
```

### CTA

```text
Share Your Feedback
तुमचा अनुभव शेअर करा
```

CTA can link to a genuine feedback form.

---

# 📝 Recommended Feedback Form Fields

```text
Name
Email (optional)
Location
Qualification
What were you looking for?
How did SearchSarkariNaukri help you?
Your feedback
Did you successfully apply for a job you found here?
Would you allow us to publish your feedback?
Would you allow us to display your name?
Would you allow us to display your location?
Would you allow us to use your photo?
```

Consent should be explicit.

---

# 🔗 Internal Linking Opportunities

Where appropriate, testimonial content can link users toward:

```text
/jobs
/qualifications
/districts
/eligibility-checker
/latest-jobs
/admit-cards
/results
```

Do not insert links unnaturally into testimonial quotes.

---

# 📐 Structured Data Recommendation

Do not add fake review or rating structured data.

If implementing testimonial/review structured data, use only data that
genuinely represents real user reviews and follows current search-engine
structured-data requirements.

The testimonial section itself does **not require fake Review schema**
to be useful.

The priority is:

```text
Real User
   ↓
Real Feedback
   ↓
Consent
   ↓
Accurate Publication
   ↓
Trust
```

---

# 🚀 Implementation Priority

### Phase 1 --- No genuine testimonials

```text
Create section framework
        ↓
Show trust/feedback invitation
        ↓
Collect genuine feedback
```

### Phase 2 --- First genuine testimonials

```text
Collect 3–5 genuine testimonials
        ↓
Obtain consent
        ↓
Remove personal information
        ↓
Publish
```

### Phase 3 --- Genuine success stories

```text
Collect detailed candidate stories
        ↓
Verify claims where possible
        ↓
Obtain consent
        ↓
Create success-story cards
        ↓
Link relevant job/category pages
```

---

# ✅ Final Acceptance Checklist

Before publishing the section:

- [ ] Every testimonial comes from a real person.
- [ ] Permission has been obtained.
- [ ] No fake names have been created.
- [ ] No fake photos have been created.
- [ ] No fake ratings have been added.
- [ ] No fake success claims have been added.
- [ ] Private information has been removed.
- [ ] Candidate quotes have not been misleadingly edited.
- [ ] Government recruitment claims are supported by official sources.
- [ ] The section works on mobile.
- [ ] Testimonials are readable and accessible.
- [ ] No keyword stuffing.
- [ ] No fake Review schema.
- [ ] Testimonials accurately represent actual user experience.

---

# 🎯 Final Recommendation

If SearchSarkariNaukri currently has **no genuine testimonials**, do not
add a fake `What Job Seekers Say` section merely because competitors
have one.

Use:

**What Job Seekers Say / उमेदवारांचे अनुभव**

with a genuine feedback invitation until enough real feedback is
collected.

Once real feedback is available, replace the invitation with authentic
testimonials and, where appropriate, verified success stories.
