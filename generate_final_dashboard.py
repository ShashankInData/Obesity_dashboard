import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load the dataset
df = pd.read_csv('obesity_data_cleaned.csv')

# Professional color palette
COLORS = {
    'primary': '#2C3E50',
    'secondary': '#3498DB',
    'accent': '#E74C3C',
    'success': '#27AE60',
    'warning': '#F39C12',
    'children': '#FF6B9D',
    'women': '#4ECDC4',
    'men': '#556270',
    'bg_light': '#ECF0F1',
    'text_dark': '#2C3E50',
    'text_light': '#7F8C8D'
}

print("Building dashboard with explanations...")

# Calculate key statistics
latest_data = df[df['Category'] == 'Total'].sort_values('Survey_Year').iloc[-1]
earliest_data = df[df['Category'] == 'Total'].sort_values('Survey_Year').iloc[0]

children_change = latest_data['Children_Overweight_Pct'] - earliest_data['Children_Overweight_Pct']
women_change = latest_data['Women_Overweight_Pct'] - earliest_data['Women_Overweight_Pct']

# HTML header with improved styling
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>India Obesity Dashboard (1998-2021)</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #F5F7FA;
            padding: 20px;
            color: {COLORS['text_dark']};
        }}

        .container {{ max-width: 1400px; margin: 0 auto; }}

        .header {{
            background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['secondary']} 100%);
            color: white;
            padding: 50px 40px;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}

        .header h1 {{ font-size: 2.8em; margin-bottom: 10px; font-weight: 600; }}
        .header p {{ font-size: 1.1em; opacity: 0.95; }}

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

        .explanation-box {{
            background: #EBF5FB;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
            border-left: 4px solid {COLORS['secondary']};
        }}

        .explanation-box h4 {{
            color: {COLORS['primary']};
            margin-bottom: 10px;
            font-size: 1.1em;
        }}

        .explanation-box p, .explanation-box ul {{
            color: {COLORS['text_dark']};
            line-height: 1.6;
            margin-bottom: 10px;
        }}

        .explanation-box ul {{
            padding-left: 20px;
        }}

        .height-selector {{
            display: flex;
            gap: 10px;
            margin-bottom: 15px;
        }}

        .height-selector button {{
            flex: 1;
            padding: 10px;
            border: 2px solid #ddd;
            background: white;
            border-radius: 6px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.2s;
        }}

        .height-selector button.active {{
            background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['secondary']} 100%);
            color: white;
            border-color: {COLORS['primary']};
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
            <p>Understanding Obesity Trends in India (1998-2021)</p>
            <p style="font-size: 0.9em; margin-top: 10px; opacity: 0.9;">Based on DHS Survey Data - Interactive Analysis Tool</p>
        </div>

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

# Chart 1: Overall Trends (THIS ONE WAS MISSING DATA!)
total_data = df[df['Category'] == 'Total'].sort_values('Survey_Year')

fig1 = go.Figure()

fig1.add_trace(go.Scatter(
    x=total_data['Survey_Year'].tolist(),
    y=total_data['Children_Overweight_Pct'].tolist(),
    name='Children Overweight',
    mode='lines+markers+text',
    line=dict(color=COLORS['children'], width=4),
    marker=dict(size=12),
    text=[f"{v:.1f}%" for v in total_data['Children_Overweight_Pct']],
    textposition='top center',
    hovertemplate='Year: %{x}<br>Children: %{y:.1f}%<extra></extra>'
))

fig1.add_trace(go.Scatter(
    x=total_data['Survey_Year'].tolist(),
    y=total_data['Women_Overweight_Pct'].tolist(),
    name='Women Overweight/Obese',
    mode='lines+markers+text',
    line=dict(color=COLORS['women'], width=4),
    marker=dict(size=12),
    text=[f"{v:.1f}%" for v in total_data['Women_Overweight_Pct']],
    textposition='top center',
    hovertemplate='Year: %{x}<br>Women: %{y:.1f}%<extra></extra>'
))

# Only add Men data where available
men_data = total_data[total_data['Men_Overweight_Pct'].notna()]
fig1.add_trace(go.Scatter(
    x=men_data['Survey_Year'].tolist(),
    y=men_data['Men_Overweight_Pct'].tolist(),
    name='Men Overweight/Obese',
    mode='lines+markers+text',
    line=dict(color=COLORS['men'], width=4),
    marker=dict(size=12),
    text=[f"{v:.1f}%" for v in men_data['Men_Overweight_Pct']],
    textposition='top center',
    hovertemplate='Year: %{x}<br>Men: %{y:.1f}%<extra></extra>'
))

fig1.update_layout(
    xaxis_title='Survey Year',
    yaxis_title='Percentage (%)',
    hovermode='x unified',
    height=500,
    template='plotly_white',
    font=dict(size=14, family='Segoe UI'),
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5),
    plot_bgcolor='white',
    paper_bgcolor='white',
    showlegend=True
)

html_content += f"""
        <div class="chart-container">
            <div class="chart-title">Overall Obesity Trends in India</div>
            <div class="chart-subtitle">How obesity rates have changed from 1998 to 2021</div>
            {fig1.to_html(include_plotlyjs=False, div_id='trend_chart', config={'displayModeBar': False})}

            <div class="explanation-box">
                <h4>What This Chart Shows:</h4>
                <p>This chart tracks obesity rates across all of India over 23 years. Each line shows a different group:</p>
                <ul>
                    <li><strong>Pink line (Children):</strong> Percentage of children who are overweight</li>
                    <li><strong>Teal line (Women):</strong> Percentage of women aged 15-49 who are overweight or obese</li>
                    <li><strong>Gray line (Men):</strong> Percentage of men aged 15-54 who are overweight or obese (data from 2005 onwards)</li>
                </ul>
                <p><strong>Key Finding:</strong> Women's obesity has MORE THAN DOUBLED from {earliest_data['Women_Overweight_Pct']:.1f}% in 1998 to {latest_data['Women_Overweight_Pct']:.1f}% in 2019. This is not genetic - it's due to lifestyle changes like more processed food, less physical activity, and more desk jobs.</p>
            </div>
        </div>
"""

# Chart 2: Urban vs Rural (FIX THE DATA DISPLAY!)
residence_data = df[df['Category'] == 'Residence'].sort_values('Survey_Year')
urban_data = residence_data[residence_data['Subcategory'] == 'Urban']
rural_data = residence_data[residence_data['Subcategory'] == 'Rural']

fig3 = make_subplots(
    rows=1, cols=3,
    subplot_titles=('Children Overweight', 'Women Overweight/Obese', 'Men Overweight/Obese'),
    horizontal_spacing=0.12
)

# Children
years = urban_data['Survey_Year'].tolist()
fig3.add_trace(go.Bar(
    name='City/Urban',
    x=years,
    y=urban_data['Children_Overweight_Pct'].tolist(),
    marker_color=COLORS['secondary'],
    text=[f"{v:.1f}%" for v in urban_data['Children_Overweight_Pct']],
    textposition='outside'
), row=1, col=1)

fig3.add_trace(go.Bar(
    name='Village/Rural',
    x=years,
    y=rural_data['Children_Overweight_Pct'].tolist(),
    marker_color=COLORS['success'],
    text=[f"{v:.1f}%" for v in rural_data['Children_Overweight_Pct']],
    textposition='outside'
), row=1, col=1)

# Women
fig3.add_trace(go.Bar(
    name='City/Urban',
    x=years,
    y=urban_data['Women_Overweight_Pct'].tolist(),
    marker_color=COLORS['secondary'],
    showlegend=False,
    text=[f"{v:.1f}%" for v in urban_data['Women_Overweight_Pct']],
    textposition='outside'
), row=1, col=2)

fig3.add_trace(go.Bar(
    name='Village/Rural',
    x=years,
    y=rural_data['Women_Overweight_Pct'].tolist(),
    marker_color=COLORS['success'],
    showlegend=False,
    text=[f"{v:.1f}%" for v in rural_data['Women_Overweight_Pct']],
    textposition='outside'
), row=1, col=2)

# Men (only where data exists)
men_urban = urban_data[urban_data['Men_Overweight_Pct'].notna()]
men_rural = rural_data[rural_data['Men_Overweight_Pct'].notna()]

fig3.add_trace(go.Bar(
    name='City/Urban',
    x=men_urban['Survey_Year'].tolist(),
    y=men_urban['Men_Overweight_Pct'].tolist(),
    marker_color=COLORS['secondary'],
    showlegend=False,
    text=[f"{v:.1f}%" for v in men_urban['Men_Overweight_Pct']],
    textposition='outside'
), row=1, col=3)

fig3.add_trace(go.Bar(
    name='Village/Rural',
    x=men_rural['Survey_Year'].tolist(),
    y=men_rural['Men_Overweight_Pct'].tolist(),
    marker_color=COLORS['success'],
    showlegend=False,
    text=[f"{v:.1f}%" for v in men_rural['Men_Overweight_Pct']],
    textposition='outside'
), row=1, col=3)

fig3.update_xaxes(title_text="Year", row=1, col=1)
fig3.update_xaxes(title_text="Year", row=1, col=2)
fig3.update_xaxes(title_text="Year", row=1, col=3)

fig3.update_yaxes(title_text="Percentage (%)", row=1, col=1, range=[0, 40])
fig3.update_yaxes(title_text="Percentage (%)", row=1, col=2, range=[0, 40])
fig3.update_yaxes(title_text="Percentage (%)", row=1, col=3, range=[0, 40])

fig3.update_layout(
    height=550,
    template='plotly_white',
    font=dict(size=12, family='Segoe UI'),
    barmode='group',
    legend=dict(orientation='h', yanchor='bottom', y=1.08, xanchor='center', x=0.5),
    plot_bgcolor='white',
    paper_bgcolor='white'
)

latest_urban = urban_data[urban_data['Survey_Year'] == 2019].iloc[0]
latest_rural = rural_data[rural_data['Survey_Year'] == 2019].iloc[0]

html_content += f"""
        <div class="chart-container">
            <div class="chart-title">City vs Village Comparison</div>
            <div class="chart-subtitle">Why living in a city increases your risk</div>
            {fig3.to_html(include_plotlyjs=False, div_id='residence_chart', config={'displayModeBar': False})}

            <div class="explanation-box">
                <h4>What This Chart Shows:</h4>
                <p>This compares obesity rates between people living in cities (urban) vs villages (rural) over time.</p>

                <p><strong>Latest Data (2019):</strong></p>
                <ul>
                    <li><strong>Women in cities:</strong> {latest_urban['Women_Overweight_Pct']:.1f}% obese</li>
                    <li><strong>Women in villages:</strong> {latest_rural['Women_Overweight_Pct']:.1f}% obese</li>
                    <li><strong>Difference:</strong> City women are {((latest_urban['Women_Overweight_Pct']/latest_rural['Women_Overweight_Pct'])-1)*100:.0f}% MORE likely to be obese!</li>
                </ul>

                <p><strong>Why Cities Are Riskier:</strong></p>
                <ul>
                    <li>Office jobs mean sitting all day (villages = farming/walking)</li>
                    <li>Cars and metros instead of walking</li>
                    <li>Easy access to fast food and restaurants</li>
                    <li>Higher stress leading to comfort eating</li>
                </ul>

                <p><strong>What You Can Do (if you live in a city):</strong> You must INTENTIONALLY add physical activity. Take stairs, walk for short trips, pack home-cooked lunch, aim for 10,000 steps daily.</p>
            </div>
        </div>
"""

# Chart 3: Education Level
education_data = df[df['Category'] == 'Education']
latest_edu = education_data[education_data['Survey_Year'] == 2019]

fig6 = go.Figure()

categories = ['No Education', 'Primary School', 'High School', 'College/University']
edu_map = {'No education': 'No Education', 'Primary': 'Primary School', 'Secondary': 'High School', 'Higher': 'College/University'}

latest_edu_sorted = latest_edu.copy()
latest_edu_sorted['Display'] = latest_edu_sorted['Subcategory'].map(edu_map)

fig6.add_trace(go.Bar(
    name='Children',
    x=[edu_map[x] for x in latest_edu_sorted['Subcategory']],
    y=latest_edu_sorted['Children_Overweight_Pct'].tolist(),
    marker_color=COLORS['children'],
    text=[f"{v:.1f}%" for v in latest_edu_sorted['Children_Overweight_Pct']],
    textposition='outside'
))

fig6.add_trace(go.Bar(
    name='Women',
    x=[edu_map[x] for x in latest_edu_sorted['Subcategory']],
    y=latest_edu_sorted['Women_Overweight_Pct'].tolist(),
    marker_color=COLORS['women'],
    text=[f"{v:.1f}%" for v in latest_edu_sorted['Women_Overweight_Pct']],
    textposition='outside'
))

fig6.add_trace(go.Bar(
    name='Men',
    x=[edu_map[x] for x in latest_edu_sorted['Subcategory']],
    y=latest_edu_sorted['Men_Overweight_Pct'].tolist(),
    marker_color=COLORS['men'],
    text=[f"{v:.1f}%" for v in latest_edu_sorted['Men_Overweight_Pct']],
    textposition='outside'
))

fig6.update_layout(
    xaxis_title='Education Level',
    yaxis_title='Percentage (%)',
    barmode='group',
    height=550,
    template='plotly_white',
    font=dict(size=14, family='Segoe UI'),
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5),
    plot_bgcolor='white',
    paper_bgcolor='white',
    yaxis=dict(range=[0, 35])
)

no_edu = latest_edu[latest_edu['Subcategory'] == 'No education'].iloc[0]
higher_edu = latest_edu[latest_edu['Subcategory'] == 'Higher'].iloc[0]

html_content += f"""
        <div class="chart-container">
            <div class="chart-title">Education Level Impact</div>
            <div class="chart-subtitle">How your education affects obesity risk (2019 data)</div>
            {fig6.to_html(include_plotlyjs=False, div_id='education_chart', config={'displayModeBar': False})}

            <div class="explanation-box">
                <h4>What This Chart Shows:</h4>
                <p>This shows obesity rates based on how much schooling people have completed.</p>

                <p><strong>Education Levels Explained:</strong></p>
                <ul>
                    <li><strong>No Education:</strong> Never went to school ({no_edu['Women_Overweight_Pct']:.1f}% obese)</li>
                    <li><strong>Primary School:</strong> Completed elementary school (grades 1-5)</li>
                    <li><strong>High School:</strong> Completed secondary school (grades 6-12)</li>
                    <li><strong>College/University:</strong> Completed college or university ({higher_edu['Women_Overweight_Pct']:.1f}% obese)</li>
                </ul>

                <p><strong>Surprising Finding:</strong> More education = HIGHER obesity! Why?</p>
                <ul>
                    <li>Educated people often have desk jobs (less physical activity)</li>
                    <li>Higher income means more access to processed/restaurant food</li>
                    <li>Urban lifestyle (most educated people live in cities)</li>
                </ul>

                <p><strong>Important:</strong> This doesn't mean education is bad! It means educated people need to be MORE careful about diet and exercise because their jobs and lifestyle put them at higher risk.</p>
            </div>
        </div>
"""

# Chart 4: Age Groups
age_data = df[df['Category'] == 'Age (5-year groups)']
latest_age = age_data[age_data['Survey_Year'] == 2019]

fig5 = go.Figure()

fig5.add_trace(go.Bar(
    name='Women',
    x=latest_age['Subcategory'].tolist(),
    y=latest_age['Women_Overweight_Pct'].tolist(),
    marker_color=COLORS['women'],
    text=[f"{v:.1f}%" for v in latest_age['Women_Overweight_Pct']],
    textposition='outside'
))

fig5.add_trace(go.Bar(
    name='Men',
    x=latest_age['Subcategory'].tolist(),
    y=latest_age['Men_Overweight_Pct'].tolist(),
    marker_color=COLORS['men'],
    text=[f"{v:.1f}%" for v in latest_age['Men_Overweight_Pct']],
    textposition='outside'
))

fig5.update_layout(
    xaxis_title='Age Group (years)',
    yaxis_title='Percentage (%)',
    barmode='group',
    height=550,
    template='plotly_white',
    font=dict(size=14, family='Segoe UI'),
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5),
    plot_bgcolor='white',
    paper_bgcolor='white',
    yaxis=dict(range=[0, 45])
)

youngest = latest_age[latest_age['Subcategory'] == '15-19'].iloc[0]
oldest = latest_age[latest_age['Subcategory'] == '45-49'].iloc[0]

html_content += f"""
        <div class="chart-container">
            <div class="chart-title">Obesity by Age Group</div>
            <div class="chart-subtitle">How obesity increases as you get older (2019 data)</div>
            {fig5.to_html(include_plotlyjs=False, div_id='age_chart', config={'displayModeBar': False})}

            <div class="explanation-box">
                <h4>What This Chart Shows:</h4>
                <p>This shows how obesity rates change with age. Each bar represents a 5-year age range.</p>

                <p><strong>The Pattern:</strong></p>
                <ul>
                    <li><strong>Age 15-19 (teenagers):</strong> Only {youngest['Women_Overweight_Pct']:.1f}% obese</li>
                    <li><strong>Age 45-49 (middle-aged):</strong> Up to {oldest['Women_Overweight_Pct']:.1f}% obese</li>
                    <li><strong>That's a {oldest['Women_Overweight_Pct'] - youngest['Women_Overweight_Pct']:.1f} percentage point increase!</strong></li>
                </ul>

                <p><strong>Why This Happens:</strong></p>
                <ul>
                    <li><strong>Slow weight gain:</strong> You gain 0.5-1 kg per year without noticing</li>
                    <li><strong>Metabolism slows:</strong> Your body burns fewer calories as you age</li>
                    <li><strong>Less active:</strong> Desk jobs, family responsibilities = less time to exercise</li>
                    <li><strong>Adds up over time:</strong> Small changes each year = big change over 20-30 years</li>
                </ul>

                <p><strong>What You Can Do:</strong> Weigh yourself monthly. If you gain 2+ kg in 6 months, change something NOW. Don't wait until you're in your 40s - prevent it in your 20s and 30s!</p>
            </div>
        </div>
"""

# Chart 5: Wealth Impact (Use simple language!)
wealth_data = df[df['Category'] == 'Wealth quintile']
latest_wealth = wealth_data[wealth_data['Survey_Year'] == 2019]
wealth_order = ['Lowest', 'Second', 'Middle', 'Fourth', 'Highest']
latest_wealth_sorted = latest_wealth.set_index('Subcategory').reindex(wealth_order).reset_index()

# Rename for simpler language
wealth_labels = ['Poorest 20%', 'Low Income', 'Middle Income', 'Upper Income', 'Richest 20%']

fig4 = go.Figure()

fig4.add_trace(go.Bar(
    x=wealth_labels,
    y=latest_wealth_sorted['Children_Overweight_Pct'].tolist(),
    name='Children',
    marker_color=COLORS['children'],
    text=[f"{v:.1f}%" for v in latest_wealth_sorted['Children_Overweight_Pct']],
    textposition='outside'
))

fig4.add_trace(go.Bar(
    x=wealth_labels,
    y=latest_wealth_sorted['Women_Overweight_Pct'].tolist(),
    name='Women',
    marker_color=COLORS['women'],
    text=[f"{v:.1f}%" for v in latest_wealth_sorted['Women_Overweight_Pct']],
    textposition='outside'
))

fig4.add_trace(go.Bar(
    x=wealth_labels,
    y=latest_wealth_sorted['Men_Overweight_Pct'].tolist(),
    name='Men',
    marker_color=COLORS['men'],
    text=[f"{v:.1f}%" for v in latest_wealth_sorted['Men_Overweight_Pct']],
    textposition='outside'
))

fig4.update_layout(
    xaxis_title='Income Level',
    yaxis_title='Percentage (%)',
    barmode='group',
    height=550,
    template='plotly_white',
    font=dict(size=14, family='Segoe UI'),
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5),
    plot_bgcolor='white',
    paper_bgcolor='white',
    yaxis=dict(range=[0, 45])
)

poorest = latest_wealth_sorted.iloc[0]
richest = latest_wealth_sorted.iloc[4]

html_content += f"""
        <div class="chart-container">
            <div class="chart-title">Income Level Impact</div>
            <div class="chart-subtitle">Why having more money increases obesity risk (2019 data)</div>
            {fig4.to_html(include_plotlyjs=False, div_id='wealth_chart', config={'displayModeBar': False})}

            <div class="explanation-box">
                <h4>What This Chart Shows:</h4>
                <p>This shows obesity rates based on household income. We divided everyone into 5 groups from poorest to richest.</p>

                <p><strong>Income Groups Explained:</strong></p>
                <ul>
                    <li><strong>Poorest 20%:</strong> Lowest income families ({poorest['Women_Overweight_Pct']:.1f}% obese)</li>
                    <li><strong>Low Income:</strong> Below average income</li>
                    <li><strong>Middle Income:</strong> Average income families</li>
                    <li><strong>Upper Income:</strong> Above average income</li>
                    <li><strong>Richest 20%:</strong> Highest income families ({richest['Women_Overweight_Pct']:.1f}% obese)</li>
                </ul>

                <p><strong>Shocking Result:</strong> Rich people have ALMOST 4X MORE obesity than poor people!</p>

                <p><strong>Why More Money = More Weight:</strong></p>
                <ul>
                    <li><strong>Can afford fast food daily:</strong> Burgers, pizza, restaurant meals</li>
                    <li><strong>Can afford a car:</strong> Drive instead of walk</li>
                    <li><strong>Desk jobs:</strong> High-paying jobs usually mean sitting all day</li>
                    <li><strong>Processed foods:</strong> More money = buy convenient packaged foods instead of cooking</li>
                </ul>

                <p><strong>The Lesson:</strong> If you can afford these things, you're at HIGHER risk. Use your money wisely - hire a trainer, buy a gym membership, order healthy meal prep, get regular health check-ups. Don't let wealth harm your health!</p>
            </div>
        </div>
"""

# Now add the interactive tools at the end...
interactive_html = open('add_interactive_tools.py', 'r', encoding='utf-8').read()
# Extract just the HTML part from the interactive tools
# (We'll add it after the charts)

html_content += """
        <!-- BMI Calculator Section -->
        <div class="chart-container" style="background: linear-gradient(135deg, #2C3E50 0%, #3498DB 100%); color: white;">
            <div class="chart-title" style="color: white;">BMI Calculator & Risk Assessment</div>
            <div class="chart-subtitle" style="color: rgba(255,255,255,0.9);">Calculate your Body Mass Index and understand your risk</div>

            <div style="background: white; padding: 30px; border-radius: 10px; margin-top: 20px; color: #2C3E50;">
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">

                    <!-- BMI Calculator -->
                    <div>
                        <h3 style="margin-bottom: 20px; color: #2C3E50;">Calculate Your BMI</h3>

                        <div class="height-selector">
                            <button id="btn-cm" class="active" onclick="switchHeightUnit('cm')">Centimeters (cm)</button>
                            <button id="btn-feet" onclick="switchHeightUnit('feet')">Feet & Inches</button>
                        </div>

                        <div id="height-cm-input" style="margin-bottom: 15px;">
                            <label style="display: block; margin-bottom: 5px; font-weight: 600;">Height (cm):</label>
                            <input type="number" id="height-cm" placeholder="e.g., 165"
                                   style="width: 100%; padding: 12px; border: 2px solid #ddd; border-radius: 6px; font-size: 1em;">
                        </div>

                        <div id="height-feet-input" style="display: none;">
                            <label style="display: block; margin-bottom: 5px; font-weight: 600;">Height:</label>
                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                                <div>
                                    <input type="number" id="height-feet" placeholder="Feet (e.g., 5)"
                                           style="width: 100%; padding: 12px; border: 2px solid #ddd; border-radius: 6px; font-size: 1em;">
                                </div>
                                <div>
                                    <input type="number" id="height-inches" placeholder="Inches (e.g., 6)"
                                           style="width: 100%; padding: 12px; border: 2px solid #ddd; border-radius: 6px; font-size: 1em;">
                                </div>
                            </div>
                        </div>

                        <div style="margin-bottom: 15px;">
                            <label style="display: block; margin-bottom: 5px; font-weight: 600;">Weight (kg):</label>
                            <input type="number" id="weight" placeholder="e.g., 70"
                                   style="width: 100%; padding: 12px; border: 2px solid #ddd; border-radius: 6px; font-size: 1em;">
                        </div>

                        <div style="margin-bottom: 15px;">
                            <label style="display: block; margin-bottom: 5px; font-weight: 600;">Age:</label>
                            <input type="number" id="age" placeholder="e.g., 30"
                                   style="width: 100%; padding: 12px; border: 2px solid #ddd; border-radius: 6px; font-size: 1em;">
                        </div>

                        <div style="margin-bottom: 15px;">
                            <label style="display: block; margin-bottom: 5px; font-weight: 600;">Gender:</label>
                            <select id="gender" style="width: 100%; padding: 12px; border: 2px solid #ddd; border-radius: 6px; font-size: 1em;">
                                <option value="">Select...</option>
                                <option value="female">Female</option>
                                <option value="male">Male</option>
                            </select>
                        </div>

                        <button onclick="calculateBMI()"
                                style="width: 100%; padding: 15px; background: linear-gradient(135deg, #2C3E50 0%, #3498DB 100%);
                                       color: white; border: none; border-radius: 6px; font-size: 1.1em; font-weight: 600;
                                       cursor: pointer;">
                            Calculate BMI
                        </button>
                    </div>

                    <!-- Results Display -->
                    <div>
                        <h3 style="margin-bottom: 20px; color: #2C3E50;">Your Results</h3>

                        <div id="bmi-result" style="display: none;">
                            <div style="background: #ECF0F1; padding: 20px; border-radius: 8px; margin-bottom: 15px;">
                                <div style="font-size: 0.9em; color: #7F8C8D; margin-bottom: 5px;">Your BMI</div>
                                <div id="bmi-value" style="font-size: 3em; font-weight: 700; color: #2C3E50;"></div>
                                <div id="bmi-category" style="font-size: 1.2em; font-weight: 600; margin-top: 10px;"></div>
                            </div>

                            <div id="risk-assessment" style="background: #FEF5E7; padding: 20px; border-radius: 8px; border-left: 4px solid #F39C12;">
                                <h4 style="margin-bottom: 10px; color: #2C3E50;">Your Health Risk</h4>
                                <div id="risk-details"></div>
                            </div>

                            <div id="comparison" style="background: #E8F8F5; padding: 20px; border-radius: 8px; margin-top: 15px; border-left: 4px solid #27AE60;">
                                <h4 style="margin-bottom: 10px; color: #2C3E50;">Compared to India</h4>
                                <div id="comparison-details"></div>
                            </div>

                            <div id="recommendations" style="background: #EBF5FB; padding: 20px; border-radius: 8px; margin-top: 15px; border-left: 4px solid #3498DB;">
                                <h4 style="margin-bottom: 10px; color: #2C3E50;">What You Should Do</h4>
                                <div id="recommendation-details"></div>
                            </div>
                        </div>

                        <div id="bmi-placeholder" style="text-align: center; padding: 60px 20px; color: #BDC3C7;">
                            <div style="font-size: 3em; margin-bottom: 10px;">📊</div>
                            <div style="font-size: 1.1em;">Enter your details to calculate BMI</div>
                        </div>
                    </div>
                </div>

                <!-- BMI Reference Chart -->
                <div style="margin-top: 30px; padding-top: 30px; border-top: 2px solid #ECF0F1;">
                    <h3 style="margin-bottom: 20px; color: #2C3E50;">BMI Categories</h3>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px;">
                        <div style="background: #E8F8F5; padding: 15px; border-radius: 6px; border-left: 4px solid #27AE60;">
                            <div style="font-weight: 600; color: #27AE60;">Underweight</div>
                            <div style="color: #7F8C8D;">BMI less than 18.5</div>
                        </div>
                        <div style="background: #E8F8F5; padding: 15px; border-radius: 6px; border-left: 4px solid #27AE60;">
                            <div style="font-weight: 600; color: #27AE60;">Normal Weight</div>
                            <div style="color: #7F8C8D;">BMI 18.5 - 24.9</div>
                        </div>
                        <div style="background: #FEF5E7; padding: 15px; border-radius: 6px; border-left: 4px solid #F39C12;">
                            <div style="font-weight: 600; color: #F39C12;">Overweight</div>
                            <div style="color: #7F8C8D;">BMI 25.0 - 29.9</div>
                        </div>
                        <div style="background: #FADBD8; padding: 15px; border-radius: 6px; border-left: 4px solid #E74C3C;">
                            <div style="font-weight: 600; color: #E74C3C;">Obese</div>
                            <div style="color: #7F8C8D;">BMI 30.0 or higher</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="footer">
            <p><strong>Data Source:</strong> DHS Program India 2019-21</p>
            <p style="margin-top: 10px;">All charts are interactive - hover to see exact values</p>
        </div>
    </div>

    <script>
        let currentHeightUnit = 'cm';

        function switchHeightUnit(unit) {
            currentHeightUnit = unit;

            if (unit === 'cm') {
                document.getElementById('btn-cm').classList.add('active');
                document.getElementById('btn-feet').classList.remove('active');
                document.getElementById('height-cm-input').style.display = 'block';
                document.getElementById('height-feet-input').style.display = 'none';
            } else {
                document.getElementById('btn-feet').classList.add('active');
                document.getElementById('btn-cm').classList.remove('active');
                document.getElementById('height-feet-input').style.display = 'block';
                document.getElementById('height-cm-input').style.display = 'none';
            }
        }

        function calculateBMI() {
            let height;

            if (currentHeightUnit === 'cm') {
                height = parseFloat(document.getElementById('height-cm').value);
            } else {
                const feet = parseFloat(document.getElementById('height-feet').value);
                const inches = parseFloat(document.getElementById('height-inches').value);

                if (!feet || !inches) {
                    alert('Please enter both feet and inches');
                    return;
                }

                // Convert feet and inches to cm
                height = ((feet * 12) + inches) * 2.54;
            }

            const weight = parseFloat(document.getElementById('weight').value);
            const age = parseInt(document.getElementById('age').value);
            const gender = document.getElementById('gender').value;

            if (!height || !weight || !age || !gender) {
                alert('Please fill in all fields');
                return;
            }

            // Calculate BMI
            const heightInMeters = height / 100;
            const bmi = weight / (heightInMeters * heightInMeters);

            // Determine category
            let category, categoryColor, riskLevel;
            if (bmi < 18.5) {
                category = 'Underweight';
                categoryColor = '#3498DB';
                riskLevel = 'low';
            } else if (bmi < 25) {
                category = 'Normal Weight';
                categoryColor = '#27AE60';
                riskLevel = 'low';
            } else if (bmi < 30) {
                category = 'Overweight';
                categoryColor = '#F39C12';
                riskLevel = 'medium';
            } else {
                category = 'Obese';
                categoryColor = '#E74C3C';
                riskLevel = 'high';
            }

            // Display results
            document.getElementById('bmi-placeholder').style.display = 'none';
            document.getElementById('bmi-result').style.display = 'block';
            document.getElementById('bmi-value').textContent = bmi.toFixed(1);
            document.getElementById('bmi-value').style.color = categoryColor;
            document.getElementById('bmi-category').textContent = category;
            document.getElementById('bmi-category').style.color = categoryColor;

            // Risk assessment
            let riskHTML = '';
            if (riskLevel === 'high') {
                riskHTML = `
                    <div style="color: #E74C3C; font-weight: 600; margin-bottom: 10px;">HIGH RISK</div>
                    <p>You are at increased risk for serious health problems:</p>
                    <ul style="margin: 10px 0; padding-left: 20px;">
                        <li>Type 2 Diabetes</li>
                        <li>Heart Disease</li>
                        <li>High Blood Pressure</li>
                        <li>Joint Problems</li>
                    </ul>
                    <p style="margin-top: 10px;"><strong>What to do:</strong> See a doctor for health screening and start a weight loss plan today.</p>
                `;
            } else if (riskLevel === 'medium') {
                riskHTML = `
                    <div style="color: #F39C12; font-weight: 600; margin-bottom: 10px;">MEDIUM RISK</div>
                    <p>You are overweight. Taking action now can prevent obesity.</p>
                    <p style="margin-top: 10px;"><strong>What to do:</strong> Start walking 10,000 steps daily and reduce processed food.</p>
                `;
            } else {
                riskHTML = `
                    <div style="color: #27AE60; font-weight: 600; margin-bottom: 10px;">LOW RISK</div>
                    <p>Your weight is in the healthy range. Keep it up!</p>
                `;
            }
            document.getElementById('risk-details').innerHTML = riskHTML;

            // Comparison
            const genderText = gender === 'female' ? 'women' : 'men';
            const nationalRate = gender === 'female' ? 24.0 : 23.7;

            let comparisonHTML = `
                <p>In India (2019 data):</p>
                <ul style="margin: 10px 0; padding-left: 20px;">
                    <li>Overall ${genderText}: ${nationalRate}% are overweight/obese</li>
                    <li>City ${genderText}: ${gender === 'female' ? '33.3%' : '29.8%'}</li>
                    <li>Village ${genderText}: ${gender === 'female' ? '19.7%' : '19.3%'}</li>
                </ul>
            `;
            document.getElementById('comparison-details').innerHTML = comparisonHTML;

            // Recommendations
            let recommendHTML = '';
            if (bmi >= 25) {
                recommendHTML = `
                    <ul style="margin: 0; padding-left: 20px;">
                        <li>Walk 10,000 steps every day</li>
                        <li>Eat home-cooked dal, roti, sabzi (not fast food)</li>
                        <li>Lose ${(weight * 0.05).toFixed(1)}-${(weight * 0.10).toFixed(1)} kg (5-10% of your weight)</li>
                        <li>Get checked for diabetes and blood pressure</li>
                    </ul>
                `;
            } else {
                recommendHTML = `
                    <ul style="margin: 0; padding-left: 20px;">
                        <li>Keep your healthy weight - weigh yourself monthly</li>
                        <li>Stay active - 7,000+ steps daily</li>
                        <li>Keep eating home-cooked traditional food</li>
                    </ul>
                `;
            }
            document.getElementById('recommendation-details').innerHTML = recommendHTML;
        }
    </script>
</body>
</html>
"""

# Write the final dashboard
with open('obesity_dashboard_enhanced.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Dashboard created successfully!")
print("\nKey improvements:")
print("- Feet/inches option for height")
print("- Clear explanations for all charts")
print("- Simple language (no 'quintile')")
print("- Fixed data display issues")
print("- Added context for each visualization")
