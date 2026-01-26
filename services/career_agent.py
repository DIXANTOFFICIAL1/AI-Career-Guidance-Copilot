import os
import json
import re
import random
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("models/text-bison-001")


def extract_json(text):
    match = re.search(r"\{[\s\S]*\}", text)
    if match:
        return json.loads(match.group())
    raise ValueError("No valid JSON found")


def get_career_guidance(user_text):
    """
    Creative AI Career Guidance Copilot
    """

    prompt = f"""
You are an AI Career Guidance Copilot.

Your goal:
- Give personalized and CREATIVE career advice
- Strongly adapt to user's background and intent
- Avoid generic responses
- Change tone and recommendations for different users

IMPORTANT:
- Think step-by-step before answering
- Be specific to the user's message
- Avoid repeating common phrases

Return ONLY valid JSON.
No markdown, no extra text.

JSON format:
{{
  "profile_type": "...",
  "career_direction": "...",
  "recommended_roles": ["...", "...", "..."],
  "skills_to_focus": ["...", "...", "..."],
  "next_3_steps": ["...", "...", "..."],
  "confidence_note": "..."
}}

User message:
{user_text}
"""

    try:
        response = model.generate_content(prompt)
        data = extract_json(response.text)

        return {
            "profile": data["profile_type"],
            "direction": data["career_direction"],
            "roles": data["recommended_roles"],
            "skills": data["skills_to_focus"],
            "steps": data["next_3_steps"],
            "note": data["confidence_note"]
        }

    except Exception:
        
        return creative_fallback(user_text)


def creative_fallback(text):
    t = text.lower()

    profiles = []
    roles = []
    skills = []

    if any(w in t for w in ["student", "college", "semester", "degree"]):
        profiles.append("Student")
        roles = ["Software Developer", "Data Analyst", "AI Intern"]
        skills = ["Programming basics", "Projects", "Problem solving"]

    if any(w in t for w in ["bcom", "commerce", "non tech"]):
        profiles.append("Career Switcher")
        roles = ["Business Analyst", "Data Analyst", "Product Operations"]
        skills = ["Excel & SQL", "Business understanding", "Analytics tools"]

    if any(w in t for w in ["job", "working", "experience", "office"]):
        profiles.append("Working Professional")
        roles = ["Specialist Role", "Technical Lead", "Domain Expert"]
        skills = ["Advanced skills", "System thinking", "Leadership"]

    if not profiles:
        profiles.append("Exploring Professional")
        roles = ["Entry-Level Tech Role", "Analyst", "Support Engineer"]
        skills = ["Core fundamentals", "Certifications", "Hands-on practice"]

    return {
        "profile": random.choice(profiles),
        "direction": "Your background suggests multiple paths. Focus on one direction and build depth instead of trying everything at once.",
        "roles": random.sample(roles, min(3, len(roles))),
        "skills": random.sample(skills, min(3, len(skills))),
        "steps": [
            "Clarify your career goal for the next 6 months",
            "Build at least one focused project",
            "Apply consistently while improving skills"
        ],
        "note": "Career clarity comes with action. Start small, stay consistent, and adjust as you learn."
    }
