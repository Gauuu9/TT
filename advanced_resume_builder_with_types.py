import streamlit as st

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
