import pandas as pd
import numpy as np
import re
from datetime import datetime

"""
OBESITY DATA CLEANING PIPELINE
Healthcare Domain - India DHS Survey Data

This script cleans the contaminated obesity dataset and prepares it for dashboard visualization.
"""

def load_raw_data(filepath):
    """Load the raw CSV file, skipping the blank first row"""
    df = pd.read_csv(filepath, skiprows=1)
    print(f"✓ Loaded raw data: {df.shape[0]} rows × {df.shape[1]} columns")
    return df


def identify_contaminated_rows(df):
    """
    Identify and flag contaminated rows (metadata, citations, headers)
    
    Contamination types:
    1. Citation text in Country column
    2. Column names appearing as data values
    3. Description text in Survey column
    """
    contaminated_mask = pd.Series([False] * len(df), index=df.index)
    
    # Check for citation text (contains "http", "ICF", "USAID", etc.)
    contaminated_mask |= df['Country'].astype(str).str.contains('http|ICF|USAID|statcompiler', case=False, na=False)
    
    # Check for column names appearing as values
    column_names = ['Children overweight', 'Women who are overweight', 'Men who are overweight']
    for col_name in column_names:
        contaminated_mask |= df['Country'].astype(str).str.contains(col_name, case=False, na=False)
        contaminated_mask |= df['Survey'].astype(str).str.contains(col_name, case=False, na=False)
    
    # Check for description text (starts with "Percentage of")
    contaminated_mask |= df['Survey'].astype(str).str.contains('^Percentage of', case=False, na=False)
    
    # Check for rows where numeric columns have non-numeric country names
    numeric_cols = df.columns[3:]  # Last 3 columns should be numeric
    for col in numeric_cols:
        # If the Country column value appears to be numeric, it's probably a contaminated row
        try:
            contaminated_mask |= pd.to_numeric(df['Country'], errors='coerce').notna()
        except:
            pass
    
    print(f"✓ Identified {contaminated_mask.sum()} contaminated rows")
    return contaminated_mask


def remove_contaminated_rows(df):
    """Remove contaminated rows from the dataset"""
    contaminated_mask = identify_contaminated_rows(df)
    
    if contaminated_mask.sum() > 0:
        print(f"\n🗑️  REMOVING {contaminated_mask.sum()} CONTAMINATED ROWS:")
        contaminated_df = df[contaminated_mask]
        for idx, row in contaminated_df.iterrows():
            country_str = str(row['Country'])[:50] if pd.notna(row['Country']) else 'NULL'
            survey_str = str(row['Survey'])[:50] if pd.notna(row['Survey']) else 'NULL'
            print(f"  Row {idx}: Country='{country_str}', Survey='{survey_str}'")
    
    df_clean = df[~contaminated_mask].copy()
    df_clean = df_clean.reset_index(drop=True)
    
    print(f"\n✓ Clean dataset: {df_clean.shape[0]} rows × {df_clean.shape[1]} columns")
    return df_clean


def extract_year_from_survey(survey_name):
    """
    Extract start and end year from survey name
    Examples:
    - "2019-21 DHS" → start=2019, end=2021
    - "2015-16 DHS" → start=2015, end=2016
    - "2005-06 DHS" → start=2005, end=2006
    - "1998-99 DHS" → start=1998, end=1999
    """
    if pd.isna(survey_name):
        return None, None
    
    # Pattern: "YYYY-YY DHS" or "YYYY-YYYY DHS"
    match = re.search(r'(\d{4})-(\d{2,4})', str(survey_name))
    if match:
        start_year = int(match.group(1))
        end_year_str = match.group(2)
        
        # Handle 2-digit end year
        if len(end_year_str) == 2:
            # Get century from start year
            century = (start_year // 100) * 100
            end_year = century + int(end_year_str)
        else:
            end_year = int(end_year_str)
        
        return start_year, end_year
    
    return None, None


def split_characteristic_column(df):
    """
    Split 'Characteristic' column into 'Category' and 'Subcategory'
    
    Examples:
    - "Residence : Urban" → Category="Residence", Subcategory="Urban"
    - "Total" → Category="Total", Subcategory="Total"
    - "Age (5-year groups) : 15-19" → Category="Age (5-year groups)", Subcategory="15-19"
    """
    df['Category'] = None
    df['Subcategory'] = None
    
    for idx, char in df['Characteristic'].items():
        if pd.isna(char):
            continue
        
        char_str = str(char).strip()
        
        if ':' in char_str:
            # Split by colon
            parts = char_str.split(':', 1)
            df.at[idx, 'Category'] = parts[0].strip()
            df.at[idx, 'Subcategory'] = parts[1].strip()
        else:
            # No colon - use the value for both
            df.at[idx, 'Category'] = char_str
            df.at[idx, 'Subcategory'] = char_str
    
    print(f"✓ Split Characteristic into Category and Subcategory")
    print(f"  Unique Categories: {df['Category'].nunique()}")
    print(f"  Categories: {sorted(df['Category'].dropna().unique())}")
    
    return df


def convert_numeric_columns(df):
    """Convert obesity metric columns to numeric, handling any remaining non-numeric values"""
    numeric_cols = [
        'Children overweight',
        'Women who are overweight or obese according to BMI (>=25.0)',
        'Men who are overweight or obese according to BMI (>=25.0)'
    ]
    
    for col in numeric_cols:
        # Convert to numeric, coercing errors to NaN
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    print(f"✓ Converted numeric columns to proper data types")
    return df


def add_derived_columns(df):
    """Add useful derived columns for analysis"""
    
    # Extract years from survey
    df[['Survey_Start_Year', 'Survey_End_Year']] = df['Survey'].apply(
        lambda x: pd.Series(extract_year_from_survey(x))
    )
    
    # Add mid-year for time series plotting
    df['Survey_Year'] = df['Survey_Start_Year']  # Use start year as primary year
    
    # Add flag for complete data (no missing values in obesity metrics)
    df['Has_Complete_Children_Data'] = df['Children overweight'].notna()
    df['Has_Complete_Women_Data'] = df['Women who are overweight or obese according to BMI (>=25.0)'].notna()
    df['Has_Complete_Men_Data'] = df['Men who are overweight or obese according to BMI (>=25.0)'].notna()
    
    # Overall completeness flag
    df['Has_All_Metrics'] = (
        df['Has_Complete_Children_Data'] & 
        df['Has_Complete_Women_Data'] & 
        df['Has_Complete_Men_Data']
    )
    
    print(f"✓ Added derived columns:")
    print(f"  - Survey_Start_Year, Survey_End_Year, Survey_Year")
    print(f"  - Data completeness flags (Has_Complete_*)")
    
    return df


def create_clean_column_names(df):
    """Rename columns to shorter, cleaner names"""
    rename_map = {
        'Children overweight': 'Children_Overweight_Pct',
        'Women who are overweight or obese according to BMI (>=25.0)': 'Women_Overweight_Pct',
        'Men who are overweight or obese according to BMI (>=25.0)': 'Men_Overweight_Pct'
    }
    
    df = df.rename(columns=rename_map)
    print(f"✓ Renamed columns to cleaner names")
    
    return df


def generate_data_quality_report(df):
    """Generate comprehensive data quality report"""
    print("\n" + "=" * 100)
    print("DATA QUALITY REPORT")
    print("=" * 100)
    
    print(f"\n📊 FINAL DATASET DIMENSIONS:")
    print(f"   Rows: {df.shape[0]}")
    print(f"   Columns: {df.shape[1]}")
    
    print(f"\n📅 TIME COVERAGE:")
    print(f"   Years: {df['Survey_Start_Year'].min()} - {df['Survey_End_Year'].max()}")
    print(f"   Surveys: {df['Survey'].nunique()}")
    print(f"   Survey names: {sorted(df['Survey'].dropna().unique())}")
    
    print(f"\n🌍 GEOGRAPHIC COVERAGE:")
    print(f"   Countries: {df['Country'].nunique()}")
    print(f"   Country names: {sorted(df['Country'].unique())}")
    
    print(f"\n📂 CATEGORIES:")
    print(f"   Unique categories: {df['Category'].nunique()}")
    for cat in sorted(df['Category'].dropna().unique()):
        count = (df['Category'] == cat).sum()
        print(f"   - {cat}: {count} rows")
    
    print(f"\n🔢 MISSING VALUES:")
    for col in ['Children_Overweight_Pct', 'Women_Overweight_Pct', 'Men_Overweight_Pct']:
        total = len(df)
        missing = df[col].isnull().sum()
        pct = (missing / total) * 100
        print(f"   {col}: {missing}/{total} ({pct:.1f}% missing)")
        
        # Breakdown by category
        if missing > 0:
            missing_by_cat = df[df[col].isnull()].groupby('Category').size()
            print(f"      Missing breakdown by category:")
            for cat, cnt in missing_by_cat.items():
                print(f"        - {cat}: {cnt} rows")
    
    print(f"\n✓ DATA COMPLETENESS:")
    print(f"   Rows with ALL metrics: {df['Has_All_Metrics'].sum()} ({df['Has_All_Metrics'].sum()/len(df)*100:.1f}%)")
    print(f"   Rows with Children data: {df['Has_Complete_Children_Data'].sum()} ({df['Has_Complete_Children_Data'].sum()/len(df)*100:.1f}%)")
    print(f"   Rows with Women data: {df['Has_Complete_Women_Data'].sum()} ({df['Has_Complete_Women_Data'].sum()/len(df)*100:.1f}%)")
    print(f"   Rows with Men data: {df['Has_Complete_Men_Data'].sum()} ({df['Has_Complete_Men_Data'].sum()/len(df)*100:.1f}%)")
    
    print(f"\n📈 OBESITY STATISTICS (where data exists):")
    for col in ['Children_Overweight_Pct', 'Women_Overweight_Pct', 'Men_Overweight_Pct']:
        print(f"\n   {col}:")
        print(f"      Min: {df[col].min():.1f}%")
        print(f"      Max: {df[col].max():.1f}%")
        print(f"      Mean: {df[col].mean():.1f}%")
        print(f"      Median: {df[col].median():.1f}%")
        print(f"      Std Dev: {df[col].std():.1f}%")
    
    print("\n" + "=" * 100)


def main():
    """Main cleaning pipeline"""
    print("\n" + "=" * 100)
    print("OBESITY DATA CLEANING PIPELINE - START")
    print("=" * 100 + "\n")
    
    # Step 1: Load raw data
    print("STEP 1: Loading raw data...")
    df = load_raw_data('/home/claude/obesity_data_raw.csv')
    
    # Step 2: Remove contaminated rows
    print("\nSTEP 2: Removing contaminated rows...")
    df = remove_contaminated_rows(df)
    
    # Step 3: Split Characteristic column
    print("\nSTEP 3: Splitting Characteristic column...")
    df = split_characteristic_column(df)
    
    # Step 4: Convert numeric columns
    print("\nSTEP 4: Converting numeric columns...")
    df = convert_numeric_columns(df)
    
    # Step 5: Add derived columns
    print("\nSTEP 5: Adding derived columns...")
    df = add_derived_columns(df)
    
    # Step 6: Rename columns
    print("\nSTEP 6: Creating clean column names...")
    df = create_clean_column_names(df)
    
    # Step 7: Reorder columns for better readability
    print("\nSTEP 7: Reordering columns...")
    column_order = [
        'Country',
        'Survey',
        'Survey_Year',
        'Survey_Start_Year',
        'Survey_End_Year',
        'Category',
        'Subcategory',
        'Characteristic',
        'Children_Overweight_Pct',
        'Women_Overweight_Pct',
        'Men_Overweight_Pct',
        'Has_Complete_Children_Data',
        'Has_Complete_Women_Data',
        'Has_Complete_Men_Data',
        'Has_All_Metrics'
    ]
    df = df[column_order]
    
    # Step 8: Save cleaned data
    print("\nSTEP 8: Saving cleaned data...")
    output_path = '/home/claude/obesity_data_cleaned.csv'
    df.to_csv(output_path, index=False)
    print(f"✓ Saved cleaned data to: {output_path}")
    
    # Step 9: Generate data quality report
    generate_data_quality_report(df)
    
    print("\n" + "=" * 100)
    print("CLEANING PIPELINE COMPLETE ✓")
    print("=" * 100 + "\n")
    
    return df


if __name__ == "__main__":
    df_cleaned = main()
    
    print("\n📋 SAMPLE OF CLEANED DATA:")
    print(df_cleaned.head(10).to_string())
    
    print("\n✅ Next steps:")
    print("   1. Review the cleaned data: obesity_data_cleaned.csv")
    print("   2. Check the data quality report above")
    print("   3. Use this data for your dashboard visualization")
