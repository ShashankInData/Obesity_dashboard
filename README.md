# India Obesity Dashboard (1998-2021)

A comprehensive, interactive data visualization dashboard analyzing obesity trends in India based on DHS (Demographic and Health Surveys) data.

## Project Overview

This project provides an in-depth analysis of obesity trends across different demographics in India over a 23-year period (1998-2021), using data from four major DHS surveys.

## Files in This Project

- **obesity_data_cleaned.csv** - Cleaned dataset with 215 records
- **obesity_data_cleaning.py** - Python script for data cleaning
- **obesity_dashboard.html** - Original dashboard
- **obesity_dashboard_enhanced.html** - Enhanced interactive dashboard (RECOMMENDED)
- **generate_enhanced_dashboard.py** - Script to generate the enhanced dashboard
- **explore_data.py** - Data exploration script
- **pyproject.toml** - UV project configuration
- **uv.lock** - UV dependency lock file

## Setup Instructions

### Prerequisites

- Python 3.9 or higher
- UV package manager (installed automatically)

### Installation

The project uses UV for dependency management. All dependencies are managed through UV:

```bash
# Dependencies are automatically installed when running scripts with UV
uv run explore_data.py
uv run generate_enhanced_dashboard.py
```

### Installed Dependencies

- pandas - Data manipulation and analysis
- numpy - Numerical computing
- matplotlib - Plotting library
- seaborn - Statistical visualization
- plotly - Interactive visualizations
- kaleido - Static image export for plotly

## Usage

### View the Dashboard

Simply open **obesity_dashboard_enhanced.html** in your web browser. The dashboard is fully self-contained and requires no server.

### Explore the Data

```bash
uv run explore_data.py
```

This will print comprehensive statistics about the dataset to the console.

### Regenerate the Dashboard

```bash
uv run generate_enhanced_dashboard.py
```

This creates a fresh version of the enhanced dashboard.

## Dashboard Features

### Interactive Visualizations

1. **Overall Trends** - Line charts showing obesity trends from 1998-2021 for children, women, and men
2. **State Comparison** - Top 15 states ranked by obesity rates
3. **Education Analysis** - Impact of education level on obesity across all survey years
4. **Wealth Quintile Analysis** - Comprehensive analysis of wealth impact on obesity
5. **Urban vs Rural** - Comparison of obesity rates between urban and rural areas
6. **Age Group Trends** - How obesity varies across different age groups

### Key Statistics Cards

- Live statistics showing current obesity rates
- Change indicators from baseline (1998)
- Survey year information

### Data Export

- Export to CSV format
- Export to JSON format
- Download complete dataset for custom analysis

### Design Features

- Fully responsive design
- Modern gradient UI with card-based layout
- Interactive charts (zoom, pan, hover)
- Mobile-friendly interface
- Professional color scheme

## Key Insights

### Rising Epidemic
Obesity rates have increased dramatically across all demographics:
- Women: 10.7% (1998) → 24.0% (2019) - **124% increase**
- Men: 9.7% (2005) → 23.7% (2019) - **144% increase**
- Children: 2.8% (1998) → 3.4% (2019)

### Urban-Rural Divide
Urban areas show significantly higher obesity rates:
- Women: Urban 33.3% vs Rural 19.7% (**69% higher**)
- Men: Urban 29.8% vs Rural 19.3% (**54% higher**)

### Wealth Paradox
Higher wealth correlates with higher obesity:
- Highest quintile: Women 38.6%, Men 36.7%
- Lowest quintile: Women 10.0%, Men 9.5%
- **Nearly 4x difference between highest and lowest quintiles**

### Age Factor
Obesity increases with age, peaking at 45-49:
- Women 15-19: 5.4% → 45-49: 37.0%
- Progressive increase across all age groups

### Regional Variations
Top 5 states by women's obesity (2019):
1. Puducherry - 46.3%
2. Chandigarh - 44.0%
3. New Delhi - 41.4%
4. Punjab - 40.8%
5. Tamil Nadu - 40.5%

## Data Source

**DHS Program STATcompiler** (ICF, 2015)
- Survey Years: 1998, 2005, 2015, 2019
- Geographic Coverage: All Indian states and union territories
- Demographics: Children, Women (15-49), Men (15-54)
- Categories: Urban/Rural, Education, Wealth, Age, State

## Technical Details

### Data Processing
- Cleaned dataset with standardized column names
- Boolean flags for data completeness
- Consistent formatting across all survey years

### Visualization Technology
- **Plotly.js** for interactive charts
- Client-side rendering (no server required)
- Responsive design with CSS Grid and Flexbox

### Performance
- Lightweight HTML (self-contained)
- Optimized chart rendering
- Fast load times

## Project Structure

```
obesity/
├── obesity_data_cleaned.csv          # Main dataset
├── obesity_data_cleaning.py          # Data cleaning script
├── obesity_dashboard.html            # Original dashboard
├── obesity_dashboard_enhanced.html   # Enhanced dashboard ⭐
├── generate_enhanced_dashboard.py    # Dashboard generator
├── explore_data.py                   # Data exploration
├── README.md                         # This file
├── pyproject.toml                    # Project configuration
└── uv.lock                          # Dependency lock file
```

## Future Enhancements

Potential areas for expansion:
- BMI category breakdown (overweight vs obese)
- Comparison with global obesity trends
- Predictive modeling for future trends
- Regional heatmaps
- Correlation analysis with economic indicators
- Interactive filters by year/category
- Mobile app version

## Contributing

This is an educational/analytical project. Feel free to:
- Extend the analysis
- Add new visualizations
- Improve data processing
- Enhance the UI/UX

## License

Data: DHS Program (publicly available)
Code: Open for educational and research purposes

## Contact & Support

For questions about the data or methodology, refer to the DHS Program documentation.

---

**Last Updated:** 2025
**Dashboard Version:** 2.0 (Enhanced)
**Data Version:** Cleaned (215 records across 4 surveys)
# Obesity_dashboard
