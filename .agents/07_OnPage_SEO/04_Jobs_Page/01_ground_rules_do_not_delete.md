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

## One explicitly approved exception

The only two copy changes flagged as *recommended edits* (not pure additions) across this whole doc set are:

- The `/jobs` page `<title>` tag and meta description (currently homepage-oriented — see file 02).
- The `/jobs` page `<h1>` text (from "All Active Government Jobs" to "Latest Government Jobs 2026 – Sarkari Naukri" — see file 02).

Everything else in files 02–11 is a **pure addition**: new sections, new pages, new schema, new links, new sitemap entries. If anything in another file reads like it requires deleting or restructuring something, stop and treat it as informational context only, not an instruction to act on.
