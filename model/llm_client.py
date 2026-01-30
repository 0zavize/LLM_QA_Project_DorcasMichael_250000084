import google.generativeai as genai
import os

# ✅ Correct: use the ENV VARIABLE NAME
genai.configure(api_key=os.getenv("AIzaSyAbVbePkVcmqyKvGQewskr0OFm_3F6I3to"))

model = genai.GenerativeModel("gemini-pro")

def main():
    question = input("Enter your question: ")

    processed_question = question.strip().lower()
    print(f"\nProcessed Question: {processed_question}")

    response = model.generate_content(processed_question)

    print("\nGemini Answer:")
    print(response.text)

if __name__ == "__main__":
    main()