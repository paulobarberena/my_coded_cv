## Input Testing

### Text to Python

```python
import re
import random
import pandas as pd

# Function to generate random strings
def random_string(length):
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=length))

# Function to generate a random CV
def generate_random_cv():
    personal_info = [
        random_string(10),  # Name
        random_string(12),  # Title
        random_string(20),  # GitHub
        random_string(20),  # LinkedIn
        random_string(25),  # Email
        random_string(15),  # Phone
        random_string(25),  # Location 1
        random_string(25),  # Location 2
        random_string(50),  # Profile 1
        random_string(50),  # Profile 2
        random_string(50),  # Profile 3
        random_string(50),  # Profile 4
        random_string(50),  # Profile 5
        random_string(50),  # Profile 6
        random_string(50)   # Profile 7
    ]

    work_experience = [
        random_string(50),  # Company 1 Logo
        random_string(20),  # Company 1 Job Title
        "01/2020 - 12/2020",  # Company 1 Dates
        random_string(50),  # Company 1 Description 1
        random_string(50),  # Company 1 Description 2
        random_string(50),  # Company 1 Description 3
        random_string(50),  # Company 1 Description 4
        random_string(50),  # Company 1 Description 5
        random_string(50),  # Company 1 Description 6
        random_string(50),  # Company 1 Description 7
        random_string(50),  # Company 1 Description 8
        random_string(50),  # Company 1 Description 9
        random_string(50),  # Company 2 Logo
        "01/2019 - 12/2019",  # Company 2 Role 1 Dates
        random_string(50),  # Company 2 Role 1 Description 1
        random_string(50),  # Company 2 Role 1 Description 2
        random_string(50),  # Company 2 Role 1 Description 3
        random_string(50),  # Company 2 Role 1 Description 4
        random_string(50),  # Company 2 Role 1 Description 5
        random_string(50),  # Company 2 Role 1 Description 6
        random_string(50),  # Company 2 Role 1 Description 7
        random_string(50),  # Company 2 Role 1 Description 8
        "01/2018 - 12/2018",  # Company 2 Role 2 Dates
        random_string(50),  # Company 2 Role 2 Description 1
        random_string(50),  # Company 2 Role 2 Description 2
        random_string(50),  # Company 2 Role 2 Description 3
        random_string(50),  # Company 2 Role 2 Description 4
        random_string(50),  # Company 2 Role 2 Description 5
        random_string(50),  # Company 2 Role 2 Description 6
        random_string(50),  # Company 2 Role 2 Description 7
        random_string(50),  # Company 2 Role 2 Description 8
        "01/2017 - 12/2017",  # Company 2 Role 3 Dates
        random_string(50),  # Company 2 Role 3 Description 1
        random_string(50),  # Company 2 Role 3 Description 2
        random_string(50),  # Company 2 Role 3 Description 3
        random_string(50),  # Company 2 Role 3 Description 4
        random_string(50),  # Company 2 Role 3 Description 5
        random_string(50),  # Company 2 Role 3 Description 6
        random_string(50),  # Company 2 Role 3 Description 7
        random_string(50),  # Company 2 Role 3 Description 8
        random_string(50),  # Company 2 Role 3 Description 9
        random_string(50),  # Company 2 Role 3 Description 10
        random_string(50),  # Company 2 Role 3 Description 11
        random_string(50),  # Company 2 Role 3 Description 12
        random_string(50),  # Company 2 Role 3 Description 13
        random_string(50)   # Company 2 Role 3 Description 14
    ]

    academic_path = [
        random_string(20),  # Overall GPA
        random_string(20),  # Institution 1 Logo
        random_string(20),  # Institution 1 Degree
        random_string(20),  # Institution 1 Partner
        "01/2023 - 12/2023",  # Institution 1 Dates
        random_string(20),  # Institution 1 Activities
        random_string(20),  # Institution 1 Projects
        random_string(20),  # Institution 2 Logo
        random_string(20),  # Institution 2 Degree
        random_string(20),  # Institution 2 Location
        "01/2022 - 12/2022",  # Institution 2 Dates
        random_string(20),  # Institution 3 Logo
        random_string(20),  # Institution 3 Interexchange
        random_string(20),  # Institution 3 Degree
        random_string(20),  # Institution 3 Location
        "01/2021 - 12/2021",  # Institution 3 Dates
        random_string(20)   # Institution 3 Achievements
    ]

    skills = [
        random_string(10), random_string(10), random_string(10),  # Languages
        random_string(10), random_string(10), random_string(10),  # Programming
        random_string(10), random_string(10), random_string(10), random_string(10),  # Data Analysis
        random_string(10), random_string(10),  # Data Visualization
        random_string(10), random_string(10), random_string(10),  # Machine Learning
        random_string(10), random_string(10), random_string(10),  # Web Development
        random_string(10), random_string(10), random_string(10),  # Finance
        random_string(10), random_string(10), random_string(10),  # Management
        random_string(10), random_string(10), random_string(10),  # Marketing
        random_string(10), random_string(10), random_string(10)   # Culinary Arts
    ]

    certifications = [
        random_string(20), random_string(20),  # Badges
        random_string(20)   # Credentials
    ]

    return personal_info + work_experience + academic_path + skills + certifications

txt_dictionary = generate_random_cv()

# Function to count characters and identify datetime strings
def count_characters_and_identify_datetimes(string_list):
    datetime_patterns = [
        re.compile(r"^\d{2}/\d{4} - \d{2}/\d{4}$"),  # mm/yyyy - mm/yyyy
        re.compile(r"^\d{4}-\d{2}-\d{2}$"),  # yyyy-mm-dd
        re.compile(r"^\d{2}-\d{2}-\d{4}$"),  # dd-mm-yyyy
        re.compile(r"^\d{2}/\d{2}/\d{4}$"),  # dd/mm/yyyy
        re.compile(r"^\d{2} \b\w{3}\b \d{4}$"),  # dd MMM yyyy
        re.compile(r"^\d{2} \b\w{4,}\b \d{4}$")  # dd MMMM yyyy
    ]
    
    results = []
    for item in string_list:
        is_datetime = any(pattern.match(item) for pattern in datetime_patterns)
        results.append((len(item), is_datetime))
    
    return results

# Get the character counts and datetime identification for each string
character_counts_and_datetimes = count_characters_and_identify_datetimes(txt_dictionary)

# Prepare the data for the DataFrame
data = {
    "Datatype": ["str" for _ in character_counts_and_datetimes],
    "Count": [count for count, _ in character_counts_and_datetimes],
    "Datetime": [is_datetime for _, is_datetime in character_counts_and_datetimes]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('txt_structure.csv', index=False)

# Updated txt_structure dictionary
txt_structure = {
    "strings": [count for count, _ in character_counts_and_datetimes],
    "dates": [is_datetime for _, is_datetime in character_counts_and_datetimes]
}

# Function to fill the python structure
def fill_python_structure(txt_dictionary):
    python_structure = {
        "personal_info": {
            "Name": {"type": "str"},
            "Title": {"type": "str"},
            "Contact": {


                "GitHub": {"type": "str"},
                "LinkedIn": {"type": "str"},
                "Email": {"type": "str"},
                "Phone": {"type": "str"},
                "Location": {
                    "type": "list",
                    "items": [
                        {"type": "str"},
                        {"type": "str"}
                    ]
                }
            },
            "Profile": {
                "type": "list",
                "items": [
                    {"type": "str"},
                    {"type": "str"},
                    {"type": "str"},
                    {"type": "str"},
                    {"type": "str"},
                    {"type": "str"},
                    {"type": "str"}
                ]
            }
        },
        "work_experience": {
            "Company 1": {
                "Logo": {"type": "html"},
                "Job Title": {"type": "str"},
                "Dates": {"type": "str"},
                "Description": {
                    "type": "list",
                    "items": [
                        {"type": "str"},
                        {"type": "str"},
                        {"type": "str"},
                        {"type": "str"},
                        {"type": "str"},
                        {"type": "str"},
                        {"type": "str"},
                        {"type": "str"},
                        {"type": "str"}
                    ]
                }
            },
            "Company with More Roles": {
                "Logo": {"type": "html"},
                "Roles": {
                    "Role 1": {
                        "Dates": {"type": "str"},
                        "Description": {
                            "type": "list",
                            "items": [
                                {"type": "str"},
                                {"type": "str"},
                                {"type": "str"},
                                {"type": "str"},
                                {"type": "str"},
                                {"type": "str"},
                                {"type": "str"},
                                {"type": "str"}
                            ]
                        }
                    },
                    "Role 2": {
                        "Dates": {"type": "str"},
                        "Description": {
                            "type": "list",
                            "items": [
                                {"type": "str"},
                                {"type": "str"},
                                {"type": "str"},
                                {"type": "str"},
                                {"type": "str"},
                                {"type": "str"},
                                {"type": "str"}
                            ]
                        }
                    },
                    "Role 3": {
                        "Dates": {"type": "str"},
                        "Description": {
                            "type": "list",
                            "items": [
                                {"type": "str"},
                                {"type": "str"},
                                {"type": "str"},
                                {"type": "str"},
                                {"type": "str"},
                                {"type": "str"},
                                {"type": "str"},
                                {"type": "str"},
                                {"type": "str"},
                                {"type": "str"},
                                {"type": "str"},
                                {"type": "str"},
                                {"type": "str"}
                            ]
                        }
                    }
                }
            }
        },
        "academic_path": {
            "Overall GPA": {"type": "html"},
            "Institution 1": {
                "Logo": {"type": "str"},
                "Degree": {"type": "str"},
                "Partner": {"type": "str"},
                "Dates": {"type": "str"},
                "Activities": {"type": "str"},
                "Projects": {"type": "str"}
            },
            "Institution 2": {
                "Logo": {"type": "str"},
                "Degree": {"type": "str"},
                "Location": {"type": "str"},
                "Dates": {"type": "str"}
            },
            "Institution 3": {
                "Logo": {"type": "str"},
                "Interexchange": {"type": "str"},
                "Degree": {"type": "str"},
                "Location": {"type": "str"},
                "Dates": {"type": "str"},
                "Achievements": {"type": "str"}
            }
        },
        "skills": {
            "Languages": {
                "type": "list",
                "items": [
                    {"type": "str"},
                    {"type": "str"},
                    {"type": "str"}
                ]
            },
            "Programming": {
                "type": "list",
                "items": [
                    {"type": "str"},
                    {"type": "str"},
                    {"type": "str"}
                ]
            },
            "Data Analysis": {
                "type": "list",
                "items": [
                    {"type": "str"},
                    {"type": "str"},
                    {"type": "str"},
                    {"type": "str"}
                ]
            },
            "Data Visualization": {
                "type": "list",
                "items": [
                    {"type": "str"},
                    {"type": "str"}
                ]
            },
            "Machine Learning": {
                "type": "list",
                "items": [
                    {"type": "str"},
                    {"type": "str"},
                    {"type": "str"}
                ]
            },
            "Web Development": {
                "type": "list",
                "items": [
                    {"type": "str"},
                    {"type": "str"},
                    {"type": "str"}
                ]
            },
            "Finance": {
                "type": "list",
                "items": [
                    {"type": "str"},
                    {"type": "str"},
                    {"type": "str"}
                ]
            },
            "Management": {
                "type": "list",
                "items": [
                    {"type": "str"},
                    {"type": "str"},
                    {"type": "str"}
                ]
            },
            "Marketing": {
                "type": "list",
                "items": [
                    {"type": "str"},
                    {"type": "str"},
                    {"type": "str"}
                ]
            },
            "Culinary Arts": {
                "type": "list",
                "items": [
                    {"type": "str"},
                    {"type": "str"},
                    {"type": "str"}
                ]
            }
        },
        "certifications": {
            "Badges": {
                "type": "list",
                "items": [
                    {"type": "str"},
                    {"type": "str"}
                ]
            },
            "Credentials": {
                "type": "list",
                "items": [
                    {"type": "str"}
                ]
            }
        }
    }

    # Index map to fill the python structure
    index = 0

    personal_info = {
        "Name": txt_dictionary[index],
        "Title": txt_dictionary[index + 1],
        "Contact": {
            "GitHub": txt_dictionary[index + 2],
            "LinkedIn": txt_dictionary[index + 3],
            "Email": txt_dictionary[index + 4],
            "Phone": txt_dictionary[index + 5],
            "Location": [
                txt_dictionary[index + 6],
                txt_dictionary[index + 7]
            ]
        },
        "Profile": [
            txt_dictionary[index + 8],
            txt_dictionary[index + 9],
            txt_dictionary[index + 10],
            txt_dictionary[index + 11],
            txt_dictionary[index + 12],
            txt_dictionary[index + 13],
            txt_dictionary[index + 14]
        ]
    }
    index += 15

    work_experience = {
        "Company 1": {
            "Logo": txt_dictionary[index],
            "Job Title": txt_dictionary[index + 1],
            "Dates": txt_dictionary[index + 2],
            "Description": [
                txt_dictionary[index + 3],
                txt_dictionary[index + 4],
                txt_dictionary[index + 5],
                txt_dictionary[index + 6],
                txt_dictionary[index + 7],
                txt_dictionary[index + 8],
                txt_dictionary[index + 9],
                txt_dictionary[index + 10],
                txt_dictionary[index + 11]
            ]
        },
        "Company with More Roles": {
            "Logo": txt_dictionary[index + 12],
            "Roles": {
                "Role 1": {
                    "Dates": txt_dictionary[index + 13],
                    "Description": [
                        txt_dictionary[index + 14],
                        txt_dictionary[index + 15],
                        txt_dictionary[index + 16],
                        txt_dictionary[index + 17],
                        txt_dictionary[index + 18],
                        txt_dictionary[index + 19],
                        txt_dictionary[index + 20],
                        txt_dictionary[index + 21]
                    ]
                },
                "Role 2": {
                    "Dates": txt_dictionary[index + 22],
                    "Description": [
                        txt_dictionary[index + 23],
                        txt_dictionary[index + 24],
                        txt_dictionary[index + 25],
                        txt_dictionary[index + 26],
                        txt_dictionary[index + 27],
                        txt_dictionary[index + 28],
                        txt_dictionary[index + 29],
                        txt_dictionary[index + 30]
                    ]
                },
                "Role 3": {
                    "Dates": txt_dictionary[index + 31],
                    "Description": [
                        txt_dictionary[index + 32],
                        txt_dictionary[index + 33],
                        txt_dictionary[index + 34],
                        txt_dictionary[index + 35],
                        txt_dictionary[index + 36],
                        txt_dictionary[index + 37],
                        txt_dictionary[index + 38],
                        txt_dictionary[index + 39],
                        txt_dictionary[index + 40],
                        txt_dictionary[index + 41],
                        txt_dictionary[index + 42],
                        txt_dictionary[index + 43],
                        txt_dictionary[index + 44]
                    ]
                }
            }
        }
    }
    index += 45

    academic_path = {
        "Overall GPA": txt_dictionary[index],
        "Institution 1": {
            "Logo": txt_dictionary[index + 1],
            "Degree": txt_dictionary[index + 2],
            "

Partner": txt_dictionary[index + 3],
            "Dates": txt_dictionary[index + 4],
            "Activities": txt_dictionary[index + 5],
            "Projects": txt_dictionary[index + 6]
        },
        "Institution 2": {
            "Logo": txt_dictionary[index + 7],
            "Degree": txt_dictionary[index + 8],
            "Location": txt_dictionary[index + 9],
            "Dates": txt_dictionary[index + 10]
        },
        "Institution 3": {
            "Logo": txt_dictionary[index + 11],
            "Interexchange": txt_dictionary[index + 12],
            "Degree": txt_dictionary[index + 13],
            "Location": txt_dictionary[index + 14],
            "Dates": txt_dictionary[index + 15],
            "Achievements": txt_dictionary[index + 16]
        }
    }
    index += 17

    skills = {
        "Languages": [txt_dictionary[index], txt_dictionary[index + 1], txt_dictionary[index + 2]],
        "Programming": [txt_dictionary[index + 3], txt_dictionary[index + 4], txt_dictionary[index + 5]],
        "Data Analysis": [txt_dictionary[index + 6], txt_dictionary[index + 7], txt_dictionary[index + 8], txt_dictionary[index + 9]],
        "Data Visualization": [txt_dictionary[index + 10], txt_dictionary[index + 11]],
        "Machine Learning": [txt_dictionary[index + 12], txt_dictionary[index + 13], txt_dictionary[index + 14]],
        "Web Development": [txt_dictionary[index + 15], txt_dictionary[index + 16], txt_dictionary[index + 17]],
        "Finance": [txt_dictionary[index + 18], txt_dictionary[index + 19], txt_dictionary[index + 20]],
        "Management": [txt_dictionary[index + 21], txt_dictionary[index + 22], txt_dictionary[index + 23]],
        "Marketing": [txt_dictionary[index + 24], txt_dictionary[index + 25], txt_dictionary[index + 26]],
        "Culinary Arts": [txt_dictionary[index + 27], txt_dictionary[index + 28], txt_dictionary[index + 29]]
    }
    index += 30

    certifications = {
        "Badges": [txt_dictionary[index], txt_dictionary[index + 1]],
        "Credentials": [txt_dictionary[index + 2]]
    }

    return personal_info, work_experience, academic_path, skills, certifications

personal_info, work_experience, academic_path, skills, certifications = fill_python_structure(txt_dictionary)

# Function to convert the structure to markdown
def to_markdown(d):
    if isinstance(d, dict):
        return '\n'.join([f"**{k}**:\n{to_markdown(v)}" for k, v in d.items()])
    elif isinstance(d, list):
        return '\n'.join([f"- {to_markdown(elem)}" for elem in d])
    else:
        return str(d)

# Print the structures in markdown
print("## Personal Info")
print(to_markdown(personal_info))
print("\n## Work Experience")
print(to_markdown(work_experience))
print("\n## Academic Path")
print(to_markdown(academic_path))
print("\n## Skills")
print(to_markdown(skills))
print("\n## Certifications")
print(to_markdown(certifications))
```

### Backtesting

```python
personal_info = [
    {
        "Name": "Luis Vinatea",
        "Title": "Data Analyst",
        "Contact": {
            "GitHub": "https://github.com/luisvinatea",
            "LinkedIn": "https://linkedin.com/in/luisvinatea",
            "Email": "mailto:luisvinateabarberena@gmail.com",
            "Phone": "https://wa.me/+5548988552904",
            "Location": [
                "https://maps.app.goo.gl/9fFpEyAD8WgabwmK7",
                "https://maps.app.goo.gl/AbScoAQwju7Jgt5A9"
            ]
        },
        "Profile": [
            "Administrator and analyst with 5 years of experience in the market.",
            "Born in Brazil of Peruvian parents, lived in the USA, Spain, and Peru.",
            "Holds a degree in Economics and a diploma in Management.",
            "Currently pursuing an MBA in financial management at OBS Business School, in collaboration with the University of Barcelona.",
            "Former restaurant owner with deep knowledge of delivery operations, restaurant budgeting, menu engineering, and sales strategy.",
            "Able to provide insights as a multilingual and multidisciplinary professional.",
            "Works as a consultant, helping small businesses make decisions supported by data analysis."
        ]
    }
]

work_experience = { 
    "Pico Alto (iFood)": { 
        "Logo": "<img src='https://github.com/luisvinatea/my_coded_cv/blob/62528b929a7629a209378b8c9fd7ab8f2d3c3898/logos/picoalto.png' alt='Pico Alto' width='100'/>",
        "Job Title": "Data Analyst (Contract)",
        "Dates": "01/2024 - Present",
        "Description": [
            "Conducted business analysis to address excessive expenditures on marketing, suppliers, and intermediation costs, resulting in cost savings.",
            "Resolved unpredictability in sales and cooling offs, thus eliminating unused labor and food waste.",
            "Recognized as iFood's super restaurant for outstanding performance.",
            "Gathered data through API integration from POS systems, bank account transactions, and advertiser accounts.",
            "Cleaned, manipulated, and processed data using Python, R programming languages, and Excel.",
            "Utilized statistical analysis to validate trends and retrieve reference data from SQL databases.",
            "Developed dashboards on Microsoft Power BI to deliver insights to stakeholders.",
            "Achieved a 10% reduction in delivery charges and increased sales conversion rate from 3% to 12%.",
            "Decreased CPC on Meta Ads by 30% and achieved 20% more leads on direct channels."
        ]
    },
    "Inca Sushi (iFood)": {
        "Logo": "<img src='https://github.com/luisvinatea/my_coded_cv/blob/62528b929a7629a209378b8c9fd7ab8f2d3c3898/logos/Logo IncaSushi monocromatico-01-01.png' alt='Inca Sushi' width='100'/>",
        "Roles": {
            "Data Analyst (Self-Employed)": {
                "Dates": "01/2021 - 01/2022",
                "Description": [
                    "Launched a ghost kitchen in a small town with limited resources and specialized cuisine, establishing a unique market presence.",
                    "Conducted market research by analyzing population census data and real estate listings to identify key demographic and economic factors.",
                    "Utilized Python and Excel to clean and process data, and Tableau for data visualization and analysis.",
                    "Identified a cost-effective kitchen location, reducing rent expenses to only 5% of total revenue.",
                    "Relocated to a better neighborhood, resulting in a 6x increase in daily orders and a peak conversion rate of 20%.",
                    "Implemented menu engineering techniques to optimize average ticket value and customer satisfaction, achieving a rating of 4.8/5.",
                    "Generated over 1 million BRL in gross income through successful operation and delivery of more than 10,000 orders.",
                    "Recognized as a top-performing restaurant by iFood."
                ]
            },
            "Marketing Analyst (Self-Employed)": {
                "Dates": "01/2022 - 01/2023",
                "Description": [
                    "Created sales strategies to drive customer traffic to the company's e-commerce platform, eliminating the need for intermediaries and significantly enhancing revenue streams.",
                    "Implemented CRM systems to develop tailored customer lists tracked through Facebook Pixel events manager for targeted marketing efforts.",
                    "Evaluated and optimized creative content and graphic design using Adobe Photoshop and SEO techniques to conduct comprehensive market research.",
                    "Created paid advertising campaigns by analyzing top-performing organic posts to maximize reach and identify potential customers.",
                    "Conducted demographic testing at the ad set level targeting specific age, gender, and distance parameters with CTAs leading to WhatsApp or Instagram DMs.",
                    "Implemented compelling offers to mitigate seasonality in sales and enhance customer engagement.",
                    "Generated 4000 leads from WhatsApp and increased direct sales by 40% to boost overall revenue.",
                    "Recognized as iFood's super restaurant for exceptional sales performance and customer service excellence."
                ]
            },
            "Project Manager (Self-Employed)": {
                "Dates": "01/2023 - 01/2024",
                "Description": [
                    "Managed inflation on inputs, navigated through layoffs, and recruited employees on a regular basis to maintain operational efficiency.",
                    "Secured credit to finance initial investment in 2021 and utilized strategic credit to cover labor obligations.",
                    "Removed top 10 unpopular dishes and eliminated menu items requiring unique ingredients.",
                    "Standardized menu prices according to Omnes' principles and increased median value.",
                    "Introduced salmon, vegetarian menus, customizable combos, and culinary arts techniques to enhance value perception.",
                    "Negotiated with suppliers to extend invoice payment terms, alleviating liquidity constraints.",
                    "Implemented food additives and safety measures to increase durability of sauces, mayonnaise, fish, and seafood.",
                    "Utilized automated systems to synchronize sales, recipe cards, and supply purchase receipts into CRM operations system.",
                    "Increased productive capacity to streamline food service operations management and reduce delivery times.",
                    "Reduced Food Cost to 23% in most dishes, significantly cutting monetary outflow to suppliers.",
                    "Raised average ticket price from 80

 to 180 BRL through effective menu strategies.",
                    "Generated over 500,000 BRL in gross income during the year 2022."
                ]
            }
        }
    }
}

academic_path = [
    {
        "Overall GPA": "<img src='https://github.com/luisvinatea/my_coded_cv/blob/62528b929a7629a209378b8c9fd7ab8f2d3c3898/logos/gpa.png' alt='GPA' width='100'/>",
        "Institution 1": {
            "Logo": "<img src='https://github.com/luisvinatea/my_coded_cv/blob/62528b929a7629a209378b8c9fd7ab8f2d3c3898/logos/OBS business school.png' alt='OBS Business School' width='100'/>",
            "Degree": "Master of Business Administration - MBA",
            "Partner": "University of Barcelona",
            "Dates": "01/2023 - 12/2023",
            "Activities": "Project Management, Business Intelligence",
            "Projects": "Consultancy"
        }
    },
    {
        "Institution 2": {
            "Logo": "<img src='https://github.com/luisvinatea/my_coded_cv/blob/62528b929a7629a209378b8c9fd7ab8f2d3c3898/logos/usb.png' alt='Universidad San Ignacio de Loyola' width='100'/>",
            "Degree": "Bachelor's degree",
            "Location": "Peru",
            "Dates": "01/2022 - 12/2022"
        }
    },
    {
        "Institution 3": {
            "Logo": "<img src='https://github.com/luisvinatea/my_coded_cv/blob/62528b929a7629a209378b8c9fd7ab8f2d3c3898/logos/ulpgc.png' alt='Universidad de Las Palmas de Gran Canaria' width='100'/>",
            "Interexchange": "Erasmus+",
            "Degree": "International Business Administration",
            "Location": "Spain",
            "Dates": "01/2021 - 12/2021",
            "Achievements": "Studied at one of the top business schools in Spain, obtained scholarships."
        }
    }
]

skills = {
    "Languages": ["Spanish", "English", "Portuguese"],
    "Programming": ["Python", "SQL", "R"],
    "Data Analysis": ["Excel", "Google Sheets", "Pandas", "Numpy"],
    "Data Visualization": ["Power BI", "Tableau"],
    "Machine Learning": ["Scikit-learn", "TensorFlow", "Keras"],
    "Web Development": ["HTML", "CSS", "JavaScript"],
    "Finance": ["Financial Analysis", "Budgeting", "Forecasting"],
    "Management": ["Project Management", "Team Leadership", "Strategic Planning"],
    "Marketing": ["SEO", "Content Marketing", "Social Media Marketing"],
    "Culinary Arts": ["Menu Engineering", "Cost Control", "Food Safety"]
}

certifications = {
    "Badges": ["Data Analysis", "Machine Learning"],
    "Credentials": ["Certified Data Analyst"]
}
