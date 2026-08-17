# 03 - URL Classification

**Project:** SearchSarkariNaukri.com

**Module:** URL Classification for Google Search Console 404 URLs

**Priority:** 🔴 Critical

**Status:** ✅ Classification Complete — 2026-08-05

---

# Purpose

This document classifies every URL from the Google Search Console 404 report into exactly one category.

Classification is based on the actual analysis of the Excel export file containing **607 URLs**.

This document is only for classification.

Implementation is handled in later documents.

---

# Reference File

Google Search Console Export

```
https___www.searchsarkarinaukri.com_-Coverage-Drilldown-2026-08-05.xlsx
```

All **607 URLs** from the report have been classified.

---

# Classification Results Summary

| Category  | Type                                  | Count   |
| --------- | ------------------------------------- | ------- |
| B         | Legacy Numeric Job URLs               | **552** |
| C         | SEO Slug URLs (with ID, slug changed) | **30**  |
| C         | SEO Slug URLs (no ID, slug truncated) | **9**   |
| G         | District Pages                        | **4**   |
| H         | City / Location Pages                 | **11**  |
| E         | Category Pages                        | **1**   |
| **TOTAL** |                                       | **607** |

---

# Category B — Legacy Numeric Job URLs

**Count: 552 URLs**

**Priority: 🔴 Critical**

**Description:**

These are old-format numeric-only job URLs from before the website migrated to SEO-friendly slug URLs.

**Pattern:**

```
/jobs/{number}
```

**Examples:**

```
/jobs/858
/jobs/983
/jobs/1104
/jobs/2223
```

**ID Range:** 14 to 2223

**Root Cause:**

URL structure was changed from `/jobs/{id}` to `/jobs/{slug}-{id}`. The old numeric URLs were never redirected. Google had indexed these URLs before the migration.

**Required Action:**

For each numeric ID, query the database:

- If the job exists → 301 redirect to current slug URL
- If the job does not exist → HTTP 410

**Investigation Required:** ✅ Database lookup needed per ID

---

**Full list of all 552 affected numeric IDs:**

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

# Category C — SEO Slug URLs (Slug Changed / Old Slug with ID)

**Count: 30 URLs**

**Priority: 🔴 Critical**

**Description:**

These are job URLs where the slug was previously indexed with one format, and the current slug in the database is different (usually shorter/longer or reformatted). The numeric ID at the end is still valid and can be used to find the correct current URL.

**Pattern:**

```
/jobs/{old-slug}-{id}
```

**Root Cause:**

Slug was regenerated when the job title or formatting rules changed. The ID remains the same but the slug part has changed.

**Required Action:**

Extract the numeric ID from the end of each URL. Query the database for the current slug for that job ID. Implement a **301 redirect** from the old slug URL to the current slug URL.

**All 30 affected URLs:**

```
/jobs/institute-of-banking-personnel-selectionibps-research-associate-faculty-technica-858
/jobs/sports-authority-of-india-sai-assistant-director-deputation-basis-all-india-2026-863
/jobs/sports-authority-of-india-sai-sai-internship-program-head-office-regional-center-862
/jobs/united-commercial-bank-uco-bank-scribe-declaration-for-recruitment-of-specialist-253
/jobs/edcil-india-limited-hiring-of-ai-advisor-2026-317
/jobs/national-career-servicencs-company-national-health-systems-resource-centre-delhi-839
/jobs/united-commercial-bank-uco-bank-recruitment-of-probationary-officers-for-written-276
/jobs/staff-selection-commission-ssc-junior-engineer-civil-mechanical-electrical-exami-860
/jobs/united-commercial-bank-uco-bank-information-handout-for-recruitment-of-specialis-252
/jobs/-aurangabad-cantonment-board-2026-895
/jobs/nielit-delhi-centre-stqc-drivers-recruitment-2026-advertisement-number-nielitndl-313
/jobs/edcil-india-limited-hiring-of-ai-advisor-2026   [ID: 2026 — Note: ID matches year, needs manual check]
/jobs/bhabha-atomic-research-centre-barc-research-associate-ra-physicschemistrylife-sc-857
/jobs/-currency-note-press-nashik-nashik-maharashtra-2026-887
/jobs/indian-railways-ir-gm-st-india-2026-18
/jobs/unique-identification-authority-of-indiauidai-extended-vacancy-circular-for-the-832
/jobs/oil-and-natural-gas-corporation-limited-ongc-trade-apprentice-diploma-apprentice-880
/jobs/united-commercial-bank-uco-bank-advt-no-hohrmrecr2025-26com-03-engagement-of-app-226
/jobs/bhabha-atomic-research-centre-barc-ocesdgfs-2026-scientific-officer-c-mumbai-kal-854
/jobs/indian-railways-ir-deputy-general-manager-civil-india-2026-25
/jobs/sports-authority-of-india-sai-inviting-application-for-appointment-for-medical-o-304
/jobs/-staff-selection-commission-mts-all-india-2026-898
/jobs/bhabha-atomic-research-centre-barc-stipendiary-trainee-category-i-scientific-ass-855
/jobs/maharashtra-public-service-commissionmpsc-motor-vehicle-prosecutor-regional-tran-847
/jobs/bhabha-atomic-research-centre-barc-technical-officerc-direct-recruitment-barc-mu-856
/jobs/unique-identification-authority-of-indiauidai-vacancy-circular-for-filling-up-po-835
/jobs/ntpc-limited-gdmo-medical-officer-ntpc-hospitals-at-various-project-sites-2026-875
/jobs/united-commercial-bank-uco-bank-details-for-recruitment-of-1050-probationary-off-282
/jobs/indian-railways-ir-general-manager-finance-india-2026-16
/jobs/indian-railways-ir-gm-te-ggm-te-india-2026-19
```

**Notable Organizations:**

- IBPS (Institute of Banking Personnel Selection)
- SAI (Sports Authority of India)
- UCO Bank (United Commercial Bank)
- BARC (Bhabha Atomic Research Centre)
- Indian Railways
- UIDAI (Unique Identification Authority of India)
- SSC (Staff Selection Commission)
- NTPC, ONGC, EDCIL, NIELIT, MPSC

---

# Category C — SEO Slug URLs (Truncated — No ID)

**Count: 9 URLs**

**Priority:** 🟡 High

**Description:**

These are job URLs where the slug was truncated (cut short). The URL does not contain a numeric ID at the end and does not match any current route. These appear to be from an earlier period when the slug generation had a character limit that was later increased.

**Pattern:**

```
/jobs/{truncated-slug-without-id}
```

**Root Cause:**

Previous slug generation had a character limit. The slug was cut before the numeric ID suffix could be appended. The current application generates longer slugs with IDs, so these truncated paths are no longer recognized.

**Required Action:**

Attempt a database prefix search on each truncated slug to find the matching job. If a match is found, implement a **301 redirect** to the correct full slug URL. If no match is found, return **HTTP 410**.

**All 9 affected URLs:**

```
/jobs/institute-of-banking-personnel-selectionibps-research-associate-facult
/jobs/sports-authority-of-india-sai-sai-internship-program-head-office-regio
/jobs/united-commercial-bank-uco-bank-details-for-recruitment-of-1050-probat
/jobs/united-commercial-bank-uco-bank-this-has-reference-to-our-earlier-recr
/jobs/united-commercial-bank-uco-bank-scribe-declaration-for-recruitment-of-
/jobs/sports-authority-of-india-sai-inviting-application-for-appointment-for
/jobs/united-commercial-bank-uco-bank-information-handout-for-recruitment-of
/jobs/united-commercial-bank-uco-bank-recruitment-of-probationary-officers-f
/jobs/united-commercial-bank-uco-bank-advt-no-hohrmrecr2025-26com-03-engagem
```

**Notable Organizations:**

- IBPS
- SAI
- UCO Bank

---

# Category G — District Pages

**Count: 4 URLs**

**Priority:** 🟡 High

**Description:**

District-level job listing pages that were previously indexed by Google. These pages no longer exist or the routing has changed.

**Pattern:**

```
/districts/{district-slug}
```

**All 4 affected URLs:**

```
/districts/new-delhi
/districts/all-districts
/districts/kanpur-nagar
/districts/mumbai
```

**Notes:**

- `/districts/all-districts` appears to be a listing of all districts — may have been removed
- The other 3 are specific district pages

**Required Action:**

Verify whether the district routing exists in the current application. If district pages exist under a different URL structure, implement a **301 redirect**. If the feature was removed entirely, return **HTTP 410**.

---

# Category H — City / Location Pages

**Count: 11 URLs**

**Priority:** 🟡 High

**Description:**

City-based job listing pages in the format `/jobs-in-{city}`. These were previously crawled and indexed by Google but are now returning 404.

**Pattern:**

```
/jobs-in-{city-slug}
```

**All 11 affected URLs:**

```
/jobs-in-new-delhi
/jobs-in-akola
/jobs-in-mumbai-suburban
/jobs-in-palghar
/jobs-in-sangli
/jobs-in-kolhapur
/jobs-in-satara
/jobs-in-mumbai-city
/jobs-in-kanpur-nagar
/jobs-in-solapur
/jobs-in-chandrapur
```

**Cities affected:**

- Maharashtra: Akola, Mumbai Suburban, Palghar, Sangli, Kolhapur, Satara, Mumbai City, Solapur, Chandrapur
- Delhi: New Delhi
- Uttar Pradesh: Kanpur Nagar

**Required Action:**

Verify if the `/jobs-in-{city}` routing exists in the current application. If city pages were moved to `/districts/{slug}` or another pattern, implement a **301 redirect**. If city pages were removed, return **HTTP 410**.

---

# Category E — Category Pages

**Count: 1 URL**

**Priority:** 🟡 High

**Description:**

A category listing page that was previously indexed.

**Pattern:**

```
/category/{category-slug}
```

**Affected URL:**

```
/category/state-government-jobs
```

**Required Action:**

Check if State Government Jobs category exists under a different URL (e.g., `/categories/state-government-jobs` or similar). If yes, redirect (301). If the category was removed, return HTTP 410.

---

# Classification Checklist

| Item                            | Status                |
| ------------------------------- | --------------------- |
| All 607 URLs reviewed           | ✅ Done               |
| Every URL assigned a category   | ✅ Done               |
| No URL in multiple categories   | ✅ Done               |
| Priority assigned to each group | ✅ Done               |
| Investigation notes documented  | ✅ Done               |
| Unknown URLs                    | None — all classified |

---

# Classification Summary Table

| Category    | Type                | Count   | Priority    | Action                    |
| ----------- | ------------------- | ------- | ----------- | ------------------------- |
| B           | Legacy Numeric URLs | 552     | 🔴 Critical | 301 or 410 per ID         |
| C (with ID) | Old Slug with ID    | 30      | 🔴 Critical | 301 to new slug           |
| C (no ID)   | Truncated Slug      | 9       | 🟡 High     | Prefix match → 301 or 410 |
| G           | District Pages      | 4       | 🟡 High     | 301 or 410                |
| H           | City Pages          | 11      | 🟡 High     | 301 or 410                |
| E           | Category Pages      | 1       | 🟡 High     | 301 or 410                |
| **TOTAL**   |                     | **607** |             |                           |

---

# Success Criteria

The classification stage is complete when:

- ✅ All 607 URLs have been reviewed.
- ✅ Every URL has exactly one category.
- ✅ No unknown URLs remain.
- ✅ No implementation has been performed.
- ✅ The team is ready to begin Database Verification.

---

# Next Document

```
04_Database_Verification.md
```

Purpose:

Verify whether each classified URL still exists in the database and determine whether it should be restored, redirected, or permanently removed.
