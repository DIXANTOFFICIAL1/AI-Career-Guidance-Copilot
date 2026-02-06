from flask import Flask, render_template, request, jsonify
from services.career_agent import get_career_guidance

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("chat.html")
    
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    if not user_message:
        return jsonify({"reply": "Please enter a message."})

    result = get_career_guidance(user_message)

    # Format output nicely for chat UI
    reply = f"""
🎯 Profile Type: {result['profile']}

📌 Career Direction:
{result['direction']}

💼 Recommended Roles:
- {result['roles'][0]}
- {result['roles'][1]}
- {result['roles'][2]}

🛠 Skills to Focus On:
- {result['skills'][0]}
- {result['skills'][1]}
- {result['skills'][2]}

🚀 Next Steps:
1. {result['steps'][0]}
2. {result['steps'][1]}
3. {result['steps'][2]}

💡 Note:
{result['note']}
"""

    return jsonify({"reply": reply.strip()})


if __name__ == "__main__":
    app.run(debug=True)









