from matcher import match


with open("data/job_description.txt", "r") as file:
    job_description = file.read()

 
with open("data/cv.txt", "r") as file:
    cv = file.read()
   
print("CV:", cv)
print("JOB:", job_description)
    
score, matched_skills,missing_skills = match(cv, job_description)
print("Match Score: ", score, "%")

print("Matched Skills:")
for skill in matched_skills:
    print("-", skill)

    
print("Missing Skills:")
for skill in missing_skills:
    print("-", skill)
