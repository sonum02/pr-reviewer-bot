# Import all the libraries
#Adding for testing
import os
import openai
from dotenv import load_dotenv
import requests
import time

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

def get_pr_changes(repo_name, pr_number, token):
    """
    Fetch the changes in a pull request from the GitHub API.
    """
    if not repo_name or not pr_number or not token:
        print("Missing required environment variables.")
        print(f"repo_name: {repo_name}, pr_number: {pr_number}, token: {token}")
        return []

    url = f"https://api.github.com/repos/{repo_name}/pulls/{pr_number}/files"
    headers = {"Authorization": f"token {token}"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        if response.status_code == 403 and 'X-RateLimit-Reset' in response.headers:
            reset_time = int(response.headers['X-RateLimit-Reset'])
            wait_time = reset_time - int(time.time())
            print(f"Rate limit exceeded. Waiting for {wait_time} seconds.")
            time.sleep(wait_time)
            return get_pr_changes(repo_name, pr_number, token)
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
    repo_name = os.getenv('GITHUB_REPOSITORY')
    pr_number = os.getenv('PR_NUMBER')
    github_token = os.getenv('GITHUB_TOKEN')

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
