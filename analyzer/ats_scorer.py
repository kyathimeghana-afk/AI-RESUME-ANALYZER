def calculate_ats_score(resume_text, keywords):

    matched_keywords = 0

    for keyword in keywords:
        if keyword.lower() in resume_text:
            matched_keywords += 1

    if len(keywords) == 0:
        return 0

    score = (matched_keywords / len(keywords)) * 100

    return round(score)
