import os
import openai
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY


def analyze_code(code):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=(
            "Analyze the following code for potential issues and improvements:\n\n"
            f"{code}"
        ),
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    with open("githubConnection.py", "r") as file:
        code = file.read()
    analysis = analyze_code(code)
    print("Code Analysis:\n", analysis)
