import pandas as pd

xls = pd.ExcelFile('SearchSarkariNaukri-Keyword-List-899.xlsx')
df = pd.read_excel(xls, sheet_name='Keywords', header=0)

print(f"Total keywords: {len(df)}")
print("\nCategories:")
for cat in df['Category'].unique():
    count = len(df[df['Category'] == cat])
    print(f"  {cat}: {count}")

print("\n" + "="*50)
print("SAMPLE KEYWORDS BY CATEGORY:")
print("="*50)

for category in ['Core Head Terms', 'Department/Exam-wise', 'District-wise', 'Informational/Long-tail', 'Qualification-wise', 'State-wise']:
    cat_df = df[df['Category'] == category].sort_values('Priority')
    print(f"\n{category} (Top 10):")
    print("-" * 40)
    for _, row in cat_df.head(10).iterrows():
        print(f"  {row['Keyword']:<30} | {row['Sub-Category']:<20} | {row['Search Intent']:<20} | {row['Priority']}")


def submit_indexnow_urls(url_list: list, host: str = "www.searchsarkarinaukri.com", key: str = "searchsarkarinaukri_key") -> dict:
    """
    Submits updated job listing URLs to IndexNow API (Bing, Yandex, Seznam).
    """
    import json
    import urllib.request

    endpoint = "https://api.indexnow.org/indexnow"
    payload = {
        "host": host,
        "key": key,
        "keyLocation": f"https://{host}/{key}.txt",
        "urlList": url_list
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(endpoint, data=data, headers={'Content-Type': 'application/json; charset=utf-8'})
    
    try:
        with urllib.request.urlopen(req) as response:
            return {"status": response.status, "message": "URLs submitted successfully to IndexNow."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

print("\n" + "="*50)
print("IndexNow Submission Helper Ready.")
print("="*50)