# Import all the libraries
import os
import openai
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

def get_pr_changes(repo_name, pr_number, token):
    """
    Fetch the changes in a pull request from the GitHub API.
    """
    url = f"https://api.github.com/repos/{repo_name}/pulls/{pr_number}/files"
    headers = {"Authorization": f"token {token}"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching PR changes: {e}")
        return []

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
            max_tokens=200,
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
    repo_name = os.getenv('GITHUB_REPOSITORY')
    pr_number = os.getenv('PR_NUMBER')
    github_token = os.getenv('GITHUB_TOKEN')

<<<<<<< HEAD
=======
    repo_name = os.getenv('GITHUB_REPOSITORY')
    pr_number = os.getenv('PR_NUMBER')
    github_token = os.getenv('GH_TOKEN')

>>>>>>> f1ea0715d156ed5cf5be696c44c4ddf6db765680
    changes = get_pr_changes(repo_name, pr_number, github_token)
    for change in changes:
        if change['status'] == 'modified' and change['filename'].endswith('.py'):
            try:
                with open(change['filename'], 'r') as file:
                    code = file.read()
            except Exception as e:
                print(f"Error reading code file {change['filename']}: {e}")
                continue

            analysis = analyze_code(code)
            
            try:
                with open("code_analysis_report.txt", "w") as report_file:
                    report_file.write("Code Analysis:\n")
                    report_file.write(analysis)
            except Exception as e:
                print(f"Error writing analysis report: {e}")

if __name__ == "__main__":
    main()
