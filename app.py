from flask import Flask, render_template, request
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""

    if request.method == "POST":
        notes = request.form.get("notes")

        prompt = f"""
You are SmartPrep AI, a helpful study assistant.

Analyze the following study notes and provide:

1. 📌 Summary
   - Summarize the notes in bullet points.

2. 📝 Quiz Questions
   - Generate 5 important quiz questions.

3. 💡 Simple Explanation
   - Explain the topic in easy language.

Study Notes:
{notes}
"""

        try:
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a helpful study assistant."},
                    {"role": "user", "content": prompt}
                ]
            )

            response = completion.choices[0].message.content

        except Exception as e:
            response = f"Error: {e}"

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)