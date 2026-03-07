import streamlit as st
import google.generativeai as genai

# ---------------------------
# CONFIGURE GEMINI API
# ---------------------------
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash-lite")

# ---------------------------
# UI
# ---------------------------

st.title("AI Project Risk Predictor")

st.markdown(
"""
Developed by **Jay Parikh**  
IT Delivery Leader | AI & Digital Delivery  
🌐 www.jay-parikh.com
"""
)

st.write("Predict delivery risks using AI")

# ---------------------------
# INPUT PARAMETERS
# ---------------------------

duration = st.slider("Project Duration (Months)", 1, 24)

team_size = st.slider("Team Size", 2, 50)

stakeholders = st.slider("Number of Stakeholders", 1, 20)

complexity = st.selectbox(
    "Technology Complexity",
    ["Low", "Medium", "High"]
)

requirements = st.selectbox(
    "Requirement Stability",
    ["Stable", "Moderate Change", "Frequent Change"]
)

experience = st.selectbox(
    "Team Experience",
    ["Low", "Medium", "High"]
)

project_type = st.selectbox(
    "Project Type",
    ["Enterprise Application", "Data Platform", "AI Project", "Cloud Migration"]
)

# ---------------------------
# AI ANALYSIS
# ---------------------------

if st.button("Analyze Risk"):

    prompt = f"""
You are an experienced IT Delivery Leader.

Analyze the project delivery risk based on the following parameters:

Project Type: {project_type}
Project Duration: {duration} months
Team Size: {team_size}
Stakeholders: {stakeholders}
Technology Complexity: {complexity}
Requirement Stability: {requirements}
Team Experience: {experience}

Provide:

1. Overall Risk Level (Low / Medium / High)
2. Delivery Risk Score (1-10)
3. Top 5 Project Risks
4. Mitigation Strategies
5. Delivery Advice for the Project Manager
"""

    response = model.generate_content(prompt)

    st.subheader("AI Risk Analysis")

    st.write(response.text)

# ---------------------------
# FOOTER
# ---------------------------

st.markdown("---")

st.caption("© 2026 Jay Parikh | AI Delivery Tools")