# 08 — JSON-LD / Structured Data Specification

**Target Hub:** `https://www.searchsarkarinaukri.com/category/state-government-jobs` (or `/state-government-jobs`)  
**Validation Standard:** Schema.org, Google Search Central Structured Data Guidelines.

---

## 1. Schema Hierarchy Overview

This directory page must implement three cohesive JSON-LD schemas:
1. **`BreadcrumbList`** — Establishes navigational position within site hierarchy.
2. **`CollectionPage` + `ItemList`** — Defines this hub as a curated collection of state-specific employment directories.
3. **`FAQPage`** — Marks up the 15 visible editorial frequently asked questions for rich snippet eligibility.

> **CRITICAL RULE:** Do NOT place `JobPosting` structured data on this directory page. `JobPosting` schema is exclusively reserved for individual, canonical vacancy URLs that contain specific `datePosted`, `validThrough`, `hiringOrganization`, and `jobLocation` parameters.

---

## 2. BreadcrumbList JSON-LD

```html
<script type="application/ld+json">
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
      "name": "State Government Jobs",
      "item": "https://www.searchsarkarinaukri.com/category/state-government-jobs"
    }
  ]
}
</script>
```

---

## 3. CollectionPage & ItemList JSON-LD

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "@id": "https://www.searchsarkarinaukri.com/category/state-government-jobs#webpage",
  "url": "https://www.searchsarkarinaukri.com/category/state-government-jobs",
  "name": "State Wise Sarkari Naukri 2026 — Government Jobs by State and UT",
  "description": "Comprehensive state government jobs directory for 2026. Explore active Sarkari Naukri vacancies across 28 Indian states and Union Territories, filtered by qualification, recruiting authority, and official PSC portals.",
  "inLanguage": "en-IN",
  "dateModified": "{{ISO_DATE_OF_REAL_UPDATE}}",
  "isPartOf": {
    "@type": "WebSite",
    "@id": "https://www.searchsarkarinaukri.com/#website",
    "url": "https://www.searchsarkarinaukri.com/",
    "name": "SearchSarkariNaukri"
  },
  "mainEntity": {
    "@type": "ItemList",
    "name": "State Wise Government Jobs Directory",
    "description": "Directory of state-specific government job portals across India",
    "itemListOrder": "https://schema.org/ItemListUnordered",
    "numberOfItems": 31,
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "Andhra Pradesh Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-andhra-pradesh"
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": "Arunachal Pradesh Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-arunachal-pradesh"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "Assam Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-assam"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "Bihar Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-bihar"
      },
      {
        "@type": "ListItem",
        "position": 5,
        "name": "Chhattisgarh Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-chhattisgarh"
      },
      {
        "@type": "ListItem",
        "position": 6,
        "name": "Goa Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-goa"
      },
      {
        "@type": "ListItem",
        "position": 7,
        "name": "Gujarat Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-gujarat"
      },
      {
        "@type": "ListItem",
        "position": 8,
        "name": "Haryana Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-haryana"
      },
      {
        "@type": "ListItem",
        "position": 9,
        "name": "Himachal Pradesh Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-himachal-pradesh"
      },
      {
        "@type": "ListItem",
        "position": 10,
        "name": "Jharkhand Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-jharkhand"
      },
      {
        "@type": "ListItem",
        "position": 11,
        "name": "Karnataka Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-karnataka"
      },
      {
        "@type": "ListItem",
        "position": 12,
        "name": "Kerala Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-kerala"
      },
      {
        "@type": "ListItem",
        "position": 13,
        "name": "Madhya Pradesh Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-madhya-pradesh"
      },
      {
        "@type": "ListItem",
        "position": 14,
        "name": "Maharashtra Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-maharashtra"
      },
      {
        "@type": "ListItem",
        "position": 15,
        "name": "Manipur Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-manipur"
      },
      {
        "@type": "ListItem",
        "position": 16,
        "name": "Meghalaya Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-meghalaya"
      },
      {
        "@type": "ListItem",
        "position": 17,
        "name": "Mizoram Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-mizoram"
      },
      {
        "@type": "ListItem",
        "position": 18,
        "name": "Nagaland Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-nagaland"
      },
      {
        "@type": "ListItem",
        "position": 19,
        "name": "Odisha Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-odisha"
      },
      {
        "@type": "ListItem",
        "position": 20,
        "name": "Punjab Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-punjab"
      },
      {
        "@type": "ListItem",
        "position": 21,
        "name": "Rajasthan Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-rajasthan"
      },
      {
        "@type": "ListItem",
        "position": 22,
        "name": "Sikkim Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-sikkim"
      },
      {
        "@type": "ListItem",
        "position": 23,
        "name": "Tamil Nadu Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-tamil-nadu"
      },
      {
        "@type": "ListItem",
        "position": 24,
        "name": "Telangana Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-telangana"
      },
      {
        "@type": "ListItem",
        "position": 25,
        "name": "Tripura Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-tripura"
      },
      {
        "@type": "ListItem",
        "position": 26,
        "name": "Uttar Pradesh Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-uttar-pradesh"
      },
      {
        "@type": "ListItem",
        "position": 27,
        "name": "Uttarakhand Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-uttaranchal"
      },
      {
        "@type": "ListItem",
        "position": 28,
        "name": "West Bengal Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-west-bengal"
      },
      {
        "@type": "ListItem",
        "position": 29,
        "name": "Delhi Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-delhi"
      },
      {
        "@type": "ListItem",
        "position": 30,
        "name": "Chandigarh Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-chandigarh"
      },
      {
        "@type": "ListItem",
        "position": 31,
        "name": "Jammu & Kashmir Government Jobs",
        "url": "https://www.searchsarkarinaukri.com/jobs-in-jammu-kashmir"
      }
    ]
  }
}
</script>
```

---

## 4. FAQPage JSON-LD (All 15 Detailed FAQs)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What are state government jobs?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "State government jobs (also referred to as state Sarkari Naukri) are public sector employment opportunities administered directly by the government of an Indian state or Union Territory. Unlike Central Government posts, state posts are organized under state administrative cadres spanning gazetted officers via State PSCs, subordinate staff, teachers, police, and healthcare workers."
      }
    },
    {
      "@type": "Question",
      "name": "Where can I find latest state government jobs?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Candidates can find verified state government jobs directly on SearchSarkariNaukri’s State Government Jobs Directory, which aggregates live vacancies across all 28 states and 8 Union Territories with direct links to official PDF advertisements and application portals. Official notices are also published in State Gazettes and State PSC websites."
      }
    },
    {
      "@type": "Question",
      "name": "Can I apply for another state's government jobs?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "In most cases, yes—citizens of India can apply for state government jobs in another state under the General / Unreserved (UR) category under Article 16 of the Constitution. However, candidates cannot claim home-state category reservations (SC/ST/OBC/EWS) and must satisfy regional language and post-specific domicile rules where applicable."
      }
    },
    {
      "@type": "Question",
      "name": "Is domicile compulsory for state government jobs?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Domicile is not universally compulsory for every state government job. State PSC civil services and technical roles are often open to all Indian citizens under the General category. However, non-gazetted, clerical, village-level, and police constable posts frequently mandate a state Domicile / Permanent Resident Certificate. Domicile is also mandatory to claim state reservation benefits."
      }
    },
    {
      "@type": "Question",
      "name": "What is the age limit for state government jobs?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Age limits vary by state and post. Minimum age is typically 18 to 21 years. Standard upper age limits for General category candidates range from 38 to 40 years in states like Maharashtra, UP, and Rajasthan, and up to 42-44 years in Telangana and Andhra Pradesh, with standard relaxations of +5 years for SC/ST and +3 years for OBC."
      }
    },
    {
      "@type": "Question",
      "name": "Which state government jobs are available after 10th pass?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Candidates with a Class 10 pass qualification can apply for Police Constables, Forest Guards (Vanrakshak), Home Guards, State Road Transport Corporation drivers and conductors, Multi-Tasking Staff (MTS), peons, and municipal field workers."
      }
    },
    {
      "@type": "Question",
      "name": "Which state government jobs are available after 12th pass?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Class 12 pass candidates qualify for Junior Clerks, Lower Division Clerks (LDC), Typists, Patwaris, Talathis, Village Development Officers (VDO), Panchayat Sachiv, Excise Constables, and Forest Beat Officers across state departments."
      }
    },
    {
      "@type": "Question",
      "name": "What state government jobs are available for graduates?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A bachelor’s degree qualifies candidates for State Civil Services (Deputy Collector, DSP, Tehsildar, BDO) recruited via State PSCs, Police Sub-Inspectors (PSI), Assistant Engineers, Medical Officers, and School Teachers (with B.Ed)."
      }
    },
    {
      "@type": "Question",
      "name": "How do I apply for state government jobs?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "To apply safely: 1) Download the official advertisement from SearchSarkariNaukri; 2) Check age, qualification, and certificate cutoff dates; 3) Access the verified government portal; 4) Complete One-Time Registration (OTR); 5) Fill the application form; 6) Upload scanned documents; 7) Pay application fees online; 8) Download and print the confirmation slip."
      }
    },
    {
      "@type": "Question",
      "name": "Are state government job applications online or offline?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Over 95% of state government job applications are conducted online through State PSC and departmental One-Time Registration (OTR) portals. Offline applications are used only occasionally for specialized contractual posts, walk-in medical drives, or district court clerkships."
      }
    },
    {
      "@type": "Question",
      "name": "How can I check eligibility for state government jobs?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Check eligibility by: 1) Calculating age on the exact notification benchmark date; 2) Verifying recognized degree equivalence; 3) Reviewing domicile and nationality rules; 4) Checking mandatory physical standards for police/forest posts; and 5) Using the SearchSarkariNaukri online Eligibility Checker tool."
      }
    },
    {
      "@type": "Question",
      "name": "Where can I find official state government job notifications?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Official notifications are published in State Government Gazettes, official State Public Service Commission websites (e.g., mpsc.gov.in, uppsc.up.nic.in), state department portals, and district NIC websites. SearchSarkariNaukri indexes and directly links candidates to these official gazettes."
      }
    },
    {
      "@type": "Question",
      "name": "What is the difference between State PSC and department recruitment?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "State PSCs are constitutional bodies recruiting primarily for Class 1 (Group A) and Class 2 (Group B) gazetted executive cadres through multi-tier examinations. Departmental recruitments are conducted directly by boards or departments for non-gazetted Group C and Group D roles (constables, clerks, nurses)."
      }
    },
    {
      "@type": "Question",
      "name": "Are state government jobs transferable?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, but transfers are strictly confined within the hiring state cadre. Statewide cadre officers recruited via State PSCs undergo periodic transfers across districts within the state. District cadre posts (such as Zilla Parishad staff and Talathis) are generally non-transferable outside their assigned district."
      }
    },
    {
      "@type": "Question",
      "name": "How frequently is this page updated?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "SearchSarkariNaukri’s State Government Jobs Directory is updated daily as soon as state recruiting agencies release new notices or extensions. Vacancy counts are dynamically recalculated, and expired posts are automatically removed upon deadline closure."
      }
    }
  ]
}
</script>
```
