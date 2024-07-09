import streamlit as st
import fitz  # PyMuPDF
import re
from datetime import datetime
from collections import defaultdict
import io

### Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(pdf_file)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

### Function to check date format and calculate work experience
def check_dates_and_experience(text):
    date_pattern = re.compile(r'\b(\d{2})[-/](\d{4})\b')
    dates = date_pattern.findall(text)
    correct_format = all(int(month) <= 12 for month, year in dates)
    
    work_experience = 0
    if correct_format and dates:
        date_objects = [datetime.strptime(f"01/{month}/{year}", "%d/%m/%Y") for month, year in dates]
        work_experience = (max(date_objects) - min(date_objects)).days // 365

    return correct_format, dates, work_experience

### Function to check for keywords
def check_keywords(text, category_keywords):
    results = defaultdict(list)
    for category, keywords in category_keywords.items():
        for keyword in keywords:
            if keyword.lower() in text.lower():
                results[category].append(keyword)
    return results
    
### Function to parse detailed information
def parse_detailed_info(text):
    universities_pattern = re.compile(r'(Universidade\sFederal\sde\sSanta\sCatarina|Le\sCordon\sBleu|OBS\sBusiness\sSchool|Universitat\sAutònoma\sde\sBarcelona|Universitat\sde\sBarcelona)', re.IGNORECASE)
    companies_pattern = re.compile(r'(Inca\sSushi|Pico\sAlto|iFood)', re.IGNORECASE)
    highest_qualification_pattern = re.compile(r'(MBA|Maestría|Licenciatura|Doctorado|Diplomado)', re.IGNORECASE)

    universities = list(set(universities_pattern.findall(text)))
    companies = list(set(companies_pattern.findall(text)))
    highest_qualification = list(set(highest_qualification_pattern.findall(text)))

    return universities, companies, highest_qualification

### Streamlit app
st.title('CV Formatter and Information Checker')

uploaded_file = st.file_uploader("Sube tu CV en formato PDF", type="pdf")

if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)
    st.subheader("Texto Extraído del CV")
    st.write(text)

### Check date formats and calculate work experience
    date_format_ok, dates, work_experience = check_dates_and_experience(text)
    if date_format_ok:
        st.success("Los formatos de fecha son correctos.")
    else:
        st.error("Formato de fecha incorrecto encontrado.")
    st.write("Fechas encontradas:", dates)
    st.write("Años de experiencia laboral:", work_experience)

### Define keywords for different categories
    category_keywords = {
        "areas_de_expertise": ["Análisis de Datos", "Marketing", "Finanzas", "Desarrollo de Software", "Ingeniería", "Consultor empresarial"],
        "job_titles": ["Gerente", "Analista", "Consultor", "Ingeniero", "Coordinador"],
        "contracts": ["Contrato", "Temporal", "Permanente", "Freelance", "Empreendimiento"],
        "studies": ["Licenciatura", "Maestría", "Doctorado", "Diplomado"]
    }

    keyword_results = check_keywords(text, category_keywords)
    for category, keywords_found in keyword_results.items():
        if keywords_found:
            st.success(f"Se encontraron palabras clave relacionadas con {category}: {', '.join(keywords_found)}.")
        else:
            st.error(f"No se encontraron palabras clave relacionadas con {category}.")
            
### Parse detailed information  
    universities, companies, highest_qualification = parse_detailed_info(text)
    st.write("Universidades atendidas:", ", ".join(universities))
    st.write("Empresas donde trabajó:", ", ".join(companies))
    st.write("Estudios de mayor nivel:", ", ".join(highest_qualification))

### Extract and display area of expertise     
    expertise_pattern = re.compile(r'Resumen\s(.+?)\sHabilidades', re.IGNORECASE | re.DOTALL)
    expertise_match = expertise_pattern.search(text)
    area_of_expertise = expertise_match.group(1).strip() if expertise_match else "No se pudo determinar el área de especialización."
    st.write("Área de especialización:", area_of_expertise)

### Prepare text for download            
    parsed_text = f"""
    Texto Extraído del CV:
    {text}

    Fechas encontradas: {dates}
    Años de experiencia laboral: {work_experience}
    Universidades atendidas: {', '.join(universities)}
    Empresas donde trabajó: {', '.join(companies)}
    Estudios de mayor nivel: {', '.join(highest_qualification)}
    Área de especialización: {area_of_expertise}
    """
### Convert the parsed text to a BytesIO object    
    text_io = io.BytesIO(parsed_text.encode('utf-8'))
    text_io.seek(0)

### Download button    
    st.download_button(
        label="Descargar texto parseado",
        data=text_io,
        file_name='parsed_cv.txt',
        mime='text/plain'
    )
