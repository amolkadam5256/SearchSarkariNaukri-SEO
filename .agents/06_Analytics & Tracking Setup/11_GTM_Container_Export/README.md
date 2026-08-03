# 11_GTM_Container_Export / README.md

> **Project:** SearchSarkariNaukri
>
> **Document:** GTM Container Export — Specification, Import & Release Notes
>
> **Scope:** This README documents *this specific export folder and file*. For the general export process, naming convention, and folder structure, see `../10_GTM_EXPORT_GUIDE.md`. For the source specification the container was generated from, see `../04_VARIABLES.md`, `../05_TRIGGERS.md`, `../06_TAGS.md`, `../07_EVENTS.md`, `../08_CONVERSIONS.md`.
>
> **Version:** 1.0

---

# 1. What This Folder Contains

```
SearchSarkariNaukri-GTM-v1.json
```

A real, structurally valid GTM container export (`exportFormatVersion: 2`) — not a placeholder. It was generated directly from the documented specification (Sections 4–8 of the numbered documents above) and contains actual `tag`, `trigger`, `variable`, `folder`, and `builtInVariable` arrays that GTM's Admin → Import Container flow can parse.

---

# 2. Container Specification (What's Inside)

| Object | Count | Notes |
|---|---|---|
| Folders | 20 | Matches the folder structure in `04_VARIABLES.md` §11, `05_TRIGGERS.md` §24, `06_TAGS.md` §25, `10_GTM_EXPORT_GUIDE.md` §4 |
| Variables | 61 | 4 Constants, 39 Data Layer Variables (Page/Job/Search/User/Consent), 5 URL Variables, 3 logic-based JS Variables, 4 Custom JavaScript Variables, 6 Auto-Event Variables |
| Built-in Variables | 10 | Click URL/Text/Classes/ID/Element, Page URL/Hostname/Path, Referrer, Event |
| Triggers | 27 | Initialization, 14 Custom Event triggers, 5 Scroll triggers, 3 Timer triggers, 2 error triggers, 2 status-code triggers |
| Tags | 29 | GA4 Configuration + 20 GA4 Event tags, 2 Consent Mode v2 tags, 1 Microsoft Clarity tag (paused), 1 Google Ads Conversion tag (paused), 1 Meta Pixel base tag (paused) |

**Container identifiers used in the export:**

| Field | Value |
|---|---|
| Public Container ID | `GTM-TC789H5W` |
| GA4 Measurement ID | `G-GGE1EC2V8F` |
| Account ID (placeholder) | `6012345678` |
| Internal Container ID (placeholder) | `98765432` |
| Container Version | `1` |

> The Account ID and internal Container ID are placeholders required by the export schema. GTM ignores them on import and re-maps every object to the destination container you import into — they do **not** need to match your real Anthropic/Google account.

---

# 3. Known Placeholders — Developer Action Required

These are intentionally left as placeholders because the source documentation does not yet specify real values for them. The container **imports and publishes successfully without touching these** — they only need attention when the corresponding platform is actually turned on:

| Tag | Placeholder | Status | Action Needed |
|---|---|---|---|
| `TAG - Clarity - Install` | `REPLACE_WITH_CLARITY_PROJECT_ID` | Paused | Get a Clarity Project ID, update the Custom HTML tag, unpause |
| `TAG - Google Ads - Conversion (Reserved)` | `REPLACE_WITH_ADS_CONVERSION_ID` / `REPLACE_WITH_ADS_CONVERSION_LABEL` | Paused | Create the conversion action in Google Ads, unpause |
| `TAG - Meta - Base Code (Reserved)` | `REPLACE_WITH_META_PIXEL_ID` | Paused | Get a Meta Pixel ID, replace the boilerplate `fbq` init code with Meta's actual current base code, unpause |
| `TAG - Consent - Google Consent Update` | Fires on `TR - Login` | Paused | This is a stand-in trigger only. Wire to your real CMP's consent-update event (e.g., `cmp_consent_update`) once a CMP is implemented — see `08_CONVERSIONS.md` §14 (Deduplication) and `02_TRACKING_REQUIREMENTS.md` §17 (Consent Requirements) |

Everything else (GA4 config, all 20 GA4 event tags, Consent Default, all variables/triggers/folders) is fully wired and ready to publish as-is.

---

# 4. Import Procedure (Quick Reference)

Full procedure with screenshots/checklist is in `../10_GTM_EXPORT_GUIDE.md` §11–§13. Summary:

1. GTM → your container → **Admin → Import Container**
2. Select `SearchSarkariNaukri-GTM-v1.json`
3. Choose workspace: create a **new empty workspace** for the first import (do not merge into a workspace with unrelated changes)
4. Import option: **Overwrite** (this is a full container build, not an incremental change — there is nothing to merge on first import)
5. Review the change summary — expect 20 folders / 61 variables / 27 triggers / 29 tags added, 0 removed
6. Confirm import
7. Open **Preview Mode** and validate against `../09_TESTING.md` before publishing

---

# 5. Import Validation Checklist

- [ ] Import completes with 0 errors
- [ ] Folder count = 20
- [ ] Variable count = 61
- [ ] Trigger count = 27
- [ ] Tag count = 29
- [ ] `TAG - GA4 - Configuration` fires on all pages in Preview
- [ ] `TAG - Consent - Google Consent Default` fires before `TAG - GA4 - Configuration` (Consent Mode v2 requirement — see `02_TRACKING_REQUIREMENTS.md` §17)
- [ ] No "variable not found" warnings in the GTM interface (would indicate a Data Layer key mismatch — cross-check against `03_DATALAYER_ARCHITECTURE.md`)
- [ ] Paused tags (Clarity, Google Ads, Meta) show as paused, not active
- [ ] GA4 DebugView receives `page_view` on load

---

# 6. Versioning

| Version | Date | Contents | Notes |
|---|---|---|---|
| v1 | Generated from spec Sections 4–8 | Initial production-ready container | Google Ads / Meta / Clarity tags present but paused pending platform IDs |

Every future change must:
- Increment the version (`v1` → `v2`, filename and `containerVersionId`)
- Be re-exported from the live GTM container (not hand-edited JSON) once the container has been imported and modified in the GTM UI
- Update this table with what changed and why

---

# 7. Release Checklist

Before publishing this container to production:

- [ ] Imported into a test/staging GTM workspace first
- [ ] Preview Mode validated on: Homepage, Job Listing, Job Detail, State, District, Department, Admit Card, Result, Search
- [ ] GA4 DebugView confirms all 20 events fire with correct parameters
- [ ] No duplicate event firing (see `09_TESTING.md` §21)
- [ ] No console/JavaScript errors introduced
- [ ] No Core Web Vitals regression (see `09_TESTING.md` §23)
- [ ] Consent Mode v2 defaults confirmed denied-by-default for `IN` region
- [ ] Developer, QA, and SEO sign-off completed per `01_PROJECT_OVERVIEW.md` §29–31
- [ ] Container published and a new GTM Version created (never overwrite Version 1 in place)

---

# 8. Related Documents

```
../01_PROJECT_OVERVIEW.md
../02_TRACKING_REQUIREMENTS.md
../03_DATALAYER_ARCHITECTURE.md
../04_VARIABLES.md
../05_TRIGGERS.md
../06_TAGS.md
../07_EVENTS.md
../08_CONVERSIONS.md
../09_TESTING.md
../10_GTM_EXPORT_GUIDE.md
```
