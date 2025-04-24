import streamlit as st
from utils.parser import extract_resume_data
from utils.matcher import calculate_match_score
from utils.visualizer import generate_graphs

# Load custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("assets/styles.css")

# App layout and title
st.markdown("""
    <div class="header">
        <h1>📄 Resume Screening App</h1>
        <p>Compare a candidate's resume with a job description using NLP and see visual match insights.</p>
    </div>
""", unsafe_allow_html=True)

# Upload Section
st.markdown("""
    <div class="upload-box">
        <h3>📤 Upload Resume</h3>
    </div>
""", unsafe_allow_html=True)

uploaded_resume = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])

st.markdown("""
    <div class="jd-box">
        <h3>📝 Job Description</h3>
    </div>
""", unsafe_allow_html=True)

uploaded_jd = st.text_area("Paste or type the job description here", height=200)

if uploaded_resume and uploaded_jd:
    with st.spinner("🔍 Extracting resume data..."):
        resume_data = extract_resume_data(uploaded_resume)

    with st.spinner("📊 Calculating match score..."):
        match_scores = calculate_match_score(resume_data, uploaded_jd)

    st.success("✅ Match Analysis Complete!")

    st.markdown("<h4>🔎 Resume Insights</h4>", unsafe_allow_html=True)
    st.json(resume_data)

    st.markdown("<h4>📈 Match Scores</h4>", unsafe_allow_html=True)
    st.json(match_scores)

    st.markdown("<h4>📊 Visual Breakdown</h4>", unsafe_allow_html=True)
    generate_graphs(match_scores)

# Footer
st.markdown("""
    <hr>
    <div class="footer">
        <p>Made with ❤️ by Tanish using Streamlit & NLP</p>
    </div>
""", unsafe_allow_html=True)
