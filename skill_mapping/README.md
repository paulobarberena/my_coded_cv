## Job Compatibility by Total Credits in Educational Path

                                                                                                                            

![Job Titles Chart](plots/job_titles.png)
```python
import matplotlib.pyplot as plt
# Define the areas for each course in df_education
course_areas = {
    'Public Law Institutions': 'Law and Political Science',
    'Economic Law': 'Law and Political Science',
    'Fundamentals of Administration': 'Administration and Management',
    'Food Quality Management': 'Food and Nutrition',
    'Diagnosis, Planning, and Control': 'Administration and Management',
    'International Finance': 'Finance and Economics',
    'Information Systems': 'Technology and Data Science',
    'Contemporary Brazilian Economy': 'Finance and Economics',
    'Accounting and Financial Statement Analysis I': 'Finance and Economics',
    'General Economic History': 'Finance and Economics',
    'Financial Department': 'Administration and Management',
    'Investment Selection': 'Finance and Economics',
    'Environment and Sustainable Development': 'Miscellaneous',
    'Bromatology': 'Food and Nutrition',
    'Treasury Management': 'Administration and Management',
    'Business Valuation': 'Finance and Economics',
    'Funding Sources': 'Finance and Economics',
    'Mergers and Acquisitions': 'Finance and Economics',
    'Economic Methodology II': 'Finance and Economics',
    'Introduction to Statistics': 'Mathematics and Statistics',
    'Economic Formation of Brazil I': 'Finance and Economics',
    'Monetary Economics': 'Finance and Economics',
    'Research Fundamentals': 'Finance and Economics',
    'Diet and Nutrition': 'Food and Nutrition',
    'Maintenance and Accident Prevention': 'Miscellaneous',
    'Risk Management': 'Administration and Management',
    'Social Accounting': 'Administration and Management',
    'Political Science': 'Law and Political Science',
    'Political Economy III': 'Law and Political Science',
    'Sociology': 'Law and Political Science',
    'Financial Mathematics': 'Mathematics and Statistics',
    'Food Technology': 'Food and Nutrition',
    'Informatics': 'Technology and Data Science',
    'Costs - Mathematics': 'Administration and Management',
    'Warehouse Management': 'Administration and Management',
    'Fundamentals of Marketing': 'Administration and Management',
    'Purchasing and Warehousing': 'Administration and Management',
    'History of Gastronomy': 'Food and Nutrition',
    'Introduction to Cooking': 'Food and Nutrition',
    'Microeconomics II': 'Finance and Economics',
    'Socio-Economic Development': 'Miscellaneous',
    'Analytical Geometry': 'Mathematics and Statistics',
    'Capital Markets': 'Finance and Economics',
    'Economic Liberalism': 'Finance and Economics',
    'Political Economy II': 'Law and Political Science',
    'Behavioral Economics': 'Finance and Economics',
    'Technical French': 'Miscellaneous',
    'Research and Technological Innovation': 'Miscellaneous',
    'Econometrics': 'Finance and Economics',
    'Economic Formation of Brazil II': 'Finance and Economics',
    'Microeconomics III': 'Finance and Economics',
    'Introduction to Economics': 'Finance and Economics',
    'Applied Legislation': 'Law and Political Science',
    'Human Nutrition': 'Food and Nutrition',
    'Viticulture and Winemaking': 'Food and Nutrition',
    'Personal Finance': 'Finance and Economics',
    'Game Theory': 'Finance and Economics',
    'Introduction to Administration': 'Administration and Management',
    'International Economics II': 'Finance and Economics',
    'Mathematics I': 'Mathematics and Statistics',
    'Mathematical Economics': 'Mathematics and Statistics',
    'Public Sector Economics': 'Finance and Economics',
    'Event Organization': 'Administration and Management',
    'Menu Engineering': 'Administration and Management',
    'Design and Equipment': 'Administration and Management',
    'Communication': 'Miscellaneous',
    'Macroeconomics II': 'Finance and Economics',
    'Economic Methodology': 'Finance and Economics',
    'Evolution of Economic Thought': 'Finance and Economics',
    'Macroeconomics III': 'Finance and Economics',
    'Food Toxicology': 'Food and Nutrition',
    'Economic Statistics': 'Finance and Economics',
    'Probability and Statistics': 'Mathematics and Statistics',
    'International Economics I': 'Finance and Economics',
    'Political Economy I': 'Law and Political Science',
    'Macroeconomics I': 'Finance and Economics',
    'Microeconomics I': 'Finance and Economics'
}

df_education['Area'] = df_education['Course'].map(course_areas)

# Prepare df_certificates to match df_education format and assign area
df_certificates['Credits'] = 2
df_certificates['Area'] = 'Technology and Data Science'
df_certificates = df_certificates.rename(columns={'Name': 'Course'})

# Consolidate dataframes
consolidated_df = pd.concat([df_education[['Area', 'Course', 'Credits']], df_certificates[['Area', 'Course', 'Credits']]], ignore_index=True)

# Step 2: Construct the areas dictionary
areas = consolidated_df.groupby('Area')['Course'].apply(list).to_dict()

# Step 3: Calculate the Credits for Each Job Title

job_titles = {
    'Business Administrator': ['Administration and Management'],
    'Operations Manager': ['Administration and Management'],
    'Business Analyst': ['Administration and Management'],
    'IT Manager': ['Administration and Management'],
    'Systems Analyst': ['Administration and Management'],
    'Finance Manager': ['Finance and Economics'],
    'Financial Analyst': ['Finance and Economics'],
    'Treasurer': ['Finance and Economics'],
    'Financial Controller': ['Finance and Economics'],
    'Valuation Analyst': ['Finance and Economics'],
    'Investment Banker': ['Finance and Economics'],
    'Financial Planner': ['Finance and Economics'],
    'Investment Advisor': ['Finance and Economics'],
    'Risk Manager': ['Administration and Management'],
    'Compliance Officer': ['Administration and Management'],
    'Social Accountant': ['Administration and Management'],
    'Auditor': ['Administration and Management'],
    'Cost Analyst': ['Administration and Management'],
    'Management Accountant': ['Administration and Management'],
    'Warehouse Manager': ['Administration and Management'],
    'Logistics Manager': ['Administration and Management'],
    'Procurement Manager': ['Administration and Management'],
    'Supply Chain Manager': ['Administration and Management'],
    'Event Planner': ['Administration and Management'],
    'Event Coordinator': ['Administration and Management'],
    'Restaurant Manager': ['Administration and Management'],
    'Menu Consultant': ['Administration and Management'],
    'Equipment Manager': ['Administration and Management'],
    'Design Engineer': ['Administration and Management'],
    'Economist': ['Finance and Economics'],
    'Policy Analyst': ['Finance and Economics'],
    'Economic Historian': ['Finance and Economics'],
    'Research Analyst': ['Finance and Economics'],
    'Central Banker': ['Finance and Economics'],
    'Market Analyst': ['Finance and Economics'],
    'Behavioral Economist': ['Finance and Economics'],
    'Data Analyst': ['Finance and Economics', 'Technology and Data Science'],
    'Mathematician': ['Mathematics and Statistics'],
    'Food Safety Manager': ['Food and Nutrition'],
    'Quality Assurance Manager': ['Food and Nutrition'],
    'Food Scientist': ['Food and Nutrition'],
    'Quality Control Analyst': ['Food and Nutrition'],
    'Nutritionist': ['Food and Nutrition'],
    'Dietitian': ['Food and Nutrition'],
    'Food Technologist': ['Food and Nutrition'],
    'Product Development Scientist': ['Food and Nutrition'],
    'Toxicologist': ['Food and Nutrition'],
    'Winemaker': ['Food and Nutrition'],
    'Viticulturist': ['Food and Nutrition'],
    'Food Historian': ['Food and Nutrition'],
    'Culinary Educator': ['Food and Nutrition'],
    'Chef': ['Food and Nutrition'],
    'Culinary Instructor': ['Food and Nutrition'],
    'IT Specialist': ['Technology and Data Science'],
    'Software Developer': ['Technology and Data Science'],
    'Data Scientist': ['Technology and Data Science'],
    'Python Developer': ['Technology and Data Science'],
    'Digital Marketer': ['Technology and Data Science'],
    'Marketing Analyst': ['Technology and Data Science'],
    'Customer Service Manager': ['Technology and Data Science'],
    'Customer Support Specialist': ['Technology and Data Science'],
    'Business Intelligence Analyst': ['Technology and Data Science'],
    'Environmental Consultant': ['Miscellaneous'],
    'Sustainability Manager': ['Miscellaneous'],
    'Maintenance Manager': ['Miscellaneous'],
    'Safety Engineer': ['Miscellaneous'],
    'Strategic Consultant': ['Miscellaneous'],
    'Translator': ['Miscellaneous'],
    'Technical Writer': ['Miscellaneous'],
    'Research Scientist': ['Miscellaneous'],
    'Innovation Manager': ['Miscellaneous'],
    'Researcher': ['Miscellaneous'],
    'Academic': ['Miscellaneous'],
    'Communications Specialist': ['Miscellaneous'],
    'Public Relations Officer': ['Miscellaneous']
}

# Create a dictionary with topics and their credits
topics_with_credits = dict(zip(consolidated_df['Course'], consolidated_df['Credits']))

# Calculate the credits for each job title
job_title_credits = {}

for job_title, related_areas in job_titles.items():
    total_credits = sum(topics_with_credits.get(topic, 0) for area in related_areas for topic in areas[area])
    job_title_credits[job_title] = total_credits

# Create a DataFrame from the job title credits dictionary
df_job_title_credits = pd.DataFrame(list(job_title_credits.items()), columns=['Job Title', 'Total Credits'])

# Calculate the percentage compatibility
max_credits = df_job_title_credits['Total Credits'].max()
df_job_title_credits['Compatibility (%)'] = (df_job_title_credits['Total Credits'] / max_credits) * 100

# Sort the DataFrame by total credits in descending order
df_job_title_credits = df_job_title_credits.sort_values(by='Total Credits', ascending=False).reset_index(drop=True)

# Extract the top 10 job titles
top_10_jobs = df_job_title_credits.head(10)

# Create a pie chart
fig, ax = plt.subplots(figsize=(10, 10))

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = top_10_jobs['Job Title']
sizes = top_10_jobs['Compatibility (%)']

ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')  

plt.show()
df_job_title_credits
```
| Job Title                     |       Total Credits           |             Compatibility (%)                     |
|:------------------------------|------------------------------:|--------------------------------------------------:|
| Data Analyst                  |                           157 |                                               100 |
| Policy Analyst                |                           130 |                                                82 |
| Investment Banker             |                           130 |                                                82 |
| Economist                     |                           130 |                                                82 |
| Economic Historian            |                           130 |                                                82 |
| Research Analyst              |                           130 |                                                82 |
| Central Banker                |                           130 |                                                82 |
| Market Analyst                |                           130 |                                                82 |
| Investment Advisor            |                           130 |                                                82 |
| Financial Planner             |                           130 |                                                82 |
| Valuation Analyst             |                           130 |                                                82 |
| Financial Controller          |                           130 |                                                82 |
| Treasurer                     |                           130 |                                                82 |
| Financial Analyst             |                           130 |                                                82 |
| Finance Manager               |                           130 |                                                82 |
| Behavioral Economist          |                           130 |                                                82 |
| Event Planner                 |                            47 |                                                29 |
| Operations Manager            |                            47 |                                                29 |
| Design Engineer               |                            47 |                                                29 |
| Equipment Manager             |                            47 |                                                29 |
| Menu Consultant               |                            47 |                                                29 |
| Restaurant Manager            |                            47 |                                                29 |
| Event Coordinator             |                            47 |                                                29 |
| Business Administrator        |                            47 |                                                29 |
| Supply Chain Manager          |                            47 |                                                29 |
| Social Accountant             |                            47 |                                                29 |
| Hospitality Manager           |                            47 |                                                29 |
| HR Manager                    |                            47 |                                                29 |
| Health and Safety Inspector   |                            27 |                                                17 |
| Public Health Manager         |                            27 |                                                17 |
| Nutritionist                  |                            27 |                                                17 |
| Viticulturist                 |                            27 |                                                17 |
| Winemaker                     |                            27 |                                                17 |
| Toxicologist                  |                            27 |                                                17 |
| Product Development Scientist |                            27 |                                                17 |
| Food Technologist             |                            27 |                                                17 |
| Dietitian                     |                            27 |                                                17 |
| Quality Control Analyst       |                            27 |                                                17 |
| Food Scientist                |                            27 |                                                17 |
| Quality Assurance Manager     |                            27 |                                                17 |
| Food Safety Manager           |                            27 |                                                17 |
| Business Intelligence Analyst |                            27 |                                                17 |
| Customer Support Specialist   |                            27 |                                                17 |
| Mathematician                 |                            25 |                                                15 |
| Environmental Consultant      |                            14 |                                                 8 |
| Sustainability Manager        |                            14 |                                                 8 |
| Maintenance Manager           |                            14 |                                                 8 |
| Safety Engineer               |                            14 |                                                 8 |
| Strategic Consultant          |                            14 |                                                 8 |
| Translator                    |                            14 |                                                 8 |
| Technical Writer              |                            14 |                                                 8 |
| Research Scientist            |                            14 |                                                 8 |
| Innovation Manager            |                            14 |                                                 8 |
| Researcher                    |                            14 |                                                 8 |
| Academic                      |                            14 |                                                 8 |
| Communications Specialist     |                            14 |                                                 8 |
| Public Relations Officer      |                            14 |                                                 8 |
