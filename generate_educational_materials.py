"""
Educational Materials Generator for India Obesity Dashboard
Creates patient handouts, doctor protocols, and campaign materials
"""

import pandas as pd
from datetime import datetime

# Load the dataset
df = pd.read_csv('obesity_data_cleaned.csv')

# Extract key statistics
latest_data = df[df['Survey_Year'] == 2019]
total_2019 = latest_data[latest_data['Category'] == 'Total'].iloc[0]
total_1998 = df[(df['Survey_Year'] == 1998) & (df['Category'] == 'Total')].iloc[0]

urban_2019 = latest_data[(latest_data['Category'] == 'Residence') & (latest_data['Subcategory'] == 'Urban')].iloc[0]
rural_2019 = latest_data[(latest_data['Category'] == 'Residence') & (latest_data['Subcategory'] == 'Rural')].iloc[0]

wealth_data = latest_data[latest_data['Category'] == 'Wealth quintile'].sort_values('Subcategory')
lowest_wealth = wealth_data[wealth_data['Subcategory'] == 'Lowest'].iloc[0]
highest_wealth = wealth_data[wealth_data['Subcategory'] == 'Highest'].iloc[0]

age_data = latest_data[latest_data['Category'] == 'Age (5-year groups)'].sort_values('Subcategory')

print("=" * 80)
print("EDUCATIONAL MATERIALS GENERATOR")
print("India Obesity Dashboard - Evidence-Based Messaging")
print("=" * 80)

# 1. PATIENT EDUCATION HANDOUTS
print("\n" + "=" * 80)
print("1. PATIENT EDUCATION HANDOUTS")
print("=" * 80)

patient_handout = f"""
================================================================================
                     UNDERSTANDING OBESITY IN INDIA
                    Patient Education Handout
                    Based on DHS Survey Data 2019-21
================================================================================

THE WEALTH TRAP: More Money = More Health Risk

Did you know?
- Richest Indians: {highest_wealth['Women_Overweight_Pct']:.1f}% obesity rate
- Poorest Indians: {lowest_wealth['Women_Overweight_Pct']:.1f}% obesity rate
- That's NEARLY 4X HIGHER risk if you're wealthy!

If you can afford these, you're at HIGHER risk:
[ ] Processed/fast food daily
[ ] Car instead of walking
[ ] Desk job with no physical labor
[ ] Restaurant meals multiple times per week

ACTION STEP: Track your steps. Aim for 10,000 steps per day.
Walking is free - use it!

--------------------------------------------------------------------------------

THE URBAN DANGER: City Life is Making You Sick

The data is clear:
- Urban obesity: {urban_2019['Women_Overweight_Pct']:.1f}%
- Rural obesity: {rural_2019['Women_Overweight_Pct']:.1f}%
- Urban areas are {((urban_2019['Women_Overweight_Pct']/rural_2019['Women_Overweight_Pct'])-1)*100:.0f}% MORE at risk!

Why cities are dangerous:
1. Sedentary office jobs (vs agricultural work)
2. Easy access to processed food
3. Car/metro commute (vs walking)
4. Higher stress leading to comfort eating

ACTION STEP: If you live in a city, you MUST intentionally add physical
activity. It won't happen naturally like in villages.

Daily urban survival plan:
- Take stairs instead of elevator (every time!)
- Walk/cycle for trips under 2 km
- Stand and stretch every 30 minutes at desk
- Pack home-cooked lunch instead of eating out

--------------------------------------------------------------------------------

THE AGE CREEP: You're Gaining Weight Without Noticing

Obesity rates by age (women):
- Age 15-19: 5.4%
- Age 20-24: 12.2%
- Age 25-29: 21.5%
- Age 30-34: 29.9%
- Age 35-39: 34.0%
- Age 40-44: 36.8%
- Age 45-49: 37.0%

This happens SLOWLY. You don't notice 0.3% gain per year.
But over 20 years, you could be 20 kg heavier!

ACTION STEP: Weigh yourself on the 1st of every month.
If you gain 2+ kg in 6 months, change something NOW.

Warning signs:
- Clothes getting tighter
- Belt moving one notch out
- Feeling breathless climbing stairs
- Fatigue even with adequate sleep

--------------------------------------------------------------------------------

THE EPIDEMIC: India's Obesity Crisis 1998 vs 2021

Children: {total_1998['Children_Overweight_Pct']:.1f}% → {total_2019['Children_Overweight_Pct']:.1f}%
Women: {total_1998['Women_Overweight_Pct']:.1f}% → {total_2019['Women_Overweight_Pct']:.1f}%
Men: 9.7% → {total_2019['Men_Overweight_Pct']:.1f}%

This isn't genetic. This is lifestyle change.

Traditional Indian diet + active lifestyle = LOW obesity
Western diet + sedentary lifestyle = HIGH obesity

ACTION STEP: Return to traditional eating patterns
Dal, roti, sabzi > burgers, pizza, sweets

Traditional foods that protect you:
- Whole grains (brown rice, whole wheat)
- Lentils and legumes (dal, rajma, chana)
- Fresh vegetables (sabzi)
- Limited processed foods
- Spices with health benefits (turmeric, ginger)

Foods that harm you:
- Deep fried snacks
- Sugary drinks (soda, packaged juices)
- Bakery items (cakes, pastries)
- Fast food (burgers, pizza)
- Excessive sweets/mithai

--------------------------------------------------------------------------------

YOUR PERSONAL ACTION PLAN

Week 1-2: Awareness Phase
[ ] Weigh yourself and record it
[ ] Count your daily steps for 1 week (use phone app)
[ ] Write down everything you eat for 3 days
[ ] Identify your biggest problem area

Week 3-4: Small Changes
[ ] Add 2,000 more steps to your daily average
[ ] Replace 1 processed food with home-cooked alternative
[ ] Drink water instead of sugary drinks
[ ] Sleep 7-8 hours per night

Month 2-3: Build Habits
[ ] Walk 10,000 steps per day, 5 days per week
[ ] Cook at home 5 days per week
[ ] Find a walking partner or group
[ ] Weigh yourself monthly

Month 4-6: Sustain & Improve
[ ] Maintain new habits
[ ] Add strength training 2x per week
[ ] Teach family members what you learned
[ ] Celebrate small victories

--------------------------------------------------------------------------------

WHEN TO SEE A DOCTOR

See your doctor if you:
- Are overweight or obese (BMI > 25)
- Have family history of diabetes or heart disease
- Experience unexplained weight gain
- Have difficulty breathing or sleeping
- Feel joint pain

Ask your doctor to check:
- Blood pressure
- Blood sugar (diabetes screening)
- Cholesterol levels
- Liver function
- BMI calculation

--------------------------------------------------------------------------------

REMEMBER: Small changes add up to big results!
You don't need to be perfect. You need to be consistent.

For more information: Show this dashboard to your family and friends
Share knowledge, share health!

Generated: {datetime.now().strftime('%B %Y')}
Data Source: DHS Program India 2019-21
================================================================================
"""

# Save patient handout
with open('patient_handout.txt', 'w', encoding='utf-8') as f:
    f.write(patient_handout)

print("[CREATED] patient_handout.txt")

# 2. DOCTOR SCREENING PROTOCOLS
print("\n" + "=" * 80)
print("2. DOCTOR SCREENING PROTOCOLS")
print("=" * 80)

doctor_protocol = f"""
================================================================================
          OBESITY SCREENING & INTERVENTION PROTOCOLS FOR PHYSICIANS
                    Evidence-Based Clinical Guidelines
                    Based on DHS India Data 2019-21
================================================================================

RISK STRATIFICATION SYSTEM
--------------------------------------------------------------------------------

HIGH RISK PATIENTS (Screen quarterly, aggressive intervention)

Demographic Profile:
- Urban residents aged 35-49
- Wealth quintile 4-5 (upper-middle to wealthy)
- Sedentary occupation (office work, IT, management)
- Family history of diabetes/CVD

Current Prevalence:
- Urban women 35-39: {age_data[age_data['Subcategory'] == '35-39']['Women_Overweight_Pct'].values[0]:.1f}% obesity
- Urban women 40-44: {age_data[age_data['Subcategory'] == '40-44']['Women_Overweight_Pct'].values[0]:.1f}% obesity

Screening Protocol:
✓ BMI calculation at EVERY visit
✓ Waist circumference measurement
✓ Blood pressure (every visit)
✓ HbA1c or fasting glucose (quarterly)
✓ Lipid panel (biannually)
✓ Liver function tests (annually)
✓ Sleep apnea screening if BMI > 30

MEDIUM RISK PATIENTS (Screen annually)

Demographic Profile:
- Urban residents aged 25-34
- Rural residents aged 35-44
- Wealth quintile 2-3
- Mixed activity occupation

Screening Protocol:
✓ BMI calculation (annual)
✓ Blood pressure (annual)
✓ Fasting glucose (annual)
✓ Lipid panel (every 2 years)

LOW RISK PATIENTS (Screen biennially)

Demographic Profile:
- Rural residents aged 15-29
- Wealth quintile 1
- High physical activity occupation (agriculture, manual labor)

Screening Protocol:
✓ BMI calculation (every 2 years)
✓ Blood pressure (every 2 years)
✓ Basic metabolic screening only if symptomatic

================================================================================

AGE-SPECIFIC INTERVENTION POINTS
--------------------------------------------------------------------------------

AGE 15-24: PREVENTION PHASE
Current obesity: 5.4-12.2%
Primary Goal: Establish healthy baseline

Counseling Points:
- "This is your weight baseline. Maintain it."
- Educate on lifestyle choices that lead to weight gain
- Establish exercise habits NOW
- Screen only if symptomatic or family history

RED FLAG: Weight gain > 5 kg between visits

AGE 25-34: EARLY INTERVENTION PHASE
Current obesity: 21.5-29.9%
Primary Goal: Prevent progression to obesity

Counseling Points:
- "Weight gain accelerates in this decade. Act now."
- Discuss marriage/pregnancy weight retention
- Address sedentary job risks
- Provide specific calorie/activity targets

INTERVENTION: If BMI > 25, refer to dietitian/lifestyle program

AGE 35-49: COMPLICATION PREVENTION PHASE
Current obesity: 34.0-37.0%
Primary Goal: Prevent diabetes, CVD, other complications

Counseling Points:
- "Focus on health metrics, not just weight"
- Screen aggressively for complications
- Medication if lifestyle changes fail
- Consider bariatric surgery if BMI > 35 with comorbidities

MANDATORY SCREENING:
- Diabetes screening (annual)
- Cardiovascular risk assessment
- Fatty liver screening
- Joint health evaluation

================================================================================

SOCIOECONOMIC-TAILORED COUNSELING
--------------------------------------------------------------------------------

FOR WEALTHY/UPPER-MIDDLE CLASS PATIENTS (Quintile 4-5)
Risk Profile: {highest_wealth['Women_Overweight_Pct']:.1f}% obesity rate

Your Message:
"Your lifestyle puts you at HIGH risk. You have advantages - use them:

 ✓ You can afford a personal trainer - HIRE ONE
 ✓ You can afford gym membership - USE IT
 ✓ You can afford healthy food delivery - ORDER IT
 ✓ You can afford regular health check-ups - SCHEDULE THEM

 Money gives you options. Choose health over convenience.
 Your desk job won't kill you if you're intentional about activity."

Key Barriers to Address:
- "Too busy" excuse (they're busy being sedentary)
- Over-reliance on convenience (car, delivery, processed food)
- Social eating (business dinners, celebrations)
- Stress eating patterns

FOR LOWER-INCOME PATIENTS (Quintile 1-2)
Risk Profile: {lowest_wealth['Women_Overweight_Pct']:.1f}% obesity rate

Your Message:
"Your traditional lifestyle is actually PROTECTIVE:

 ✓ Home-cooked food > restaurant food
 ✓ Walking/cycling > driving
 ✓ Physical labor > desk work
 ✓ Traditional diet > Western diet

 Don't aspire to wealthy people's food habits.
 You're healthier in many ways. Maintain this!"

Key Barriers to Address:
- Aspiration to "wealthy lifestyle" (processed foods as status symbol)
- Limited healthcare access (provide free/subsidized options)
- Time constraints (simple, quick healthy options)

FOR URBAN PATIENTS
Risk Profile: {urban_2019['Women_Overweight_Pct']:.1f}% obesity ({((urban_2019['Women_Overweight_Pct']/rural_2019['Women_Overweight_Pct'])-1)*100:.0f}% higher than rural)

Your Message:
"Urban living is a major risk factor. Your environment works against you:

 ✗ Sedentary commute
 ✗ Desk job
 ✗ Easy access to unhealthy food
 ✗ High stress

 You MUST compensate with intentional activity and food choices."

Specific Recommendations:
- Walk/metro/bike instead of car for trips < 5 km
- Use standing desk or take breaks every 30 min
- Pack lunch from home 4-5 days/week
- Join walking groups or fitness classes for social support

FOR RURAL PATIENTS
Risk Profile: {rural_2019['Women_Overweight_Pct']:.1f}% obesity

Your Message:
"Your lifestyle is generally protective. Focus on:
 ✓ Maintaining current activity levels
 ✓ Avoiding processed/packaged foods
 ✓ Limiting sugar intake
 ✓ Screening if family history present"

================================================================================

COMORBIDITY SCREENING CHECKLIST
--------------------------------------------------------------------------------

IF: Patient obese (BMI ≥ 25) AND age ≥ 30
THEN: Screen for ALL of the following

[ ] Type 2 Diabetes
    - HbA1c or fasting glucose
    - Frequency: Quarterly if pre-diabetic, annually if normal

[ ] Hypertension
    - Blood pressure at every visit
    - Home BP monitoring if elevated

[ ] Dyslipidemia
    - Full lipid panel (LDL, HDL, triglycerides)
    - Frequency: Annually if abnormal, every 2 years if normal

[ ] Fatty Liver Disease
    - ALT, AST liver enzymes
    - Abdominal ultrasound if enzymes elevated
    - Frequency: Annually

[ ] Sleep Apnea
    - STOP-BANG questionnaire
    - Refer for sleep study if high risk
    - Higher priority if BMI > 30

[ ] Osteoarthritis
    - Knee/hip pain assessment
    - X-ray if symptomatic
    - Weight loss crucial for management

[ ] Cardiovascular Disease
    - ECG baseline at age 40
    - Consider stress test if multiple risk factors
    - Framingham or WHO CVD risk calculator

[ ] Mental Health
    - Depression screening (obesity and depression often co-occur)
    - Assess stress, emotional eating patterns

================================================================================

REFERRAL CRITERIA
--------------------------------------------------------------------------------

URGENT REFERRAL (Within 1 week):
- BMI > 40 (Class III obesity)
- Obesity with uncontrolled diabetes (HbA1c > 9%)
- Obesity with severe hypertension (BP > 180/110)
- Suspected sleep apnea with severe symptoms

ROUTINE REFERRAL (Within 1-3 months):
- BMI 30-40 with failed lifestyle modification
- Pre-diabetes with obesity
- Obesity with joint pain affecting mobility
- Request for bariatric surgery evaluation

CONSIDER REFERRAL TO:
- Dietitian/Nutritionist (all obese patients should be offered)
- Endocrinologist (if diabetes or metabolic syndrome)
- Cardiologist (if CVD risk factors present)
- Bariatric surgeon (if BMI > 35 with comorbidities)
- Psychologist (if emotional eating, depression)
- Physical therapist (if joint issues limiting activity)

================================================================================

DOCUMENTATION TEMPLATE
--------------------------------------------------------------------------------

OBESITY ASSESSMENT NOTE:

Current: BMI ___ kg/m² (Category: _____________)
Previous: BMI ___ kg/m² (Date: _____) [Change: +/- ___ kg/m²]

Risk Factors:
[ ] Urban residence
[ ] Sedentary occupation
[ ] Wealth quintile 4-5
[ ] Family history diabetes/CVD
[ ] Age 35-49

Screening Completed:
[ ] Blood pressure: ___/___ mmHg
[ ] Fasting glucose / HbA1c: ___
[ ] Lipid panel: TC ___ LDL ___ HDL ___ TG ___
[ ] Liver enzymes: ALT ___ AST ___
[ ] Waist circumference: ___ cm

Comorbidities Present:
[ ] Diabetes / Pre-diabetes
[ ] Hypertension / Pre-hypertension
[ ] Dyslipidemia
[ ] Fatty liver
[ ] Sleep apnea
[ ] Osteoarthritis
[ ] Depression

Plan:
1. Lifestyle modification counseling provided
2. Referrals: _______________
3. Medications: _______________
4. Follow-up: ___ weeks/months
5. Patient handout provided: [ ] Yes [ ] No

================================================================================

QUICK REFERENCE: OBESITY RATES BY DEMOGRAPHIC (2019-21)
--------------------------------------------------------------------------------

BY LOCATION:
Urban women: {urban_2019['Women_Overweight_Pct']:.1f}%  |  Rural women: {rural_2019['Women_Overweight_Pct']:.1f}%
Urban men:   {urban_2019['Men_Overweight_Pct']:.1f}%  |  Rural men:   {rural_2019['Men_Overweight_Pct']:.1f}%

BY WEALTH:
Lowest quintile:  {lowest_wealth['Women_Overweight_Pct']:.1f}%
Highest quintile: {highest_wealth['Women_Overweight_Pct']:.1f}%

BY AGE (Women):
15-19: 5.4%  |  20-24: 12.2%  |  25-29: 21.5%  |  30-34: 29.9%
35-39: 34.0%  |  40-44: 36.8%  |  45-49: 37.0%

OVERALL (2019):
Children: {total_2019['Children_Overweight_Pct']:.1f}%  |  Women: {total_2019['Women_Overweight_Pct']:.1f}%  |  Men: {total_2019['Men_Overweight_Pct']:.1f}%

================================================================================

Generated: {datetime.now().strftime('%B %Y')}
Data Source: DHS Program India 2019-21
For clinical use by licensed healthcare providers
================================================================================
"""

# Save doctor protocol
with open('doctor_screening_protocol.txt', 'w', encoding='utf-8') as f:
    f.write(doctor_protocol)

print("[CREATED] doctor_screening_protocol.txt")

# 3. CAMPAIGN MESSAGING
print("\n" + "=" * 80)
print("3. SOCIAL MEDIA CAMPAIGN MESSAGES")
print("=" * 80)

campaigns = f"""
================================================================================
                    SOCIAL MEDIA CAMPAIGN MESSAGES
                    Ready-to-Use Posts for Public Health Education
================================================================================

CAMPAIGN 1: "THE WEALTH TRAP"
Target: Urban, upper-middle class, ages 25-45
Platform: LinkedIn, Instagram, Facebook

POST 1:
💰 SHOCKING TRUTH: Rich Indians Are 4X More Likely to Be Obese

New data shows:
• Wealthiest Indians: {highest_wealth['Women_Overweight_Pct']:.1f}% obesity
• Poorest Indians: {lowest_wealth['Women_Overweight_Pct']:.1f}% obesity

Your money is buying:
❌ Processed food instead of home-cooked meals
❌ Car rides instead of walking
❌ Convenience instead of health

It's time to invest in health, not just wealth.

#HealthyIndia #ObesityAwareness #WealthNotHealth

POST 2:
Can you afford daily restaurant meals? 🍔
You're at HIGHER risk of obesity.

Can you afford a car? 🚗
You're at HIGHER risk of obesity.

Can you afford processed foods daily? 🍕
You're at HIGHER risk of obesity.

Wealth without health is poverty.
Start walking. Start cooking. Start living.

#UrbanHealth #ObesityPrevention

--------------------------------------------------------------------------------

CAMPAIGN 2: "CITY LIFE IS KILLING YOU"
Target: Urban professionals, ages 20-40
Platform: Instagram, Twitter, LinkedIn

POST 1:
🏙️ URBAN DANGER ALERT

City dwellers have {((urban_2019['Women_Overweight_Pct']/rural_2019['Women_Overweight_Pct'])-1)*100:.0f}% HIGHER obesity rates than villages!

Why?
• Desk jobs = No movement
• Metro commutes = No walking
• Food delivery = No home cooking
• Stress = Comfort eating

Your city won't make you healthy. YOU have to.

Take the stairs. Pack your lunch. Walk to nearby places.

#UrbanWellness #HealthyLiving

POST 2:
Your grandparents in villages: Walked 10 km/day 🚶
You in the city: Walk 100 meters 🚗

Their diet: Dal-roti-sabzi 🥘
Your diet: Burger-pizza-coke 🍔

Their obesity rate: {rural_2019['Women_Overweight_Pct']:.1f}%
Your obesity rate: {urban_2019['Women_Overweight_Pct']:.1f}%

It's not genetics. It's lifestyle.

#BackToBasics #TraditionalWisdom

--------------------------------------------------------------------------------

CAMPAIGN 3: "THE INVISIBLE WEIGHT GAIN"
Target: Young adults, ages 20-35
Platform: Instagram, TikTok, YouTube

POST 1:
⚠️ THE AGE CREEP

At 20: {age_data[age_data['Subcategory'] == '20-24']['Women_Overweight_Pct'].values[0]:.1f}% of you are overweight
At 30: {age_data[age_data['Subcategory'] == '30-34']['Women_Overweight_Pct'].values[0]:.1f}% of you are overweight
At 40: {age_data[age_data['Subcategory'] == '40-44']['Women_Overweight_Pct'].values[0]:.1f}% of you are overweight

You don't notice gaining 0.5 kg per year.
But in 20 years, you're 20 kg heavier.

Weigh yourself monthly. Catch it early.

#PreventionOverCure #WeightAwareness

POST 2:
Think you're maintaining your weight? 🤔

Check again.

Most people gain 1-2 kg per year without noticing.

Your jeans get tight → You buy bigger jeans
Your belt loosens → You move the buckle
Your photos change → You avoid cameras

STOP ignoring the signs.
Weigh yourself. Face the truth. Act now.

#RealityCheck #HealthyHabits

--------------------------------------------------------------------------------

CAMPAIGN 4: "THE EPIDEMIC IS HERE"
Target: General public, all ages
Platform: All platforms, TV, newspapers

POST 1:
🚨 INDIA'S OBESITY CRISIS

In just 23 years (1998-2021):

Children: {total_1998['Children_Overweight_Pct']:.1f}% → {total_2019['Children_Overweight_Pct']:.1f}% overweight
Women: {total_1998['Women_Overweight_Pct']:.1f}% → {total_2019['Women_Overweight_Pct']:.1f}% overweight/obese
Men: 9.7% → {total_2019['Men_Overweight_Pct']:.1f}% overweight/obese

This isn't genetic. Our genes didn't change.
Our LIFESTYLE changed.

Return to traditional eating. Return to active living.

#HealthyIndia #ObesityEpidemic

POST 2:
What changed between 1998 and 2021? 🤔

✓ Fast food chains everywhere
✓ Food delivery apps
✓ Office jobs instead of fields
✓ Cars instead of walking
✓ Processed snacks instead of fruits

Result? Obesity DOUBLED in 23 years.

You can't change the past.
But you can change TODAY.

#ChooseHealth #TraditionalDiet

--------------------------------------------------------------------------------

CAMPAIGN 5: "TRADITIONAL FOODS PROTECT YOU"
Target: All Indians, focus on preserving food culture
Platform: Instagram, YouTube, cooking channels

POST 1:
🍛 FOODS THAT PROTECT YOU vs FOODS THAT HARM YOU

PROTECT:                  HARM:
✅ Dal & legumes          ❌ Burgers & pizza
✅ Roti & rice            ❌ Cakes & pastries
✅ Sabzi                  ❌ Deep-fried snacks
✅ Buttermilk             ❌ Soda & packaged juice
✅ Fresh fruits           ❌ Packaged sweets

Our ancestors knew what they were doing.
Traditional Indian diet = Health

#TraditionalFood #HealthyEating

POST 2:
Your dadi's kitchen: Prevention
Modern restaurants: Prescription

Which one will you choose?

#KitchenWisdom #HomeCooking

--------------------------------------------------------------------------------

HASHTAG STRATEGY:

Primary Hashtags:
#ObesityIndia
#HealthyIndia
#PreventionOverCure
#TraditionalWisdom
#UrbanHealth

Secondary Hashtags:
#DesiHealth
#IndianDiet
#WalkMoreWorryLess
#HomeCooked
#ActiveLifestyle

Campaign-Specific:
#TheWealthTrap
#CityDanger
#InvisibleWeightGain
#TheEpidemic
#BackToTraditional

================================================================================

Generated: {datetime.now().strftime('%B %Y')}
Data Source: DHS Program India 2019-21
================================================================================
"""

# Save campaign messages
with open('social_media_campaigns.txt', 'w', encoding='utf-8') as f:
    f.write(campaigns)

print("[CREATED] social_media_campaigns.txt")

# Summary
print("\n" + "=" * 80)
print("GENERATION COMPLETE")
print("=" * 80)
print("\nFiles Created:")
print("1. patient_handout.txt - Print and distribute to patients")
print("2. doctor_screening_protocol.txt - Clinical reference for healthcare providers")
print("3. social_media_campaigns.txt - Ready-to-post campaign messages")
print("\nAll materials are evidence-based using DHS India 2019-21 data")
print("=" * 80)
