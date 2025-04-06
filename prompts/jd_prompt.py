MATCH_PROMPT = """
You are a smart AI assistant. Your job is to assess how well a resume fits a job description.

Job Description:
{jd}

Resume:
{resume}

Output the following:

1. Eligibility Check: State whether the candidate meets the minimum eligibility criteria (e.g., education, experience, location, certifications). Answer with "Eligible" or "Not Eligible", and briefly explain why.

2. Score (0–100): A numerical rating of how well the resume matches the job description in terms of relevant skills, tools, experience, and keywords and also explain how it get that score.

3. Summary of Matched Skills: List the key skills and qualifications from the job description that are present in the resume.

4. Gaps or Missing Points: Identify important skills, experiences, or keywords required in the job description but missing or weak in the resume.

5. Suggestions to Improve Fit: Provide actionable recommendations to better align the resume with the job description, including any missing skills, tools, achievements, or formatting issues.
"""
Resume_PROMPT = """
You are an intelligent AI resume writer. Your task is to create a professional, ATS-friendly resume tailored to a given job description using the provided user details.
User Details:
{resume}
Job Description:
{jd}

Output:
Generate a resume in professional tone and format that:
- Matches the JD using relevant keywords and structure.
- Highlights skills, experience, and achievements aligned with the role.
- Is clean, ATS-optimized, and ready to be compiled into PDF or Overleaf format.
"""
