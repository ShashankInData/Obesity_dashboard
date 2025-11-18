import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('obesity_data_cleaned.csv')

print("=" * 80)
print("OBESITY DATASET EXPLORATION")
print("=" * 80)

# Basic Information
print("\n1. DATASET SHAPE")
print(f"   Rows: {df.shape[0]}")
print(f"   Columns: {df.shape[1]}")

# Column Information
print("\n2. COLUMN INFORMATION")
print(f"   Columns: {list(df.columns)}")

# Data Types
print("\n3. DATA TYPES")
print(df.dtypes)

# Missing Values
print("\n4. MISSING VALUES")
missing = df.isnull().sum()
missing_pct = (missing / len(df)) * 100
missing_df = pd.DataFrame({
    'Missing Count': missing,
    'Percentage': missing_pct
})
print(missing_df[missing_df['Missing Count'] > 0])

# Unique Values
print("\n5. UNIQUE VALUES PER COLUMN")
for col in df.columns:
    print(f"   {col}: {df[col].nunique()}")

# Survey Years
print("\n6. SURVEY YEARS DISTRIBUTION")
print(df['Survey_Year'].value_counts().sort_index())

# Categories
print("\n7. CATEGORIES BREAKDOWN")
print(df['Category'].value_counts())

# Subcategories
print("\n8. SUBCATEGORIES BREAKDOWN")
print(df['Subcategory'].value_counts())

# Obesity Statistics
print("\n9. OBESITY STATISTICS SUMMARY")
numeric_cols = ['Children_Overweight_Pct', 'Women_Overweight_Pct', 'Men_Overweight_Pct']
print(df[numeric_cols].describe())

# Overall Trends by Year
print("\n10. AVERAGE OBESITY RATES BY SURVEY YEAR")
year_stats = df[df['Category'] == 'Total'].groupby('Survey_Year')[numeric_cols].mean()
print(year_stats)

# Education Impact
print("\n11. OBESITY RATES BY EDUCATION LEVEL (Latest Survey)")
latest_year = df['Survey_Year'].max()
education_data = df[(df['Category'] == 'Education') & (df['Survey_Year'] == latest_year)]
if not education_data.empty:
    print(education_data[['Subcategory', 'Children_Overweight_Pct',
                          'Women_Overweight_Pct', 'Men_Overweight_Pct']].to_string(index=False))

# Wealth Impact
print("\n12. OBESITY RATES BY WEALTH QUINTILE (Latest Survey)")
wealth_data = df[(df['Category'] == 'Wealth quintile') & (df['Survey_Year'] == latest_year)]
if not wealth_data.empty:
    print(wealth_data[['Subcategory', 'Children_Overweight_Pct',
                       'Women_Overweight_Pct', 'Men_Overweight_Pct']].to_string(index=False))

# Urban vs Rural
print("\n13. OBESITY RATES: URBAN VS RURAL (Latest Survey)")
residence_data = df[(df['Category'] == 'Residence') & (df['Survey_Year'] == latest_year)]
if not residence_data.empty:
    print(residence_data[['Subcategory', 'Children_Overweight_Pct',
                          'Women_Overweight_Pct', 'Men_Overweight_Pct']].to_string(index=False))

# Top 10 States by Women's Obesity (Latest Survey)
print("\n14. TOP 10 STATES BY WOMEN'S OBESITY RATE (Latest Survey)")
states_data = df[(df['Category'] == 'States') & (df['Survey_Year'] == latest_year)]
if not states_data.empty:
    top_states = states_data.nlargest(10, 'Women_Overweight_Pct')[
        ['Subcategory', 'Women_Overweight_Pct', 'Men_Overweight_Pct', 'Children_Overweight_Pct']
    ]
    print(top_states.to_string(index=False))

# Data Completeness
print("\n15. DATA COMPLETENESS ANALYSIS")
completeness_cols = ['Has_Complete_Children_Data', 'Has_Complete_Women_Data',
                     'Has_Complete_Men_Data', 'Has_All_Metrics']
for col in completeness_cols:
    true_count = df[col].sum()
    print(f"   {col}: {true_count} ({(true_count/len(df)*100):.1f}%)")

# Age Group Analysis (Latest Survey)
print("\n16. OBESITY RATES BY AGE GROUP (Latest Survey - Women)")
age_data = df[(df['Category'] == 'Age (5-year groups)') & (df['Survey_Year'] == latest_year)]
if not age_data.empty:
    print(age_data[['Subcategory', 'Women_Overweight_Pct', 'Men_Overweight_Pct']].to_string(index=False))

# Trend Analysis
print("\n17. OVERALL OBESITY TREND OVER TIME")
total_data = df[df['Category'] == 'Total'][['Survey_Year', 'Children_Overweight_Pct',
                                             'Women_Overweight_Pct', 'Men_Overweight_Pct']]
print(total_data.to_string(index=False))

print("\n" + "=" * 80)
print("EXPLORATION COMPLETE")
print("=" * 80)
