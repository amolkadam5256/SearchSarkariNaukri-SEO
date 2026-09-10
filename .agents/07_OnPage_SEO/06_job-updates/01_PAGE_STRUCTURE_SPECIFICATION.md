# 01 — PAGE STRUCTURE SPECIFICATION

**Section:** Complete HTML Structure  
**Priority:** P0  
**Type:** Technical Specification  
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

## Complete HTML Structure

### 1. Header (Preserve Existing)
```html
<header>
  <!-- Keep existing header exactly as is -->
  <!-- No changes to navigation -->
  <!-- No changes to navbar -->
  <!-- No changes to logo -->
  <!-- No changes to mobile menu -->
</header>
```

### 2. Breadcrumb (Improve Semantic Markup)
```html
<nav aria-label="Breadcrumb">
  <ol itemscope itemtype="https://schema.org/BreadcrumbList">
    <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <a href="/" itemprop="item">
        <span itemprop="name">Home</span>
      </a>
      <meta itemprop="position" content="1" />
    </li>
    <li aria-current="page" itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <span itemprop="name">Job Updates</span>
      <meta itemprop="position" content="2" />
    </li>
  </ol>
</nav>
```

### 3. H1 (Single H1 Required)
```html
<h1>Sarkari Naukri & Government Job Alerts 2026</h1>
```

### 4. Introduction Section
```html
<section id="introduction">
  <p>Find the latest Sarkari Naukri and government job updates in India, including new recruitment notifications, vacancies, application deadlines, exam updates and other important recruitment information.</p>
  
  <p>Search Sarkari Naukri brings job seekers together with current government recruitment information across central and state departments. You can browse jobs by qualification, category and location, then check the official recruitment notification before applying.</p>
</section>
```

### 5. First CTA Section
```html
<section id="cta-primary">
  <h2>Get Free Sarkari Naukri Alerts</h2>
  <div class="cta-buttons">
    <a href="#whatsapp-cta" class="btn btn-whatsapp">WhatsApp</a>
    <a href="#telegram-cta" class="btn btn-telegram">Telegram</a>
  </div>
  <p>All alerts are free to join. Always verify the final eligibility requirements, dates, fees and application procedure in the official recruitment notification.</p>
</section>
```

### 6. Latest Government Job Alerts (Dynamic Section)
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
      <!-- Do not hardcode - use real job data -->
    </tbody>
  </table>
</section>
```

### 7. Government Jobs Closing Soon (Dynamic Section)
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
      <!-- Do not hardcode - use real job data -->
    </tbody>
  </table>
</section>
```

### 8. Free Sarkari Naukri Alerts on WhatsApp & Telegram
```html
<section id="whatsapp-telegram-alerts">
  <h2>Free Sarkari Naukri Alerts on WhatsApp & Telegram</h2>
  
  <div class="alert-platforms">
    <div class="platform whatsapp">
      <h3>WhatsApp</h3>
      <p>Get job notifications and deadline reminders directly on WhatsApp.</p>
      <a href="#whatsapp-join-link" class="btn btn-whatsapp">Join WhatsApp Community</a>
    </div>
    
    <div class="platform telegram">
      <h3>Telegram</h3>
      <p>Follow the channel for recruitment updates, exam news and other important alerts.</p>
      <a href="#telegram-join-link" class="btn btn-telegram">Join Telegram Channel</a>
    </div>
  </div>
  
  <div class="what-users-receive">
    <h3>What Users Receive</h3>
    <ul>
      <li>Daily government job notifications</li>
      <li>Application deadline reminders</li>
      <li>Exam updates and admit card alerts</li>
      <li>Result announcements</li>
      <li>Important recruitment notices</li>
    </ul>
  </div>
  
  <div class="why-alerts-useful">
    <h3>Why Alerts Are Useful</h3>
    <p>Government recruitment notifications are issued throughout the year across various departments. Subscribing to alerts ensures you do not miss important vacancies, deadline changes, admit card releases or result announcements.</p>
  </div>
</section>
```

### 9. Government Jobs by Qualification
```html
<section id="jobs-by-qualification">
  <h2>Government Jobs by Qualification</h2>
  
  <div class="qualification-grid">
    <div class="qualification-item">
      <h3>10th Pass Government Jobs</h3>
      <p>Find government job opportunities available for candidates who have completed Class 10. Check current vacancies, eligibility, age requirements, application dates and official notifications before applying.</p>
      <a href="/jobs?qualification=10th" class="btn btn-view">View 10th Pass Jobs</a>
    </div>
    
    <div class="qualification-item">
      <h3>12th Pass Government Jobs</h3>
      <p>Find government job opportunities available for candidates who have completed Class 12. Check current vacancies, eligibility, age requirements, application dates and official notifications before applying.</p>
      <a href="/jobs?qualification=12th" class="btn btn-view">View 12th Pass Jobs</a>
    </div>
    
    <div class="qualification-item">
      <h3>Graduate Government Jobs</h3>
      <p>Find government job opportunities available for graduate candidates. Check current vacancies, eligibility, age requirements, application dates and official notifications before applying.</p>
      <a href="/jobs?qualification=graduate" class="btn btn-view">View Graduate Jobs</a>
    </div>
    
    <div class="qualification-item">
      <h3>ITI Government Jobs</h3>
      <p>Find government job opportunities available for ITI certificate holders. Check current vacancies, eligibility, age requirements, application dates and official notifications before applying.</p>
      <a href="/jobs?qualification=iti" class="btn btn-view">View ITI Jobs</a>
    </div>
    
    <div class="qualification-item">
      <h3>Diploma Government Jobs</h3>
      <p>Find government job opportunities available for diploma holders. Check current vacancies, eligibility, age requirements, application dates and official notifications before applying.</p>
      <a href="/jobs?qualification=diploma" class="btn btn-view">View Diploma Jobs</a>
    </div>
    
    <div class="qualification-item">
      <h3>Postgraduate Government Jobs</h3>
      <p>Find government job opportunities available for postgraduate candidates. Check current vacancies, eligibility, age requirements, application dates and official notifications before applying.</p>
      <a href="/jobs?qualification=postgraduate" class="btn btn-view">View Postgraduate Jobs</a>
    </div>
  </div>
</section>
```

### 10. Government Jobs by Category
```html
<section id="jobs-by-category">
  <h2>Government Jobs by Category</h2>
  
  <div class="category-grid">
    <div class="category-item">
      <h3>Railway Government Jobs</h3>
      <p>RRB/RRC recruitment, Railway vacancies, Group D, NTPC, ALP, Technician and other railway recruitment updates.</p>
      <a href="/exams/rrb-ntpc" class="btn btn-view">View Railway Jobs</a>
    </div>
    
    <div class="category-item">
      <h3>Banking Government Jobs</h3>
      <p>SBI, IBPS, RBI and other banking recruitment notifications.</p>
      <a href="/exams/sbi-po-clerk" class="btn btn-view">View Banking Jobs</a>
    </div>
    
    <div class="category-item">
      <h3>Police Government Jobs</h3>
      <p>Police Bharti, constable, SI and other police recruitment updates.</p>
      <a href="/exams/maharashtra-police-bharti" class="btn btn-view">View Police Jobs</a>
    </div>
    
    <div class="category-item">
      <h3>SSC Government Jobs</h3>
      <p>SSC CGL, CHSL, MTS and other Staff Selection Commission recruitment updates.</p>
      <a href="/exams/ssc-cgl" class="btn btn-view">View SSC Jobs</a>
    </div>
    
    <div class="category-item">
      <h3>UPSC Government Jobs</h3>
      <p>Civil Services, IAS, IPS and other UPSC recruitment notifications.</p>
      <a href="/exams/upsc-civil-services" class="btn btn-view">View UPSC Jobs</a>
    </div>
    
    <div class="category-item">
      <h3>Defence Government Jobs</h3>
      <p>Army, Navy, Air Force and other defence recruitment notifications.</p>
      <a href="/exams/indian-army" class="btn btn-view">View Defence Jobs</a>
    </div>
    
    <div class="category-item">
      <h3>Teaching Government Jobs</h3>
      <p>TET, CTET, UGC NET and other teaching recruitment notifications.</p>
      <a href="/exams/ctet" class="btn btn-view">View Teaching Jobs</a>
    </div>
    
    <div class="category-item">
      <h3>Maharashtra Government Jobs</h3>
      <p>MPSC, Police Bharti, Talathi, ZP and other Maharashtra government recruitment.</p>
      <a href="/districts" class="btn btn-view">View Maharashtra Jobs</a>
    </div>
    
    <div class="category-item">
      <h3>PSU Government Jobs</h3>
      <p>Public Sector Undertaking recruitment notifications across various sectors.</p>
      <a href="/exams/psu" class="btn btn-view">View PSU Jobs</a>
    </div>
  </div>
</section>
```

### 11. Government Jobs by State
```html
<section id="jobs-by-state">
  <h2>Government Jobs by State</h2>
  
  <div class="state-grid">
    <a href="/districts" class="state-item">Maharashtra</a>
    <a href="/state/up" class="state-item">Uttar Pradesh</a>
    <a href="/state/bihar" class="state-item">Bihar</a>
    <a href="/state/rajasthan" class="state-item">Rajasthan</a>
    <a href="/state/mp" class="state-item">Madhya Pradesh</a>
    <a href="/state/gujarat" class="state-item">Gujarat</a>
    <a href="/state/karnataka" class="state-item">Karnataka</a>
    <a href="/state/tamilnadu" class="state-item">Tamil Nadu</a>
    <a href="/state/delhi" class="state-item">Delhi</a>
    <a href="/state/westbengal" class="state-item">West Bengal</a>
  </div>
</section>
```

### 12. Why Use Search Sarkari Naukri for Job Alerts
```html
<section id="why-use">
  <h2>Why Use Search Sarkari Naukri for Government Job Updates?</h2>
  
  <p>Finding a suitable government vacancy is not only about discovering a job title. Applicants also need to check eligibility, age requirements, important dates, fees, documents and the official application process.</p>
  
  <p>Search Sarkari Naukri helps organize this information into easier-to-browse job and exam resources.</p>
  
  <ul>
    <li>Browse current government job opportunities</li>
    <li>Find jobs based on qualification and category</li>
    <li>Explore government recruitment by state and district</li>
    <li>Check exam, admit card and result updates</li>
    <li>Use the Eligibility Checker for a basic profile match</li>
    <li>Save important jobs and set reminders</li>
    <li>Receive daily-curated updates through WhatsApp and Telegram</li>
  </ul>
  
  <p>Search Sarkari Naukri is an independent information platform and is not affiliated with any government department. Before submitting an application, always check the official recruitment notification and official website.</p>
</section>
```

### 13. How Our Sarkari Naukri Alerts Work
```html
<section id="how-alerts-work">
  <h2>How Our Sarkari Naukri Alerts Work</h2>
  
  <div class="steps">
    <div class="step">
      <h3>Step 1</h3>
      <p>Join the Search Sarkari Naukri WhatsApp Community or Telegram Channel using the links provided on this page.</p>
    </div>
    
    <div class="step">
      <h3>Step 2</h3>
      <p>Receive daily-curated government job notifications directly on your WhatsApp or Telegram.</p>
    </div>
    
    <div class="step">
      <h3>Step 3</h3>
      <p>Click the job link to view complete vacancy details, eligibility, important dates and application instructions.</p>
    </div>
    
    <div class="step">
      <h3>Step 4</h3>
      <p>Verify the information in the official recruitment notification and apply through the official website before the deadline.</p>
    </div>
  </div>
</section>
```

### 14. How to Check a Government Job Before Applying
```html
<section id="how-to-check">
  <h2>How to Check a Government Job Before Applying</h2>
  
  <ul>
    <li>Read the official recruitment notification carefully</li>
    <li>Check eligibility criteria (qualification, age limit, nationality)</li>
    <li>Verify important dates (application start date, last date, exam date)</li>
    <li>Review application fee and payment method</li>
    <li>Check required documents and their specifications</li>
    <li>Understand the selection process (exam, interview, document verification)</li>
    <li>Confirm the official application website</li>
    <li>Verify vacancy details (post name, number of posts, pay scale)</li>
  </ul>
</section>
```

### 15. Verify Recruitment Information
```html
<section id="verify-information">
  <h2>Verify Recruitment Information</h2>
  
  <p>We collect recruitment information from official notifications and recruitment websites. Before applying, candidates should open the official notification and confirm the vacancy, eligibility, age limit, application fee, important dates and application process.</p>
  
  <div class="verification-info">
    <p><strong>Last Updated:</strong> [Dynamic date]</p>
    <p><strong>Reviewed Date:</strong> [Dynamic date]</p>
    <p><strong>Editorial Policy:</strong> <a href="/editorial-policy">View Editorial Policy</a></p>
    <p><strong>Official Source:</strong> Always verify with official recruitment notification</p>
    <p><strong>Recruitment Authority:</strong> Respective government department</p>
  </div>
</section>
```

### 16. Internal Resource Links
```html
<section id="internal-links">
  <h2>Related Resources</h2>
  
  <div class="link-grid">
    <a href="/jobs">Sarkari Naukri - Government Jobs</a>
    <a href="/exams">Government Exams</a>
    <a href="/exams/mpsc-rajyaseva">MPSC Rajyaseva</a>
    <a href="/exams/maharashtra-police-bharti">Maharashtra Police Bharti</a>
    <a href="/exams/rrb-ntpc">Railway Jobs</a>
    <a href="/exams/sbi-po-clerk">Banking Jobs</a>
    <a href="/results">Government Results</a>
    <a href="/admit-cards">Admit Cards</a>
    <a href="/districts">Government Jobs by District</a>
    <a href="/eligibility-checker">Eligibility Checker</a>
    <a href="/age-calculator">Age Calculator</a>
    <a href="/current-affairs">Current Affairs</a>
  </div>
</section>
```

### 17. Sarkari Naukri 2026 FAQs
```html
<section id="faq">
  <h2>Frequently Asked Questions About Sarkari Naukri</h2>
  
  <div class="faq-item">
    <h3>What is Sarkari Naukri?</h3>
    <p>Sarkari Naukri refers to employment opportunities offered through central and state government departments, public-sector organizations and other government bodies in India.</p>
  </div>
  
  <div class="faq-item">
    <h3>Where can I find the latest Sarkari Naukri?</h3>
    <p>You can browse current government recruitment updates through the Jobs and Job Updates sections of Search Sarkari Naukri. Always check the official recruitment notification before applying.</p>
  </div>
  
  <div class="faq-item">
    <h3>Are government job alerts free?</h3>
    <p>Yes. The Search Sarkari Naukri WhatsApp Community and Telegram Channel promoted on this page are free to join.</p>
  </div>
  
  <div class="faq-item">
    <h3>How can I get Sarkari Naukri alerts on WhatsApp?</h3>
    <p>Join the Search Sarkari Naukri WhatsApp Community through the official join link on this page. You can receive daily-curated recruitment updates and deadline reminders.</p>
  </div>
  
  <div class="faq-item">
    <h3>How can I get government job alerts on Telegram?</h3>
    <p>Join the official Search Sarkari Naukri Telegram Channel using the Telegram link provided on this page.</p>
  </div>
  
  <div class="faq-item">
    <h3>Can I find government jobs by qualification?</h3>
    <p>Yes. Job seekers can browse opportunities according to qualifications such as 10th pass, 12th pass, Graduate, ITI and Diploma, where the relevant job data is available.</p>
  </div>
  
  <div class="faq-item">
    <h3>How can I check my eligibility for a government job?</h3>
    <p>Read the eligibility requirements in the official recruitment notification. Search Sarkari Naukri also provides an Eligibility Checker for a basic profile match.</p>
  </div>
  
  <div class="faq-item">
    <h3>Are Search Sarkari Naukri and the government the same organization?</h3>
    <p>No. Search Sarkari Naukri is an independent government-job information platform. Candidates should verify recruitment information through the official notification and official website before applying.</p>
  </div>
</section>
```

### 18. Second CTA
```html
<section id="cta-secondary">
  <h2>Don't Miss the Next Government Job Notification</h2>
  <div class="cta-buttons">
    <a href="#whatsapp-cta" class="btn btn-whatsapp">Join WhatsApp</a>
    <a href="#telegram-cta" class="btn btn-telegram">Join Telegram</a>
  </div>
</section>
```

### 19. Final CTA
```html
<section id="cta-final">
  <h2>Get Daily Government Job Alerts Free</h2>
  <div class="cta-buttons">
    <a href="#whatsapp-cta" class="btn btn-whatsapp">WhatsApp Alerts</a>
    <a href="#telegram-cta" class="btn btn-telegram">Telegram Alerts</a>
  </div>
</section>
```

### 20. Footer (Preserve Existing)
```html
<footer>
  <!-- Keep existing footer exactly as is -->
  <!-- No changes to footer links -->
  <!-- No changes to footer structure -->
  <!-- No changes to disclaimer -->
</footer>
```

---

## Semantic HTML Requirements

### Heading Hierarchy
- H1: 1 instance (Sarkari Naukri & Government Job Alerts 2026)
- H2: Section headings (Latest Government Job Alerts, Government Jobs by Qualification, etc.)
- H3: Subsection headings (10th Pass Government Jobs, Railway Government Jobs, etc.)
- No skipped heading levels
- No duplicate H1s

### Accessibility Requirements
- Semantic HTML elements (nav, section, article, aside, footer)
- ARIA labels where needed
- Alt text for images
- Proper form labels
- Keyboard navigation support
- Visible focus states
- Sufficient color contrast
- Screen reader compatibility

### Mobile Optimization
- Responsive design
- Touch-friendly CTA buttons
- Readable font sizes on mobile
- Horizontal scrolling prevention
- Accessible tables on mobile

---

**Implementation Priority:** P0  
**Estimated Complexity:** Medium  
**Dependencies:** Database job listings, existing WhatsApp/Telegram integration
