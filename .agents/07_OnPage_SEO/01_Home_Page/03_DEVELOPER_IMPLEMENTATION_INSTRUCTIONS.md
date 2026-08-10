# 🛠️ Developer Implementation Guide & Section Instructions — Home Page

**Target URL:** `https://www.searchsarkarinaukri.com/`  
**Page Module:** Home Page (`01_Home_Page`)  
**Format:** Pure Markdown Instructions for Development Team  
**File Location:** [`.agents/07_OnPage_SEO/01_Home_Page/03_DEVELOPER_IMPLEMENTATION_INSTRUCTIONS.md`](file:///c:/Users/computer1/Desktop/Growthik_Media/02_Clients/03_SearchSarkariNaukri/SearchSarkariNaukri/.agents/07_OnPage_SEO/01_Home_Page/03_DEVELOPER_IMPLEMENTATION_INSTRUCTIONS.md)

---

## 📋 Summary of Required Homepage Sections

Developers must implement the following 8 sections sequentially on the Home Page root component (`/`):

1. **Hero Header & Search Bar Section** (`<h1>` + Subtitle + Trending Keywords Pills)
2. **Closing Soon & Deadline Urgency Section** (`<h2>` + Ending Soon Jobs List)
3. **Department & Exam Category Grid** (`<h2>` + 8 Exam Category Cards)
4. **Qualification Filter Matrix** (`<h2>` + 6 Education Level Cards)
5. **Maharashtra District-Wise Jobs Section** (`<h2>` + 36 District Link Matrix)
6. **How Search Sarkari Naukri Works Section** (`<h2>` + 6-Step Workflow Cards)
7. **Long-Form SEO Content Section** (`<h2>` + 3 Informational Content Blocks)
8. **Frequently Asked Questions (FAQ) Section** (`<h2>` + 4 Accordion Items + `FAQPage` JSON-LD Schema)

---

## ⚙️ Developer Instructions Section by Section

### 1. Hero Header & Search Bar
* **Instruction:** Render a single `<h1>` tag containing `Sarkari Naukri 2026 — Search Latest Government Jobs & Vacancies in India`.
* **Keyword Pills UI:** Render a horizontal scrolling/flex list of trending search tags pointing directly to category URLs:
  - `MPSC Bharti 2026` -> `/jobs?category=mpsc`
  - `Maharashtra Police Bharti` -> `/jobs?category=police`
  - `Talathi Bharti 2026` -> `/jobs?category=talathi`
  - `10th Pass Govt Jobs` -> `/qualifications/10th-pass`
  - `RRB Railway Recruitment` -> `/jobs?category=railway`
  - `SSC CGL 2026` -> `/jobs?category=ssc`

---

### 2. Urgent Updates / Closing Soon Banner
* **Instruction:** Add an urgency component displaying job listings where the application deadline ends within 7 days.
* **Header Tag:** `<h2>` tag set to `Ending Soon: Government Jobs Last Date Today & Closing Vacancies`.

---

### 3. Department & Exam Category Grid
* **Instruction:** Display 8 interactive category cards linking to filtered job listings:
  - Card 1: **MPSC Bharti 2026** (`/jobs?category=mpsc`)
  - Card 2: **Maharashtra Police Bharti 2026** (`/jobs?category=police`)
  - Card 3: **Talathi Bharti 2026** (`/jobs?category=talathi`)
  - Card 4: **RRB Railway Jobs 2026** (`/jobs?category=railway`)
  - Card 5: **SSC Jobs 2026** (`/jobs?category=ssc`)
  - Card 6: **Banking Jobs** (`/jobs?category=banking`)
  - Card 7: **UPSC Civil Services** (`/jobs?category=upsc`)
  - Card 8: **Zilla Parishad (ZP) Jobs** (`/jobs?category=zp`)

---

### 4. Qualification-Wise Filter Matrix
* **Instruction:** Render 6 cards for qualification-level filtering:
  - **10th Pass Govt Jobs** (`/qualifications/10th-pass`)
  - **12th Pass Govt Jobs** (`/qualifications/12th-pass`)
  - **ITI Govt Jobs** (`/qualifications/iti`)
  - **Diploma Govt Jobs** (`/qualifications/diploma`)
  - **Graduate Govt Jobs** (`/qualifications/graduate`)
  - **Engineering Govt Jobs** (`/qualifications/engineering`)

---

### 5. Maharashtra District-Wise Jobs Section
* **Instruction:** Render a 3-column responsive grid featuring top Maharashtra districts:
  - Pune, Mumbai, Nagpur, Nashik, Thane, Chh. Sambhajinagar, Solapur, Kolhapur, Latur.
  - Include a prominent text link: `→ See all 36 Maharashtra districts` linking to `/districts`.

---

### 6. How Search Sarkari Naukri Works Section
* **Instruction:** Render a 6-step timeline/card component directly above the Long-Form SEO section.
* **Header Tag:** `<h2>` set to `How Search Sarkari Naukri Works — 6 Simple Steps to Get Your Dream Government Job`.
* **Step Breakdown:**
  - **Step 1: Search Jobs** — Discover Sarkari Naukri 2026, MPSC, Police Bharti, Railway, and SSC vacancies.
  - **Step 2: Check Eligibility** — Use the Eligibility Checker tool to match qualifications (10th, 12th, Graduate).
  - **Step 3: Save Job** — Bookmark job posts to personalized applicant dashboard.
  - **Step 4: Set Reminder** — Automated WhatsApp and push notification alerts before last date closes.
  - **Step 5: Verify Official Notification** — Download verified official advertisement PDFs directly.
  - **Step 6: Apply Online** — Direct apply links for MPSC, Police Bharti, and Talathi online registration portals.

---

### 7. Long-Form SEO Content Section
* **Instruction:** Ensure full crawler accessibility (server-side prerendered or inline in semantic HTML).
* **Header Tag:** `<h2>` set to `Complete Guide to Finding Government Jobs in Maharashtra & India 2026`.
* **Sub-headings (`<h3>`):**
  - `How SearchSarkariNaukri Tracks Daily Government Vacancies`
  - `Key Documents Required to Apply Online for Govt Jobs`

---

### 8. FAQ & JSON-LD Structured Data
* **Instruction:** Render 4 FAQ accordions with `<h2>` title `Frequently Asked Questions (FAQ) — Sarkari Naukri 2026`.
* **Schema Injection:** Inject the JSON-LD schema array into `<head>` dynamically:
  - `Organization`
  - `WebSite` with `SearchAction` (`/jobs?search={search_term_string}`)
  - `BreadcrumbList`
  - `FAQPage`
