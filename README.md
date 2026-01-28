# 🎓 AI Career Guidance Copilot

An AI-powered career guidance web application that provides **personalized, context-aware career advice** based on user input. The system behaves like a conversational AI (similar to ChatGPT / Google Gemini) and helps students, career switchers, and working professionals make informed career decisions.

This project is developed as part of **Microsoft Copilot Internship programs** and aligns with **UN Sustainable Development Goal (SDG 4: Quality Education)**.

---

## 🚀 Features

- 🧠 AI-powered career recommendations using **Google Gemini API**
- 💬 Live conversational chat interface
- 🎯 Personalized guidance based on user profile and situation
- 👩‍🎓 Supports Students, Career Switchers, and Working Professionals
- 🛡️ Safe error handling with rule-based fallback responses
- 🎨 Clean and responsive UI using HTML, CSS, and JavaScript

---

## 🛠️ Technologies Used

- **Python**
- **Flask (Backend)**
- **Google Gemini Generative AI API**
- **HTML, CSS, JavaScript**
- **dotenv for environment variables**

---

## 🌍 SDG Alignment

**SDG 4 – Quality Education**  
This project helps users gain career clarity, develop relevant skills, and access guidance using AI, supporting inclusive and accessible education and career planning.

---

## 📁 Project Structure

AI-Career-Guidance-Copilot/
│
├── app.py
├── requirements.txt
├── runtime.txt
├── .gitignore
├── .env (not committed)
│
├── services/
│ └── career_agent.py
│
├── templates/
│ └── chat.html
│
└── static/
├── style.css
└── chat.js

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/DIXANTOFFICIAL1/AI-Career-Guidance-Copilot.git
cd AI-Career-Guidance-Copilot

2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Configure Environment Variables
Create a .env file in the root directory:

GOOGLE_API_KEY=your_google_gemini_api_key_here
⚠️ Do NOT upload .env to GitHub.

▶️ Run the Application
python app.py
Open your browser and visit:

http://127.0.0.1:5000
🧪 Example Prompts
“I am a 2nd year student confused between AI and web development”

“I completed BCom and want to move into tech”

“I am working in IT support for 2 years and feel stuck”

“What skills should I learn to become a data analyst?”

Each prompt generates different, context-aware responses.

📈 Impact
Helps users gain career clarity using AI

Reduces confusion in early career decision-making

Encourages skill development and lifelong learning

Makes career guidance accessible and scalable

🔒 Disclaimer
This project provides career awareness and guidance only.
It does not guarantee job placement and should not be considered professional or legal advice.

📜 License
This project is intended for educational and internship purposes.

👤 Author
Dixant Soni
GitHub: https://github.com/DIXANTOFFICIAL1

📚 References
Google Gemini Generative AI Documentation

IBM SkillsBuild Learning Resources

Microsoft Copilot & AI Learning Modules

Flask Official Documentation

United Nations Sustainable Development Goals (SDGs)

