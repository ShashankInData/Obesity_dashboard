"""
Quick Project Information Script
Displays key information about the India Obesity Dashboard project
"""

import pandas as pd
import os

print("=" * 80)
print("INDIA OBESITY DASHBOARD - PROJECT INFORMATION")
print("=" * 80)

# Check if files exist
files = [
    'obesity_data_cleaned.csv',
    'obesity_dashboard.html',
    'obesity_dashboard_enhanced.html',
    'generate_enhanced_dashboard.py',
    'explore_data.py',
    'README.md'
]

print("\nFILE STATUS:")
for file in files:
    exists = "[OK]" if os.path.exists(file) else "[MISSING]"
    print(f"  {exists} {file}")

# Load and display dataset info
if os.path.exists('obesity_data_cleaned.csv'):
    df = pd.read_csv('obesity_data_cleaned.csv')

    print("\nDATASET SUMMARY:")
    print(f"  Total Records: {len(df)}")
    print(f"  Total Columns: {len(df.columns)}")
    print(f"  Survey Years: {sorted(df['Survey_Year'].unique())}")
    print(f"  Categories: {df['Category'].nunique()}")
    print(f"  States Covered: {len(df[df['Category'] == 'States'])}")

    print("\nLATEST OBESITY RATES (2019):")
    latest = df[df['Category'] == 'Total'].sort_values('Survey_Year').iloc[-1]
    print(f"  Children: {latest['Children_Overweight_Pct']:.1f}%")
    print(f"  Women: {latest['Women_Overweight_Pct']:.1f}%")
    print(f"  Men: {latest['Men_Overweight_Pct']:.1f}%")

    print("\nTOP 5 STATES BY WOMEN'S OBESITY (2019):")
    states = df[(df['Category'] == 'States') & (df['Survey_Year'] == 2019)]
    top_states = states.nlargest(5, 'Women_Overweight_Pct')
    for idx, row in top_states.iterrows():
        state = row['Subcategory'].replace('States : ', '').replace(' (L1)', '')
        print(f"  {state}: {row['Women_Overweight_Pct']:.1f}%")

print("\nQUICK START:")
print("  1. Open 'obesity_dashboard_enhanced.html' in your browser")
print("  2. Run 'uv run explore_data.py' for detailed statistics")
print("  3. Run 'uv run generate_enhanced_dashboard.py' to regenerate dashboard")

print("\nDEPENDENCIES:")
try:
    import pandas
    import numpy
    import matplotlib
    import seaborn
    import plotly
    print("  [OK] All dependencies installed")
except ImportError as e:
    print(f"  [MISSING] Missing: {e.name}")
    print("  Run: uv sync")

print("\nPROJECT STRUCTURE:")
print("  obesity/")
print("  |-- Data Files")
print("  |   |-- obesity_data_cleaned.csv")
print("  |-- Dashboards")
print("  |   |-- obesity_dashboard.html")
print("  |   |-- obesity_dashboard_enhanced.html (RECOMMENDED)")
print("  |-- Scripts")
print("  |   |-- explore_data.py")
print("  |   |-- generate_enhanced_dashboard.py")
print("  |   |-- obesity_data_cleaning.py")
print("  |-- Documentation")
print("      |-- README.md")

print("\n" + "=" * 80)
print("For full documentation, see README.md")
print("=" * 80)
