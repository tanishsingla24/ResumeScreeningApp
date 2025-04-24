import re
import spacy
from pdfminer.high_level import extract_text
from docx import Document

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_file):
    return extract_text(pdf_file)

def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    return "\n".join([p.text for p in doc.paragraphs])

def extract_resume_data(file):
    if file.name.endswith(".pdf"):
        text = extract_text_from_pdf(file)
    elif file.name.endswith(".docx"):
        text = extract_text_from_docx(file)
    else:
        return {}

    doc = nlp(text)
    skills = [token.text for token in doc if token.pos_ == "NOUN"]
    email = re.findall(r"[\w\.-]+@[\w\.-]+", text)
    phone = re.findall(r"\+?\d[\d\s.-]{8,}\d", text)

    return {
        "email": email[0] if email else "Not found",
        "phone": phone[0] if phone else "Not found",
        "skills": list(set(skills))[:10]
    }
