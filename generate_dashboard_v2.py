import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load the dataset
df = pd.read_csv('obesity_data_cleaned.csv')

# Professional color palette
COLORS = {
    'primary': '#2C3E50',      # Dark blue-gray
    'secondary': '#3498DB',    # Bright blue
    'accent': '#E74C3C',       # Red
    'success': '#27AE60',      # Green
    'warning': '#F39C12',      # Orange
    'children': '#FF6B9D',     # Pink
    'women': '#4ECDC4',        # Teal
    'men': '#556270',          # Gray-blue
    'bg_light': '#ECF0F1',     # Light gray
    'text_dark': '#2C3E50',
    'text_light': '#7F8C8D'
}

# HTML header and styling
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>India Obesity Dashboard (1998-2021)</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #F5F7FA;
            padding: 20px;
            color: {COLORS['text_dark']};
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}

        .header {{
            background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['secondary']} 100%);
            color: white;
            padding: 50px 40px;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}

        .header h1 {{
            font-size: 2.8em;
            margin-bottom: 10px;
            font-weight: 600;
        }}

        .header p {{
            font-size: 1.1em;
            opacity: 0.95;
        }}

        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}

        .stat-card {{
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.08);
            border-left: 4px solid;
            transition: transform 0.2s, box-shadow 0.2s;
        }}

        .stat-card:hover {{
            transform: translateY(-3px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }}

        .stat-card.children {{ border-color: {COLORS['children']}; }}
        .stat-card.women {{ border-color: {COLORS['women']}; }}
        .stat-card.men {{ border-color: {COLORS['men']}; }}
        .stat-card.surveys {{ border-color: {COLORS['warning']}; }}

        .stat-label {{
            color: {COLORS['text_light']};
            font-size: 0.95em;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 10px;
        }}

        .stat-value {{
            font-size: 3em;
            font-weight: 700;
            margin: 10px 0;
        }}

        .stat-value.children {{ color: {COLORS['children']}; }}
        .stat-value.women {{ color: {COLORS['women']}; }}
        .stat-value.men {{ color: {COLORS['men']}; }}
        .stat-value.surveys {{ color: {COLORS['warning']}; }}

        .stat-change {{
            font-size: 1em;
            color: {COLORS['accent']};
            font-weight: 500;
        }}

        .chart-container {{
            background: white;
            padding: 30px;
            margin: 20px 0;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.08);
        }}

        .chart-title {{
            font-size: 1.6em;
            margin-bottom: 10px;
            color: {COLORS['primary']};
            font-weight: 600;
        }}

        .chart-subtitle {{
            font-size: 1em;
            color: {COLORS['text_light']};
            margin-bottom: 20px;
        }}

        .insights-section {{
            background: white;
            padding: 40px;
            margin: 30px 0;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.08);
        }}

        .insights-section h2 {{
            color: {COLORS['primary']};
            margin-bottom: 25px;
            font-size: 2em;
            font-weight: 600;
        }}

        .insight-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }}

        .insight-card {{
            background: {COLORS['bg_light']};
            padding: 20px;
            border-radius: 8px;
            border-left: 3px solid {COLORS['secondary']};
        }}

        .insight-card h3 {{
            color: {COLORS['primary']};
            margin-bottom: 10px;
            font-size: 1.2em;
        }}

        .insight-card p {{
            color: {COLORS['text_dark']};
            line-height: 1.6;
        }}

        .export-section {{
            background: white;
            padding: 30px;
            margin: 30px 0;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.08);
            text-align: center;
        }}

        .export-btn {{
            background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['secondary']} 100%);
            color: white;
            padding: 15px 40px;
            border: none;
            border-radius: 6px;
            font-size: 1em;
            font-weight: 600;
            cursor: pointer;
            margin: 10px;
            transition: transform 0.2s, box-shadow 0.2s;
        }}

        .export-btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }}

        .footer {{
            text-align: center;
            padding: 30px;
            color: {COLORS['text_light']};
            margin-top: 40px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>India Obesity Dashboard</h1>
            <p>Comprehensive Analysis of Obesity Trends (1998-2021)</p>
            <p style="font-size: 0.9em; margin-top: 10px; opacity: 0.9;">Based on DHS Survey Data</p>
        </div>
"""

# Calculate key statistics
latest_data = df[df['Category'] == 'Total'].sort_values('Survey_Year').iloc[-1]
earliest_data = df[df['Category'] == 'Total'].sort_values('Survey_Year').iloc[0]

children_change = latest_data['Children_Overweight_Pct'] - earliest_data['Children_Overweight_Pct']
women_change = latest_data['Women_Overweight_Pct'] - earliest_data['Women_Overweight_Pct']

# Stats cards
html_content += f"""
        <div class="stats-grid">
            <div class="stat-card children">
                <div class="stat-label">Children Overweight</div>
                <div class="stat-value children">{latest_data['Children_Overweight_Pct']:.1f}%</div>
                <div class="stat-change">+{children_change:.1f}% since 1998</div>
            </div>
            <div class="stat-card women">
                <div class="stat-label">Women Overweight/Obese</div>
                <div class="stat-value women">{latest_data['Women_Overweight_Pct']:.1f}%</div>
                <div class="stat-change">+{women_change:.1f}% since 1998</div>
            </div>
            <div class="stat-card men">
                <div class="stat-label">Men Overweight/Obese</div>
                <div class="stat-value men">{latest_data['Men_Overweight_Pct']:.1f}%</div>
                <div class="stat-change">Latest Survey (2019)</div>
            </div>
            <div class="stat-card surveys">
                <div class="stat-label">Survey Years</div>
                <div class="stat-value surveys">4</div>
                <div class="stat-change">1998, 2005, 2015, 2019</div>
            </div>
        </div>
"""

# Insights section
html_content += f"""
        <div class="insights-section">
            <h2>Key Insights</h2>
            <div class="insight-grid">
                <div class="insight-card">
                    <h3>Rising Epidemic</h3>
                    <p>Obesity rates have more than doubled from 1998 to 2021. Women's obesity increased by {women_change:.1f} percentage points, representing a critical public health challenge.</p>
                </div>
                <div class="insight-card">
                    <h3>Urban-Rural Divide</h3>
                    <p>Urban areas show 69% higher obesity rates for women (33.3% vs 19.7% rural). Lifestyle and dietary changes are major contributors.</p>
                </div>
                <div class="insight-card">
                    <h3>Wealth Impact</h3>
                    <p>The highest wealth quintile has nearly 4x the obesity rate of the lowest quintile. Higher income correlates with higher obesity risk.</p>
                </div>
                <div class="insight-card">
                    <h3>Age Factor</h3>
                    <p>Obesity rates increase steadily with age, peaking at 45-49 years (37% for women), suggesting cumulative lifestyle impacts.</p>
                </div>
            </div>
        </div>
"""

# Chart 1: Overall Trends
total_data = df[df['Category'] == 'Total'].sort_values('Survey_Year')

fig1 = go.Figure()

fig1.add_trace(go.Scatter(
    x=total_data['Survey_Year'],
    y=total_data['Children_Overweight_Pct'],
    name='Children Overweight',
    mode='lines+markers',
    line=dict(color=COLORS['children'], width=3),
    marker=dict(size=10),
    hovertemplate='Year: %{x}<br>Children: %{y:.1f}%<extra></extra>'
))

fig1.add_trace(go.Scatter(
    x=total_data['Survey_Year'],
    y=total_data['Women_Overweight_Pct'],
    name='Women Overweight/Obese',
    mode='lines+markers',
    line=dict(color=COLORS['women'], width=3),
    marker=dict(size=10),
    hovertemplate='Year: %{x}<br>Women: %{y:.1f}%<extra></extra>'
))

fig1.add_trace(go.Scatter(
    x=total_data['Survey_Year'],
    y=total_data['Men_Overweight_Pct'],
    name='Men Overweight/Obese',
    mode='lines+markers',
    line=dict(color=COLORS['men'], width=3),
    marker=dict(size=10),
    hovertemplate='Year: %{x}<br>Men: %{y:.1f}%<extra></extra>'
))

fig1.update_layout(
    xaxis_title='Survey Year',
    yaxis_title='Prevalence (%)',
    hovermode='x unified',
    height=500,
    template='plotly_white',
    font=dict(size=14, family='Segoe UI'),
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5),
    plot_bgcolor='white',
    paper_bgcolor='white'
)

html_content += f"""
        <div class="chart-container">
            <div class="chart-title">Overall Obesity Trends</div>
            <div class="chart-subtitle">Progression from 1998 to 2021 across all demographics</div>
            {fig1.to_html(include_plotlyjs=False, div_id='trend_chart')}
        </div>
"""

# Chart 2: State Comparison
states_data = df[(df['Category'] == 'States') & (df['Survey_Year'] == 2019)].copy()
states_data = states_data.nlargest(15, 'Women_Overweight_Pct')
states_data['State_Short'] = states_data['Subcategory'].str.replace('States : ', '').str.replace(' (L1)', '')

fig2 = go.Figure()

fig2.add_trace(go.Bar(
    name='Women',
    x=states_data['State_Short'],
    y=states_data['Women_Overweight_Pct'],
    marker_color=COLORS['women'],
    hovertemplate='%{x}<br>Women: %{y:.1f}%<extra></extra>'
))

fig2.add_trace(go.Bar(
    name='Men',
    x=states_data['State_Short'],
    y=states_data['Men_Overweight_Pct'],
    marker_color=COLORS['men'],
    hovertemplate='%{x}<br>Men: %{y:.1f}%<extra></extra>'
))

fig2.add_trace(go.Bar(
    name='Children',
    x=states_data['State_Short'],
    y=states_data['Children_Overweight_Pct'],
    marker_color=COLORS['children'],
    hovertemplate='%{x}<br>Children: %{y:.1f}%<extra></extra>'
))

fig2.update_layout(
    xaxis_title='State/Territory',
    yaxis_title='Prevalence (%)',
    barmode='group',
    height=600,
    template='plotly_white',
    font=dict(size=12, family='Segoe UI'),
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5),
    xaxis={'tickangle': -45},
    plot_bgcolor='white',
    paper_bgcolor='white'
)

html_content += f"""
        <div class="chart-container">
            <div class="chart-title">Top 15 States by Obesity Rate</div>
            <div class="chart-subtitle">2019-21 Survey Data</div>
            {fig2.to_html(include_plotlyjs=False, div_id='states_chart')}
        </div>
"""

# Chart 3: Urban vs Rural
residence_data = df[df['Category'] == 'Residence'].sort_values('Survey_Year')
urban_data = residence_data[residence_data['Subcategory'] == 'Urban']
rural_data = residence_data[residence_data['Subcategory'] == 'Rural']

fig3 = make_subplots(
    rows=1, cols=3,
    subplot_titles=('Children Overweight', 'Women Overweight/Obese', 'Men Overweight/Obese')
)

# Children
fig3.add_trace(go.Bar(
    name='Urban',
    x=urban_data['Survey_Year'],
    y=urban_data['Children_Overweight_Pct'],
    marker_color=COLORS['secondary']
), row=1, col=1)

fig3.add_trace(go.Bar(
    name='Rural',
    x=rural_data['Survey_Year'],
    y=rural_data['Children_Overweight_Pct'],
    marker_color=COLORS['success']
), row=1, col=1)

# Women
fig3.add_trace(go.Bar(
    name='Urban',
    x=urban_data['Survey_Year'],
    y=urban_data['Women_Overweight_Pct'],
    marker_color=COLORS['secondary'],
    showlegend=False
), row=1, col=2)

fig3.add_trace(go.Bar(
    name='Rural',
    x=rural_data['Survey_Year'],
    y=rural_data['Women_Overweight_Pct'],
    marker_color=COLORS['success'],
    showlegend=False
), row=1, col=2)

# Men
fig3.add_trace(go.Bar(
    name='Urban',
    x=urban_data['Survey_Year'],
    y=urban_data['Men_Overweight_Pct'],
    marker_color=COLORS['secondary'],
    showlegend=False
), row=1, col=3)

fig3.add_trace(go.Bar(
    name='Rural',
    x=rural_data['Survey_Year'],
    y=rural_data['Men_Overweight_Pct'],
    marker_color=COLORS['success'],
    showlegend=False
), row=1, col=3)

fig3.update_xaxes(title_text="Year", row=1, col=1)
fig3.update_xaxes(title_text="Year", row=1, col=2)
fig3.update_xaxes(title_text="Year", row=1, col=3)

fig3.update_yaxes(title_text="Prevalence (%)", row=1, col=1)
fig3.update_yaxes(title_text="Prevalence (%)", row=1, col=2)
fig3.update_yaxes(title_text="Prevalence (%)", row=1, col=3)

fig3.update_layout(
    height=500,
    template='plotly_white',
    font=dict(size=12, family='Segoe UI'),
    barmode='group',
    legend=dict(orientation='h', yanchor='bottom', y=1.08, xanchor='center', x=0.5),
    plot_bgcolor='white',
    paper_bgcolor='white'
)

html_content += f"""
        <div class="chart-container">
            <div class="chart-title">Urban vs Rural Comparison</div>
            <div class="chart-subtitle">Obesity rates across survey years</div>
            {fig3.to_html(include_plotlyjs=False, div_id='residence_chart')}
        </div>
"""

# Chart 4: Wealth Quintile
wealth_data = df[df['Category'] == 'Wealth quintile'].sort_values(['Survey_Year', 'Subcategory'])
latest_wealth = wealth_data[wealth_data['Survey_Year'] == 2019]
wealth_order = ['Lowest', 'Second', 'Middle', 'Fourth', 'Highest']
latest_wealth = latest_wealth.set_index('Subcategory').reindex(wealth_order).reset_index()

fig4 = go.Figure()

fig4.add_trace(go.Bar(
    x=latest_wealth['Subcategory'],
    y=latest_wealth['Children_Overweight_Pct'],
    name='Children',
    marker_color=COLORS['children']
))

fig4.add_trace(go.Bar(
    x=latest_wealth['Subcategory'],
    y=latest_wealth['Women_Overweight_Pct'],
    name='Women',
    marker_color=COLORS['women']
))

fig4.add_trace(go.Bar(
    x=latest_wealth['Subcategory'],
    y=latest_wealth['Men_Overweight_Pct'],
    name='Men',
    marker_color=COLORS['men']
))

fig4.update_layout(
    xaxis_title='Wealth Quintile',
    yaxis_title='Prevalence (%)',
    barmode='group',
    height=500,
    template='plotly_white',
    font=dict(size=14, family='Segoe UI'),
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5),
    plot_bgcolor='white',
    paper_bgcolor='white'
)

html_content += f"""
        <div class="chart-container">
            <div class="chart-title">Wealth Quintile Impact</div>
            <div class="chart-subtitle">2019-21 Survey - Higher wealth correlates with higher obesity</div>
            {fig4.to_html(include_plotlyjs=False, div_id='wealth_chart')}
        </div>
"""

# Chart 5: Age Groups
age_data = df[df['Category'] == 'Age (5-year groups)']
latest_age = age_data[age_data['Survey_Year'] == 2019]

fig5 = go.Figure()

fig5.add_trace(go.Bar(
    name='Women',
    x=latest_age['Subcategory'],
    y=latest_age['Women_Overweight_Pct'],
    marker_color=COLORS['women']
))

fig5.add_trace(go.Bar(
    name='Men',
    x=latest_age['Subcategory'],
    y=latest_age['Men_Overweight_Pct'],
    marker_color=COLORS['men']
))

fig5.update_layout(
    xaxis_title='Age Group (years)',
    yaxis_title='Prevalence (%)',
    barmode='group',
    height=500,
    template='plotly_white',
    font=dict(size=14, family='Segoe UI'),
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5),
    plot_bgcolor='white',
    paper_bgcolor='white'
)

html_content += f"""
        <div class="chart-container">
            <div class="chart-title">Obesity by Age Group</div>
            <div class="chart-subtitle">2019-21 Survey - Obesity increases with age</div>
            {fig5.to_html(include_plotlyjs=False, div_id='age_chart')}
        </div>
"""

# Chart 6: Education Level
education_data = df[df['Category'] == 'Education']
latest_edu = education_data[education_data['Survey_Year'] == 2019]

fig6 = go.Figure()

fig6.add_trace(go.Bar(
    name='Children',
    x=latest_edu['Subcategory'],
    y=latest_edu['Children_Overweight_Pct'],
    marker_color=COLORS['children']
))

fig6.add_trace(go.Bar(
    name='Women',
    x=latest_edu['Subcategory'],
    y=latest_edu['Women_Overweight_Pct'],
    marker_color=COLORS['women']
))

fig6.add_trace(go.Bar(
    name='Men',
    x=latest_edu['Subcategory'],
    y=latest_edu['Men_Overweight_Pct'],
    marker_color=COLORS['men']
))

fig6.update_layout(
    xaxis_title='Education Level',
    yaxis_title='Prevalence (%)',
    barmode='group',
    height=500,
    template='plotly_white',
    font=dict(size=14, family='Segoe UI'),
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5),
    plot_bgcolor='white',
    paper_bgcolor='white'
)

html_content += f"""
        <div class="chart-container">
            <div class="chart-title">Education Level Impact</div>
            <div class="chart-subtitle">2019-21 Survey</div>
            {fig6.to_html(include_plotlyjs=False, div_id='education_chart')}
        </div>
"""

# Export section
html_content += """
        <div class="export-section">
            <h2 style="margin-bottom: 20px; color: """ + COLORS['primary'] + """;">Export Data</h2>
            <p style="margin-bottom: 20px; color: """ + COLORS['text_light'] + """;">Download the complete dataset for your own analysis</p>
            <button class="export-btn" onclick="exportToCSV()">Download CSV</button>
            <button class="export-btn" onclick="exportToJSON()">Download JSON</button>
        </div>

        <div class="footer">
            <p><strong>Data Source:</strong> DHS Program STATcompiler (ICF, 2015)</p>
            <p><strong>Analysis Period:</strong> 1998-2021 | <strong>Geographic Focus:</strong> India</p>
            <p style="margin-top: 15px;">Dashboard created with Python (pandas, plotly) | All charts are interactive</p>
        </div>
    </div>

    <script>
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
    </script>
</body>
</html>
"""

# Write the dashboard
with open('obesity_dashboard_enhanced.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Dashboard created successfully!")
print("File: obesity_dashboard_enhanced.html")
print("Open the file in your browser to view")
