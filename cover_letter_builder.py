import streamlit as st
from PIL import Image

# Set up the website title and layout
st.set_page_config(page_title="ProResume", layout="centered")

# Add the main title
st.markdown("<h1 style='text-align: center; color: white;'>ProResume</h1>", unsafe_allow_html=True)

# Add the subtitle and description
st.markdown(
    "<h2 style='text-align: center; color: white;'>Build Resumes That Shine!</h2>",
    unsafe_allow_html=True,
)
st.markdown(
    """
    <p style='text-align: center; color: white;'>
    With our user-friendly resume builder, you can effortlessly design a standout resume 
    that highlights your skills and experience. Let your unique story shine and catch the 
    eye of employers!
    </p>
    """,
    unsafe_allow_html=True,
)

# Add the "Get Started" button centered in a column
col1, col2, col3 = st.columns([2, 2, 1])  # Create three columns with ratios
with col2:  # Use the center column
    if st.button("Get Started"):
        st.markdown("<p style='text-align: left; color: white;'>Let's get started with building your resume!</p>", unsafe_allow_html=True)

# Add the three features section
st.markdown("<hr>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)




# Feature 1: AI-Powered Resume Optimization
with col1:
    st.image("https://img.icons8.com/clouds/100/000000/brain.png")  # Example icon from icons8
    st.markdown("<h4 style='text-align: center; color: white;'>AI-Powered Resume Generation</h4>", unsafe_allow_html=True)

# Feature 2: Skills Recommendation
with col2:
    # Replace with the local image path
    image = Image.open(r"C:\Users\GAURAV\Downloads\cl.png")
    image = image.resize((130, 100))  # Specify new size
    st.image(image)
    st.markdown("<h4 style='text-align: center; color: white;'>Generate your personalised cover letter</h4>", unsafe_allow_html=True)
    

# Feature 3: Resume Analysis
with col3:
    st.image("https://img.icons8.com/clouds/100/000000/document.png")  # Example icon from icons8
    st.markdown("<h4 style='text-align: center; color: white;'>Resume Analyzer and Skill Recommendation</h4>", unsafe_allow_html=True)

# Add background color and style
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
    }
    h1, h2, h3, p {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
