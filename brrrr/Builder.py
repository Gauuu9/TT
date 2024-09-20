import streamlit as st
from fpdf import FPDF

# Simple PDF generation function
def generate_simple_pdf(name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt=f"Resume for {name}", ln=True, align='C')
    pdf.output(f"resume_{name}_test.pdf")

# Streamlit code for debugging
def main():
    st.title("Resume Builder")

    name = st.text_input("Full Name")
    if st.button("Generate Test PDF"):
        if name:
            generate_simple_pdf(name)
            st.success("PDF generated!")
            with open(f"resume_{name}_test.pdf", "rb") as f:
                st.download_button("Download Test PDF", f, file_name=f"resume_{name}_test.pdf")
        else:
            st.error("Please enter your name.")

if __name__ == '__main__':
    main()