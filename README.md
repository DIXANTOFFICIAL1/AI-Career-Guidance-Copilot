# 🎓 AI Career Guidance Copilot

An AI-powered career guidance web application that provides **personalized, context-aware career advice** based on user input. The system behaves like a conversational AI (similar to ChatGPT / Google Gemini) and helps students, career switchers, and working professionals make informed career decisions.

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

## 📂 Project Structure

```text
AI-Career-Guidance-Copilot/
│
├── app.py
├── requirements.txt
├── runtime.txt
├── .gitignore
├── .env                  # Not committed (stores API key)
│
├── services/
│   └── career_agent.py
│
├── templates/
│   └── chat.html
│
└── static/
    ├── style.css
    └── chat.js
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/DIXANTOFFICIAL1/AI-Career-Guidance-Copilot.git
cd AI-Career-Guidance-Copilot

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Configure Environment Variables

Create a .env file in the root directory:
GOOGLE_API_KEY=your_google_gemini_api_key_here
⚠️ Important: Do NOT upload .env to GitHub.

4️⃣ Run the Application

python app.py
Open your browser and visit:
http://127.0.0.1:5000
```
## 💬 Example Prompts

- “I am a 2nd year student confused between AI and web development”
- “I completed BCom and want to move into tech roles”
- “I am working in IT support for 2 years and feel stuck”
- “What skills should I learn to move into AI roles?”
- Each prompt generates different, personalized outputs based on user context.

## 🎯 Target Users

- Students exploring career options
- Career switchers moving into tech
- Working professionals seeking growth
- Early-stage job seekers and interns

## 📈 Impact

- Helps users gain career clarity using AI
- Reduces confusion in early career decision-making
- Encourages skill development and lifelong learning
- Makes career guidance accessible and scalable

## 🔗 References

- Google Generative AI Documentation
- Microsoft Copilot & AI Learning Resources
- United Nations Sustainable Development Goals (SDGs)
- Flask Official Documentation
- Research articles on AI-based decision support systems

## 📜 License

This project is intended for educational and internship purposes.

## 👤 Author

- Dixant Soni
- AI & Software Development Enthusiast
- GitHub: https://github.com/DIXANTOFFICIAL1
