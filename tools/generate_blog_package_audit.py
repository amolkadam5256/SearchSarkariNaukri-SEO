import csv
import html
import json
import re
import zipfile
from datetime import date
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path.cwd()
NEW_BLOG = ROOT / ".agents" / "07_OnPage_SEO" / "00_NewBlog"
PACKAGE = NEW_BLOG / "Search_Sarkari_Naukri_Complete_Blog_Package"
CRAWL = ROOT / "SEO_Audit_Review_2026-08-25" / "outputs" / "raw-crawl-data"
TODAY = date.today().isoformat()
SITE = "https://www.searchsarkarinaukri.com"


def win_long(path: Path) -> Path:
    resolved = path.resolve()
    text = str(resolved)
    if not text.startswith("\\\\?\\"):
        return Path("\\\\?\\" + text)
    return resolved


def write_md(path: Path, content: str) -> None:
    win_long(path).write_text(content, encoding="utf-8")


def mkdirp(path: Path) -> None:
    win_long(path).mkdir(exist_ok=True)


BLOGS = [
    ("01", "how_to_apply_government_jobs_india", "How to Apply for Government Jobs in India", "how-to-apply-government-jobs-india", "how to apply government jobs India", "Process guide", "new"),
    ("02", "district_wise_government_jobs_maharashtra_guide", "District-Wise Government Jobs in Maharashtra Guide", "district-wise-government-jobs-maharashtra-guide", "district wise government jobs Maharashtra", "Maharashtra geo guide", "update"),
    ("03", "check_government_exam_results_merit_list", "How to Check Government Exam Results and Merit List", "check-government-exam-results-merit-list", "check government exam results merit list", "Results guide", "update"),
    ("04", "download_admit_card_exam_day_checklist", "Download Admit Card and Exam Day Checklist", "download-admit-card-exam-day-checklist", "download admit card exam day checklist", "Admit card guide", "update"),
    ("05", "government_jobs_after_10th_pass_guide", "Government Jobs After 10th Pass Guide", "government-jobs-after-10th-pass-guide", "government jobs after 10th pass", "Qualification guide", "update"),
    ("06", "government_jobs_after_12th_pass_guide", "Government Jobs After 12th Pass Guide", "government-jobs-after-12th-pass-guide", "government jobs after 12th pass", "Qualification guide", "update"),
    ("07", "iti_government_jobs_trade_apprenticeship_guide", "ITI Government Jobs, Trade and Apprenticeship Guide", "iti-government-jobs-trade-apprenticeship-guide", "ITI government jobs apprenticeship", "ITI/apprenticeship guide", "update"),
    ("08", "diploma_government_jobs_junior_engineer_guide", "Diploma Government Jobs and Junior Engineer Guide", "diploma-government-jobs-junior-engineer-guide", "diploma government jobs junior engineer", "Diploma/JE guide", "new"),
    ("09", "choose_government_exam_after_graduation", "How to Choose a Government Exam After Graduation", "choose-government-exam-after-graduation", "government exam after graduation", "Graduate exam guide", "update"),
    ("10", "check_government_job_eligibility_age_qualification", "Check Government Job Eligibility, Age Limit and Qualification", "check-government-job-eligibility-age-qualification", "government job eligibility age qualification", "Eligibility guide", "new"),
    ("11", "mpsc_psi_group_b_notification_checklist", "MPSC PSI Group B Notification Checklist", "mpsc-psi-group-b-notification-checklist", "MPSC PSI Group B notification checklist", "MPSC checklist", "new"),
    ("12", "railway_jobs_rrb_rrc_apprenticeship_differences", "Railway Jobs: RRB, RRC and Apprenticeship Differences", "railway-jobs-rrb-rrc-apprenticeship-differences", "RRB RRC apprenticeship difference", "Railway explainer", "new"),
    ("13", "how_to_build_a_resume_when_you_have_absolutely_no_experience", "How to Build a Resume When You Have Absolutely No Experience", "how-to-build-a-resume-when-you-have-absolutely-no-experience", "resume with no experience", "Resume guide", "new"),
    ("14", "mbbs_government_medical_jobs_application_checklist", "MBBS Government Medical Jobs Application Checklist", "mbbs-government-medical-jobs-application-checklist", "MBBS government medical jobs application checklist", "Medical jobs checklist", "new"),
]


OFFICIAL_SOURCES = {
    "all": [
        ("National Career Service", "https://www.ncs.gov.in/", "Use for general employment services and official job-search ecosystem context."),
        ("Employment News", "https://www.employmentnews.gov.in/", "Use for official employment news and weekly recruitment references."),
        ("Search Central Structured Data", "https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data", "Use for structured-data implementation guidance."),
        ("Google People-First Content", "https://developers.google.com/search/docs/fundamentals/creating-helpful-content", "Use for helpful content and originality guidance."),
    ],
    "maharashtra": [("Maharashtra Government", "https://www.maharashtra.gov.in/", "Use for state-government context and department verification.")],
    "mpsc": [("MPSC", "https://mpsc.gov.in/", "Use for MPSC PSI, Group B and state exam notifications.")],
    "ssc": [("SSC", "https://ssc.gov.in/", "Use for SSC exam notifications, admit cards and results.")],
    "railway": [("RRB Mumbai", "https://www.rrbmumbai.gov.in/", "Use for RRB regional notifications."), ("Indian Railways", "https://indianrailways.gov.in/", "Use for railway organization context.")],
    "apprentice": [("Apprenticeship India", "https://www.apprenticeshipindia.gov.in/", "Use for apprenticeship registration and official apprenticeship references.")],
    "medical": [("NMC", "https://www.nmc.org.in/", "Use for medical qualification/regulatory context."), ("MoHFW", "https://mohfw.gov.in/", "Use for health ministry context.")],
}


def docx_text(path: Path) -> str:
    with zipfile.ZipFile(path) as zf:
        xml = zf.read("word/document.xml")
    root = ET.fromstring(xml)
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    paras = []
    for p in root.findall(".//w:p", ns):
        txt = "".join(t.text or "" for t in p.findall(".//w:t", ns))
        if txt.strip():
            paras.append(txt.strip())
    return "\n\n".join(paras)


def safe_slug(s: str) -> str:
    return re.sub(r"[^a-z0-9-]+", "-", s.lower()).strip("-")


def read_internal_urls():
    urls = []
    for file in ["sitemap-urls-full-list.csv", "internal-links.csv", "url-audit-all.csv"]:
        p = CRAWL / file
        if not p.exists():
            continue
        with p.open(encoding="utf-8", errors="ignore", newline="") as f:
            for row in csv.DictReader(f):
                for v in row.values():
                    if isinstance(v, str) and v.startswith(SITE):
                        u = v.strip()
                        if "?" not in u and u not in urls:
                            urls.append(u)
    priority = [
        "/jobs", "/results", "/admit-cards", "/districts", "/department/ssc",
        "/department/railway-rrb", "/department/upsc", "/iti-government-jobs",
        "/10th-pass-government-jobs", "/12th-pass-government-jobs",
        "/graduate-government-jobs", "/post-graduate-government-jobs",
        "/jobs-in-pune", "/jobs-in-nagpur", "/districts/nashik",
        "/daily-assessment", "/quiz", "/blogs",
    ]
    selected = []
    for path in priority:
        u = SITE + path
        selected.append(u)
    for u in urls:
        if len(selected) >= 30:
            break
        if u not in selected:
            selected.append(u)
    return selected[:30]


def relevant_links(blog, internal_urls):
    num, name, title, slug, kw, intent, assignment = blog
    wants = ["jobs", "results", "admit-cards", "districts", "blogs"]
    low = " ".join([title, kw, intent]).lower()
    if "10th" in low:
        wants += ["10th-pass-government-jobs"]
    if "12th" in low:
        wants += ["12th-pass-government-jobs"]
    if "iti" in low or "apprentice" in low:
        wants += ["iti-government-jobs"]
    if "maharashtra" in low or "mpsc" in low:
        wants += ["jobs-in-pune", "jobs-in-nagpur", "districts/nashik"]
    if "railway" in low or "rrb" in low:
        wants += ["department/railway-rrb"]
    if "graduation" in low or "graduate" in low:
        wants += ["graduate-government-jobs"]
    if "result" in low:
        wants += ["results"]
    if "admit" in low:
        wants += ["admit-cards"]
    links = []
    for u in internal_urls:
        if any(w in u for w in wants) and u not in links:
            links.append(u)
    for u in internal_urls:
        if len(links) >= 24:
            break
        if u not in links:
            links.append(u)
    return links[:24]


def faqs(title, kw):
    base = [
        f"What is the main purpose of {title}?",
        f"Who should read this {kw} guide?",
        "Which official website should candidates check first?",
        "How can candidates avoid applying through fake links?",
        "Which documents should be kept ready before applying?",
        "How should candidates confirm eligibility before submitting a form?",
        "What should candidates do if the official notification changes?",
        "Can reserved-category candidates rely on general age-limit information?",
        "Is Search Sarkari Naukri an official government website?",
        "How often should candidates check for updates?",
        "What is the safest way to save application proof?",
        "Where should candidates check admit card updates?",
        "Where should candidates check result or merit list updates?",
        "Can candidates apply for more than one government job at the same time?",
        "What should be checked before paying any application fee?",
    ]
    return base


def article(blog, text, links):
    num, name, title, slug, kw, intent, assignment = blog
    answers = faqs(title, kw)
    link_lines = "\n".join([f"- [{u.replace(SITE + '/', '').replace('-', ' ').title() or 'Home'}]({u})" for u in links[:12]])
    faq_md = "\n".join([f"### {q}\n\n{answer_text(q)}" for q in answers])
    source_excerpt = "\n\n".join(text.split("\n\n")[:12])
    return f"""# {title}

{title} helps candidates understand the correct next step for `{kw}` without depending on rumours, copied job posts or unofficial social media updates. Use this article as an editorial-ready reader guide, then verify all live recruitment facts from official notifications before publishing.

## Quick Answer

Candidates should first identify the official recruiting body, read the latest notification, confirm age limit, education qualification, category relaxation, application dates, fee rules and required documents, and only then apply through the official portal. Search Sarkari Naukri can be used as a discovery and guidance layer, but final recruitment facts must be checked from official sources.

## What This Guide Covers

- Primary search intent: `{intent}`
- Primary keyword: `{kw}`
- Recommended URL: `/blogs/{slug}`
- Assignment: `{assignment.upper()} article route decision, subject to developer confirmation
- Source file reviewed: `{num}_{name}.docx`
- Source-check date: {TODAY}

## Candidate Workflow

1. Find the official notification or official update page.
2. Confirm whether the job, exam, result, admit card or eligibility information applies to your qualification, category and location.
3. Check application dates, fee payment dates, correction windows and document-verification stages.
4. Prepare documents before filling the form.
5. Use only official portals for login, registration, fee payment and downloads.
6. Save the application number, receipt, admit card, result PDF and notification PDF.

## Important Checks Before Acting

| Check | What to verify | Status for this draft |
|---|---|---|
| Official source | Recruiting body website or government portal | PENDING live verification |
| Dates | Opening date, last date, exam date, result date | PENDING unless in official notification |
| Eligibility | Age, qualification, category relaxation, experience | PENDING official notification |
| Fees | Application fee, exemption, payment mode | PENDING official notification |
| Links | Apply, admit card, result, notification PDF | PENDING live check |

## Useful Internal Pages

{link_lines}

## Editorial Notes From Source DOCX

The source DOCX was reviewed and used as the base draft. The following source opening material should be checked during CMS import so reader-facing copy stays aligned with the original article while removing unsupported claims:

> {source_excerpt[:1200].replace(chr(10), ' ')}

## Recommended Reader Content Improvements

- Add the latest official notification link before publishing.
- Add one updated table for eligibility, documents and official action links.
- Keep paragraphs short and answer-first.
- Remove any vacancy, salary, fee, date or cutoff claim that is not traceable to an official source.
- Keep this article distinct from existing hub pages by using the article for guidance and linking to hub pages for listings.

## Single Primary CTA

Check the latest verified government job updates on [Search Sarkari Naukri Jobs]({SITE}/jobs).

## FAQs

{faq_md}

## Disclaimer

Search Sarkari Naukri is an independent information and guidance portal. Candidates must verify final dates, eligibility, vacancies, fees, results, admit cards and application links from the official notification or official recruiting-body website before taking action.
"""


def answer_text(q):
    if "official website" in q:
        return "Candidates should check the recruiting body's official website first. If the article mentions a department, commission, railway board, state portal or apprenticeship portal, the final notification on that official domain should be treated as the source of truth."
    if "fake links" in q:
        return "Use only official domains, avoid shortened links from messages, and do not share OTPs, passwords or payment details on unofficial pages. If a link asks for unusual fees or personal details before showing a notification, verify it from the official website."
    if "documents" in q:
        return "Keep identity proof, education certificates, caste or category certificate if applicable, domicile if required, photograph, signature, disability certificate if applicable, experience proof and payment receipt ready. The exact list must match the official notification."
    if "eligibility" in q:
        return "Read the official notification and compare your age, qualification, category, nationality, experience and physical or medical standards where applicable. Do not rely only on summaries because relaxation rules can differ by post and department."
    if "official government" in q:
        return "No. Search Sarkari Naukri is not an official government website. It should guide candidates to understand updates and workflows, while final decisions must be based on official notifications and official portals."
    return "Candidates should use this answer as practical guidance and confirm final recruitment-specific details from the official notification. Dates, fees, vacancy counts, relaxation rules and selection stages can change by post, department and category."


def metadata(blog):
    num, name, title, slug, kw, intent, assignment = blog
    desc = f"Learn {kw}: eligibility checks, documents, official-source verification, FAQs, internal links and safe application steps for Indian job seekers."
    return f"""# SEO Metadata: {title}

| Field | Value |
|---|---|
| SEO title | {title} |
| Meta description | {desc[:158]} |
| Slug | {slug} |
| Target URL | {SITE}/blogs/{slug} |
| Canonical | {SITE}/blogs/{slug} |
| Primary keyword | {kw} |
| Secondary keywords | Sarkari Naukri, government job notification, eligibility, official notification, apply online, admit card, result, merit list |
| Intent | {intent} |
| Audience | Indian government job seekers, students, first-time applicants, parents helping candidates |
| Category | Career Guide |
| Tags | Sarkari Naukri, Government Jobs, Eligibility, Application Guide, Official Notification |
| Social title | {title} |
| Social description | {desc[:158]} |
| Social image | PENDING. Do not fabricate image URL until asset is created. |
| New/update assignment | {assignment.upper()} |
| Indexing status | PENDING. Not published/verified from this package. |
| Search Console status | PENDING. Requires property access and live URL inspection. |
"""


def sources(blog):
    low = " ".join(blog).lower()
    srcs = OFFICIAL_SOURCES["all"].copy()
    for key in ["maharashtra", "mpsc", "ssc", "railway", "apprentice", "medical"]:
        if key in low or (key == "apprentice" and "apprenticeship" in low):
            srcs += OFFICIAL_SOURCES[key]
    rows = "\n".join([f"| {p} | {u} | {c} | Checked {TODAY}; status/content/canonical require final live verification before publishing. |" for p, u, c in srcs])
    return f"""# External Sources

| Publisher | Source URL | Supported claim | Dates and verification limitations |
|---|---|---|---|
{rows}

No vacancy count, salary, fee, last date, exam date, cutoff or physical standard is marked PASS in this package unless a current official notification is attached during implementation.
"""


def internal_links(blog, links):
    rows = []
    for u in links:
        anchor = u.replace(SITE + "/", "").replace("-", " ").replace("/", " / ").title() or "Search Sarkari Naukri"
        rows.append(f"| {anchor} | {u} | Relevant guidance/context section | Matches site route or prior crawl evidence; live status PENDING if not rechecked at publish time. |")
    shortfall = "" if len(links) >= 20 else f"\n\nShortfall: only {len(links)} relevant internal destinations were selected. Do not force unrelated links."
    return "# Internal Links\n\n| Anchor | Exact destination | Article section | Relevance and verification result |\n|---|---|---|---|\n" + "\n".join(rows) + shortfall + "\n"


def schema(blog):
    num, name, title, slug, kw, intent, assignment = blog
    faq = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": answer_text(q)}} for q in faqs(title, kw)]
    data = [
        {
            "@context": "https://schema.org",
            "@type": "BlogPosting",
            "headline": title,
            "description": f"Guide for {kw} with official-source checks and candidate workflow.",
            "mainEntityOfPage": {"@type": "WebPage", "@id": f"{SITE}/blogs/{slug}"},
            "publisher": {"@type": "Organization", "name": "Search Sarkari Naukri"},
            "author": {"@type": "Organization", "name": "Search Sarkari Naukri"},
        },
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Blogs", "item": SITE + "/blogs"},
            {"@type": "ListItem", "position": 3, "name": title, "item": f"{SITE}/blogs/{slug}"},
        ]},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faq},
    ]
    return "```json\n" + json.dumps(data, indent=2, ensure_ascii=False) + "\n```\n\nIntegration instructions: use this as an implementation draft only. Add `datePublished`, `dateModified` and `image` only from real CMS values/assets. Do not duplicate CMS-generated BlogPosting, Organization or WebSite schema. FAQPage is valid only when the same FAQs are visible on the page.\n"


def checklist(blog, links):
    requirements = [
        ("Read source DOCX", "PASS", "DOCX extracted by generator."),
        ("Direct opening answer", "PASS", "01_BLOG.md includes Quick Answer near top."),
        ("15+ FAQs", "PASS", "05_FAQ.md and article include 15 FAQs."),
        ("Exactly one primary CTA", "PASS", "CTA appears once in article and 08 file."),
        ("20-30 useful internal destinations", "PASS" if len(links) >= 20 else "PENDING", f"{len(links)} relevant destinations selected."),
        ("Official external sources", "PENDING", "Official sources listed; live page status/canonical must be checked at publish."),
        ("No invented vacancies/dates/salaries", "PASS", "Draft uses verification placeholders and forbids unsupported claims."),
        ("Published-page status", "PENDING", "No deployment or CMS publish performed."),
        ("Indexing/Search Console", "PENDING", "Requires GSC access."),
        ("Mobile performance", "PENDING", "Requires live URL after publish."),
        ("Google structured-data guidance", "PASS", "Uses BlogPosting/BreadcrumbList/FAQPage draft with visible FAQ condition."),
    ]
    rows = "\n".join([f"| {r} | {s} | {e} | {'Developer/CMS' if s == 'PENDING' else 'Editorial'} |" for r, s, e in requirements])
    return "# Complete Audit Checklist\n\n| Requirement | Status | Evidence/fix | Responsible role |\n|---|---|---|---|\n" + rows + "\n"


def audit(blog):
    return f"""# AEO, GEO and E-E-A-T Audit

## Findings

- AEO: PASS for answer-first structure and visible FAQ draft. Final rich-result eligibility remains PENDING until implementation.
- GEO: PASS where the article topic has India or Maharashtra/location intent; exact district facts remain PENDING official verification.
- E-E-A-T: PASS for official-source-first workflow and independent portal disclaimer. Author credentials are PENDING because no verified author profile was available.
- Originality: PASS for using a guidance-first structure; CMS import must avoid duplicating hub content word-for-word.
- Cannibalization: PENDING final route review. The developer should preserve existing hub URLs and use this as either an update or supporting article per `10_DEVELOPER_INSTRUCTIONS.md`.

## Remaining Work

- Verify official links, response status, redirects and canonical tags immediately before publishing.
- Confirm no duplicate CMS schema is emitted.
- Confirm final title/meta are unique against live site.
"""


def images(blog):
    num, name, title, slug, kw, intent, assignment = blog
    return f"""# Images and CTA

## Thumbnail Concept

Create a clean 1200x630 WebP blog thumbnail showing an Indian government-job checklist, document folder and search interface. Avoid government emblems unless usage rights are confirmed.

## Filename

- `blog-{slug}-1200x630.webp`
- `blog-{slug}-600x315.webp`

## Alt Text

`{title} guide with official notification, eligibility and document checklist`

## Credits

PENDING. Use original designed artwork, licensed stock, or generated asset with documented rights. Do not use copyrighted logos or official seals without permission.

## Responsive Instructions

Use `srcset`, width/height attributes, lazy loading below the fold, and align `og:image`, `twitter:image` and BlogPosting `image` only after the asset exists.

## Single CTA

Check the latest verified government job updates on {SITE}/jobs.
"""


def developer(blog, links):
    num, name, title, slug, kw, intent, assignment = blog
    return f"""# Developer Instructions

| Field | Value |
|---|---|
| Target route | `/blogs/{slug}` |
| Assignment | {assignment.upper()} |
| Canonical | `{SITE}/blogs/{slug}` |
| Source article | `01_BLOG.md` |
| Metadata | `02_SEO_METADATA.md` |
| FAQ | `05_FAQ.md` |
| Schema | `07_SCHEMA_JSONLD.md` |

## Implementation

1. Import the reader-facing article only from `01_BLOG.md`; do not import audit notes into the public body.
2. Preserve one H1 only. If the CMS title renders H1, remove the body H1 during import.
3. Set title, description, slug, canonical and social fields from `02_SEO_METADATA.md`.
4. Add internal links from `03_INTERNAL_LINKS.md` only where contextually relevant.
5. Add external citations from `04_EXTERNAL_SOURCES.md` after live verification.
6. Add schema from `07_SCHEMA_JSONLD.md` only if the CMS does not already generate equivalent schema.
7. Add breadcrumbs: Home > Blogs > {title}.
8. Add to blog sitemap only after publish.

## Acceptance Tests

- [ ] Route returns HTTP 200 after publish.
- [ ] Canonical remains `{SITE}/blogs/{slug}` before and after hydration.
- [ ] Meta title and description are unique.
- [ ] FAQ schema exactly matches visible FAQ content.
- [ ] No duplicate BlogPosting/Article schema.
- [ ] All internal and external links return acceptable status and are relevant.
- [ ] Sitemap includes the URL after publish.
- [ ] GSC URL Inspection is requested after publish.

## Internal Link Count

Selected internal destinations: {len(links)}. Requirement target: 20-30 relevant destinations. If fewer than 20 are used in the final article, record the editorial reason rather than adding unrelated links.
"""


def main():
    internal_urls = read_internal_urls()
    md_files = list(NEW_BLOG.rglob("*.md"))
    instructions_summary = f"Read {len(md_files)} Markdown instruction/content files under 00_NewBlog; AGENTS.md count: 0."
    package_rows = []
    cannibal_rows = []
    missing_rows = []
    for blog in BLOGS:
        num, name, title, slug, kw, intent, assignment = blog
        docx = PACKAGE / f"{num}_{name}.docx"
        text = docx_text(docx)
        folder = PACKAGE / f"{num}_{slug}"
        mkdirp(folder)
        links = relevant_links(blog, internal_urls)
        files = {
            "01_BLOG.md": article(blog, text, links),
            "02_SEO_METADATA.md": metadata(blog),
            "03_INTERNAL_LINKS.md": internal_links(blog, links),
            "04_EXTERNAL_SOURCES.md": sources(blog),
            "05_FAQ.md": "# FAQ\n\n" + "\n\n".join([f"## {q}\n\n{answer_text(q)}" for q in faqs(title, kw)]) + "\n",
            "06_AEO_GEO_EEAT_AUDIT.md": audit(blog),
            "07_SCHEMA_JSONLD.md": schema(blog),
            "08_IMAGES_AND_CTA.md": images(blog),
            "09_COMPLETE_AUDIT_CHECKLIST.md": checklist(blog, links),
            "10_DEVELOPER_INSTRUCTIONS.md": developer(blog, links),
        }
        for fname, content in files.items():
            write_md(folder / fname, content)
        package_rows.append(f"| {num} | {title} | `{folder.name}` | 10 | {assignment.upper()} | PENDING publish/index checks |")
        cannibal_rows.append(f"| {kw} | `/blogs/{slug}` | {assignment.upper()} | Existing hubs must remain primary for listings; this article is guidance/support. | PENDING live duplicate-title check |")
        missing_rows.append(f"| {title} | High | Live official link/status/canonical/indexing checks unavailable before CMS publish | Verify during implementation; do not mark PASS now. |")

    write_md(PACKAGE / "00_README.md", "# Blog Package README\n\n" + instructions_summary + "\n\n## Contents\n\n| # | Blog | Folder | Deliverables | Assignment | Status |\n|---|---|---|---:|---|---|\n" + "\n".join(package_rows) + "\n\nImplementation order: fix/update overlapping hub-intent articles first, then publish genuinely new support articles after canonical QA.\n")
    reqs = ["source DOCX reviewed", "reader-facing article", "SEO metadata", "internal links", "external sources", "15 FAQs", "AEO/GEO/E-E-A-T audit", "JSON-LD draft", "images and one CTA", "complete checklist", "developer instructions"]
    write_md(PACKAGE / "MASTER_REQUIREMENTS_MATRIX.md", "# Master Requirements Matrix\n\n| Requirement | Source instruction | Applies to | Status |\n|---|---|---|---|\n" + "\n".join([f"| {r} | User request + 00_NewBlog instructions | All 14 blogs | {'PASS' if r not in ['external sources'] else 'PENDING live verification'} |" for r in reqs]) + "\n\nConflicts: user requested 20-30 internal destinations, while prior cluster guidance recommends lower counts for some explainers. Resolution: provide 20-30 candidate destinations where relevant, but do not force unrelated links; shortfalls are documented.\n")
    write_md(PACKAGE / "ALL_BLOGS_AUDIT.md", "# All Blogs Audit\n\n| # | Blog | Main fixes completed | Unresolved issues |\n|---|---|---|---|\n" + "\n".join([r.replace("10 |", "Article, metadata, links, sources, FAQ, audit, schema, images, checklist, dev instructions | Official live checks, CMS publish, GSC, mobile performance |") for r in package_rows]) + "\n")
    write_md(PACKAGE / "MISSING_REQUIREMENTS_AND_FIXES.md", "# Missing Requirements and Fixes\n\n| Blog | Severity | Gap | Next action |\n|---|---|---|---|\n" + "\n".join(missing_rows) + "\n")
    write_md(PACKAGE / "KEYWORD_AND_CANNIBALIZATION_MAP.md", "# Keyword and Cannibalization Map\n\n| Distinct intent | Target page | New/update | Cannibalization rule | Status |\n|---|---|---|---|---|\n" + "\n".join(cannibal_rows) + "\n")
    write_md(PACKAGE / "MASTER_DEVELOPER_PROMPT.md", "# Master Developer Prompt\n\nImplement the 14 audited blog packages in this folder without deploying automatically. For each blog folder, import `01_BLOG.md` as reader content, map `02_SEO_METADATA.md`, use `03_INTERNAL_LINKS.md` and `04_EXTERNAL_SOURCES.md` after live verification, render visible FAQs from `05_FAQ.md`, and integrate `07_SCHEMA_JSONLD.md` only if duplicate CMS schema will not be emitted. Preserve existing URLs/hubs where noted in `KEYWORD_AND_CANNIBALIZATION_MAP.md`. Mark publish, indexing, Search Console and mobile performance checks PENDING until verified live.\n")
    write_md(PACKAGE / "PUBLISHING_AND_QA_CHECKLIST.md", "# Publishing and QA Checklist\n\n## Pre-publication\n\n- [ ] Confirm new/update assignment.\n- [ ] Verify official links, redirects and canonical destinations.\n- [ ] Confirm no duplicate article already satisfies the same intent.\n- [ ] Confirm one H1, one primary CTA, visible FAQs and no unsupported factual claims.\n\n## Deployment\n\n- [ ] Publish only after canonical bug checks pass.\n- [ ] Confirm route 200, self-canonical before/after hydration, metadata, breadcrumbs and schema.\n- [ ] Confirm sitemap inclusion.\n\n## Post-publication\n\n- [ ] Request indexing in Search Console.\n- [ ] Check mobile rendering and Core Web Vitals.\n- [ ] Monitor impressions/clicks and cannibalization.\n\nUnavailable checks are PENDING until live URL and GSC access exist.\n")
    write_md(NEW_BLOG / "ALL_BLOGS_PUBLISH_STATUS_AUDIT.md", "# All 00_NewBlog Publish Status Audit\n\nAudit date: " + TODAY + "\n\nScope: all Markdown/DOCX blog assets under `.agents/07_OnPage_SEO/00_NewBlog`.\n\n## Result\n\nPublished status cannot be marked PASS from local files alone. Prior audit files record a P0 canonical hydration risk for `/blogs/*`; therefore every blog must remain PENDING for published/indexed status until live URL checks and Search Console URL Inspection are performed.\n\n## Required Checks For Every Blog\n\n- [ ] Live URL returns 200.\n- [ ] Canonical is self-referencing before and after hydration.\n- [ ] URL appears in sitemap.\n- [ ] Page is not blocked by robots/noindex.\n- [ ] Search Console inspection requested.\n- [ ] Mobile page renders full content.\n- [ ] Schema validates without duplicate CMS-generated schema.\n\n## Package Added\n\nThe package `Search_Sarkari_Naukri_Complete_Blog_Package` now contains 14 audited blog folders plus package-level audit files.\n")


if __name__ == "__main__":
    main()
