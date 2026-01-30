from flask import Flask, render_template, request
import google.generativeai as genai
import os

app = Flask(__name__)

# Configure Gemini API key (use environment variable)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def process_question(question):
    return question.strip().lower()

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

@app.route("/", methods=["GET", "POST"])
def index():
    original_question = ""
    processed_question = ""
    answer = ""

    if request.method == "POST":
        original_question = request.form["question"]
        processed_question = process_question(original_question)
        answer = get_gemini_response(processed_question)

    return render_template(
        "index.html",
        original_question=original_question,
        processed_question=processed_question,
        answer=answer
    )

if __name__ == "__main__":
    app.run(debug=True)
