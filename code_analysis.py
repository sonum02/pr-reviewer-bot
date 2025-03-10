# Code analysis file to analyze the code for potential issues
# and improvements using OpenAI's API
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
            {"role": "system", "content": 
             "You are a code analysis assistant."},
            {"role": "user", 
             "content": f"Analyze below code for potential issues and improvements:\n\n{code}"
             }
        ],
        max_tokens=150,
        temperature=0.5,
    )
    return response.choices[0].message['content'].strip()


if __name__ == "__main__":
    with open("githubConnection.py", "r") as file:
        code = file.read()
    analysis = analyze_code(code)
    print("Code Analysis:\n", analysis)
