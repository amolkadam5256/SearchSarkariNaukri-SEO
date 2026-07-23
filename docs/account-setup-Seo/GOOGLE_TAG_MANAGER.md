# Google Tag Manager (GTM)

Project

SearchSarkariNaukri

---

# Overview

Google Tag Manager centralizes all marketing, analytics, and conversion tracking for the website.

Instead of installing multiple scripts individually, all tracking is managed from GTM.

---

# Container Information

| Item           | Value                               |
| -------------- | ----------------------------------- |
| Account        | searchsarkarinaukri                 |
| Website        | https://www.searchsarkarinaukri.com |
| Container Name | www.searchsarkarinaukri.com         |
| Container ID   | GTM-TC789H5W                        |
| Environment    | Production                          |
| Status         | Active                              |

---

# Folder Structure

docs/

accounts/

google/

GOOGLE_TAG_MANAGER.md

exports/

gtm/

gtm-production-import.json

gtm-production.json

README.md

---

# Export Files

Primary exports

../../exports/gtm/gtm-production-import.json

../../exports/gtm/gtm-production.json

These files contain the complete enterprise GTM configuration.

Never edit manually.

Always export after publishing.

---

# Importing Container

Open

Google Tag Manager

Container

Import Container

Select

gtm-production-import.json

Choose Workspace

Default Workspace

Import Mode

Merge

Recommended

Overwrite

Only for new empty containers

Click

Confirm

Review Changes

Submit

Publish

---

# Installation

Container ID

GTM-TC789H5W

---

## Head

Paste immediately inside

<head>

```html
<!-- Google Tag Manager -->

<script>
  (function (w, d, s, l, i) {
    w[l] = w[l] || [];

    w[l].push({
      "gtm.start": new Date().getTime(),

      event: "gtm.js",
    });

    var f = d.getElementsByTagName(s)[0],
      j = d.createElement(s),
      dl = l != "dataLayer" ? "&l=" + l : "";

    j.async = true;

    j.src = "https://www.googletagmanager.com/gtm.js?id=" + i + dl;

    f.parentNode.insertBefore(j, f);
  })(window, document, "script", "dataLayer", "GTM-TC789H5W");
</script>

<!-- End Google Tag Manager -->
```

---

## Body

Immediately after

<body>

```html
<!-- Google Tag Manager (noscript) -->

<noscript>
  <iframe
    src="https://www.googletagmanager.com/ns.html?id=GTM-TC789H5W"
    height="0"
    width="0"
    style="display:none;visibility:hidden"
  >
  </iframe>
</noscript>

<!-- End Google Tag Manager -->
```

---

# Next.js

App Router

app/layout.tsx

Head

Insert GTM Script

Body

Insert noscript iframe

Deploy

---

# Container Contents

This container includes

Google Analytics 4

Google Ads

Meta Pixel

LinkedIn Insight

Microsoft Clarity

Custom Events

Conversions

Remarketing

Data Layer

Scroll Tracking

Form Tracking

Search Tracking

Video Tracking

Error Tracking

Outbound Links

Downloads

---

# Built-in Variables

Enable

Page URL

Page Path

Hostname

Referrer

Click Classes

Click ID

Click URL

Click Text

Form Classes

Form ID

Scroll Depth

Video Status

Video Percent

Error Message

Error URL

---

# Data Layer Variables

Examples

page_location

page_title

page_path

content_name

content_category

content_type

cta_text

destination

goal

service

search_term

search_string

form_type

form_name

form_location

lead_type

platform

currency

value

error_type

status_code

method

---

# Events

page_view

job_view

job_search

job_apply

login

register

newsletter_signup

whatsapp_click

phone_call

contact_click

cta_click

scroll_depth

video_progress

file_download

search

filter

share

bookmark

error

api_error

---

# Triggers

Page View

DOM Ready

Window Loaded

All Pages

History Change

Element Visibility

Scroll Depth

Timer

Click

Form Submission

Custom Event

YouTube

---

# Tags

GA4 Configuration

GA4 Events

Meta Pixel

Google Ads

Remarketing

LinkedIn Insight

Microsoft Clarity

Custom HTML

Consent Mode

---

# Publishing Workflow

Workspace

↓

Preview

↓

Fix Errors

↓

Submit

↓

Version Name

↓

Publish

↓

Export JSON

↓

Commit to Git

---

# Naming Convention

Tags

GA4 -

META -

ADS -

LINKEDIN -

MS -

Variables

DLV -

CONST -

JS -

URL -

Triggers

EV -

PV -

CLK -

FORM -

SCROLL -

Folders

Analytics

Advertising

Conversions

SEO

Testing

---

# Versioning

Every Publish

Export JSON

Store

exports/gtm/

Example

v1

v2

v3

v4

Never overwrite old versions.

---

# Preview Testing

Preview

↓

Connect Website

↓

Verify

Tags Fired

Variables

Data Layer

Network Requests

Console Errors

---

# Production Checklist

☐ GTM Installed

☐ Container Imported

☐ Preview Passed

☐ Tags Fired

☐ GA4 Working

☐ Meta Pixel Working

☐ Ads Working

☐ Clarity Working

☐ Events Working

☐ Publish Complete

☐ Export Saved

☐ Git Commit

---

# Maintenance

Weekly

Review

Failed Tags

Errors

Preview

Monthly

Clean Variables

Remove Old Tags

Optimize Triggers

Backup Container

Export JSON

---

# Related Files

GOOGLE_ANALYTICS.md

GOOGLE_SEARCH_CONSOLE.md

GOOGLE_ADS.md

LOOKER_STUDIO.md

BIGQUERY.md

exports/gtm/README.md

exports/gtm/gtm-production-import.json

exports/gtm/gtm-production.json
