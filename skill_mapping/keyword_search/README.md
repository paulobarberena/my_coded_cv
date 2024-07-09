# Job Board Hunt
```python
import requests
import json
from collections import Counter
import re
import pandas as pd
```

### Define API Credentials and Endpoint
```python
app_id = 'register at adzuna'
app_key = 'request your key'
base_url = 'https://api.adzuna.com/v1/api/jobs/gb/search/6'  # Choose the page to search every time you run the code (1, 2, 3, etc.)
```

### List of Job Titles to Search For
```python
job_titles = [
    "Data Analyst", "Policy Analyst", "Investment Banker", "Economist", "Economic Historian", "Research Analyst",
    "Central Banker", "Market Analyst", "Investment Advisor", "Financial Planner", "Valuation Analyst",
    "Financial Controller", "Treasurer", "Financial Analyst", "Finance Manager", "Behavioral Economist",
    "Event Planner", "Operations Manager", "Design Engineer", "Equipment Manager", "Menu Consultant",
    "Restaurant Manager", "Event Coordinator", "Business Administrator", "Supply Chain Manager", "Social Accountant",
    "Hospitality Manager", "HR Manager", "Health and Safety Inspector", "Public Health Manager", "Nutritionist",
    "Viticulturist", "Winemaker", "Toxicologist", "Product Development Scientist", "Food Technologist", "Dietitian",
    "Quality Control Analyst", "Food Scientist", "Quality Assurance Manager", "Food Safety Manager",
    "Business Intelligence Analyst", "Customer Support Specialist", "Mathematician", "Environmental Consultant",
    "Sustainability Manager", "Maintenance Manager", "Safety Engineer", "Strategic Consultant", "Translator",
    "Technical Writer", "Research Scientist", "Innovation Manager", "Researcher", "Academic", "Communications Specialist",
    "Public Relations Officer"
]
```

### Function to Clean and Tokenize Text
```python
def tokenize(text):
    text = text.lower()
    tokens = re.findall(r'\b\w+\b', text)
    return tokens
```

### Initialize Dictionary to Store Keyword Counts for Each Job Title
```python
job_keywords = {}
```

### Define Filtering Function
```python
def filter_sort_deduplicate_threshold_reset_index(df, job_titles, count_threshold):
    """
    Filter the DataFrame to include only rows with specified job titles, sort by 'Count' in descending order,
    remove duplicates from the 'Keyword' column, keep only rows where 'Count' is at least the specified threshold,
    and reset the index.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to filter, sort, deduplicate, apply the threshold, and reset index.
    job_titles (list): A list of job titles to include in the filtered DataFrame.
    count_threshold (int): The minimum count value to keep a row.
    
    Returns:
    pd.DataFrame: The filtered, sorted, deduplicated, threshold-applied, and index-reset DataFrame.
    """
    # Filter the DataFrame by job titles
    filtered_df = df[df['Job Title'].isin(job_titles)]
    # Sort the filtered DataFrame by 'Count' in descending order
    sorted_filtered_df = filtered_df.sort_values(by='Count', ascending=False)
    # Remove duplicates from the 'Keyword' column, keeping the first occurrence
    deduplicated_df = sorted_filtered_df.drop_duplicates(subset='Keyword', keep='first')
    # Keep only the rows where 'Count' is at least the specified threshold
    threshold_filtered_df = deduplicated_df[deduplicated_df['Count'] >= count_threshold]
    # Reset the index of the resulting DataFrame
    reset_index_df = threshold_filtered_df.reset_index(drop=True)
    
    return reset_index_df
```

### Load Existing Final DataFrame from CSV File
```python
try:
    final_df = pd.read_csv('final_job_keywords.csv')
except FileNotFoundError:
    final_df = pd.DataFrame(columns=['Job Title', 'Keyword', 'Count'])
```

### Iterate Over Each Job Title and Query the API
```python
for title in job_titles:
    params = {
        'app_id': app_id,
        'app_key': app_key,
        'results_per_page': 50,  # Increase the number of results per page
        'what': title,
        'content-type': 'application/json'
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data.get('results'):
        all_descriptions = []
        for job in data['results']:
            description = job.get('description', '')
            all_descriptions.extend(tokenize(description))
        
        # Count the frequency of each word
        keyword_counts = Counter(all_descriptions)
        
        # Filter out common stopwords if necessary
        stopwords = set(['and', 'the', 'to', 'of', 'in', 'a', 'for', 'with', 'on', 'as', 'is', 'are', 'that', 'this'])
        filtered_keywords = {word: count for word, count in keyword_counts.items() if word not in stopwords}
        
        # Store the most common keywords and their counts in the dictionary
        job_keywords[title] = filtered_keywords
```

### Convert the Dictionary to a DataFrame
```python
data_list = []
for job_title, keywords in job_keywords.items():
    for keyword, count in keywords.items():
        data_list.append([job_title, keyword, count])

df = pd.DataFrame(data_list, columns=['Job Title', 'Keyword', 'Count'])

# Sort the DataFrame by Job Title and Count
sorted_df = df.sort_values(by=['Job Title', 'Count'], ascending=[True, False])

job_titles_to_filter = [
    'Data Analyst', 'Policy Analyst', 'Investment Banker', 'Economist', 
    'Economic Historian', 'Research Analyst', 'Central Banker', 'Market Analyst', 
    'Investment Advisor', 'Financial Planner', 'Valuation Analyst', 'Financial Controller', 
    'Treasurer', 'Financial Analyst', 'Finance Manager'
]
count_threshold = 50

# Get new filtered DataFrame
new_filtered_df = filter_sort_deduplicate_threshold_reset_index(sorted_df, job_titles_to_filter, count_threshold)

# Calculate number of rows added to final_df
rows_before = len(final_df)
# Append new keywords to the final_df
final_df = pd.concat([final_df, new_filtered_df]).drop_duplicates(subset=['Job Title', 'Keyword'], keep='last').reset_index(drop=True)

rows_added = len(final_df) - rows_before

# Print the number of rows added
print(f"Rows added for job title '{title}': {rows_added}")
```

### Display the Final DataFrame
```python
print(final_df)
```

### Save the Final DataFrame to a CSV File
```python
final_df.to_csv('final_job_keywords.csv', index=False)
```
