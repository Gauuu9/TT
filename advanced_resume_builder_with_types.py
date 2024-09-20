import streamlit as st
from fpdf import FPDF

# Function to generate a minimalist PDF resume
def generate_minimalist_pdf(name, email, phone, summary, skills, education, experience, job_type, resume_type):
    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt=f"{resume_type} {job_type} Resume", ln=True, align='C')

    # Name and Contact Info
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Name: {name}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Email: {email}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Phone: {phone}", ln=True, align='L')

    # Summary
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Summary:", ln=True, align='L')
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(200, 10, txt=summary)

    # Skills
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Skills:", ln=True, align='L')
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(200, 10, txt=skills)

    # Education
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Education:", ln=True, align='L')
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(200, 10, txt=education)

    # Experience
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Experience:", ln=True, align='L')
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(200, 10, txt=experience)

    pdf.output(f"resume_{name}_{resume_type}_minimalist.pdf")

# Function to generate a detailed PDF resume
def generate_detailed_pdf(name, email, phone, summary, skills, education, experience, job_type, resume_type):
    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font("Arial", 'B', 20)
    pdf.cell(200, 10, txt=f"{resume_type} Resume for {job_type}", ln=True, align='C')

    # Contact Info with spacing
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt=f"{name}", ln=True, align='L')
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Email: {email}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Phone: {phone}", ln=True, align='L')
    
    pdf.ln(10)  # Line break for spacing

    # Summary
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Summary", ln=True, align='L')
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(200, 10, txt=summary)

    # Skills
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Skills", ln=True, align='L')
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(200, 10, txt=skills)

    # Education
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Education", ln=True, align='L')
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(200, 10, txt=education)

    # Experience
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Work Experience", ln=True, align='L')
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(200, 10, txt=experience)

    pdf.output(f"resume_{name}_{resume_type}_detailed.pdf")

# Streamlit code for web app
def main():
    st.title("Advanced Resume Builder")

    # Input fields for personal details
    st.subheader("Personal Details")
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")

    # Job application type selection
    st.subheader("Job Application Type")
    job_type = st.selectbox("Select the type of job you're applying for:", 
                            ['Software Engineer', 'Data Scientist', 'Product Manager', 'Designer'])

    # Resume type selection
    st.subheader("Resume Type")
    resume_type = st.selectbox("Select the resume type:", 
                               ['Traditional', 'Functional', 'Combination', 'Targeted'])

    # Resume format selection
    st.subheader("Resume Format")
    resume_format = st.radio("Choose the resume format:", 
                             ['Minimalist', 'Detailed'])

    # Summary section
    st.subheader("Summary")
    summary = st.text_area("Write a brief summary about yourself")

    # Skills section
    st.subheader("Skills")
    skills = st.text_area("List your skills (comma separated)")

    # Education section
    st.subheader("Education")
    education = st.text_area("Provide details of your education")

    # Experience section
    st.subheader("Experience")
    experience = st.text_area("Describe your work experience")

    # Button to generate PDF
    if st.button("Generate Resume"):
        if name and email and phone:
            if resume_format == 'Minimalist':
                generate_minimalist_pdf(name, email, phone, summary, skills, education, experience, job_type, resume_type)
                st.success(f"{resume_type} Minimalist Resume generated! Download the PDF below.")
                with open(f"resume_{name}_{resume_type}_minimalist.pdf", "rb") as f:
                    st.download_button("Download Minimalist Resume", f, file_name=f"resume_{name}_{resume_type}_minimalist.pdf")
            elif resume_format == 'Detailed':
                generate_detailed_pdf(name, email, phone, summary, skills, education, experience, job_type, resume_type)
                st.success(f"{resume_type} Detailed Resume generated! Download the PDF below.")
                with open(f"resume_{name}_{resume_type}_detailed.pdf", "rb") as f:
                    st.download_button("Download Detailed Resume", f, file_name=f"resume_{name}_{resume_type}_detailed.pdf")
        else:
            st.error("Please fill in all the required fields.")

if __name__ == '__main__':
    main()
