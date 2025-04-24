# Resume Screening App using NLP

A simple app built with Streamlit to screen resumes and compare them to job descriptions using NLP and graph visualizations.

## 🔧 Features
- Upload resume (PDF/DOCX)
- Paste job description
- Extracts name, email, phone, skills
- Calculates skill, education, and experience match
- Shows pie, bar, and gauge charts

## 🚀 How to Run

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py
