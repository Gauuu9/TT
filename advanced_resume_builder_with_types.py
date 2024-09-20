import streamlit as st
from fpdf import FPDF
import language_tool_python

# Function to generate resume
def generate_resume(data):
    resume = f"""
    # Resume

    ## {data['full_name']}
    **Email:** {data['email']}  
    **Phone:** {data['phone']}  
    **LinkedIn:** {data['linkedin']}  

    ## Summary
    {data['summary']}

    ## Education
    {data['education']}

    ## Experience
    {data['experience']}

    ## Skills
    {data['skills']}
    """
    return resume

# Function to generate cover letter
def generate_cover_letter(data):
    cover_letter = f"""
    {data['date']}
    
    {data['company_name']}  
    {data['company_address']}  

    Dear Hiring Manager,

    I am writing to express my interest in the {data['job_title']} position at {data['company_name']}. 
    {data['cover_letter_content']}

    Thank you for considering my application. I look forward to the opportunity to discuss my qualifications further.

    Sincerely,  
    {data['full_name']}
    """
    return cover_letter

# Function to create PDF
def create_pdf(content):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    for line in content.split('\n'):
        pdf.multi_cell(0, 10, line)

    return pdf.output(dest='S').encode('latin1')

# Function to check grammar
def check_grammar(text):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    return matches

# Streamlit UI
st.title("Resume and Cover Letter Builder")

# Common input fields
st.header("Personal Information")
full_name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
linkedin = st.text_input("LinkedIn Profile URL")
summary = st.text_area("Summary/Objective")
education = st.text_area("Education")
experience = st.text_area("Experience")
skills = st.text_area("Skills")

# Cover Letter specific fields
st.header("Cover Letter Details")
date = st.text_input("Date")
company_name = st.text_input("Company Name")
company_address = st.text_input("Company Address")
job_title = st.text_input("Job Title")
cover_letter_content = st.text_area("Cover Letter Content")

# Check details button
if st.button("Check Details"):
    errors = []
    inputs = {
        "Full Name": full_name,
        "Email": email,
        "Phone": phone,
        "LinkedIn": linkedin,
        "Summary": summary,
        "Education": education,
        "Experience": experience,
        "Skills": skills,
        "Date": date,
        "Company Name": company_name,
        "Company Address": company_address,
        "Job Title": job_title,
        "Cover Letter Content": cover_letter_content,
    }

    for field, text in inputs.items():
        matches = check_grammar(text)
        if matches:
            errors.append(f"{field}: {len(matches)} error(s) found.")

    if errors:
        st.warning("Grammatical errors found:")
        for error in errors:
            st.write(error)
    else:
        st.success("No grammatical errors found!")

# Generate buttons
if st.button("Generate Resume"):
    resume = generate_resume({
        'full_name': full_name,
        'email': email,
        'phone': phone,
        'linkedin': linkedin,
        'summary': summary,
        'education': education,
        'experience': experience,
        'skills': skills,
    })
    st.subheader("Your Resume")
    st.markdown(resume)
    
    # Create PDF
    pdf_resume = create_pdf(resume)
    st.download_button("Download Resume as PDF", data=pdf_resume, file_name="resume.pdf")

if st.button("Generate Cover Letter"):
    cover_letter = generate_cover_letter({
        'date': date,
        'company_name': company_name,
        'company_address': company_address,
        'job_title': job_title,
        'cover_letter_content': cover_letter_content,
        'full_name': full_name,
    })
    st.subheader("Your Cover Letter")
    st.markdown(cover_letter)
    
    # Create PDF
    pdf_cover_letter = create_pdf(cover_letter)
    st.download_button("Download Cover Letter as PDF", data=pdf_cover_letter, file_name="cover_letter.pdf")
