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