import urllib.request
import xml.etree.ElementTree as ET
import os

sitemaps_info = [
    ("sitemap-static.xml", "https://www.searchsarkarinaukri.com/sitemap-static.xml"),
    ("sitemap-jobs.xml", "https://www.searchsarkarinaukri.com/sitemap-jobs.xml"),
    ("sitemap-locations.xml", "https://www.searchsarkarinaukri.com/sitemap-locations.xml"),
    ("sitemap-qualifications.xml", "https://www.searchsarkarinaukri.com/sitemap-qualifications.xml"),
    ("sitemap-departments.xml", "https://www.searchsarkarinaukri.com/sitemap-departments.xml"),
    ("sitemap-cross-filter.xml", "https://www.searchsarkarinaukri.com/sitemap-cross-filter.xml"),
    ("sitemap-news.xml", "https://www.searchsarkarinaukri.com/sitemap-news.xml"),
    ("sitemap-blogs.xml", "https://www.searchsarkarinaukri.com/sitemap-blogs.xml"),
    ("sitemap-results.xml", "https://www.searchsarkarinaukri.com/sitemap-results.xml"),
    ("sitemap-admit-cards.xml", "https://www.searchsarkarinaukri.com/sitemap-admit-cards.xml"),
    ("sitemap-districts.xml", "https://www.searchsarkarinaukri.com/sitemap-districts.xml"),
]

req_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

parsed_data = {}
total_pages = 0

print("Fetching sitemaps...")
for name, url in sitemaps_info:
    try:
        req = urllib.request.Request(url, headers=req_headers)
        with urllib.request.urlopen(req) as resp:
            xml_data = resp.read()
            root = ET.fromstring(xml_data)
            url_entries = []
            for elem in root.findall('ns:url', ns):
                loc_elem = elem.find('ns:loc', ns)
                lastmod_elem = elem.find('ns:lastmod', ns)
                changefreq_elem = elem.find('ns:changefreq', ns)
                priority_elem = elem.find('ns:priority', ns)
                
                loc = loc_elem.text.strip() if loc_elem is not None and loc_elem.text else ''
                lastmod = lastmod_elem.text.strip() if lastmod_elem is not None and lastmod_elem.text else 'N/A'
                changefreq = changefreq_elem.text.strip() if changefreq_elem is not None and changefreq_elem.text else 'N/A'
                priority = priority_elem.text.strip() if priority_elem is not None and priority_elem.text else 'N/A'
                
                if loc:
                    url_entries.append({
                        'loc': loc,
                        'lastmod': lastmod,
                        'changefreq': changefreq,
                        'priority': priority
                    })
            parsed_data[name] = {
                'url': url,
                'entries': url_entries,
                'count': len(url_entries)
            }
            total_pages += len(url_entries)
            print(f"Parsed {name}: {len(url_entries)} pages")
    except Exception as e:
        print(f"Error reading {name}: {e}")
        parsed_data[name] = {
            'url': url,
            'entries': [],
            'count': 0,
            'error': str(e)
        }

# Generate Markdown Document
md_lines = []
md_lines.append("# SearchSarkariNaukri.com — Complete Sitemap & Master URL Inventory")
md_lines.append("")
md_lines.append("**Audit Date:** 2026-08-10  ")
md_lines.append("**Source Sitemap Index:** `https://www.searchsarkarinaukri.com/sitemap.xml`  ")
md_lines.append(f"**Total Sub-Sitemaps:** {len(sitemaps_info)}  ")
md_lines.append(f"**Total Pages / Master URL Count:** **{total_pages} URLs**  ")
md_lines.append("")
md_lines.append("---")
md_lines.append("")
md_lines.append("## 📊 Summary Overview")
md_lines.append("")
md_lines.append("| # | Sitemap File | Sitemap URL | Page Count |")
md_lines.append("|---|---|---|---|")

for idx, (name, url) in enumerate(sitemaps_info, 1):
    count = parsed_data[name]['count']
    md_lines.append(f"| {idx} | `{name}` | [{url}]({url}) | **{count}** |")

md_lines.append(f"| | **GRAND TOTAL** | **All Sitemaps Combined** | **{total_pages}** |")
md_lines.append("")
md_lines.append("---")
md_lines.append("")

md_lines.append("## 📁 Detailed Breakdown & URL Lists by Category")
md_lines.append("")

for idx, (name, url) in enumerate(sitemaps_info, 1):
    data = parsed_data[name]
    md_lines.append(f"### {idx}. `{name}`")
    md_lines.append(f"- **Sitemap URL:** {url}")
    md_lines.append(f"- **Total URLs in this sitemap:** {data['count']}")
    md_lines.append("")
    
    if data['entries']:
        md_lines.append("```text")
        for entry in data['entries']:
            md_lines.append(entry['loc'])
        md_lines.append("```")
    else:
        md_lines.append("*No URLs found or failed to load.*")
    md_lines.append("")

md_lines.append("---")
md_lines.append("")
md_lines.append("## 🔗 Master List — All URLs (Plain Text format)")
md_lines.append("")
md_lines.append("```text")
for name, _ in sitemaps_info:
    for entry in parsed_data[name]['entries']:
        md_lines.append(entry['loc'])
md_lines.append("```")

# Write to 00_MASTER_ALL_URLS.md
out_md_path = r"c:\Users\computer1\Desktop\Growthik_Media\02_Clients\03_SearchSarkariNaukri\SearchSarkariNaukri\.agents\05_Sitemap\00_MASTER_ALL_URLS.md"
with open(out_md_path, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print(f"Written Markdown report to {out_md_path}")

# Write to 00_MASTER_ALL_URLS.txt
out_txt_path = r"c:\Users\computer1\Desktop\Growthik_Media\02_Clients\03_SearchSarkariNaukri\SearchSarkariNaukri\.agents\05_Sitemap\00_MASTER_ALL_URLS.txt"
txt_lines = [f"SearchSarkariNaukri.com Master URL List - Total URLs: {total_pages}", "=" * 70, ""]
for name, _ in sitemaps_info:
    txt_lines.append(f"--- {name} ({parsed_data[name]['count']} URLs) ---")
    for entry in parsed_data[name]['entries']:
        txt_lines.append(entry['loc'])
    txt_lines.append("")

with open(out_txt_path, "w", encoding="utf-8") as f:
    f.write("\n".join(txt_lines))

print(f"Written TXT report to {out_txt_path}")
