# 02 - SEMANTIC HTML STRUCTURE

**Route:** `/exams/upsc-cse`  
**Purpose:** Semantic tags, heading hierarchy and component layout

---

## Heading Rules

- Use exactly one `h1`.
- Use `h2` for major page sections.
- Use `h3` for section subsections.
- Use `h4` inside cards, grouped lists, or table helper sections only when needed.
- Use `h5` and `h6` only if the design genuinely needs deeper hierarchy, such as nested syllabus topics inside a collapsible group.
- Do not skip heading levels for visual styling. Use CSS classes for size, not wrong heading levels.

## Required Heading Map

```text
h1 UPSC Civil Services Examination 2026 - Eligibility, Syllabus, Pattern & Dates

h2 UPSC CSE 2026 Current Status
h2 UPSC CSE at a Glance
h2 Table of Contents
h2 What is the UPSC Civil Services Examination?
h2 Services Through UPSC Civil Services Examination
h2 UPSC CSE 2026 Important Dates
h2 UPSC CSE Eligibility
  h3 Nationality Requirements
  h3 Educational Qualification
    h4 Graduates
    h4 Final-year or Result-pending Candidates
    h4 Professional Qualifications
    h4 Proof of Qualification
  h3 UPSC CSE Age Limit
  h3 UPSC CSE Age Relaxation
  h3 How Many Attempts Are Allowed for UPSC CSE?
h2 UPSC CSE Selection Process
h2 UPSC CSE Prelims Exam Pattern
h2 UPSC Prelims Syllabus
  h3 General Studies Paper I
  h3 General Studies Paper II / CSAT
h2 UPSC Civil Services Main Examination Pattern
  h3 Qualifying Papers
  h3 Merit Papers
h2 UPSC Mains Syllabus
  h3 Essay
  h3 General Studies Paper I
    h4 History
    h4 Geography
    h4 Society
  h3 General Studies Paper II
    h4 Governance
    h4 Constitution and Polity
    h4 Social Justice
    h4 International Relations
  h3 General Studies Paper III
    h4 Technology
    h4 Economy
    h4 Environment
    h4 Security and Disaster Management
  h3 General Studies Paper IV
    h4 Ethics
    h4 Integrity
    h4 Aptitude
    h4 Case Studies
h2 UPSC Optional Subjects
h2 UPSC Personality Test / Interview
h2 UPSC CSE Marks and Final Merit
h2 UPSC CSE Previous Year Question Papers
h2 UPSC CSE Results and Cut-offs
h2 UPSC CSE Exam Centres and Service Coverage
h2 How the UPSC CSE Application Process Works
h2 UPSC CSE Application Fee
h2 Documents and Information to Keep Ready
h2 How to Prepare for UPSC CSE
h2 UPSC CSE Preparation Guides
h2 Daily UPSC Practice
h2 Starting UPSC Preparation?
h2 Other UPSC Examinations
h2 Official UPSC Links
h2 Frequently Asked Questions
  h3 What is UPSC CSE?
  h3 Who conducts UPSC Civil Services Examination?
  h3 What qualification is required for UPSC CSE?
  h3 What is the UPSC CSE age limit?
  h3 How many attempts are allowed for UPSC CSE?
  h3 Is CSAT qualifying in UPSC Prelims?
  h3 Are Prelims marks included in final merit?
  h3 How many papers are there in UPSC Mains?
  h3 What is an optional subject in UPSC CSE?
  h3 What services are available through UPSC CSE?
  h3 Where can I download previous UPSC question papers?
  h3 Where should I verify official UPSC dates and rules?
h2 Verification / Editorial Note
h2 Related SearchSarkariNaukri Resources
```

## Semantic Page Skeleton

```html
<main id="main-content">
  <nav aria-label="Breadcrumb">...</nav>

  <header class="exam-hero">
    <p class="eyebrow">Government Exams</p>
    <h1>UPSC Civil Services Examination 2026 - Eligibility, Syllabus, Pattern & Dates</h1>
    <p>...</p>
    <ul aria-label="UPSC CSE quick facts">...</ul>
    <nav aria-label="UPSC CSE quick links">...</nav>
  </header>

  <section id="current-status" aria-labelledby="current-status-heading">
    <h2 id="current-status-heading">UPSC CSE 2026 Current Status</h2>
    <table>...</table>
  </section>

  <section id="quick-facts" aria-labelledby="quick-facts-heading">
    <h2 id="quick-facts-heading">UPSC CSE at a Glance</h2>
    <dl>...</dl>
  </section>

  <nav id="table-of-contents" aria-labelledby="toc-heading">
    <h2 id="toc-heading">Table of Contents</h2>
    <ol>...</ol>
  </nav>

  <section id="overview" aria-labelledby="overview-heading">...</section>
  <section id="services" aria-labelledby="services-heading">...</section>
  <section id="dates" aria-labelledby="dates-heading">...</section>

  <section id="eligibility" aria-labelledby="eligibility-heading">
    <h2 id="eligibility-heading">UPSC CSE Eligibility</h2>
    <section id="nationality" aria-labelledby="nationality-heading">...</section>
    <section id="qualification" aria-labelledby="qualification-heading">...</section>
    <section id="age-limit" aria-labelledby="age-limit-heading">...</section>
    <section id="age-relaxation" aria-labelledby="age-relaxation-heading">...</section>
    <section id="attempts" aria-labelledby="attempts-heading">...</section>
  </section>

  <section id="selection-process" aria-labelledby="selection-process-heading">...</section>
  <section id="prelims" aria-labelledby="prelims-heading">...</section>
  <section id="prelims-syllabus" aria-labelledby="prelims-syllabus-heading">...</section>
  <section id="mains" aria-labelledby="mains-heading">...</section>
  <section id="mains-syllabus" aria-labelledby="mains-syllabus-heading">...</section>
  <section id="optional-subjects" aria-labelledby="optional-subjects-heading">...</section>
  <section id="interview" aria-labelledby="interview-heading">...</section>
  <section id="final-merit" aria-labelledby="final-merit-heading">...</section>
  <section id="previous-papers" aria-labelledby="previous-papers-heading">...</section>
  <section id="cutoff" aria-labelledby="cutoff-heading">...</section>
  <section id="exam-centres" aria-labelledby="exam-centres-heading">...</section>
  <section id="apply" aria-labelledby="apply-heading">...</section>
  <section id="fee" aria-labelledby="fee-heading">...</section>
  <section id="documents" aria-labelledby="documents-heading">...</section>
  <section id="preparation" aria-labelledby="preparation-heading">...</section>
  <section id="practice" aria-labelledby="practice-heading">...</section>
  <section id="related-upsc-exams" aria-labelledby="related-upsc-exams-heading">...</section>
  <section id="official-links" aria-labelledby="official-links-heading">...</section>
  <section id="faq" aria-labelledby="faq-heading">...</section>
  <section id="verification" aria-labelledby="verification-heading">...</section>
  <section id="related-resources" aria-labelledby="related-resources-heading">...</section>
</main>
```

## Table Rules

- Use `<table>` for structured comparisons and dates.
- Use `<th scope="col">` for column headers.
- Add captions where useful.
- On mobile, use responsive table wrappers without horizontal page overflow.

## Links

- Same-page navigation should use anchors.
- Internal links must be crawlable `<a href>`.
- External official links should use `target="_blank" rel="noopener noreferrer"` where the site's pattern allows.
- Anchor text must be descriptive.

## Components

Recommended React/component tree:

```text
<UpscCsePage>
  <Breadcrumbs />
  <ExamHero />
  <ExamCycleStatus />
  <QuickFacts />
  <TableOfContents />
  <Overview />
  <Services />
  <ImportantDates />
  <Eligibility>
    <Nationality />
    <Qualification />
    <AgeLimit />
    <AgeRelaxation />
    <Attempts />
  </Eligibility>
  <SelectionProcess />
  <Prelims>
    <PrelimsPattern />
    <PrelimsSyllabus />
  </Prelims>
  <Mains>
    <MainsPattern />
    <MainsSyllabus />
    <OptionalSubjects />
  </Mains>
  <PersonalityTest />
  <FinalMerit />
  <PreviousPapers />
  <ResultsAndCutoffs />
  <ExamCentres />
  <ApplicationProcess />
  <ApplicationFee />
  <DocumentsChecklist />
  <PreparationStrategy />
  <PreparationGuides />
  <DailyPractice />
  <RelatedUpscExams />
  <OfficialUpscLinks />
  <Faq />
  <VerificationNote />
  <RelatedResources />
</UpscCsePage>
```

---

**Last Updated:** 22 September 2026
