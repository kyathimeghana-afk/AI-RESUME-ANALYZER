def generate_tips(weaknesses):

    tips = []

    suggestions = {
        "No skills section found":
        "Add a clear Skills section highlighting technical and soft skills.",

        "No projects section found":
        "Include a Projects section to showcase your practical work.",

        "No internships or work experience mentioned":
        "Add internships, volunteering, or practical experiences.",

        "No certifications mentioned":
        "Add relevant certifications to strengthen your resume."
    }

    for weakness in weaknesses:
        if weakness in suggestions:
            tips.append(suggestions[weakness])

    return tips
