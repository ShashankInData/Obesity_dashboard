# Quick Start Guide

## View the Dashboard (Easiest Method)

1. Open **[obesity_dashboard_enhanced.html](obesity_dashboard_enhanced.html)** in your web browser
2. That's it! The dashboard is fully interactive and self-contained

## What You'll See

The enhanced dashboard includes:

### Summary Statistics Cards
- Current obesity rates for children, women, and men
- Trends since 1998
- Quick overview of survey data

### Interactive Charts (7 Major Visualizations)

1. **Overall Trends** - Line chart showing obesity progression from 1998-2021
2. **State Comparison** - Top 15 states ranked by obesity rates
3. **Education Impact** - How education level affects obesity across time
4. **Wealth Analysis** - Comprehensive 4-panel analysis of wealth impact
5. **Urban vs Rural** - Side-by-side comparison over time
6. **Age Groups** - How obesity varies by age
7. **Key Insights** - Highlighted findings with context

### Export Features
- Download data as CSV
- Download data as JSON
- Use for your own analysis

## Run Data Exploration

To see detailed statistics in the console:

```bash
uv run explore_data.py
```

This will print:
- Dataset dimensions
- Missing value analysis
- Statistical summaries
- Top states by obesity
- Trends over time
- Much more!

## Regenerate the Dashboard

If you modify the data or want to customize the dashboard:

```bash
uv run generate_enhanced_dashboard.py
```

This creates a fresh copy of `obesity_dashboard_enhanced.html`

## View Project Info

Quick overview of all files and statistics:

```bash
uv run project_info.py
```

## Understanding the Data

### Survey Years
- 1998-99 DHS
- 2005-06 DHS
- 2015-16 DHS
- 2019-21 DHS

### Demographics Tracked
- **Children**: Overweight percentage
- **Women (15-49)**: Overweight/Obese percentage
- **Men (15-54)**: Overweight/Obese percentage

### Categories Analyzed
- Urban vs Rural residence
- Education levels (None, Primary, Secondary, Higher)
- Wealth quintiles (Lowest to Highest)
- Age groups (5-year intervals)
- All Indian states and union territories
- Overall population totals

## Key Findings at a Glance

**Alarming Trends:**
- Women's obesity more than **doubled** (10.7% → 24.0%)
- Men's obesity increased **144%** (9.7% → 23.7%)
- Urban areas have **69% higher** obesity than rural areas
- Highest wealth quintile has **4x** the obesity of lowest

**Regional Hotspots:**
- Puducherry: 46.3% (women)
- Chandigarh: 44.0% (women)
- New Delhi: 41.4% (women)

**Age Impact:**
- Obesity increases steadily with age
- Peaks at 45-49 years (37% for women)

## Interactive Features

All charts support:
- **Hover** - See exact values
- **Zoom** - Click and drag to zoom into specific areas
- **Pan** - Shift-drag to move around
- **Legend** - Click to show/hide data series
- **Reset** - Double-click to reset view

## File Reference

- `obesity_dashboard_enhanced.html` - **Main dashboard (START HERE)**
- `obesity_data_cleaned.csv` - Clean dataset
- `explore_data.py` - Detailed data exploration
- `generate_enhanced_dashboard.py` - Dashboard generator
- `project_info.py` - Project overview
- `README.md` - Full documentation

## Next Steps

1. **Explore the dashboard** - Open the HTML file
2. **Review the data** - Run explore_data.py
3. **Read the README** - For comprehensive documentation
4. **Customize** - Modify generate_enhanced_dashboard.py for custom visualizations

## Troubleshooting

**Charts not showing?**
- Make sure you're opening the HTML file in a modern browser (Chrome, Firefox, Edge)
- The file must be opened locally, not from a text editor

**Want to modify the dashboard?**
- Edit `generate_enhanced_dashboard.py`
- Run it with `uv run generate_enhanced_dashboard.py`
- Refresh your browser

**Need different visualizations?**
- The Plotly library supports many chart types
- See examples at https://plotly.com/python/

## Support

For questions about:
- **Data source**: See DHS Program documentation
- **Technical issues**: Check README.md
- **Customization**: Review generate_enhanced_dashboard.py comments

---

**Happy Exploring!** 🏥📊
