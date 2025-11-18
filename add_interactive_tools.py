"""
Add Interactive BMI Calculator and Risk Assessment to Dashboard
"""

import pandas as pd

# Load the dataset for reference statistics
df = pd.read_csv('obesity_data_cleaned.csv')
latest_data = df[df['Survey_Year'] == 2019]

# Read the existing dashboard
with open('obesity_dashboard_enhanced.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Find the position to insert (before the export section)
insert_position = html_content.find('<div class="export-section">')

# Create the interactive tools HTML
interactive_tools = """
        <!-- BMI Calculator Section -->
        <div class="chart-container" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;">
            <div class="chart-title" style="color: white;">BMI Calculator & Risk Assessment</div>
            <div class="chart-subtitle" style="color: rgba(255,255,255,0.9);">Calculate your Body Mass Index and understand your risk based on India data</div>

            <div style="background: white; padding: 30px; border-radius: 10px; margin-top: 20px; color: #2C3E50;">
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">

                    <!-- BMI Calculator -->
                    <div>
                        <h3 style="margin-bottom: 20px; color: #2C3E50;">Calculate Your BMI</h3>

                        <div style="margin-bottom: 15px;">
                            <label style="display: block; margin-bottom: 5px; font-weight: 600;">Height (cm):</label>
                            <input type="number" id="height" placeholder="e.g., 165"
                                   style="width: 100%; padding: 12px; border: 2px solid #ddd; border-radius: 6px; font-size: 1em;">
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
                                style="width: 100%; padding: 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                                       color: white; border: none; border-radius: 6px; font-size: 1.1em; font-weight: 600;
                                       cursor: pointer; transition: transform 0.2s;">
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
                                <h4 style="margin-bottom: 10px; color: #2C3E50;">Risk Assessment</h4>
                                <div id="risk-details"></div>
                            </div>

                            <div id="comparison" style="background: #E8F8F5; padding: 20px; border-radius: 8px; margin-top: 15px; border-left: 4px solid #27AE60;">
                                <h4 style="margin-bottom: 10px; color: #2C3E50;">How You Compare</h4>
                                <div id="comparison-details"></div>
                            </div>

                            <div id="recommendations" style="background: #EBF5FB; padding: 20px; border-radius: 8px; margin-top: 15px; border-left: 4px solid #3498DB;">
                                <h4 style="margin-bottom: 10px; color: #2C3E50;">Recommendations</h4>
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
                    <h3 style="margin-bottom: 20px; color: #2C3E50;">BMI Reference Chart</h3>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px;">
                        <div style="background: #E8F8F5; padding: 15px; border-radius: 6px; border-left: 4px solid #27AE60;">
                            <div style="font-weight: 600; color: #27AE60;">Underweight</div>
                            <div style="color: #7F8C8D;">BMI &lt; 18.5</div>
                        </div>
                        <div style="background: #E8F8F5; padding: 15px; border-radius: 6px; border-left: 4px solid #27AE60;">
                            <div style="font-weight: 600; color: #27AE60;">Normal</div>
                            <div style="color: #7F8C8D;">BMI 18.5 - 24.9</div>
                        </div>
                        <div style="background: #FEF5E7; padding: 15px; border-radius: 6px; border-left: 4px solid #F39C12;">
                            <div style="font-weight: 600; color: #F39C12;">Overweight</div>
                            <div style="color: #7F8C8D;">BMI 25.0 - 29.9</div>
                        </div>
                        <div style="background: #FADBD8; padding: 15px; border-radius: 6px; border-left: 4px solid #E74C3C;">
                            <div style="font-weight: 600; color: #E74C3C;">Obese</div>
                            <div style="color: #7F8C8D;">BMI ≥ 30.0</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Risk Factor Assessment -->
        <div class="chart-container">
            <div class="chart-title">Personal Risk Factor Assessment</div>
            <div class="chart-subtitle">Answer these questions to understand your obesity risk</div>

            <div style="background: #F8F9FA; padding: 30px; border-radius: 10px; margin-top: 20px;">
                <div style="display: grid; gap: 20px;">

                    <div style="background: white; padding: 20px; border-radius: 8px;">
                        <label style="display: block; font-weight: 600; margin-bottom: 10px; color: #2C3E50;">
                            1. Do you live in an urban area?
                        </label>
                        <select id="residence" class="risk-input" style="width: 100%; padding: 10px; border: 2px solid #ddd; border-radius: 6px;">
                            <option value="">Select...</option>
                            <option value="urban">Yes, Urban</option>
                            <option value="rural">No, Rural</option>
                        </select>
                        <div style="font-size: 0.85em; color: #7F8C8D; margin-top: 5px;">
                            Urban areas have 69% higher obesity rates
                        </div>
                    </div>

                    <div style="background: white; padding: 20px; border-radius: 8px;">
                        <label style="display: block; font-weight: 600; margin-bottom: 10px; color: #2C3E50;">
                            2. What is your occupation type?
                        </label>
                        <select id="occupation" class="risk-input" style="width: 100%; padding: 10px; border: 2px solid #ddd; border-radius: 6px;">
                            <option value="">Select...</option>
                            <option value="sedentary">Sedentary (Office/Desk work)</option>
                            <option value="moderate">Moderate activity</option>
                            <option value="active">High activity (Manual labor/Agriculture)</option>
                        </select>
                    </div>

                    <div style="background: white; padding: 20px; border-radius: 8px;">
                        <label style="display: block; font-weight: 600; margin-bottom: 10px; color: #2C3E50;">
                            3. How would you describe your household income?
                        </label>
                        <select id="income" class="risk-input" style="width: 100%; padding: 10px; border: 2px solid #ddd; border-radius: 6px;">
                            <option value="">Select...</option>
                            <option value="low">Low income</option>
                            <option value="middle">Middle income</option>
                            <option value="high">Upper-middle to high income</option>
                        </select>
                        <div style="font-size: 0.85em; color: #7F8C8D; margin-top: 5px;">
                            Higher income = 4x higher obesity risk in India
                        </div>
                    </div>

                    <div style="background: white; padding: 20px; border-radius: 8px;">
                        <label style="display: block; font-weight: 600; margin-bottom: 10px; color: #2C3E50;">
                            4. How often do you eat processed/fast food?
                        </label>
                        <select id="diet" class="risk-input" style="width: 100%; padding: 10px; border: 2px solid #ddd; border-radius: 6px;">
                            <option value="">Select...</option>
                            <option value="rarely">Rarely (less than once/week)</option>
                            <option value="sometimes">Sometimes (1-3 times/week)</option>
                            <option value="often">Often (4+ times/week)</option>
                        </select>
                    </div>

                    <div style="background: white; padding: 20px; border-radius: 8px;">
                        <label style="display: block; font-weight: 600; margin-bottom: 10px; color: #2C3E50;">
                            5. How many steps do you walk per day (approximately)?
                        </label>
                        <select id="steps" class="risk-input" style="width: 100%; padding: 10px; border: 2px solid #ddd; border-radius: 6px;">
                            <option value="">Select...</option>
                            <option value="low">Less than 3,000 steps</option>
                            <option value="moderate">3,000 - 7,000 steps</option>
                            <option value="high">7,000+ steps</option>
                        </select>
                    </div>

                    <button onclick="assessRisk()"
                            style="padding: 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                                   color: white; border: none; border-radius: 6px; font-size: 1.1em; font-weight: 600;
                                   cursor: pointer; transition: transform 0.2s;">
                        Assess My Risk
                    </button>

                    <div id="risk-result" style="display: none; background: white; padding: 25px; border-radius: 8px; border-left: 4px solid #3498DB;">
                        <h3 style="color: #2C3E50; margin-bottom: 15px;">Your Risk Assessment Results</h3>
                        <div id="risk-score-display"></div>
                        <div id="risk-factors-list" style="margin-top: 15px;"></div>
                        <div id="action-plan" style="margin-top: 20px; padding-top: 20px; border-top: 2px solid #ECF0F1;"></div>
                    </div>
                </div>
            </div>
        </div>

        <script>
        // BMI Calculator
        function calculateBMI() {
            const height = parseFloat(document.getElementById('height').value);
            const weight = parseFloat(document.getElementById('weight').value);
            const age = parseInt(document.getElementById('age').value);
            const gender = document.getElementById('gender').value;

            if (!height || !weight || !age || !gender) {
                alert('Please fill in all fields');
                return;
            }

            if (height < 100 || height > 250) {
                alert('Please enter a valid height (100-250 cm)');
                return;
            }

            if (weight < 20 || weight > 300) {
                alert('Please enter a valid weight (20-300 kg)');
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
                    <p>Your BMI indicates obesity. You are at increased risk for:</p>
                    <ul style="margin: 10px 0; padding-left: 20px;">
                        <li>Type 2 Diabetes</li>
                        <li>Heart Disease</li>
                        <li>High Blood Pressure</li>
                        <li>Joint Problems</li>
                        <li>Sleep Apnea</li>
                    </ul>
                    <p style="margin-top: 10px;"><strong>Action needed:</strong> Consult a healthcare provider for comprehensive screening and weight management plan.</p>
                `;
            } else if (riskLevel === 'medium') {
                riskHTML = `
                    <div style="color: #F39C12; font-weight: 600; margin-bottom: 10px;">MEDIUM RISK</div>
                    <p>You are overweight and at moderate risk for obesity-related conditions.</p>
                    <p style="margin-top: 10px;"><strong>Action needed:</strong> Focus on lifestyle modifications now to prevent progression to obesity.</p>
                `;
            } else {
                riskHTML = `
                    <div style="color: #27AE60; font-weight: 600; margin-bottom: 10px;">LOW RISK</div>
                    <p>Your BMI is in the healthy range. Continue maintaining your current lifestyle.</p>
                `;
            }
            document.getElementById('risk-details').innerHTML = riskHTML;

            // Comparison to India data
            const genderText = gender === 'female' ? 'women' : 'men';
            const nationalRate = gender === 'female' ? 24.0 : 23.7;
            let ageGroup = '';
            let ageRate = 0;

            if (age >= 15 && age < 20) {
                ageGroup = '15-19';
                ageRate = gender === 'female' ? 5.4 : 6.6;
            } else if (age >= 20 && age < 25) {
                ageGroup = '20-24';
                ageRate = gender === 'female' ? 12.2 : 13.6;
            } else if (age >= 25 && age < 30) {
                ageGroup = '25-29';
                ageRate = gender === 'female' ? 21.5 : 22.6;
            } else if (age >= 30 && age < 35) {
                ageGroup = '30-34';
                ageRate = gender === 'female' ? 29.9 : 29.5;
            } else if (age >= 35 && age < 40) {
                ageGroup = '35-39';
                ageRate = gender === 'female' ? 34.0 : 31.4;
            } else if (age >= 40 && age < 45) {
                ageGroup = '40-44';
                ageRate = gender === 'female' ? 36.8 : 31.7;
            } else if (age >= 45 && age < 50) {
                ageGroup = '45-49';
                ageRate = gender === 'female' ? 37.0 : 32.5;
            }

            let comparisonHTML = `
                <p>In India (2019-21 survey):</p>
                <ul style="margin: 10px 0; padding-left: 20px;">
                    <li>Overall ${genderText}: ${nationalRate}% are overweight/obese</li>
                    ${ageGroup ? `<li>Your age group (${ageGroup}): ${ageRate}% are overweight/obese</li>` : ''}
                    <li>Urban areas: ${gender === 'female' ? '33.3%' : '29.8%'} (higher risk)</li>
                    <li>Rural areas: ${gender === 'female' ? '19.7%' : '19.3%'} (lower risk)</li>
                </ul>
            `;
            document.getElementById('comparison-details').innerHTML = comparisonHTML;

            // Recommendations
            let recommendHTML = '';
            if (bmi >= 25) {
                recommendHTML = `
                    <ul style="margin: 0; padding-left: 20px;">
                        <li><strong>Target:</strong> Aim to lose 5-10% of your current weight (${(weight * 0.05).toFixed(1)}-${(weight * 0.10).toFixed(1)} kg)</li>
                        <li><strong>Activity:</strong> Walk 10,000 steps per day (use a phone app to track)</li>
                        <li><strong>Diet:</strong> Return to traditional Indian foods - dal, roti, sabzi instead of processed foods</li>
                        <li><strong>Monitoring:</strong> Weigh yourself monthly and track progress</li>
                        <li><strong>Medical:</strong> Get screened for diabetes, blood pressure, and cholesterol</li>
                    </ul>
                `;
            } else {
                recommendHTML = `
                    <ul style="margin: 0; padding-left: 20px;">
                        <li><strong>Maintain:</strong> Keep your current healthy weight</li>
                        <li><strong>Activity:</strong> Continue regular physical activity (7,000+ steps/day)</li>
                        <li><strong>Diet:</strong> Stick to traditional home-cooked meals</li>
                        <li><strong>Monitoring:</strong> Check weight quarterly to catch any changes early</li>
                    </ul>
                `;
            }
            document.getElementById('recommendation-details').innerHTML = recommendHTML;
        }

        // Risk Assessment
        function assessRisk() {
            const residence = document.getElementById('residence').value;
            const occupation = document.getElementById('occupation').value;
            const income = document.getElementById('income').value;
            const diet = document.getElementById('diet').value;
            const steps = document.getElementById('steps').value;

            if (!residence || !occupation || !income || !diet || !steps) {
                alert('Please answer all questions');
                return;
            }

            let riskScore = 0;
            let riskFactors = [];

            // Residence (Urban = higher risk)
            if (residence === 'urban') {
                riskScore += 3;
                riskFactors.push({
                    factor: 'Urban Residence',
                    impact: 'High',
                    description: 'Urban areas have 69% higher obesity rates than rural areas'
                });
            }

            // Occupation (Sedentary = higher risk)
            if (occupation === 'sedentary') {
                riskScore += 3;
                riskFactors.push({
                    factor: 'Sedentary Occupation',
                    impact: 'High',
                    description: 'Desk jobs significantly increase obesity risk'
                });
            } else if (occupation === 'moderate') {
                riskScore += 1;
            }

            // Income (Higher = higher risk in India)
            if (income === 'high') {
                riskScore += 3;
                riskFactors.push({
                    factor: 'High Income',
                    impact: 'High',
                    description: 'Wealthiest Indians have 4x higher obesity rates'
                });
            } else if (income === 'middle') {
                riskScore += 2;
                riskFactors.push({
                    factor: 'Middle Income',
                    impact: 'Medium',
                    description: 'Moderate risk due to access to processed foods'
                });
            }

            // Diet
            if (diet === 'often') {
                riskScore += 3;
                riskFactors.push({
                    factor: 'Frequent Processed Food',
                    impact: 'High',
                    description: 'Regular fast food consumption increases obesity risk'
                });
            } else if (diet === 'sometimes') {
                riskScore += 2;
            }

            // Steps
            if (steps === 'low') {
                riskScore += 3;
                riskFactors.push({
                    factor: 'Low Physical Activity',
                    impact: 'High',
                    description: 'Less than 3,000 steps/day is sedentary'
                });
            } else if (steps === 'moderate') {
                riskScore += 1;
            }

            // Determine risk level
            let riskLevel, riskColor, riskText;
            if (riskScore <= 4) {
                riskLevel = 'LOW RISK';
                riskColor = '#27AE60';
                riskText = 'Your lifestyle choices are generally protective against obesity.';
            } else if (riskScore <= 9) {
                riskLevel = 'MEDIUM RISK';
                riskColor = '#F39C12';
                riskText = 'You have some risk factors. Making changes now can prevent obesity.';
            } else {
                riskLevel = 'HIGH RISK';
                riskColor = '#E74C3C';
                riskText = 'You have multiple high-risk factors. Immediate lifestyle changes recommended.';
            }

            // Display results
            document.getElementById('risk-result').style.display = 'block';

            let scoreHTML = `
                <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 15px;">
                    <div style="background: ${riskColor}; color: white; padding: 15px 25px; border-radius: 8px; font-size: 1.3em; font-weight: 700;">
                        ${riskLevel}
                    </div>
                    <div style="flex: 1;">
                        <div style="font-size: 1.1em; color: #2C3E50;">${riskText}</div>
                        <div style="margin-top: 5px; color: #7F8C8D;">Risk Score: ${riskScore}/15</div>
                    </div>
                </div>
            `;
            document.getElementById('risk-score-display').innerHTML = scoreHTML;

            // Display risk factors
            if (riskFactors.length > 0) {
                let factorsHTML = '<h4 style="color: #2C3E50; margin-bottom: 10px;">Your Risk Factors:</h4>';
                factorsHTML += '<div style="display: grid; gap: 10px;">';

                riskFactors.forEach(rf => {
                    const impactColor = rf.impact === 'High' ? '#E74C3C' : '#F39C12';
                    factorsHTML += `
                        <div style="background: #F8F9FA; padding: 12px; border-radius: 6px; border-left: 3px solid ${impactColor};">
                            <div style="font-weight: 600; color: #2C3E50;">${rf.factor} <span style="color: ${impactColor}; font-size: 0.9em;">(${rf.impact} Impact)</span></div>
                            <div style="font-size: 0.9em; color: #7F8C8D; margin-top: 3px;">${rf.description}</div>
                        </div>
                    `;
                });
                factorsHTML += '</div>';
                document.getElementById('risk-factors-list').innerHTML = factorsHTML;
            } else {
                document.getElementById('risk-factors-list').innerHTML = '<p style="color: #27AE60; font-weight: 600;">Great! You have no major risk factors.</p>';
            }

            // Action plan
            let actionsHTML = '<h4 style="color: #2C3E50; margin-bottom: 10px;">Your Action Plan:</h4><ul style="padding-left: 20px;">';

            if (residence === 'urban') {
                actionsHTML += '<li><strong>Urban Living:</strong> Take stairs, walk for short trips, pack home-cooked lunch</li>';
            }
            if (occupation === 'sedentary') {
                actionsHTML += '<li><strong>Desk Job:</strong> Stand and stretch every 30 min, walk 10,000 steps/day</li>';
            }
            if (income === 'high' || income === 'middle') {
                actionsHTML += '<li><strong>Food Choices:</strong> Choose traditional Indian foods over expensive processed options</li>';
            }
            if (diet === 'often' || diet === 'sometimes') {
                actionsHTML += '<li><strong>Diet Change:</strong> Reduce processed food to less than once/week, cook at home</li>';
            }
            if (steps === 'low' || steps === 'moderate') {
                actionsHTML += '<li><strong>Increase Activity:</strong> Target 10,000 steps/day, join a walking group</li>';
            }

            if (riskScore <= 4) {
                actionsHTML += '<li><strong>Maintain:</strong> Keep up your healthy habits and monitor quarterly</li>';
            } else if (riskScore > 9) {
                actionsHTML += '<li><strong>Urgent:</strong> Consider consulting a healthcare provider for comprehensive assessment</li>';
            }

            actionsHTML += '</ul>';
            document.getElementById('action-plan').innerHTML = actionsHTML;

            // Scroll to results
            document.getElementById('risk-result').scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
        </script>

"""

# Insert the interactive tools
if insert_position != -1:
    new_html = html_content[:insert_position] + interactive_tools + html_content[insert_position:]

    # Write the updated dashboard
    with open('obesity_dashboard_enhanced.html', 'w', encoding='utf-8') as f:
        f.write(new_html)

    print("Interactive tools added successfully!")
    print("- BMI Calculator with personalized results")
    print("- Risk Factor Assessment questionnaire")
    print("- Comparison with India national data")
    print("- Personalized recommendations")
    print("\nOpen obesity_dashboard_enhanced.html to see the new features!")
else:
    print("Error: Could not find insertion point in the dashboard")
