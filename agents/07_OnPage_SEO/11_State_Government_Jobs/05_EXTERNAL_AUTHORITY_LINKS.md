# 05 — External Authority Link Plan: Official State Public Service Commissions

**Target Section:** Section 12 — Official State PSC / Recruitment Websites Directory  
**Purpose:** Establish authentic external E-E-A-T signals by connecting candidates directly to constitutional recruiting bodies across India, strictly labeled as **Official Website**.

---

## 1. Developer Implementation Rules

1. **Strictly Official Domains:** Link exclusively to verified government domains (`.gov.in`, `.nic.in`, or designated state portals). Never link to unofficial third-party job blogs or aggregators.
2. **Explicit Labeling:** Every external link text or attribute must be clearly labeled as **"Official Website"** or **"Official Portal"**.
3. **Security Attributes:** Whenever `target="_blank"` is employed, developers must include `rel="noopener noreferrer"`.
4. **No Unwarranted `nofollow`:** As verified state constitutional bodies, these external links demonstrate legitimate factual citation and should remain standard follow links or editorial citations without artificial manipulation.
5. **Responsive Table / Mobile UX:** The table must either scroll horizontally with smooth touch scrolling (`overflow-x: auto; -webkit-overflow-scrolling: touch;`) or transform into accessible card components on mobile screens below 768px.

---

## 2. Master Directory of 28 State Public Service Commissions

| # | State | Commission Name | Acronym | Official Verified URL | SearchSarkariNaukri Internal Hub |
|---|---|---|---|---|---|
| 1 | **Andhra Pradesh** | Andhra Pradesh Public Service Commission | APPSC | `https://psc.ap.gov.in` | `/jobs-in-andhra-pradesh` |
| 2 | **Arunachal Pradesh** | Arunachal Pradesh Public Service Commission | APPSC | `https://appsc.gov.in` | `/jobs-in-arunachal-pradesh` |
| 3 | **Assam** | Assam Public Service Commission | APSC | `https://apsc.nic.in` | `/jobs-in-assam` |
| 4 | **Bihar** | Bihar Public Service Commission | BPSC | `https://bpsc.bihar.gov.in` | `/jobs-in-bihar` |
| 5 | **Chhattisgarh** | Chhattisgarh Public Service Commission | CGPSC | `https://psc.cg.gov.in` | `/jobs-in-chhattisgarh` |
| 6 | **Goa** | Goa Public Service Commission | GPSC | `https://gpsc.goa.gov.in` | `/jobs-in-goa` |
| 7 | **Gujarat** | Gujarat Public Service Commission | GPSC | `https://gpsc.gujarat.gov.in` | `/jobs-in-gujarat` |
| 8 | **Haryana** | Haryana Public Service Commission | HPSC | `https://hpsc.gov.in` | `/jobs-in-haryana` |
| 9 | **Himachal Pradesh** | Himachal Pradesh Public Service Commission | HPPSC | `https://hppsc.hp.gov.in` | `/jobs-in-himachal-pradesh` |
| 10 | **Jharkhand** | Jharkhand Public Service Commission | JPSC | `https://www.jpsc.gov.in` | `/jobs-in-jharkhand` |
| 11 | **Karnataka** | Karnataka Public Service Commission | KPSC | `https://kpsc.kar.nic.in` | `/jobs-in-karnataka` |
| 12 | **Kerala** | Kerala Public Service Commission | KPSC | `https://www.keralapsc.gov.in` | `/jobs-in-kerala` |
| 13 | **Madhya Pradesh** | Madhya Pradesh Public Service Commission | MPPSC | `https://mppsc.mp.gov.in` | `/jobs-in-madhya-pradesh` |
| 14 | **Maharashtra** | Maharashtra Public Service Commission | MPSC | `https://mpsc.gov.in` | `/jobs-in-maharashtra` |
| 15 | **Manipur** | Manipur Public Service Commission | MPSC | `https://mpscmanipur.gov.in` | `/jobs-in-manipur` |
| 16 | **Meghalaya** | Meghalaya Public Service Commission | MPSC | `https://mpsc.meghalaya.gov.in` | `/jobs-in-meghalaya` |
| 17 | **Mizoram** | Mizoram Public Service Commission | MPSC | `https://mpsc.mizoram.gov.in` | `/jobs-in-mizoram` |
| 18 | **Nagaland** | Nagaland Public Service Commission | NPSC | `https://npsc.nagaland.gov.in` | `/jobs-in-nagaland` |
| 19 | **Odisha** | Odisha Public Service Commission | OPSC | `https://www.opsc.gov.in` | `/jobs-in-odisha` |
| 20 | **Punjab** | Punjab Public Service Commission | PPSC | `https://www.ppsc.gov.in` | `/jobs-in-punjab` |
| 21 | **Rajasthan** | Rajasthan Public Service Commission | RPSC | `https://rpsc.rajasthan.gov.in` | `/jobs-in-rajasthan` |
| 22 | **Sikkim** | Sikkim Public Service Commission | SPSC | `https://spsc.sikkim.gov.in` | `/jobs-in-sikkim` |
| 23 | **Tamil Nadu** | Tamil Nadu Public Service Commission | TNPSC | `https://www.tnpsc.gov.in` | `/jobs-in-tamil-nadu` |
| 24 | **Telangana** | Telangana Public Service Commission | TGPSC | `https://www.tgpsc.gov.in` | `/jobs-in-telangana` |
| 25 | **Tripura** | Tripura Public Service Commission | TPSC | `https://tpsc.tripura.gov.in` | `/jobs-in-tripura` |
| 26 | **Uttar Pradesh** | Uttar Pradesh Public Service Commission | UPPSC | `https://uppsc.up.nic.in` | `/jobs-in-uttar-pradesh` |
| 27 | **Uttarakhand** | Uttarakhand Public Service Commission | UKPSC | `https://psc.uk.gov.in` | `/jobs-in-uttaranchal` |
| 28 | **West Bengal** | West Bengal Public Service Commission | WBPSC | `https://psc.wb.gov.in` | `/jobs-in-west-bengal` |

---

## 3. National Central Authorities for Comparison Context

When contextual comparisons are drawn in Section 5 (Central vs State Jobs), developers may reference these national official sources:

| Authority | Mandate | Official URL | Contextual Usage |
|---|---|---|---|
| **Union Public Service Commission (UPSC)** | Central Civil & Defence Services | `https://www.upsc.gov.in` | Section 5 (Comparison) |
| **Staff Selection Commission (SSC)** | Central Non-Gazetted Staffing | `https://ssc.gov.in` | Section 5 (Comparison) |
| **National Career Service (NCS)** | Ministry of Labour & Employment Portal | `https://www.ncs.gov.in` | Section 16 (Alerts & verification) |
| **Employment News (Rozgar Samachar)** | Ministry of Information & Broadcasting | `https://employmentnews.gov.in` | Section 17 (Verification standards) |

---

## 4. Maintenance and Link Health Protocol

- Run a quarterly link-health scan across all 28 PSC domains.
- If a state portal migrates to a newer state NIC subdomain (e.g., TSPSC migrating to TGPSC), update the target URL immediately while preserving commission nomenclature.
