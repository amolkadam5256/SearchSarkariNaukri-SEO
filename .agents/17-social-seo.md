# 17 — Social SEO & Instant Multi-Channel Distribution

## 17.1 Open Graph & Social Metadata Code Standards

Every HTML page must render full Open Graph and Twitter Card tags in the `<head>` section:

```html
<!-- Open Graph Metadata -->
<meta property="og:title" content="SSC CGL 2026 Notification — Apply Online for 5000+ Vacancies" />
<meta property="og:description" content="SSC CGL 2026 recruitment notification out. Last date: 15 August 2026. Check eligibility, age limit, fee, and apply online." />
<meta property="og:image" content="https://www.searchsarkarinaukri.com/images/og/ssc-cgl-2026.webp" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:url" content="https://www.searchsarkarinaukri.com/jobs/ssc-cgl-2026" />
<meta property="og:type" content="article" />
<meta property="og:site_name" content="SearchSarkariNaukri" />
<meta property="og:locale" content="en_IN" />

<!-- Twitter Card Metadata -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@searchsarkari" />
<meta name="twitter:title" content="SSC CGL 2026 Notification — Apply Online" />
<meta name="twitter:description" content="SSC CGL 2026 recruitment notification out. Apply before 15 August 2026." />
<meta name="twitter:image" content="https://www.searchsarkarinaukri.com/images/og/ssc-cgl-2026.webp" />
```

---

## 17.2 Social Platform Strategy Matrix

| Platform | Channel / Profile | Format | Frequency | Primary Goal |
|----------|-------------------|--------|-----------|--------------|
| **Telegram Channel** | `@searchsarkarinaukri` | Real-time text + link alerts | 5–10 alerts/day | Instant traffic & candidate retention |
| **WhatsApp Channel** | Official Channel | Daily summary broadcasts | 1–2 broadcasts/day | High CTR mobile retention |
| **Facebook** | Page | Image post + short summary + link | 2–3 posts/day | Traffic & social signals |
| **Instagram** | `@searchsarkarinaukri` | Carousel graphics, reels, stories | 1–2 posts/day | Brand awareness & Gen-Z reach |
| **LinkedIn** | Company Page | Professional articles & statistics | 3–5 posts/week | Authority & B2B partnerships |
| **X (Twitter)** | `@searchsarkari` | Breaking news tweets + hashtags | 5–10 tweets/day | Real-time news indexation |
| **YouTube** | Official Channel | Prep videos & step-by-step guides | 2–3 videos/week | Video SEO & search traffic |
| **Pinterest** | Business Account | Infographic pins & exam calendars | 5–10 pins/week | Image search referral traffic |

---

## 17.3 Content Distribution Workflow Diagram

```
New Content Published on Website (CMS)
       │
       ├── Webhook Trigger 1: Telegram Channel (Instant Broadcast)
       ├── Webhook Trigger 2: WhatsApp Channel (Instant Broadcast)
       ├── Webhook Trigger 3: X / Twitter Auto-Tweet
       ├── Webhook Trigger 4: Facebook Page Auto-Post
       └── Scheduled Task: Pinterest Pin & Instagram Graphic Creation
```
