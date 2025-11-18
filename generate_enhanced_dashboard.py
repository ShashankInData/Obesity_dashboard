import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# Load the dataset
df = pd.read_csv('obesity_data_cleaned.csv')

# HTML header and styling
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>India Obesity Dashboard (1998-2021) - Enhanced</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            min-height: 100vh;
        }

        .container {
            max-width: 1600px;
            margin: 0 auto;
        }

        .header {
            background: white;
            color: #2c3e50;
            padding: 40px;
            border-radius: 15px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            text-align: center;
        }

        .header h1 {
            font-size: 3em;
            margin-bottom: 10px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .header p {
            color: #7f8c8d;
            font-size: 1.2em;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }

        .stat-card {
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            text-align: center;
            transition: transform 0.3s ease;
        }

        .stat-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }

        .stat-value {
            font-size: 2.5em;
            font-weight: bold;
            margin: 10px 0;
        }

        .stat-label {
            color: #7f8c8d;
            font-size: 1.1em;
        }

        .stat-change {
            font-size: 1.2em;
            margin-top: 10px;
        }

        .increase { color: #e74c3c; }
        .stable { color: #f39c12; }

        .chart-container {
            background: white;
            padding: 30px;
            margin: 20px 0;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        .chart-title {
            font-size: 1.8em;
            margin-bottom: 15px;
            color: #2c3e50;
            border-left: 5px solid #667eea;
            padding-left: 15px;
        }

        .insights-box {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 15px;
            margin: 20px 0;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        .insights-box h2 {
            margin-bottom: 20px;
            font-size: 2em;
        }

        .insight-item {
            background: rgba(255,255,255,0.1);
            padding: 15px;
            margin: 15px 0;
            border-radius: 10px;
            border-left: 4px solid white;
        }

        .insight-item h3 {
            margin-bottom: 8px;
            font-size: 1.3em;
        }

        .controls {
            background: white;
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 20px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        .control-group {
            display: inline-block;
            margin-right: 20px;
        }

        .control-group label {
            font-weight: bold;
            margin-right: 10px;
            color: #2c3e50;
        }

        .control-group select {
            padding: 10px;
            border-radius: 8px;
            border: 2px solid #667eea;
            font-size: 1em;
            cursor: pointer;
        }

        .export-btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 12px 30px;
            border: none;
            border-radius: 8px;
            font-size: 1em;
            cursor: pointer;
            transition: transform 0.3s ease;
            float: right;
        }

        .export-btn:hover {
            transform: scale(1.05);
        }

        .footer {
            background: white;
            padding: 30px;
            margin-top: 30px;
            border-radius: 15px;
            text-align: center;
            color: #7f8c8d;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        @media (max-width: 768px) {
            .header h1 {
                font-size: 2em;
            }
            .stats-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏥 India Obesity Dashboard</h1>
            <p>Comprehensive Analysis of Obesity Trends (1998-2021)</p>
            <p style="font-size: 0.9em; margin-top: 10px;">Based on DHS Survey Data | Enhanced Interactive Version</p>
        </div>
"""

# Calculate key statistics
latest_data = df[df['Category'] == 'Total'].sort_values('Survey_Year').iloc[-1]
earliest_data = df[df['Category'] == 'Total'].sort_values('Survey_Year').iloc[0]

children_change = latest_data['Children_Overweight_Pct'] - earliest_data['Children_Overweight_Pct']
women_change = latest_data['Women_Overweight_Pct'] - earliest_data['Women_Overweight_Pct']
men_latest = latest_data['Men_Overweight_Pct']

# Stats cards
html_content += f"""
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-label">Children Overweight</div>
                <div class="stat-value" style="color: #FF6B6B;">{latest_data['Children_Overweight_Pct']:.1f}%</div>
                <div class="stat-change increase">↑ {children_change:.1f}% since 1998</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Women Overweight/Obese</div>
                <div class="stat-value" style="color: #4ECDC4;">{latest_data['Women_Overweight_Pct']:.1f}%</div>
                <div class="stat-change increase">↑ {women_change:.1f}% since 1998</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Men Overweight/Obese</div>
                <div class="stat-value" style="color: #95E1D3;">{men_latest:.1f}%</div>
                <div class="stat-change increase">Latest Survey (2019)</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Survey Years</div>
                <div class="stat-value" style="color: #667eea;">4</div>
                <div class="stat-change stable">1998, 2005, 2015, 2019</div>
            </div>
        </div>
"""

# Insights box
html_content += """
        <div class="insights-box">
            <h2>🔍 Key Insights from the Data</h2>

            <div class="insight-item">
                <h3>⚠️ Rising Obesity Epidemic</h3>
                <p>Obesity rates have increased dramatically across all demographics from 1998 to 2021. Women's obesity has more than doubled (10.7% → 24.0%), representing a critical public health challenge.</p>
            </div>

            <div class="insight-item">
                <h3>🏙️ Urban-Rural Divide</h3>
                <p>Urban areas show significantly higher obesity rates (Women: 33.3% vs 19.7% rural). Urban lifestyle, dietary changes, and reduced physical activity are major contributors.</p>
            </div>

            <div class="insight-item">
                <h3>💰 Wealth Paradox</h3>
                <p>Higher wealth correlates strongly with higher obesity risk. The highest wealth quintile has nearly 4x the obesity rate of the lowest quintile (Women: 38.6% vs 10.0%).</p>
            </div>

            <div class="insight-item">
                <h3>👥 Age Factor</h3>
                <p>Obesity rates increase steadily with age, peaking in the 45-49 age group at 37% for women. This suggests cumulative lifestyle impacts over time.</p>
            </div>

            <div class="insight-item">
                <h3>🎓 Education Impact</h3>
                <p>Higher education shows mixed results - while awareness may be higher, lifestyle factors in educated urban populations contribute to increased obesity rates.</p>
            </div>
        </div>
"""

# Overall trend chart
total_data = df[df['Category'] == 'Total'].sort_values('Survey_Year')

fig1 = go.Figure()

fig1.add_trace(go.Scatter(
    x=total_data['Survey_Year'],
    y=total_data['Children_Overweight_Pct'],
    name='Children Overweight',
    mode='lines+markers',
    line=dict(color='#FF6B6B', width=4),
    marker=dict(size=12),
    hovertemplate='Year: %{x}<br>Children: %{y:.1f}%<extra></extra>'
))

fig1.add_trace(go.Scatter(
    x=total_data['Survey_Year'],
    y=total_data['Women_Overweight_Pct'],
    name='Women Overweight/Obese',
    mode='lines+markers',
    line=dict(color='#4ECDC4', width=4),
    marker=dict(size=12),
    hovertemplate='Year: %{x}<br>Women: %{y:.1f}%<extra></extra>'
))

fig1.add_trace(go.Scatter(
    x=total_data['Survey_Year'],
    y=total_data['Men_Overweight_Pct'],
    name='Men Overweight/Obese',
    mode='lines+markers',
    line=dict(color='#95E1D3', width=4),
    marker=dict(size=12),
    hovertemplate='Year: %{x}<br>Men: %{y:.1f}%<extra></extra>'
))

fig1.update_layout(
    title='📈 Overall Obesity Trends in India (1998-2021)',
    xaxis_title='Survey Year',
    yaxis_title='Prevalence (%)',
    hovermode='x unified',
    height=500,
    template='plotly_white',
    font=dict(size=14),
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5)
)

html_content += f"""
        <div class="chart-container">
            <div class="chart-title">Overall Trends</div>
            {fig1.to_html(include_plotlyjs=False, div_id='trend_chart')}
        </div>
"""

# State comparison - Top 15 states for latest year
states_data = df[(df['Category'] == 'States') & (df['Survey_Year'] == 2019)].copy()
states_data = states_data.nlargest(15, 'Women_Overweight_Pct')

fig2 = go.Figure()

fig2.add_trace(go.Bar(
    name='Women',
    x=states_data['Subcategory'].str.replace('States : ', '').str.replace(' (L1)', ''),
    y=states_data['Women_Overweight_Pct'],
    marker_color='#4ECDC4',
    hovertemplate='%{x}<br>Women: %{y:.1f}%<extra></extra>'
))

fig2.add_trace(go.Bar(
    name='Men',
    x=states_data['Subcategory'].str.replace('States : ', '').str.replace(' (L1)', ''),
    y=states_data['Men_Overweight_Pct'],
    marker_color='#95E1D3',
    hovertemplate='%{x}<br>Men: %{y:.1f}%<extra></extra>'
))

fig2.add_trace(go.Bar(
    name='Children',
    x=states_data['Subcategory'].str.replace('States : ', '').str.replace(' (L1)', ''),
    y=states_data['Children_Overweight_Pct'],
    marker_color='#FF6B6B',
    hovertemplate='%{x}<br>Children: %{y:.1f}%<extra></extra>'
))

fig2.update_layout(
    title='🗺️ Top 15 States by Obesity Rate (2019-21 Survey)',
    xaxis_title='State/Territory',
    yaxis_title='Prevalence (%)',
    barmode='group',
    height=600,
    template='plotly_white',
    font=dict(size=12),
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5),
    xaxis={'tickangle': -45}
)

html_content += f"""
        <div class="chart-container">
            <div class="chart-title">State-by-State Comparison</div>
            {fig2.to_html(include_plotlyjs=False, div_id='states_chart')}
        </div>
"""

# Education level analysis - All years
education_data = df[df['Category'] == 'Education'].sort_values('Survey_Year')

fig3 = make_subplots(
    rows=1, cols=3,
    subplot_titles=('Children Overweight', 'Women Overweight/Obese', 'Men Overweight/Obese'),
    horizontal_spacing=0.1
)

education_levels = ['No education', 'Primary', 'Secondary', 'Higher']
colors = ['#e74c3c', '#f39c12', '#3498db', '#2ecc71']

for i, edu_level in enumerate(education_levels):
    edu_subset = education_data[education_data['Subcategory'] == edu_level]

    # Children
    fig3.add_trace(go.Scatter(
        x=edu_subset['Survey_Year'],
        y=edu_subset['Children_Overweight_Pct'],
        name=edu_level,
        mode='lines+markers',
        line=dict(color=colors[i], width=3),
        marker=dict(size=8),
        legendgroup=edu_level,
        showlegend=True
    ), row=1, col=1)

    # Women
    fig3.add_trace(go.Scatter(
        x=edu_subset['Survey_Year'],
        y=edu_subset['Women_Overweight_Pct'],
        name=edu_level,
        mode='lines+markers',
        line=dict(color=colors[i], width=3),
        marker=dict(size=8),
        legendgroup=edu_level,
        showlegend=False
    ), row=1, col=2)

    # Men
    fig3.add_trace(go.Scatter(
        x=edu_subset['Survey_Year'],
        y=edu_subset['Men_Overweight_Pct'],
        name=edu_level,
        mode='lines+markers',
        line=dict(color=colors[i], width=3),
        marker=dict(size=8),
        legendgroup=edu_level,
        showlegend=False
    ), row=1, col=3)

fig3.update_xaxes(title_text="Year", row=1, col=1)
fig3.update_xaxes(title_text="Year", row=1, col=2)
fig3.update_xaxes(title_text="Year", row=1, col=3)

fig3.update_yaxes(title_text="Prevalence (%)", row=1, col=1)
fig3.update_yaxes(title_text="Prevalence (%)", row=1, col=2)
fig3.update_yaxes(title_text="Prevalence (%)", row=1, col=3)

fig3.update_layout(
    title_text='🎓 Education Level Impact on Obesity Over Time',
    height=500,
    template='plotly_white',
    font=dict(size=12),
    legend=dict(orientation='h', yanchor='bottom', y=-0.2, xanchor='center', x=0.5),
    hovermode='x unified'
)

html_content += f"""
        <div class="chart-container">
            <div class="chart-title">Education Level Analysis</div>
            {fig3.to_html(include_plotlyjs=False, div_id='education_chart')}
        </div>
"""

# Wealth quintile detailed analysis
wealth_data = df[df['Category'] == 'Wealth quintile'].sort_values(['Survey_Year', 'Subcategory'])
wealth_order = ['Lowest', 'Second', 'Middle', 'Fourth', 'Highest']

fig4 = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Women - All Years', 'Men - All Years',
                    'Children - All Years', 'Latest Survey Comparison'),
    specs=[[{'type': 'scatter'}, {'type': 'scatter'}],
           [{'type': 'scatter'}, {'type': 'bar'}]],
    horizontal_spacing=0.12,
    vertical_spacing=0.15
)

# Women trends
for year in sorted(wealth_data['Survey_Year'].unique()):
    year_data = wealth_data[wealth_data['Survey_Year'] == year]
    year_data = year_data.set_index('Subcategory').reindex(wealth_order).reset_index()

    fig4.add_trace(go.Scatter(
        x=year_data['Subcategory'],
        y=year_data['Women_Overweight_Pct'],
        name=f'{year}',
        mode='lines+markers',
        line=dict(width=3),
        marker=dict(size=8)
    ), row=1, col=1)

# Men trends
for year in sorted(wealth_data['Survey_Year'].unique()):
    year_data = wealth_data[wealth_data['Survey_Year'] == year]
    year_data = year_data.set_index('Subcategory').reindex(wealth_order).reset_index()

    fig4.add_trace(go.Scatter(
        x=year_data['Subcategory'],
        y=year_data['Men_Overweight_Pct'],
        name=f'{year}',
        mode='lines+markers',
        line=dict(width=3),
        marker=dict(size=8),
        showlegend=False
    ), row=1, col=2)

# Children trends
for year in sorted(wealth_data['Survey_Year'].unique()):
    year_data = wealth_data[wealth_data['Survey_Year'] == year]
    year_data = year_data.set_index('Subcategory').reindex(wealth_order).reset_index()

    fig4.add_trace(go.Scatter(
        x=year_data['Subcategory'],
        y=year_data['Children_Overweight_Pct'],
        name=f'{year}',
        mode='lines+markers',
        line=dict(width=3),
        marker=dict(size=8),
        showlegend=False
    ), row=2, col=1)

# Latest year comparison
latest_wealth = wealth_data[wealth_data['Survey_Year'] == 2019]
latest_wealth = latest_wealth.set_index('Subcategory').reindex(wealth_order).reset_index()

fig4.add_trace(go.Bar(
    x=latest_wealth['Subcategory'],
    y=latest_wealth['Children_Overweight_Pct'],
    name='Children',
    marker_color='#FF6B6B'
), row=2, col=2)

fig4.add_trace(go.Bar(
    x=latest_wealth['Subcategory'],
    y=latest_wealth['Women_Overweight_Pct'],
    name='Women',
    marker_color='#4ECDC4'
), row=2, col=2)

fig4.add_trace(go.Bar(
    x=latest_wealth['Subcategory'],
    y=latest_wealth['Men_Overweight_Pct'],
    name='Men',
    marker_color='#95E1D3'
), row=2, col=2)

fig4.update_xaxes(title_text="Wealth Quintile", row=1, col=1)
fig4.update_xaxes(title_text="Wealth Quintile", row=1, col=2)
fig4.update_xaxes(title_text="Wealth Quintile", row=2, col=1)
fig4.update_xaxes(title_text="Wealth Quintile", row=2, col=2)

fig4.update_yaxes(title_text="Women (%)", row=1, col=1)
fig4.update_yaxes(title_text="Men (%)", row=1, col=2)
fig4.update_yaxes(title_text="Children (%)", row=2, col=1)
fig4.update_yaxes(title_text="Prevalence (%)", row=2, col=2)

fig4.update_layout(
    title_text='💰 Wealth Quintile Impact - Comprehensive Analysis',
    height=800,
    template='plotly_white',
    font=dict(size=11),
    showlegend=True,
    legend=dict(orientation='h', yanchor='bottom', y=-0.1, xanchor='center', x=0.5)
)

html_content += f"""
        <div class="chart-container">
            <div class="chart-title">Wealth Quintile Detailed Analysis</div>
            {fig4.to_html(include_plotlyjs=False, div_id='wealth_chart')}
        </div>
"""

# Urban vs Rural over time
residence_data = df[df['Category'] == 'Residence'].sort_values('Survey_Year')

fig5 = make_subplots(
    rows=1, cols=3,
    subplot_titles=('Children Overweight', 'Women Overweight/Obese', 'Men Overweight/Obese')
)

urban_data = residence_data[residence_data['Subcategory'] == 'Urban']
rural_data = residence_data[residence_data['Subcategory'] == 'Rural']

# Children
fig5.add_trace(go.Bar(
    name='Urban',
    x=urban_data['Survey_Year'],
    y=urban_data['Children_Overweight_Pct'],
    marker_color='#FF6B6B'
), row=1, col=1)

fig5.add_trace(go.Bar(
    name='Rural',
    x=rural_data['Survey_Year'],
    y=rural_data['Children_Overweight_Pct'],
    marker_color='#4ECDC4'
), row=1, col=1)

# Women
fig5.add_trace(go.Bar(
    name='Urban',
    x=urban_data['Survey_Year'],
    y=urban_data['Women_Overweight_Pct'],
    marker_color='#FF6B6B',
    showlegend=False
), row=1, col=2)

fig5.add_trace(go.Bar(
    name='Rural',
    x=rural_data['Survey_Year'],
    y=rural_data['Women_Overweight_Pct'],
    marker_color='#4ECDC4',
    showlegend=False
), row=1, col=3)

# Men
fig5.add_trace(go.Bar(
    name='Urban',
    x=urban_data['Survey_Year'],
    y=urban_data['Men_Overweight_Pct'],
    marker_color='#FF6B6B',
    showlegend=False
), row=1, col=3)

fig5.add_trace(go.Bar(
    name='Rural',
    x=rural_data['Survey_Year'],
    y=rural_data['Men_Overweight_Pct'],
    marker_color='#4ECDC4',
    showlegend=False
), row=1, col=3)

fig5.update_xaxes(title_text="Year", row=1, col=1)
fig5.update_xaxes(title_text="Year", row=1, col=2)
fig5.update_xaxes(title_text="Year", row=1, col=3)

fig5.update_yaxes(title_text="Prevalence (%)", row=1, col=1)
fig5.update_yaxes(title_text="Prevalence (%)", row=1, col=2)
fig5.update_yaxes(title_text="Prevalence (%)", row=1, col=3)

fig5.update_layout(
    title_text='🏙️ Urban vs Rural Obesity Rates Over Time',
    height=500,
    template='plotly_white',
    font=dict(size=12),
    barmode='group',
    legend=dict(orientation='h', yanchor='bottom', y=1.08, xanchor='center', x=0.5)
)

html_content += f"""
        <div class="chart-container">
            <div class="chart-title">Urban vs Rural Trends</div>
            {fig5.to_html(include_plotlyjs=False, div_id='residence_chart')}
        </div>
"""

# Age group analysis
age_data = df[df['Category'] == 'Age (5-year groups)'].sort_values(['Survey_Year', 'Subcategory'])

fig6 = make_subplots(
    rows=1, cols=2,
    subplot_titles=('Women by Age Group', 'Men by Age Group')
)

for year in sorted(age_data['Survey_Year'].unique()):
    year_data = age_data[age_data['Survey_Year'] == year]

    fig6.add_trace(go.Scatter(
        x=year_data['Subcategory'],
        y=year_data['Women_Overweight_Pct'],
        name=f'{year}',
        mode='lines+markers',
        line=dict(width=3),
        marker=dict(size=8)
    ), row=1, col=1)

    fig6.add_trace(go.Scatter(
        x=year_data['Subcategory'],
        y=year_data['Men_Overweight_Pct'],
        name=f'{year}',
        mode='lines+markers',
        line=dict(width=3),
        marker=dict(size=8),
        showlegend=False
    ), row=1, col=2)

fig6.update_xaxes(title_text="Age Group", row=1, col=1)
fig6.update_xaxes(title_text="Age Group", row=1, col=2)

fig6.update_yaxes(title_text="Prevalence (%)", row=1, col=1)
fig6.update_yaxes(title_text="Prevalence (%)", row=1, col=2)

fig6.update_layout(
    title_text='👥 Age Group Analysis Across Survey Years',
    height=500,
    template='plotly_white',
    font=dict(size=12),
    legend=dict(orientation='h', yanchor='bottom', y=-0.2, xanchor='center', x=0.5),
    hovermode='x unified'
)

html_content += f"""
        <div class="chart-container">
            <div class="chart-title">Age Group Trends</div>
            {fig6.to_html(include_plotlyjs=False, div_id='age_chart')}
        </div>
"""

# Data export functionality and footer
html_content += """
        <div class="chart-container">
            <div class="chart-title">📥 Export Data</div>
            <p style="margin-bottom: 20px; color: #7f8c8d;">Download the complete dataset for your own analysis</p>
            <button class="export-btn" onclick="exportToCSV()">Download CSV</button>
            <button class="export-btn" onclick="exportToJSON()" style="margin-left: 10px;">Download JSON</button>
            <div style="clear: both;"></div>
        </div>

        <div class="footer">
            <h3 style="color: #2c3e50; margin-bottom: 15px;">About This Dashboard</h3>
            <p><strong>Data Source:</strong> DHS Program STATcompiler (ICF, 2015)</p>
            <p><strong>Analysis Period:</strong> 1998-2021 | <strong>Geographic Focus:</strong> India</p>
            <p><strong>Total Records:</strong> 215 data points across 4 survey periods</p>
            <p style="margin-top: 15px; font-size: 0.9em;">Dashboard created with Python (pandas, plotly) | All charts are interactive - hover, zoom, and pan to explore</p>
            <p style="margin-top: 10px; font-size: 0.85em; color: #95a5a6;">Enhanced version with comprehensive visualizations and export capabilities</p>
        </div>
    </div>

    <script>
        // Export functionality
        const csvData = `""" + df.to_csv(index=False).replace('`', '\\`').replace('${', '\\${') + """`;

        function exportToCSV() {
            const blob = new Blob([csvData], { type: 'text/csv;charset=utf-8;' });
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = 'india_obesity_data.csv';
            link.click();
        }

        function exportToJSON() {
            const lines = csvData.split('\\n');
            const headers = lines[0].split(',');
            const jsonData = [];

            for (let i = 1; i < lines.length - 1; i++) {
                const obj = {};
                const currentLine = lines[i].split(',');

                for (let j = 0; j < headers.length; j++) {
                    obj[headers[j]] = currentLine[j];
                }
                jsonData.push(obj);
            }

            const blob = new Blob([JSON.stringify(jsonData, null, 2)], { type: 'application/json' });
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = 'india_obesity_data.json';
            link.click();
        }

        // Smooth scroll for better UX
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });
    </script>
</body>
</html>
"""

# Write the enhanced dashboard
with open('obesity_dashboard_enhanced.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Enhanced dashboard created successfully!")
print("File: obesity_dashboard_enhanced.html")
print("Open the file in your browser to view the interactive dashboard")
