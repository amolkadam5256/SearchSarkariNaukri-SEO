# 🛠️ Developer Handoff — Fix Google Search Console 404 Errors

## SearchSarkariNaukri.com

---

**Prepared by:** SEO Team / Growthik Media  
**Date:** 2026-08-05  
**Project:** SearchSarkariNaukri.com  
**Issue:** Google Search Console → Page Indexing → Not Found (404)  
**Total Affected URLs:** 607  
**Priority:** 🔴 Critical

---

## 📌 What This Document Is

This is a **complete developer action document**.

It contains:

- The exact problem
- Every affected URL
- The exact fix required for each URL group
- Code implementation instructions
- Testing checklist
- What you must NOT change

Read this document fully before writing any code.

---

## 🚫 Scope — What You Must NOT Change

Do NOT modify any of the following during this task:

- UI layout or design
- React components or CSS
- Navigation or header/footer design
- Database records or schema
- Existing business logic
- Existing API routes (except as needed for routing)
- Any feature unrelated to the 404 fix

Only fix URL routing, redirects, and HTTP response codes for the specific URLs listed in this document.

---

## 🔍 Root Cause

The website migrated job URL format from:

```
OLD:  /jobs/123
NEW:  /jobs/org-name-job-title-123
```

The **old numeric URLs were never redirected**.

Google had indexed 552+ old URLs before the migration. They are still being crawled and returning 404.

Additionally:

- Some old SEO slug URLs have changed (slug was regenerated)
- City and district pages are returning 404
- One category page is returning 404

---

## 📊 Affected URL Summary

| Group     | Pattern                                | Count   | Fix                 |
| --------- | -------------------------------------- | ------- | ------------------- |
| A         | `/jobs/{number}` (numeric only)        | **552** | 301 → current slug  |
| B         | `/jobs/{old-slug}-{id}` (slug changed) | **30**  | 301 → new slug      |
| C         | `/jobs/{truncated-slug}` (no ID)       | **9**   | Prefix search → 301 |
| D         | `/jobs-in-{city}` (city pages)         | **11**  | 301 or 410          |
| E         | `/districts/{slug}` (district pages)   | **4**   | 301 or 410          |
| F         | `/category/{slug}` (category page)     | **1**   | 301 or 410          |
| **TOTAL** |                                        | **607** |                     |

---

## ✅ Group A — Legacy Numeric URLs (552 URLs)

### Pattern

```
https://www.searchsarkarinaukri.com/jobs/858
https://www.searchsarkarinaukri.com/jobs/983
https://www.searchsarkarinaukri.com/jobs/1104
```

### Required Fix

For each numeric ID:

1. Query database: does a job with this ID exist?
2. **If YES** → `HTTP 301` redirect to `/jobs/{current-slug}-{id}`
3. **If NO** → return `HTTP 410 Gone`

### Implementation — Next.js Route Handler

In your existing job detail route (e.g. `app/jobs/[slug]/page.tsx` or `pages/jobs/[slug].tsx`):

```typescript
// In your job page handler
export async function generateMetadata({ params }) {
  const { slug } = params;

  // Check if slug is purely numeric
  const numericId = /^\d+$/.test(slug) ? parseInt(slug) : null;

  if (numericId) {
    // Look up job by ID
    const job = await db.job.findUnique({ where: { id: numericId } });

    if (job) {
      // Redirect to SEO slug URL
      redirect(`/jobs/${job.slug}-${job.id}`, 301);
    } else {
      // Job does not exist
      notFound(); // or return 410
    }
  }
}
```

**For HTTP 410 (Gone) instead of 404:**

```typescript
import { notFound } from "next/navigation";

// In Next.js App Router, use notFound() for removed pages
// For proper 410, use middleware or a custom response
export default function JobPage({ params }) {
  // ... job not found case
  return notFound();
}
```

**Alternative — next.config.js redirects (for known ID ranges):**

```javascript
// next.config.js
async redirects() {
  return [
    {
      source: '/jobs/:id(\\d+)',
      destination: '/jobs/lookup/:id',  // a lookup API that does the redirect
      permanent: true,
    },
  ];
}
```

### All 552 Numeric Job IDs

Query your database for each of these IDs and generate the redirect or 410:

```
14, 16, 18, 19, 25, 29, 58, 297, 832, 835, 839, 847, 854, 855, 856, 857, 858, 860, 875, 880,
883, 887, 895, 898, 973, 974, 975, 977, 978, 980, 981, 983, 984, 986, 988, 989, 990, 991, 993, 994,
995, 996, 997, 998, 999, 1015, 1016, 1017, 1018, 1019, 1021, 1022, 1025, 1026, 1028, 1030, 1031, 1032, 1033, 1035,
1036, 1037, 1038, 1040, 1041, 1042, 1043, 1045, 1073, 1078, 1079, 1081, 1082, 1084, 1087, 1088, 1090, 1091, 1092, 1093,
1094, 1095, 1096, 1097, 1098, 1100, 1101, 1103, 1104, 1105, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1116, 1118, 1120,
1123, 1128, 1133, 1134, 1135, 1136, 1290, 1291, 1292, 1293, 1295, 1296, 1299, 1301, 1304, 1305, 1307, 1308, 1310, 1311,
1313, 1317, 1322, 1361, 1363, 1365, 1366, 1373, 1376, 1383, 1386, 1387, 1388, 1389, 1391, 1396, 1397, 1398, 1401, 1402,
1403, 1404, 1405, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1416, 1417, 1418, 1420, 1421, 1422, 1423, 1424, 1425,
1427, 1428, 1429, 1431, 1432, 1433, 1434, 1436, 1438, 1439, 1440, 1442, 1443, 1444, 1445, 1447, 1448, 1449, 1450, 1454,
1455, 1457, 1458, 1461, 1462, 1463, 1464, 1468, 1469, 1471, 1478, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1489, 1497,
1498, 1499, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1513, 1514, 1516, 1518, 1521, 1522, 1523, 1525,
1526, 1530, 1536, 1538, 1549, 1550, 1551, 1552, 1555, 1556, 1559, 1562, 1563, 1564, 1566, 1569, 1570, 1571, 1573, 1574,
1576, 1579, 1580, 1581, 1582, 1583, 1584, 1585, 1586, 1588, 1589, 1590, 1591, 1592, 1593, 1594, 1595, 1596, 1597, 1598,
1599, 1600, 1601, 1602, 1603, 1604, 1605, 1607, 1608, 1609, 1611, 1612, 1613, 1614, 1615, 1616, 1617, 1618, 1621, 1623,
1625, 1627, 1628, 1630, 1635, 1636, 1646, 1647, 1649, 1650, 1652, 1653, 1656, 1657, 1658, 1660, 1661, 1662, 1663, 1664,
1668, 1670, 1671, 1672, 1673, 1674, 1675, 1676, 1677, 1679, 1681, 1682, 1683, 1685, 1686, 1687, 1688, 1690, 1691, 1692,
1694, 1695, 1696, 1697, 1698, 1699, 1702, 1703, 1704, 1705, 1708, 1710, 1713, 1714, 1716, 1717, 1719, 1721, 1725, 1726,
1727, 1728, 1729, 1732, 1733, 1735, 1736, 1737, 1738, 1740, 1741, 1744, 1746, 1747, 1748, 1753, 1758, 1760, 1763, 1767,
1768, 1769, 1770, 1772, 1774, 1777, 1779, 1780, 1781, 1782, 1783, 1785, 1786, 1787, 1791, 1799, 1800, 1804, 1805, 1809,
1810, 1811, 1814, 1815, 1816, 1817, 1819, 1826, 1827, 1828, 1829, 1831, 1835, 1836, 1837, 1838, 1839, 1841, 1844, 1847,
1850, 1851, 1852, 1854, 1857, 1862, 1863, 1864, 1865, 1868, 1870, 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879,
1881, 1882, 1885, 1887, 1889, 1890, 1892, 1895, 1896, 1901, 1903, 1904, 1907, 1908, 1910, 1911, 1912, 1914, 1916, 1917,
1920, 1922, 1924, 1926, 1927, 1936, 1938, 1939, 1941, 1943, 1948, 1956, 1964, 1966, 1967, 1975, 1981, 1983, 1985, 1986,
1987, 1988, 1992, 1994, 1995, 1996, 1998, 1999, 2001, 2005, 2006, 2008, 2011, 2013, 2015, 2016, 2018, 2019, 2021, 2023,
2025, 2028, 2032, 2033, 2036, 2037, 2038, 2039, 2044, 2046, 2047, 2051, 2052, 2053, 2055, 2056, 2065, 2067, 2068, 2070,
2071, 2072, 2074, 2078, 2079, 2080, 2081, 2083, 2084, 2086, 2092, 2095, 2096, 2098, 2099, 2100, 2102, 2104, 2110, 2111,
2113, 2116, 2122, 2125, 2129, 2133, 2140, 2143, 2144, 2145, 2146, 2149, 2154, 2155, 2158, 2166, 2168, 2199, 2200, 2201,
2204, 2205, 2206, 2209, 2210, 2212, 2213, 2215, 2217, 2218, 2219, 2223
```

---

## ✅ Group B — Old SEO Slug URLs (Slug Changed) — 30 URLs

### Pattern

These URLs contain a numeric ID at the end but the slug portion has changed.

```
/jobs/old-slug-name-{id}
```

### Required Fix

1. Extract the numeric ID from the end of the slug
2. Query database: `SELECT slug FROM jobs WHERE id = {id}`
3. If current slug ≠ requested slug → `HTTP 301` redirect to `/jobs/{current-slug}-{id}`
4. If job does not exist → `HTTP 410`

### Implementation

This fix is handled by the **same canonical slug enforcement** logic from Group A.

In your job page handler, after loading the job by ID:

```typescript
// Extract ID from slug
const parts = slug.split("-");
const id = parseInt(parts[parts.length - 1]);

if (!isNaN(id)) {
  const job = await db.job.findUnique({ where: { id } });

  if (!job) {
    // Return 410
    notFound();
  }

  const expectedSlug = `${job.slug}-${job.id}`;
  if (slug !== expectedSlug) {
    // Slug has changed — redirect to current canonical URL
    redirect(`/jobs/${expectedSlug}`, 301);
  }

  // Correct slug — serve the page normally
  return renderJob(job);
}
```

### All 30 Affected URLs

| Old URL                                                                                    | Job ID  | Action                     |
| ------------------------------------------------------------------------------------------ | ------- | -------------------------- |
| /jobs/institute-of-banking-personnel-selectionibps-research-associate-faculty-technica-858 | 858     | Check slug → redirect      |
| /jobs/sports-authority-of-india-sai-assistant-director-deputation-basis-all-india-2026-863 | 863     | Check slug → redirect      |
| /jobs/sports-authority-of-india-sai-sai-internship-program-head-office-regional-center-862 | 862     | Check slug → redirect      |
| /jobs/united-commercial-bank-uco-bank-scribe-declaration-for-recruitment-of-specialist-253 | 253     | Check slug → redirect      |
| /jobs/edcil-india-limited-hiring-of-ai-advisor-2026-317                                    | 317     | Check slug → redirect      |
| /jobs/national-career-servicencs-company-national-health-systems-resource-centre-delhi-839 | 839     | Check slug → redirect      |
| /jobs/united-commercial-bank-uco-bank-recruitment-of-probationary-officers-for-written-276 | 276     | Check slug → redirect      |
| /jobs/staff-selection-commission-ssc-junior-engineer-civil-mechanical-electrical-exami-860 | 860     | Check slug → redirect      |
| /jobs/united-commercial-bank-uco-bank-information-handout-for-recruitment-of-specialis-252 | 252     | Check slug → redirect      |
| /jobs/-aurangabad-cantonment-board-2026-895                                                | 895     | Check slug → redirect      |
| /jobs/nielit-delhi-centre-stqc-drivers-recruitment-2026-advertisement-number-nielitndl-313 | 313     | Check slug → redirect      |
| /jobs/edcil-india-limited-hiring-of-ai-advisor-2026                                        | ⚠️ 2026 | Manual — ID = year, verify |
| /jobs/bhabha-atomic-research-centre-barc-research-associate-ra-physicschemistrylife-sc-857 | 857     | Check slug → redirect      |
| /jobs/-currency-note-press-nashik-nashik-maharashtra-2026-887                              | 887     | Check slug → redirect      |
| /jobs/indian-railways-ir-gm-st-india-2026-18                                               | 18      | Check slug → redirect      |
| /jobs/unique-identification-authority-of-indiauidai-extended-vacancy-circular-for-the-832  | 832     | Check slug → redirect      |
| /jobs/oil-and-natural-gas-corporation-limited-ongc-trade-apprentice-diploma-apprentice-880 | 880     | Check slug → redirect      |
| /jobs/united-commercial-bank-uco-bank-advt-no-hohrmrecr2025-26com-03-engagement-of-app-226 | 226     | Check slug → redirect      |
| /jobs/bhabha-atomic-research-centre-barc-ocesdgfs-2026-scientific-officer-c-mumbai-kal-854 | 854     | Check slug → redirect      |
| /jobs/indian-railways-ir-deputy-general-manager-civil-india-2026-25                        | 25      | Check slug → redirect      |
| /jobs/sports-authority-of-india-sai-inviting-application-for-appointment-for-medical-o-304 | 304     | Check slug → redirect      |
| /jobs/-staff-selection-commission-mts-all-india-2026-898                                   | 898     | Check slug → redirect      |
| /jobs/bhabha-atomic-research-centre-barc-stipendiary-trainee-category-i-scientific-ass-855 | 855     | Check slug → redirect      |
| /jobs/maharashtra-public-service-commissionmpsc-motor-vehicle-prosecutor-regional-tran-847 | 847     | Check slug → redirect      |
| /jobs/bhabha-atomic-research-centre-barc-technical-officerc-direct-recruitment-barc-mu-856 | 856     | Check slug → redirect      |
| /jobs/unique-identification-authority-of-indiauidai-vacancy-circular-for-filling-up-po-835 | 835     | Check slug → redirect      |
| /jobs/ntpc-limited-gdmo-medical-officer-ntpc-hospitals-at-various-project-sites-2026-875   | 875     | Check slug → redirect      |
| /jobs/united-commercial-bank-uco-bank-details-for-recruitment-of-1050-probationary-off-282 | 282     | Check slug → redirect      |
| /jobs/indian-railways-ir-general-manager-finance-india-2026-16                             | 16      | Check slug → redirect      |
| /jobs/indian-railways-ir-gm-te-ggm-te-india-2026-19                                        | 19      | Check slug → redirect      |

---

## ✅ Group C — Truncated Slug URLs (9 URLs)

### Pattern

These are old URLs where the slug was cut short. No numeric ID at the end.

```
/jobs/united-commercial-bank-uco-bank-scribe-declaration-for-recruitment-of-
```

### Required Fix

Do a **prefix search** in the database to match the truncated slug to a full slug.

```typescript
// Prefix search example
const job = await db.job.findFirst({
  where: {
    slug: {
      startsWith: truncatedSlug.replace(/^\/jobs\//, ""),
    },
  },
});

if (job) {
  redirect(`/jobs/${job.slug}-${job.id}`, 301);
} else {
  notFound(); // 410
}
```

### All 9 Truncated URLs

| Truncated URL                                                                | Search Prefix                                                 | Action              |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------- | ------------------- |
| /jobs/institute-of-banking-personnel-selectionibps-research-associate-facult | `institute-of-banking-personnel-selectionibps`                | Prefix search → 301 |
| /jobs/sports-authority-of-india-sai-sai-internship-program-head-office-regio | `sports-authority-of-india-sai-sai-internship`                | Prefix search → 301 |
| /jobs/united-commercial-bank-uco-bank-details-for-recruitment-of-1050-probat | `united-commercial-bank-uco-bank-details-for`                 | Prefix search → 301 |
| /jobs/united-commercial-bank-uco-bank-this-has-reference-to-our-earlier-recr | `united-commercial-bank-uco-bank-this-has-reference`          | Prefix search → 301 |
| /jobs/united-commercial-bank-uco-bank-scribe-declaration-for-recruitment-of- | `united-commercial-bank-uco-bank-scribe-declaration`          | Prefix search → 301 |
| /jobs/sports-authority-of-india-sai-inviting-application-for-appointment-for | `sports-authority-of-india-sai-inviting-application`          | Prefix search → 301 |
| /jobs/united-commercial-bank-uco-bank-information-handout-for-recruitment-of | `united-commercial-bank-uco-bank-information-handout`         | Prefix search → 301 |
| /jobs/united-commercial-bank-uco-bank-recruitment-of-probationary-officers-f | `united-commercial-bank-uco-bank-recruitment-of-probationary` | Prefix search → 301 |
| /jobs/united-commercial-bank-uco-bank-advt-no-hohrmrecr2025-26com-03-engagem | `united-commercial-bank-uco-bank-advt-no`                     | Prefix search → 301 |

---

## ✅ Group D — City Pages (11 URLs)

### Pattern

```
/jobs-in-{city-name}
```

### Required Fix

Check whether `/jobs-in-{city}` routing exists in the application.

- If city pages exist → fix routing so they return `HTTP 200`
- If city pages have been moved to `/districts/{slug}` → `HTTP 301` redirect
- If city pages were removed → `HTTP 410`

### All 11 City URLs

| URL                      | City            | Action                      |
| ------------------------ | --------------- | --------------------------- |
| /jobs-in-new-delhi       | New Delhi       | Verify routing → 200 or 410 |
| /jobs-in-akola           | Akola           | Verify routing → 200 or 410 |
| /jobs-in-mumbai-suburban | Mumbai Suburban | Verify routing → 200 or 410 |
| /jobs-in-palghar         | Palghar         | Verify routing → 200 or 410 |
| /jobs-in-sangli          | Sangli          | Verify routing → 200 or 410 |
| /jobs-in-kolhapur        | Kolhapur        | Verify routing → 200 or 410 |
| /jobs-in-satara          | Satara          | Verify routing → 200 or 410 |
| /jobs-in-mumbai-city     | Mumbai City     | Verify routing → 200 or 410 |
| /jobs-in-kanpur-nagar    | Kanpur Nagar    | Verify routing → 200 or 410 |
| /jobs-in-solapur         | Solapur         | Verify routing → 200 or 410 |
| /jobs-in-chandrapur      | Chandrapur      | Verify routing → 200 or 410 |

---

## ✅ Group E — District Pages (4 URLs)

### Pattern

```
/districts/{district-slug}
```

### Required Fix

Check whether `/districts/{slug}` routing exists.

- If routing exists → fix so it returns `HTTP 200`
- If routing removed → `HTTP 410`

### All 4 District URLs

| URL                      | Action                      |
| ------------------------ | --------------------------- |
| /districts/new-delhi     | Verify routing → 200 or 410 |
| /districts/all-districts | Likely removed → HTTP 410   |
| /districts/kanpur-nagar  | Verify routing → 200 or 410 |
| /districts/mumbai        | Verify routing → 200 or 410 |

---

## ✅ Group F — Category Page (1 URL)

### URL

```
/category/state-government-jobs
```

### Required Fix

Check if the State Government Jobs category exists.

- If exists under `/categories/state-government-jobs` or another path → `HTTP 301` redirect
- If removed → `HTTP 410`

---

## 📋 HTTP Response Reference

| Situation                                | Response                                |
| ---------------------------------------- | --------------------------------------- |
| Job exists, URL is old format            | **HTTP 301** → redirect to current URL  |
| Job exists, slug has changed             | **HTTP 301** → redirect to current slug |
| Job does NOT exist                       | **HTTP 410** Gone                       |
| Page was removed with no replacement     | **HTTP 410** Gone                       |
| Archived/expired job still in DB         | **HTTP 200** (serve the page)           |
| Category/city/district exists at new URL | **HTTP 301** → redirect                 |

> ⚠️ Do NOT use HTTP 302 (temporary). Use only HTTP 301 for permanent redirects.
> ⚠️ Do NOT redirect everything to the homepage.
> ⚠️ Do NOT redirect to unrelated pages.

---

## 🏗️ Recommended Implementation Order

```
Step 1
Fix Group A (552 numeric URLs) — highest impact
One dynamic route handler resolves 90% of all 404s

↓

Step 2
Fix Group B (30 old slug URLs) — same handler as Step 1
Canonical slug enforcement resolves these automatically

↓

Step 3
Fix Group C (9 truncated slug URLs) — prefix search in handler

↓

Step 4
Fix Group D — City pages (11 URLs)
Check routing. Add 301 or 410.

↓

Step 5
Fix Group E — District pages (4 URLs)
Check routing. Add 301 or 410.

↓

Step 6
Fix Group F — Category page (1 URL)
Add 301 or 410.

↓

Step 7
Sitemap cleanup
Remove old numeric and invalid URLs from sitemap.
Only keep URLs that return HTTP 200.

↓

Step 8
Internal links audit
Search codebase for any hardcoded /jobs/{number} links.
Update to use current slug URLs.

↓

Step 9
Deploy to production

↓

Step 10
Verify in browser using curl or DevTools
Test sample URLs from each group

↓

Step 11
Request "Validate Fix" in Google Search Console
Page Indexing → Not Found (404) → Validate Fix
```

---

## 🧪 Testing Checklist

Before deployment, test the following:

### Group A — Numeric URL Tests

```bash
# Test: should redirect to slug URL
curl -I https://www.searchsarkarinaukri.com/jobs/858
# Expected: HTTP 301 → Location: /jobs/{slug}-858

# Test: should return 410 (if ID doesn't exist)
curl -I https://www.searchsarkarinaukri.com/jobs/99999
# Expected: HTTP 410
```

### Group B — Old Slug URL Tests

```bash
# Test: should redirect to current slug
curl -I "https://www.searchsarkarinaukri.com/jobs/bhabha-atomic-research-centre-barc-stipendiary-trainee-category-i-scientific-ass-855"
# Expected: HTTP 301 → /jobs/{current-slug}-855
```

### Verify No Redirect Loops

```bash
# Follow redirects — must resolve in 1 hop
curl -IL https://www.searchsarkarinaukri.com/jobs/858
# Must NOT loop. Must resolve in exactly 1 redirect.
```

### Sitemap Test

```bash
# Check sitemap does not contain old numeric URLs
curl https://www.searchsarkarinaukri.com/sitemap.xml | grep "/jobs/[0-9]"
# Expected: no results
```

### Regression Test

Verify that currently working job pages still return 200:

```bash
curl -I https://www.searchsarkarinaukri.com/jobs/{any-current-working-job-slug}
# Expected: HTTP 200
```

---

## ✅ Developer Completion Checklist

Complete every item before notifying the SEO team.

| Task                                                   | Done |
| ------------------------------------------------------ | ---- |
| Read this entire document                              | ☐    |
| Implemented numeric URL handler (Group A)              | ☐    |
| Implemented canonical slug enforcement (Group B)       | ☐    |
| Implemented truncated slug prefix search (Group C)     | ☐    |
| Verified city page routing (Group D)                   | ☐    |
| Verified district page routing (Group E)               | ☐    |
| Verified category page routing (Group F)               | ☐    |
| Sitemap cleaned (no 404/410/301 source URLs)           | ☐    |
| Internal links audited (no `/jobs/{number}` hardcoded) | ☐    |
| All redirects tested with curl or browser              | ☐    |
| No redirect loops confirmed                            | ☐    |
| Regression test passed (existing pages still work)     | ☐    |
| Deployed to production                                 | ☐    |
| Confirmed fixes live in production                     | ☐    |

---

## 📁 Reference Files

All supporting documentation is in this folder:

```
.agents/00_Report_Issues/Google-Search-Console/01_404_Not_Found/
```

| File                          | Contents                              |
| ----------------------------- | ------------------------------------- |
| README.md                     | Project scope and rules               |
| 02_GSC_404_Report_Analysis.md | Full URL analysis with all IDs        |
| 03_URL_Classification.md      | All 607 URLs classified               |
| 05_URL_Mapping.md             | Group-by-group implementation mapping |
| 06_Redirect_Strategy.md       | Redirect rules and decision matrix    |
| 07_Archive_Expired_Jobs.md    | Archive page decisions                |
| 09_Sitemap_Cleanup.md         | Sitemap cleanup instructions          |
| 10_Internal_Links_Fix.md      | Internal link audit guide             |
| 12_Testing_Checklist.md       | Full testing checklist                |

The GSC Excel export is also in this folder:

```
https___www.searchsarkarinaukri.com_-Coverage-Drilldown-2026-08-05.xlsx
```

---

## 📞 After You Finish

Once all fixes are deployed and confirmed in production:

1. Notify the SEO team that implementation is complete
2. SEO team will open Google Search Console
3. Navigate to: Page Indexing → Not Found (404)
4. Click **"Validate Fix"**
5. Google will recrawl and confirm the fixes (typically 1–4 weeks)

---

_End of Developer Handoff Document_  
_Prepared by: Growthik Media SEO Team_  
_Do not modify this document without SEO team review_
