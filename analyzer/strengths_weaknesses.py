def analyze_strengths_weaknesses(text):

    strengths = []
    weaknesses = []

    if "skills" in text:
        strengths.append("Skills section detected")
    else:
        weaknesses.append("No skills section found")

    if "project" in text:
        strengths.append("Projects section detected")
    else:
        weaknesses.append("No projects section found")

    if "experience" in text or "internship" in text:
        strengths.append("Work experience detected")
    else:
        weaknesses.append("No internships or work experience mentioned")

    if "certification" in text:
        strengths.append("Certifications mentioned")
    else:
        weaknesses.append("No certifications mentioned")

    return strengths, weaknesses
