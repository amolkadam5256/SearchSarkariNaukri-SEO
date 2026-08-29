# 02 - Google Search Console 404 Report Analysis

**Project:** SearchSarkariNaukri.com

**Module:** Google Search Console → Page Indexing → Not Found (404)

**Priority:** 🔴 Critical

**Status:** ✅ Analysis Complete — 2026-08-05

---

# Purpose

This document analyzes the **Google Search Console 404 report** before any development work begins.

Its purpose is to understand:

- Which URLs are affected
- What types of URLs are failing
- Why they are failing
- Which URLs should be fixed
- Which URLs should remain removed

This document is **analysis only**.

It does **not** contain implementation steps.

Implementation is covered in later documents.

---

# Primary Objective

Analyze every URL reported in the Google Search Console export and classify the problem before making any code changes.

The objective is to prevent incorrect fixes such as:

- Restoring pages that should remain deleted
- Redirecting pages to unrelated destinations
- Creating unnecessary redirects
- Accidentally restoring duplicate URLs

---

# Reference Files

Use the following files throughout the analysis.

## Google Search Console Export

```
https___www.searchsarkarinaukri.com_-Coverage-Drilldown-2026-08-05.xlsx
```

This Excel file contains all **607 affected URLs**.

**Sheet: Table** — Contains all 607 URLs with Last Crawled date.

**Sheet: Chart** — Shows affected pages trend (May–Aug 2026).

**Sheet: Metadata** — Confirms: Property = All known pages, Issue = Not found (404).

Every reported URL has been reviewed during this analysis.

---

# Analysis Results — URL Breakdown

## Total Affected URLs

```
607 URLs
```

## URL Category Summary

| Category | Type | Count | % of Total |
|----------|------|-------|------------|
| B | Legacy Numeric Job URLs (`/jobs/123`) | **552** | **90.9%** |
| C | SEO Slug URLs with ID (`/jobs/org-name-123`) | **30** | **4.9%** |
| C | SEO Slug URLs without ID (truncated) | **9** | **1.5%** |
| G | District Pages (`/districts/slug`) | **4** | **0.7%** |
| H | City/Location Pages (`/jobs-in-city`) | **11** | **1.8%** |
| E | Category Pages (`/category/slug`) | **1** | **0.2%** |

---

# URL Pattern Analysis

## Pattern 1 — Legacy Numeric Job URLs

**Count: 552 URLs (90.9% of all 404s)**

**Format:**
```
/jobs/{numeric_id}
```

**Examples:**
```
https://www.searchsarkarinaukri.com/jobs/858
https://www.searchsarkarinaukri.com/jobs/983
https://www.searchsarkarinaukri.com/jobs/1104
https://www.searchsarkarinaukri.com/jobs/2223
```

**ID Range:** 14 to 2223

**All affected numeric IDs:**
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

**Root Cause:**

The website migrated from numeric URLs (`/jobs/123`) to SEO-friendly slug URLs (`/jobs/org-name-title-123`). The old numeric URLs were never redirected and are still being crawled by Google because they were previously indexed.

**Required Action:**

Each numeric ID must be checked in the database. If the job still exists under a new slug URL, implement a **301 redirect** from `/jobs/{id}` to `/jobs/{slug}-{id}`.

---

## Pattern 2 — SEO Slug URLs with Numeric ID

**Count: 30 URLs (4.9% of all 404s)**

**Format:**
```
/jobs/{org-name-title}-{id}
```

**All affected URLs:**
```
https://www.searchsarkarinaukri.com/jobs/institute-of-banking-personnel-selectionibps-research-associate-faculty-technica-858
https://www.searchsarkarinaukri.com/jobs/sports-authority-of-india-sai-assistant-director-deputation-basis-all-india-2026-863
https://www.searchsarkarinaukri.com/jobs/sports-authority-of-india-sai-sai-internship-program-head-office-regional-center-862
https://www.searchsarkarinaukri.com/jobs/united-commercial-bank-uco-bank-scribe-declaration-for-recruitment-of-specialist-253
https://www.searchsarkarinaukri.com/jobs/edcil-india-limited-hiring-of-ai-advisor-2026-317
https://www.searchsarkarinaukri.com/jobs/national-career-servicencs-company-national-health-systems-resource-centre-delhi-839
https://www.searchsarkarinaukri.com/jobs/united-commercial-bank-uco-bank-recruitment-of-probationary-officers-for-written-276
https://www.searchsarkarinaukri.com/jobs/staff-selection-commission-ssc-junior-engineer-civil-mechanical-electrical-exami-860
https://www.searchsarkarinaukri.com/jobs/united-commercial-bank-uco-bank-information-handout-for-recruitment-of-specialis-252
https://www.searchsarkarinaukri.com/jobs/-aurangabad-cantonment-board-2026-895
https://www.searchsarkarinaukri.com/jobs/nielit-delhi-centre-stqc-drivers-recruitment-2026-advertisement-number-nielitndl-313
https://www.searchsarkarinaukri.com/jobs/edcil-india-limited-hiring-of-ai-advisor-2026
https://www.searchsarkarinaukri.com/jobs/bhabha-atomic-research-centre-barc-research-associate-ra-physicschemistrylife-sc-857
https://www.searchsarkarinaukri.com/jobs/-currency-note-press-nashik-nashik-maharashtra-2026-887
https://www.searchsarkarinaukri.com/jobs/indian-railways-ir-gm-st-india-2026-18
https://www.searchsarkarinaukri.com/jobs/unique-identification-authority-of-indiauidai-extended-vacancy-circular-for-the-832
https://www.searchsarkarinaukri.com/jobs/oil-and-natural-gas-corporation-limited-ongc-trade-apprentice-diploma-apprentice-880
https://www.searchsarkarinaukri.com/jobs/united-commercial-bank-uco-bank-advt-no-hohrmrecr2025-26com-03-engagement-of-app-226
https://www.searchsarkarinaukri.com/jobs/bhabha-atomic-research-centre-barc-ocesdgfs-2026-scientific-officer-c-mumbai-kal-854
https://www.searchsarkarinaukri.com/jobs/indian-railways-ir-deputy-general-manager-civil-india-2026-25
https://www.searchsarkarinaukri.com/jobs/sports-authority-of-india-sai-inviting-application-for-appointment-for-medical-o-304
https://www.searchsarkarinaukri.com/jobs/-staff-selection-commission-mts-all-india-2026-898
https://www.searchsarkarinaukri.com/jobs/bhabha-atomic-research-centre-barc-stipendiary-trainee-category-i-scientific-ass-855
https://www.searchsarkarinaukri.com/jobs/maharashtra-public-service-commissionmpsc-motor-vehicle-prosecutor-regional-tran-847
https://www.searchsarkarinaukri.com/jobs/bhabha-atomic-research-centre-barc-technical-officerc-direct-recruitment-barc-mu-856
https://www.searchsarkarinaukri.com/jobs/unique-identification-authority-of-indiauidai-vacancy-circular-for-filling-up-po-835
https://www.searchsarkarinaukri.com/jobs/ntpc-limited-gdmo-medical-officer-ntpc-hospitals-at-various-project-sites-2026-875
https://www.searchsarkarinaukri.com/jobs/united-commercial-bank-uco-bank-details-for-recruitment-of-1050-probationary-off-282
https://www.searchsarkarinaukri.com/jobs/indian-railways-ir-general-manager-finance-india-2026-16
https://www.searchsarkarinaukri.com/jobs/indian-railways-ir-gm-te-ggm-te-india-2026-19
```

**Root Cause:**

These URLs were previously indexed with a slug that has since changed (slug was regenerated or updated). The IDs are still valid — the slug portion is outdated or truncated differently than the current slug.

**Required Action:**

For each URL, extract the Job ID from the suffix. Look up the current slug in the database. If the slug differs, implement a **301 redirect** from the old slug URL to the new slug URL. If the job no longer exists, return **HTTP 410**.

---

## Pattern 3 — SEO Slug URLs without Numeric ID (Truncated)

**Count: 9 URLs (1.5% of all 404s)**

**Format:**
```
/jobs/{truncated-slug}
```

These slugs are truncated (cut off) and do not match any full slug in the database.

**All affected URLs:**
```
https://www.searchsarkarinaukri.com/jobs/institute-of-banking-personnel-selectionibps-research-associate-facult
https://www.searchsarkarinaukri.com/jobs/sports-authority-of-india-sai-sai-internship-program-head-office-regio
https://www.searchsarkarinaukri.com/jobs/united-commercial-bank-uco-bank-details-for-recruitment-of-1050-probat
https://www.searchsarkarinaukri.com/jobs/united-commercial-bank-uco-bank-this-has-reference-to-our-earlier-recr
https://www.searchsarkarinaukri.com/jobs/united-commercial-bank-uco-bank-scribe-declaration-for-recruitment-of-
https://www.searchsarkarinaukri.com/jobs/sports-authority-of-india-sai-inviting-application-for-appointment-for
https://www.searchsarkarinaukri.com/jobs/united-commercial-bank-uco-bank-information-handout-for-recruitment-of
https://www.searchsarkarinaukri.com/jobs/united-commercial-bank-uco-bank-recruitment-of-probationary-officers-f
https://www.searchsarkarinaukri.com/jobs/united-commercial-bank-uco-bank-advt-no-hohrmrecr2025-26com-03-engagem
```

**Root Cause:**

Slugs were generated with a URL length limit that was later increased. Google previously indexed the shorter version. The current application generates longer slugs, so these short slugs no longer match any route.

**Required Action:**

Match each truncated slug to the correct full slug using a prefix search on the database. Implement a **301 redirect** from the truncated slug to the full correct URL. If no match is found, return **HTTP 410**.

---

## Pattern 4 — District Pages

**Count: 4 URLs (0.7% of all 404s)**

**Format:**
```
/districts/{district-slug}
```

**All affected URLs:**
```
https://www.searchsarkarinaukri.com/districts/new-delhi
https://www.searchsarkarinaukri.com/districts/all-districts
https://www.searchsarkarinaukri.com/districts/kanpur-nagar
https://www.searchsarkarinaukri.com/districts/mumbai
```

**Root Cause:**

District pages were previously accessible but may have been removed or the routing was changed. The `/districts/all-districts` URL appears to be a listing page that no longer exists.

**Required Action:**

Verify whether district pages exist in the current application routing. If they exist under a different URL structure, redirect. If they were removed, return **HTTP 410**.

---

## Pattern 5 — City / Location Pages

**Count: 11 URLs (1.8% of all 404s)**

**Format:**
```
/jobs-in-{city-slug}
```

**All affected URLs:**
```
https://www.searchsarkarinaukri.com/jobs-in-new-delhi
https://www.searchsarkarinaukri.com/jobs-in-akola
https://www.searchsarkarinaukri.com/jobs-in-mumbai-suburban
https://www.searchsarkarinaukri.com/jobs-in-palghar
https://www.searchsarkarinaukri.com/jobs-in-sangli
https://www.searchsarkarinaukri.com/jobs-in-kolhapur
https://www.searchsarkarinaukri.com/jobs-in-satara
https://www.searchsarkarinaukri.com/jobs-in-mumbai-city
https://www.searchsarkarinaukri.com/jobs-in-kanpur-nagar
https://www.searchsarkarinaukri.com/jobs-in-solapur
https://www.searchsarkarinaukri.com/jobs-in-chandrapur
```

**Root Cause:**

City-based job listing pages were previously generated and indexed by Google. These pages may have been removed, routing may have changed, or city slugs may have been renamed.

**Required Action:**

Verify if city pages exist in current routing. If they were moved to a different URL, redirect. If they were removed, return **HTTP 410**.

---

## Pattern 6 — Category Pages

**Count: 1 URL (0.2% of all 404s)**

**Format:**
```
/category/{category-slug}
```

**All affected URLs:**
```
https://www.searchsarkarinaukri.com/category/state-government-jobs
```

**Root Cause:**

This category page was previously indexed but no longer exists at this URL. The routing for category pages may have changed.

**Required Action:**

Verify if the State Government Jobs category exists under a different URL. If yes, redirect (301). If not, return HTTP 410.

---

# Investigation Checklist — Completed

| Item | Status |
|------|--------|
| Excel report opened | ✅ Done |
| All 607 URLs reviewed | ✅ Done |
| URL patterns identified | ✅ Done |
| URL groups counted | ✅ Done |
| Possible causes identified | ✅ Done |
| Classification prepared | ✅ Done |

---

# Summary of Findings

✅ **552 URLs** are Legacy Numeric Job URLs — the dominant issue

✅ **30 URLs** are old SEO slug URLs where the slug has changed

✅ **9 URLs** are truncated slug URLs that no longer match current routes

✅ **11 URLs** are City/Location pages that no longer exist

✅ **4 URLs** are District pages that no longer exist

✅ **1 URL** is a Category page that no longer exists at this path

---

# Root Cause Summary

The primary root cause is a **URL structure migration** from numeric-only job URLs (`/jobs/123`) to SEO-friendly slug URLs (`/jobs/org-name-title-123`). The redirect from old to new URLs was never implemented, causing Google to continue crawling and reporting 552+ old URLs as 404.

Secondary causes include:

- Slug regeneration changing existing job URLs
- URL truncation limits changing during development
- City, district, and category pages being removed without 410 or redirect

---

# Next Document

```
03_URL_Classification.md
```

This document classifies every URL into logical groups and determines the appropriate resolution strategy for each type before implementation begins.
