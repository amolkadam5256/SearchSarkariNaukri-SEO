# 07 — SCHEMA MARKUP SPECIFICATION

**Section:** Structured Data Implementation  
**Priority:** P1  
**Type:** Technical Implementation  
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

## Schema Markup Strategy

### Main Districts Page

#### WebPage Schema
```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Maharashtra Government Jobs by District",
  "description": "Find Maharashtra government jobs by district. Explore Pune, Mumbai, Nagpur, Nashik and all 36 districts for latest Sarkari Naukri.",
  "url": "https://www.searchsarkarinaukri.com/districts",
  "dateModified": "2026-09-08",
  "isPartOf": {
    "@type": "WebSite",
    "name": "SearchSarkariNaukri",
    "url": "https://www.searchsarkarinaukri.com"
  }
}
```

#### BreadcrumbList Schema
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
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Maharashtra Districts",
      "item": "https://www.searchsarkarinaukri.com/districts"
    }
  ]
}
```

#### ItemList Schema (For District Directory)
```json
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Pune",
      "url": "https://www.searchsarkarinaukri.com/districts/pune",
      "description": "Government Jobs in Pune - 26 Active Jobs"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Mumbai City",
      "url": "https://www.searchsarkarinaukri.com/districts/mumbai-city",
      "description": "Government Jobs in Mumbai City - 86 Active Jobs"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Nagpur",
      "url": "https://www.searchsarkarinaukri.com/districts/nagpur",
      "description": "Government Jobs in Nagpur - 26 Active Jobs"
    }
  ]
}
```

---

## Individual District Page Schema

### WebPage Schema Template
```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Government Jobs in {District Name}",
  "description": "Find latest government jobs in {District Name}, Maharashtra.",
  "url": "https://www.searchsarkarinaukri.com/districts/{district-slug}",
  "dateModified": "{dynamic-date}",
  "isPartOf": {
    "@type": "WebSite",
    "name": "SearchSarkariNaukri",
    "url": "https://www.searchsarkarinaukri.com"
  }
}
```

### BreadcrumbList Schema Template
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
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Maharashtra Districts",
      "item": "https://www.searchsarkarinaukri.com/districts"
    },
    {
      "@type": "ListItem",
      "position": 4,
      "name": "{District Name}",
      "item": "https://www.searchsarkarinaukri.com/districts/{district-slug}"
    }
  ]
}
```

---

## FAQ Schema Specification

### FAQPage Schema (If Eligible)

**Only implement if:**
- FAQ content is visible on the page
- FAQ meets Google's current requirements
- Questions and answers are genuinely helpful

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How can I find government jobs by district in Maharashtra?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Maharashtra government jobs can be searched district-wise by selecting your district from the district directory above and reviewing currently active recruitment notifications. Eligibility, vacancies and application dates vary by recruitment."
      }
    },
    {
      "@type": "Question",
      "name": "How many districts are there in Maharashtra?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Maharashtra has 36 districts organized into 6 regions: Mumbai & Konkan, North Maharashtra, West Maharashtra, Marathwada, Vidarbha (Amravati) and Vidarbha (Nagpur)."
      }
    },
    {
      "@type": "Question",
      "name": "Which Maharashtra districts have government job vacancies?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Government job vacancies vary by district and recruitment notification. Some districts like Pune, Mumbai, Nagpur and Nashik may have more recruitment due to the presence of municipal corporations, major institutions and government departments. Check individual district pages for current vacancies."
      }
    },
    {
      "@type": "Question",
      "name": "How can I find government jobs in Pune?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Select Pune from the district directory or visit the Government Jobs in Pune page to view currently available recruitment opportunities in Pune district. Check eligibility, vacancies and application dates for each recruitment."
      }
    },
    {
      "@type": "Question",
      "name": "How can I find government jobs in Mumbai?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Select Mumbai City or Mumbai Suburban from the district directory to view government recruitment opportunities in Mumbai. Government jobs in Mumbai include positions in municipal corporations, state government offices and public sector organizations."
      }
    },
    {
      "@type": "Question",
      "name": "Are Maharashtra government jobs available for 10th pass candidates?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, 10th pass candidates can find government jobs in Maharashtra depending on the recruitment notification. Positions may include constable, clerk, peon, driver and other roles depending on the department and organization."
      }
    },
    {
      "@type": "Question",
      "name": "Are there government jobs for 12th pass candidates in Maharashtra?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, 12th pass candidates can find government jobs in Maharashtra across various departments including police, administration, clerk positions and other roles depending on the recruitment eligibility criteria."
      }
    },
    {
      "@type": "Question",
      "name": "Are graduate government jobs available in Maharashtra districts?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, graduate government jobs are available in Maharashtra districts across administration, education, healthcare, engineering and other departments depending on the recruitment notification and qualification requirements."
      }
    },
    {
      "@type": "Question",
      "name": "Where should I check the official recruitment notification?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The individual job page should provide the official notification or official organisation link. Candidates should verify recruitment details including eligibility, dates, fees and application process from the official notification before applying."
      }
    },
    {
      "@type": "Question",
      "name": "Does every Maharashtra district have active government vacancies?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, government job vacancies vary by district and recruitment notification. Some districts may have more active recruitment depending on the departments operating in that region. Recruitment is issued by different government organisations throughout the year."
      }
    },
    {
      "@type": "Question",
      "name": "How frequently are district government jobs updated?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "District government jobs are updated as new recruitment notifications are published by government organisations. Candidates should regularly check for new opportunities and application deadlines."
      }
    },
    {
      "@type": "Question",
      "name": "Can I apply for a government job from another Maharashtra district?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Eligibility and application rules depend on the recruitment notification. Some recruitments may have domicile requirements while others are open to eligible candidates across Maharashtra. Check the official notification for specific eligibility criteria."
      }
    }
  ]
}
```

---

## Implementation Rules

### DO NOT:

❌ Add fake schema data  
❌ Fabricate job counts or vacancy numbers  
❌ Add JobPosting schema to district listing pages  
❌ Add FAQ schema for hidden/not-implemented FAQs  
❌ Use same schema on all district pages without customization  
❌ Add schema for pages that don't exist yet

### DO:

✅ Use accurate data from database  
✅ Generate schema dynamically where appropriate  
✅ Validate with Google Rich Results Test  
✅ Keep schema in sync with page content  
✅ Update dateModified when content changes  
✅ Use proper URL structure  

---

## Validation Checklist

### Main Districts Page
- [ ] WebPage schema implemented
- [ ] BreadcrumbList schema implemented
- [ ] ItemList schema for district directory
- [ ] FAQ schema (if eligible)
- [ ] All URLs are accurate
- [ ] All names are accurate
- [ ] No duplicate schema types
- [ ] Validated with testing tools

### District Pages
- [ ] WebPage schema implemented
- [ ] BreadcrumbList schema implemented
- [ ] URLs are district-specific
- [ ] Names are district-specific
- [ ] dateModified is dynamic
- [ ] No duplicate schema
- [ ] Validated with testing tools

---

**Last Updated:** 8 September 2026  
**Status:** Implementation Ready