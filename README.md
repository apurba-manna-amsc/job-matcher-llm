# JobFit AI – An LLM-powered Resume Matcher using Groq

This project helps job seekers evaluate how well their **resume matches a job description** using **LLMs (Large Language Models)** via the **Groq API**. It parses your resume, compares it with the job description, and provides a detailed score, skills match, and improvement suggestions.

## 🌐 Live Demo

Try it now: [Job Matcher App on Streamlit 🚀](https://job-matcher-llm-cggjbrpyovqhycufxfxspj.streamlit.app/)

## 🚀 Features

- 📄 **Upload Resume** (PDF)
- 🖍️ **Paste Job Description**
- ⚙️ **LLM-Powered Matching** using `llama3-70b-8192` on Groq
- ✅ Eligibility Check
- 🎯 Matching Score (0–100)
- 🧠 Skill Match Summary
- ⚠️ Gap Analysis
- 💡 Suggestions to Improve Fit

## 🔧 Technologies Used

- Python
- Streamlit
- Groq API (LLM)
- PyPDF2
- python-dotenv

## 📦 Installation

```bash
git clone https://github.com/your-username/job-matcher-llm.git
cd job-matcher-llm
python -m venv env
source env/bin/activate  # for Linux/macOS
env\Scripts\activate     # for Windows
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_api_key_here
```

> ⚠️ Never commit your `.env` file to GitHub. Instead, use `.env.example` as a reference.

## ▶️ Run the App Locally

```bash
streamlit run app.py
```

## ☁️ Deploying on Streamlit Cloud

1. Push your code to a public GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).
3. Create a new app and select your repo.
4. Go to **`Secrets` tab** and add:
   ```toml
   GROQ_API_KEY = "your_actual_groq_api_key"
   ```

## 📂 Project Structure

```
job-matcher-llm/
├── app.py                  # Streamlit frontend
├── matcher.py              # JD-Resume matching logic using Groq LLM
├── utils.py                # Resume extraction and cleaning
├── prompts/
│   └── jd_prompt.py        # LLM prompt templates
├── .env.example            # Env variable template
├── requirements.txt        # Dependencies
└── README.md               # You're here!
```

## 📚 References

- [Krish Naik – YouTube Channel](https://www.youtube.com/@krishnaik06)
- [Groq Console Docs](https://console.groq.com/docs/overview)
- [Applicant Tracking System using Gemini Pro LLM – Medium Article](https://medium.com/@gitesh08/applicant-tracking-system-ats-using-gemini-pro-llm-d044aee2b974)
- [Track My Resume – GitHub Repo](https://github.com/Gitesh08/Track-my-resume)


## 🛡️ Disclaimer

This project is intended for educational and demonstrative purposes. Matching results are based on AI analysis and should be reviewed critically.

## 📬 Contact

Made with 💙 by [Apurba Manna]  
📧 98apurbamanna@gmail.com 
🔗 [LinkedIn](https://www.linkedin.com/in/apurba-manna/)

