import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from skills import skills



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

    

    documents = [cv, job_description]
    vectorizer = TfidfVectorizer() 
    tfidf_matrix = vectorizer.fit_transform(documents) # fit veriyi öğrenir, transform da dönüştürür

    similarity = cosine_similarity(tfidf_matrix[0:1],tfidf_matrix[1:2])
    score = similarity[0][0]
    # yüzdeye çevirmek için
    score = round(score * 100,2)

 

    return score, matched_skills, missing_skills