#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import docx
from pdfminer.high_level import extract_text
import spacy
import re

# Install the model if it is not installed
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def parse_docx(file_path):
    doc = docx.Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

def parse_pdf(file_path):
    return extract_text(file_path)

def extract_information(text):
    doc = nlp(text)
    names = [ent.text for ent in doc.ents if ent.label_ == 'PERSON']
    
    # Extracting experience, education, and city
    experience_pattern = re.compile(r'(\d{1,2}\s+years?|\d{1,2}\+?\s+years?)', re.IGNORECASE)
    education_pattern = re.compile(r'\b(Bachelor|Master|PhD|Technician|Certificate)\b', re.IGNORECASE)
    city_pattern = re.compile(r'\b(Florianópolis|Lima|Barcelona)\b', re.IGNORECASE)

    experience = experience_pattern.findall(text)
    education = education_pattern.findall(text)
    cities = city_pattern.findall(text)

    return {
        'names': names,
        'experience': experience,
        'education': education,
        'cities': cities
    }

def compatibility_scoring(resume_text, job_keywords):
    resume_words = resume_text.lower().split()
    score = sum(1 for word in job_keywords if word in resume_words)
    return score

def highlight_matches(resume_text, job_keywords):
    resume_words = resume_text.split()
    highlighted_text = []
    for word in resume_words:
        if word.lower() in job_keywords:
            highlighted_text.append(f"**{word}**")
        else:
            highlighted_text.append(word)
    return ' '.join(highlighted_text)

def display_parsed_text(parsed_info):
    for key, value in parsed_info.items():
        st.write(f"{key}: {', '.join(value)}")

def main():
    st.title("ATS System")
    
    job_description = st.text_area("Enter the job description:")
    job_keywords = job_description.lower().split()
    
    uploaded_files = st.file_uploader("Upload resumes", accept_multiple_files=True, type=['pdf', 'docx'])
    
    if st.button("Process Resumes"):
        results = []
        
        for uploaded_file in uploaded_files:
            if uploaded_file.name.endswith('.pdf'):
                resume_text = parse_pdf(uploaded_file)
            elif uploaded_file.name.endswith('.docx'):
                resume_text = parse_docx(uploaded_file)
            else:
                continue
            
            score = compatibility_scoring(resume_text, job_keywords)
            highlighted_resume = highlight_matches(resume_text, job_keywords)
            parsed_info = extract_information(resume_text)
            
            results.append({
                'file': uploaded_file.name,
                'score': score,
                'highlighted': highlighted_resume,
                'parsed': parsed_info
            })
        
        results.sort(key=lambda x: x['score'], reverse=True)
        for result in results:
            st.write(f"Resume: {result['file']}, Score: {result['score']}")
            st.write("Highlighted Resume Text:")
            st.markdown(result['highlighted'])
            display_parsed_text(result['parsed'])

if __name__ == "__main__":
    main()


# In[ ]:




