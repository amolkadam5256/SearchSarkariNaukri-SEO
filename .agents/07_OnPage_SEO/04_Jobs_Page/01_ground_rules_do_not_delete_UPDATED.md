# 01 — Ground Rules: Additive-Only SEO Implementation

These rules apply to **every file in this set (01–11)** and override anything below if there is ever a conflict. Read this file first. Give this file to any developer or AI coding agent before they touch the project.

## Non-negotiable constraints

1. **Do not delete any existing file, folder, component, route, or config.**
2. **Do not rename or move any existing file or folder.**
3. **Do not remove any existing section, filter, card, button, or UI element** on `/jobs` or any other page.
4. **Do not change the existing visual design, layout, colors, fonts, or component structure.** No UI redesign — this is a content/SEO layer, not a visual refresh.
5. **Do not change existing URLs.** Existing indexed URLs (job pages, district pages, category pages) must keep working exactly as they do today. New URLs are *added*, not substituted.
6. **Do not remove or overwrite existing meta tags, schema, or copy** — only add new fields/sections or *extend* existing ones (e.g., adding a canonical tag where none exists is fine; replacing an existing working canonical is not, unless it is factually wrong).
7. **Every change should be reviewable as a diff that only adds lines**, with the rare exception of fixing a genuine bug (e.g., a broken canonical pointing to the wrong page) — and even then, flag it separately instead of bundling it silently into a content update.

## What "additive" means in practice

| Allowed | Not allowed |
|---|---|
| Append a new `<section>` below the existing job grid | Remove or reorder the existing job grid |
| Add a new `<h2>` block for FAQs at the bottom of the page | Change the existing `<h1>` copy without approval (see file 02 for the one approved H1 change) |
| Add new JSON-LD `<script type="application/ld+json">` blocks | Delete or replace an existing schema block that already works |
| Create new routes like `/qualification/12th-pass-government-jobs` | Delete or 301 away from any URL currently receiving traffic |
| Add new internal links in the footer/nav | Remove existing nav items |
| Add new sitemap files referenced from the sitemap index | Delete or truncate the existing `sitemap.xml` |
| Add a `Last Updated` / `Status: Open` badge to a job card | Remove any existing field from a job card |

## How to use files 02–11

Each file is a self-contained work order for one part of the site. They are numbered in a safe implementation sequence (see file 11 for the master checklist), but each can be handed to a developer independently. Every file repeats the "additive only" instruction at the top so it survives being copy-pasted out of context.

## Approved exceptions — where a controlled edit is allowed

Two categories of non-additive change are explicitly approved. Everything else in files 02–12 is a **pure addition**: new sections, new pages, new schema, new links, new sitemap entries.

### Category 1 — Two specific copy changes

- The `/jobs` page `<title>` tag and meta description (currently homepage-oriented — see file 02).
- The `/jobs` page `<h1>` text (from "All Active Government Jobs" to "Latest Government Jobs 2026 – Sarkari Naukri" — see file 02).

### Category 2 — Demonstrably incorrect existing SEO implementations

The additive-only rule is meant to prevent *unnecessary* restructuring and content churn — it is not meant to force the site to keep a **genuinely broken** SEO element in place. Editing is allowed when an existing element is **factually wrong or actively harmful**, for example:

- A canonical tag pointing to the wrong URL (e.g. a job page canonicalizing to the homepage by mistake).
- A `noindex` directive left on a page that should be indexable (e.g. leftover from staging).
- Structured data with fabricated, expired, or clearly incorrect field values (a fake `validThrough` date, a hardcoded `employmentType` that doesn't match the notification).
- A sitemap listing dead/redirected/`noindex` URLs.
- A robots.txt rule accidentally blocking an important section of the site.

**Conditions for using this exception:**

1. The issue must be demonstrably incorrect, not a stylistic preference or a "could be better" judgment call.
2. The fix must be isolated in its own commit/PR, labeled `fix:`, and called out explicitly in the change description — never silently folded into a `feat:` content addition.
3. When in doubt about whether something qualifies, treat it as informational and flag it for review rather than editing it unilaterally.

This exception is what lets files 02, 05, 06, 08, and 12 correctly instruct fixes to things like pagination canonicals, hardcoded schema fields, and sitemap/noindex errors, without contradicting the no-deletion/no-restructure rule.


## 14. React Project Audit → Implementation Plan → Execution Gate

Before implementing **any** instruction from Files 01–12, the developer or AI coding agent must first inspect the actual project as a **React application** and read/reconcile **all 12 SEO files (01–12) together**.

### Required order — do not skip or combine these stages

1. **Read and understand Files 01–12 completely**
   - Treat File 01 as the governing constraint.
   - Treat File 12 as the final execution/sign-off document.
   - Check every file for dependencies, overlaps, approved exceptions, and implementation order.
   - Do not implement a later-file instruction in isolation if it depends on an earlier file.

2. **Audit the actual React project before making changes**
   - Identify the React framework/build setup (for example React Router, Next.js, Vite, CRA, or another React-based setup).
   - Identify the existing `/jobs` route and its actual component/page implementation.
   - Identify how jobs are fetched from the API/data source.
   - Identify the existing SSR/SSG/prerender capability, if any.
   - Identify routing, metadata/head handling, canonical handling, robots handling, sitemap generation, JSON-LD/schema implementation, pagination, filters, and shared layouts/components.
   - Identify the existing job detail template and all relevant category, qualification, district, recruiter, exam, result, admit-card, and blog templates.
   - Identify any existing SEO components/utilities so new work can extend them instead of creating competing implementations.
   - Inspect the current project before deciding how any instruction should be implemented.

3. **Create a plain implementation plan before coding**
   - Produce a clear file-by-file and component-by-component implementation plan based on the **actual React project structure**, not assumptions.
   - Map each requirement from Files 01–12 to the exact route, component, utility, server layer, API/data layer, or configuration that will be changed.
   - Clearly identify:
     - additions
     - approved edits
     - genuine technical fixes requiring a separate `fix:` change
     - files/components that must remain untouched
     - dependencies between changes
     - validation required after each phase
   - If any instruction from Files 01–12 conflicts with the actual project architecture, **stop and flag the conflict before coding**. Do not invent a workaround silently.

4. **Review the implementation plan before execution**
   - Confirm that the plan preserves the additive-only rules in this file.
   - Confirm that no existing route, URL, UI section, filter, card, component, or design will be removed or restructured.
   - Confirm that React interactivity will remain intact.
   - Confirm that SSR/SSG/prerendering, if required, will be implemented in a way compatible with the existing React architecture rather than replacing the application.
   - Confirm that existing SEO/schema implementations will be audited before adding duplicates.
   - Confirm that the plan follows the implementation sequence in File 11 and the full-site audit/execution gate in File 12.

5. **Only after the plan is reviewed, begin implementation**
   - Execute the approved plan in the sequence defined by Files 11–12.
   - Do not make unplanned architectural changes during implementation.
   - If a new technical issue is discovered, pause that part of the implementation, document the issue, and classify it as either:
     - an approved additive change,
     - a demonstrably incorrect existing implementation requiring an isolated `fix:` change, or
     - a new decision requiring review.
   - Do not silently expand the scope.

6. **Validate after implementation**
   - Run the project's normal build/type-check/test/lint process where applicable.
   - Verify the changed React routes still render and hydrate correctly.
   - Verify existing search, filters, sorting, pagination, cards, buttons, and other interactions still work.
   - Verify the rendered HTML contains the intended SEO content.
   - Follow the Google URL Inspection, Rich Results Test, sitemap, canonical, robots, and indexing validation requirements in Files 02–12.
   - Review the final diff and confirm it is additive except for explicitly approved or separately labeled `fix:` changes.

### Mandatory rule

**Do not start coding immediately after reading the SEO files. First audit the actual React project, then create the implementation plan, then review that plan against Files 01–12, and only then execute the implementation.**

This point is a mandatory **implementation gate** and does not replace or weaken any existing rule in this file.
