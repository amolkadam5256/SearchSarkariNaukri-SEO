import urllib.request
import urllib.error
import concurrent.futures
import time
import os
import json

txt_file = r"c:\Users\computer1\Desktop\Growthik_Media\02_Clients\03_SearchSarkariNaukri\SearchSarkariNaukri\.agents\05_Sitemap\00_MASTER_ALL_URLS.txt"
report_md = r"c:\Users\computer1\Desktop\Growthik_Media\02_Clients\03_SearchSarkariNaukri\SearchSarkariNaukri\.agents\05_Sitemap\01_URL_HEALTH_AUDIT_REPORT.md"
report_json = r"c:\Users\computer1\Desktop\Growthik_Media\02_Clients\03_SearchSarkariNaukri\SearchSarkariNaukri\.agents\05_Sitemap\url_health_data.json"

print("Reading URLs from master file...")
urls = []
current_sitemap = "General"
url_to_sitemap = {}

with open(txt_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line.startswith("--- ") and "URLs)" in line:
            current_sitemap = line.split("--- ")[1].split(" (")[0]
        elif line.startswith("http://") or line.startswith("https://"):
            urls.append(line)
            url_to_sitemap[line] = current_sitemap

total_urls = len(urls)
print(f"Loaded {total_urls} URLs to verify across sitemaps.")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

def check_url(url):
    req = urllib.request.Request(url, headers=headers, method='HEAD')
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return url, resp.status, "OK", url_to_sitemap.get(url, "Unknown")
    except urllib.error.HTTPError as e:
        # If HEAD method not allowed (405), fallback to GET
        if e.code == 405:
            try:
                req_get = urllib.request.Request(url, headers=headers, method='GET')
                with urllib.request.urlopen(req_get, timeout=10) as resp_get:
                    return url, resp_get.status, "OK", url_to_sitemap.get(url, "Unknown")
            except urllib.error.HTTPError as e_get:
                return url, e_get.code, f"HTTP Error {e_get.code}", url_to_sitemap.get(url, "Unknown")
            except Exception as e_gen:
                return url, 0, str(e_gen), url_to_sitemap.get(url, "Unknown")
        return url, e.code, f"HTTP Error {e.code}", url_to_sitemap.get(url, "Unknown")
    except urllib.error.URLError as e:
        return url, 0, f"URL Error: {e.reason}", url_to_sitemap.get(url, "Unknown")
    except Exception as e:
        return url, 0, f"Exception: {str(e)}", url_to_sitemap.get(url, "Unknown")

results = []
working_count = 0
not_found_404_count = 0
other_error_count = 0

start_time = time.time()
print("Starting health check with 20 parallel threads...")

completed = 0
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    future_to_url = {executor.submit(check_url, url): url for url in urls}
    for future in concurrent.futures.as_completed(future_to_url):
        url, status_code, msg, sitemap_cat = future.result()
        completed += 1
        results.append({
            'url': url,
            'status': status_code,
            'message': msg,
            'sitemap': sitemap_cat
        })
        if status_code == 200:
            working_count += 1
        elif status_code == 404:
            not_found_404_count += 1
        else:
            other_error_count += 1
        
        if completed % 100 == 0 or completed == total_urls:
            print(f"Progress: {completed}/{total_urls} URLs checked... ({working_count} 200 OK, {not_found_404_count} 404s, {other_error_count} errors)")

elapsed = round(time.time() - start_time, 2)
print(f"Finished checking {total_urls} URLs in {elapsed} seconds.")

# Group statistics by sitemap
sitemap_stats = {}
for r in results:
    sm = r['sitemap']
    if sm not in sitemap_stats:
        sitemap_stats[sm] = {'total': 0, '200': 0, '404': 0, 'other': 0}
    sitemap_stats[sm]['total'] += 1
    if r['status'] == 200:
        sitemap_stats[sm]['200'] += 1
    elif r['status'] == 404:
        sitemap_stats[sm]['404'] += 1
    else:
        sitemap_stats[sm]['other'] += 1

# Generate Markdown Report
md = []
md.append("# 🏥 SearchSarkariNaukri.com — Complete URL Health & 404 Audit Report")
md.append("")
md.append(f"**Audit Date:** 2026-08-10  ")
md.append(f"**Total URLs Tested:** **{total_urls}**  ")
md.append(f"**Time Taken:** {elapsed} seconds  ")
md.append(f"**Overall Health Pass Rate:** **{(working_count/total_urls)*100:.2f}%**  ")
md.append("")
md.append("---")
md.append("")
md.append("## 📊 Overall Executive Summary")
md.append("")
md.append("| Status Category | Status Code | Count | Percentage |")
md.append("|---|---|---|---|")
md.append(f"| ✅ **Working (Live)** | `200 OK` | **{working_count}** | **{(working_count/total_urls)*100:.2f}%** |")
md.append(f"| ❌ **Broken (Not Found)** | `404 Not Found` | **{not_found_404_count}** | **{(not_found_404_count/total_urls)*100:.2f}%** |")
md.append(f"| ⚠️ **Other Status / Errors** | `Redirect / 5xx / Error` | **{other_error_count}** | **{(other_error_count/total_urls)*100:.2f}%** |")
md.append(f"| **TOTAL** | | **{total_urls}** | **100.00%** |")
md.append("")
md.append("---")
md.append("")
md.append("## 📁 Breakdown by Sub-Sitemap")
md.append("")
md.append("| Sitemap File | Total URLs | 200 OK (Working) | 404 Not Found | Other / Errors | Health % |")
md.append("|---|---|---|---|---|---|")

for sm, stat in sitemap_stats.items():
    pct = (stat['200'] / stat['total'] * 100) if stat['total'] > 0 else 0
    md.append(f"| `{sm}` | {stat['total']} | **{stat['200']}** | {stat['404']} | {stat['other']} | {pct:.1f}% |")

md.append("")
md.append("---")
md.append("")

# Detail Broken 404 URLs
broken_urls = [r for r in results if r['status'] == 404]
md.append(f"## ❌ Broken Pages (`404 Not Found`) — Total: {len(broken_urls)}")
md.append("")
if broken_urls:
    md.append("| # | Sitemap Category | URL | Status Code |")
    md.append("|---|---|---|---|")
    for idx, r in enumerate(broken_urls, 1):
        md.append(f"| {idx} | `{r['sitemap']}` | [{r['url']}]({r['url']}) | `404` |")
else:
    md.append("🎉 **No 404 errors found! All URLs are healthy and returning 200 OK.**")

md.append("")
md.append("---")
md.append("")

# Detail Other Error URLs (e.g. 5xx, timeouts)
other_error_urls = [r for r in results if r['status'] not in (200, 404)]
md.append(f"## ⚠️ Other Non-200 Status Pages — Total: {len(other_error_urls)}")
md.append("")
if other_error_urls:
    md.append("| # | Sitemap Category | URL | Status Code / Details |")
    md.append("|---|---|---|---|")
    for idx, r in enumerate(other_error_urls, 1):
        md.append(f"| {idx} | `{r['sitemap']}` | [{r['url']}]({r['url']}) | `{r['status']}` ({r['message']}) |")
else:
    md.append("✨ **No other errors or redirects found.**")

with open(report_md, "w", encoding="utf-8") as f:
    f.write("\n".join(md))

print(f"Report successfully saved to {report_md}")

with open(report_json, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print(f"Raw health data saved to {report_json}")
