from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match_score(resume_data, jd_text):
    resume_skills = " ".join(resume_data.get("skills", []))
    corpus = [resume_skills, jd_text]
    vectorizer = CountVectorizer().fit_transform(corpus)
    vectors = vectorizer.toarray()
    cosine_sim = cosine_similarity([vectors[0]], [vectors[1]])[0][0]

    return {
        "Skill Match %": round(cosine_sim * 100, 2),
        "Experience Match %": 65.0,  # Placeholder
        "Education Match %": 75.0,   # Placeholder
        "Overall Match %": round((cosine_sim * 100 + 65 + 75) / 3, 2)
    }
