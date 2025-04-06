# matcher.py

import os
from openai import OpenAI
from prompts.jd_prompt import MATCH_PROMPT, Resume_PROMPT
from dotenv import load_dotenv
load_dotenv()


client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

MODEL = "llama3-70b-8192"


def match_jd_resume(jd: str, resume: str):
    if not client.api_key:
        raise ValueError("Groq API key not found. Set 'GROQ_API_KEY' in environment variables.")

    prompt = MATCH_PROMPT.format(jd=jd.strip(), resume=resume.strip())
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        content = response.choices[0].message.content

        return content

    except Exception as e:
        return 0, f"❌ Error from Groq API: {str(e)}"
    

