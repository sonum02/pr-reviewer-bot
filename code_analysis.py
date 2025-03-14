# Import the required libraries

import os
import openai
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

def analyze_code(code):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a code analysis assistant."},
            {"role": "user", "content": (
                "Analyze the following code for potential issues and "
                f"improvements:\n\n{code}"
            )}
        ],
        max_tokens=150,
        temperature=0.5,
    )
    return response.choices[0].message['content'].strip()

def main():
    with open("githubConnection.py", "r") as file:
        code = file.read()
    analysis = analyze_code(code)
    with open("code_analysis_report.txt", "w") as report_file:
        report_file.write("Code Analysis:\n")
        report_file.write(analysis)

if __name__ == "__main__":
    main()