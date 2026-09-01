import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.skills import skills



def match(cv, job_description):

    cv = cv.lower()
    job_description =job_description.lower()
     
    matched_skills =[]
    missing_skills= []  

   
    for skill in skills:
        if re.search(r"\b" + skill.lower() + r"\b", job_description):
           if re.search(r"\b" + skill.lower() + r"\b", cv):
               matched_skills.append(skill)
           else:
               missing_skills.append(skill) 

    total_skills = len(matched_skills) + len(missing_skills)       

    if total_skills > 0:
       skill_score = len(matched_skills) / total_skills * 100
    else:
        return score, matched_skills, missing_skills   

    

    documents = [cv, job_description]
    vectorizer = TfidfVectorizer() 
    tfidf_matrix = vectorizer.fit_transform(documents) # fit veriyi öğrenir, transform da dönüştürür

    similarity = cosine_similarity(tfidf_matrix[0:1],tfidf_matrix[1:2])
    score = similarity[0][0]
    # yüzdeye çevirmek için
    score = round(score * 100,2)
    final_score = round(score * 0.4 + skill_score * 0.6, 2)

 

    return final_score, matched_skills, missing_skills