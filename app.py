# app.py

import streamlit as st
import os
from matcher import match_jd_resume
from utils import extract_text_from_pdf, clean_text

st.set_page_config(page_title="JobFit AI", layout="wide")
st.title("JobFit AI – An LLM-powered Resume Matcher using Groq")

st.markdown("""
Upload your **resume** (PDF) and paste the **job description** to evaluate how well you match the role.
""")

# --- Job Description input ---
jd_text = st.text_area("📄 Paste Job Description", height=250)

# --- Resume upload ---
resume_file = st.file_uploader("📤 Upload Resume (PDF)", type=["pdf"])

resume_text = ""
if resume_file:
    with open("uploaded_resume.pdf", "wb") as f:
        f.write(resume_file.read())
    extracted = extract_text_from_pdf("uploaded_resume.pdf")
    resume_text = clean_text(extracted)

    st.success("✅ Resume uploaded and processed successfully.")
    st.expander("🔍 View Extracted Resume Text").write(extracted)

# --- Match Button ---
if st.button("🚀 Match Now", key="match_button"):
    if not jd_text or not resume_text:
        st.warning("⚠️ Please provide both job description and resume!")
    else:
        with st.spinner("Analyzing with LLM..."):
            result = match_jd_resume(jd_text, resume_text)
            st.subheader("🎯 Match Results")
            st.markdown("### 📋 LLM Feedback")
            st.markdown(result)


