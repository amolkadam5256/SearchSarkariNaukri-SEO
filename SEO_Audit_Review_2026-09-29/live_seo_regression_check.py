#!/usr/bin/env python3
"""
Live SEO regression checks for SearchSarkariNaukri (no deletes — verify only).
Run: python live_seo_regression_check.py
"""
from __future__ import annotations

import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

BASE = "https://www.searchsarkarinaukri.com"
UA = "SearchSarkariNaukri-SEO-Regression/1.0"

# Sample jobs: (path_suffix, substring that should appear in HTML body)
# Use job IDs whose slug and body match (5015/5020 are NHSRCL/ESIC — not Canara).
JOB_SAMPLES = [
    (
        "/jobs/canara-bank-graduate-apprentice-recruitment-2026-apply-online-for-3500-posts--6681",
        "Canara",
    ),
    (
        "/jobs/canara-bank-graduate-apprentice-recruitment-2026-west-bengal-apply-online-for-150-posts--6682",
        "Canara",
    ),
]


def fetch(url: str, method: str = "GET") -> tuple[int, str, dict]:
    req = urllib.request.Request(
        url, headers={"User-Agent": UA}, method=method
    )
    try:
        with urllib.request.urlopen(req, timeout=25) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            return resp.status, body, dict(resp.headers)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace") if e.fp else ""
        return e.code, body, dict(e.headers) if e.headers else {}


def check_sitemap_index() -> list[str]:
    errors: list[str] = []
    status, body, _ = fetch(f"{BASE}/sitemap.xml")
    if status != 200:
        errors.append(f"CRITICAL: sitemap.xml HTTP {status} (expected 200)")
        return errors
    try:
        root = ET.fromstring(body)
    except ET.ParseError as e:
        errors.append(f"CRITICAL: sitemap.xml not valid XML: {e}")
        return errors
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locs = root.findall(".//sm:loc", ns) or root.findall(".//loc")
    if not locs:
        errors.append("CRITICAL: sitemap index has no <loc> entries")
        return errors
    for loc in locs[:15]:
        child = (loc.text or "").strip()
        if not child:
            continue
        st, _, _ = fetch(child, method="HEAD")
        if st != 200:
            # HEAD may fail; try GET
            st, _, _ = fetch(child)
        if st != 200:
            errors.append(f"CRITICAL: child sitemap {child} HTTP {st}")
    return errors


def check_robots() -> list[str]:
    errors: list[str] = []
    status, body, _ = fetch(f"{BASE}/robots.txt")
    if status != 200:
        errors.append(f"HIGH: robots.txt HTTP {status}")
        return errors
    if "Sitemap:" not in body:
        errors.append("HIGH: robots.txt missing Sitemap directive")
    return errors


def check_homepage() -> list[str]:
    errors: list[str] = []
    status, body, _ = fetch(f"{BASE}/")
    if status != 200:
        errors.append(f"CRITICAL: homepage HTTP {status}")
        return errors
    if "Sarkari Naukri" not in body and "Government Jobs" not in body:
        errors.append("HIGH: homepage missing expected primary heading text")
    return errors


def check_job_slug_parity() -> list[str]:
    errors: list[str] = []
    for path, needle in JOB_SAMPLES:
        status, body, _ = fetch(f"{BASE}{path}")
        if status != 200:
            errors.append(f"CRITICAL: {path} HTTP {status}")
            continue
        if needle.lower() not in body.lower():
            errors.append(
                f"CRITICAL: slug/content mismatch on {path} — "
                f"expected '{needle}' in visible HTML (wrong job or cache bug)"
            )
        if "application deadline has passed" in body.lower() and "canara" not in body.lower():
            errors.append(
                f"CRITICAL: {path} shows expired unrelated job — fix ID/slug routing"
            )
    return errors


def check_district_redirect() -> list[str]:
    errors: list[str] = []
    url = f"{BASE}/jobs?district_slug=pune"
    req = urllib.request.Request(url, headers={"User-Agent": UA}, method="GET")
    try:
        opener = urllib.request.build_opener(urllib.request.HTTPRedirectHandler)
        urllib.request.install_opener(opener)
        with urllib.request.urlopen(req, timeout=25) as resp:
            final = resp.geturl()
            if "district" not in final and "pune" not in final.lower():
                errors.append(
                    f"HIGH: {url} should redirect to district/pune hub; got {final}"
                )
    except urllib.error.HTTPError as e:
        if e.code >= 400:
            errors.append(f"HIGH: district_slug redirect error HTTP {e.code}")
    except Exception as e:
        errors.append(f"MEDIUM: district_slug check failed: {e}")
    return errors


def main() -> int:
    all_errors: list[str] = []
    all_errors.extend(check_robots())
    all_errors.extend(check_homepage())
    all_errors.extend(check_sitemap_index())
    all_errors.extend(check_job_slug_parity())
    all_errors.extend(check_district_redirect())

    print("SearchSarkariNaukri live SEO regression check\n")
    if not all_errors:
        print("PASS: no critical/high failures detected.")
        return 0
    for err in all_errors:
        print(f"  - {err}")
    print(f"\nFAIL: {len(all_errors)} issue(s). See 01_REGRESSION_FIX_IMPLEMENTATION_NO_DELETE.md")
    return 1


if __name__ == "__main__":
    sys.exit(main())
