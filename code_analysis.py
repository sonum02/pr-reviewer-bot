import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

def analyze_code(code):
    """
    Analyze the given code using OpenAI's GPT-4 model.
    """
    try:
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
    except Exception as e:
        print(f"Error analyzing code: {e}")
        return "Error analyzing code."

def main():
    """
    Main function to read the code from a file, analyze it, and save the analysis report.
    """
    try:
        with open("githubConnection.py", "r") as file:
            code = file.read()
    except Exception as e:
        print(f"Error reading code file: {e}")
        return

    analysis = analyze_code(code)
    
    try:
        with open("code_analysis_report.txt", "w") as report_file:
            report_file.write("Code Analysis:\n")
            report_file.write(analysis)
    except Exception as e:
        print(f"Error writing analysis report: {e}")

if __name__ == "__main__":
    main()
    