## Calculating my overall GPA from 3 different grading scales (Spain, Peru and Brazil)

### Combined Cumulative GPA: 3.31  
### Total Hours Studied: 5514.00

[View Education Table](luisvinatea/my_coded_cv/dataframes/df_education.csv)






```python
import numpy as np
import pandas as pd

# Define normalize_grade function
def normalize_grade(grade, max_grade, pass_threshold):
    if grade < pass_threshold:
        return (grade / pass_threshold) * 60  # Below passing threshold grades are scaled
    return 60 + ((grade - pass_threshold) / (max_grade - pass_threshold) * 40)

# Function to create DataFrame and calculate hours
def create_df(data, columns, credit_col=None):
    df = pd.DataFrame(data, columns=columns)
    if credit_col:
        df['Hours'] = df[credit_col] * 18
    return df

# Data for OBS Business School (course, credits, grade)
courses_obs = [
    ("Financial Department", 5, 9.31),
    ("Funding Sources", 5, 9.1),
    ("International Finance", 5, 9.75),
    ("Investment Selection", 5, 9.3),
    ("Business Valuation", 5, 9.2),
    ("Mergers and Acquisitions", 5, 8.9),
    ("Risk Management", 5, 8.5),
    ("Information Systems", 5, 9.5),
    ("Treasury Management", 5, 9.2),
    ("Diagnosis, Planning, and Control", 5, 9.8),
    ("Master's Final Project", 10, 9)
]
df_obs = create_df(courses_obs, ['Course', 'Credits', 'Grade'], 'Credits')

# Data for Le Cordon Bleu Perú
courses_ilcb = [
    ("Food Quality Management", 2, 20.0),
    ("Menu Engineering", 2, 14.0),
    ("Applied Legislation", 2, 15.0),
    ("Research and Technological Innovation", 2, 16.0),
    ("Event Organization", 3, 14.0),
    ("Viticulture and Winemaking", 3, 15.0),
    ("Diet and Nutrition", 3, 18.0),
    ("Fundamentals of Administration", 3, 20.0),
    ("Environment and Sustainable Development", 2, 19.0),
    ("Food Toxicology", 3, 13.0),
    ("Design and Equipment", 2, 14.0),
    ("Fundamentals of Marketing", 2, 17.0),
    ("Warehouse Management", 2, 17.0),
    ("Introduction to Cooking", 6, 17.0),
    ("Technical French", 3, 16.0),
    ("Costs - Mathematics", 2, 17.0),
    ("Informatics", 2, 17.0),
    ("Research Fundamentals", 2, 18.0),
    ("Human Nutrition", 3, 15.0),
    ("Food Technology", 3, 17.0),
    ("Bromatology", 3, 19.0),
    ("Purchasing and Warehousing", 3, 17.0),
    ("Communication", 1, 14.0),
    ("History of Gastronomy", 1, 17.0),
    ("Maintenance and Accident Prevention", 2, 18.0)
]
df_ilcb = create_df(courses_ilcb, ['Course', 'Credits', 'Grade'], 'Credits')

# Data for Universidade Federal de Santa Catarina
courses_ufsc = [
    ("Evolution of Economic Thought", 6.5, 72),
    ("International Economics II", 7.0, 72),
    ("International Economics I", 6.0, 72),
    ("Game Theory", 7.0, 72),
    ("Socio-Economic Development", 8.0, 72),
    ("Probability and Statistics", 6.0, 90),
    ("Analytical Geometry", 8.0, 72),
    ("Introduction to Economics", 7.5, 72),
    ("Social Accounting", 8.5, 72),
    ("General Economic History", 9.5, 72),
    ("Introduction to Statistics", 9.0, 72),
    ("Mathematics I", 7.0, 72),
    ("Political Economy I", 6.0, 72),
    ("Mathematical Economics", 7.0, 72),
    ("Macroeconomics I", 6.0, 72),
    ("Microeconomics I", 6.0, 72),
    ("Sociology", 8.5, 72),
    ("Macroeconomics II", 6.5, 72),
    ("Microeconomics II", 8.0, 72),
    ("Economic Statistics", 6.0, 72),
    ("Political Economy II", 8.0, 72),
    ("Personal Finance", 7.0, 72),
    ("Political Science", 8.5, 72),
    ("Economic Methodology", 6.5, 72),
    ("Macroeconomics III", 6.0, 72),
    ("Microeconomics III", 7.5, 72),
    ("Econometrics", 7.5, 72),
    ("Political Economy III", 8.5, 72),
    ("Capital Markets", 8.0, 72),
    ("Economic Formation of Brazil I", 9.0, 60),
    ("Monetary Economics", 9.0, 72),
    ("Special Topics - Development Area", 10.0, 72),
    ("Financial Mathematics", 8.5, 72),
    ("Introduction to Administration", 7.0, 72),
    ("Economic Methodology II", 9.0, 72),
    ("Economic Formation of Brazil II", 7.5, 72),
    ("Public Sector Economics", 7.0, 72),
    ("Economic Liberalism", 8.0, 72),
    ("Public Law Institutions", 10.0, 36),
    ("Economic Law", 10.0, 36),
    ("Accounting and Financial Statement Analysis I", 9.5, 72),
    ("Monograph", 9.0, 288),
    ("Behavioral Economics", 8.0, 72),
    ("Contemporary Brazilian Economy", 9.5, 72)
]
df_ufsc = create_df(courses_ufsc, ['Course', 'Grade', 'Hours'])
df_ufsc['Credits'] = df_ufsc['Hours'] / 18

# Normalize grades to a 0-100 scale
for df, max_grade, pass_threshold in [(df_obs, 10, 5), (df_ilcb, 20, 13), (df_ufsc, 10, 6)]:
    df['Grade'] = df['Grade'].apply(normalize_grade, args=(max_grade, pass_threshold))

# Add institution columns to df_ufsc, df_ilcb, df_obs
for df, institution in [(df_ufsc, 'Universidade Federal de Santa Catarina'), 
                        (df_ilcb, 'Le Cordon Bleu Perú'), 
                        (df_obs, 'OBS Business School')]:
    df['Institution'] = institution

# Merge the DataFrames
df_combined = pd.concat([df_ufsc, df_obs, df_ilcb], ignore_index=True)

df_combined['Grade (USA)'] = df_combined['Grade'] / 25
df_combined.drop('Grade', axis=1, inplace=True)

df_education = df_combined.sort_values(by='Grade (USA)', ascending=False)
df_education.reset_index(drop=True, inplace=True)

# Calculate the cumulative GPA
cumulative_gpa = np.average(df_education['Grade (USA)'], weights=df_combined['Credits'])

# Print the combined cumulative GPA
print(f"Combined Cumulative GPA: {cumulative_gpa:.2f}")
print(f"Total Hours Studied: {np.sum(df_education, axis=0)['Hours']:.2f}")
```
