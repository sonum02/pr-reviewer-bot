# Configure GitHub API access and authentication

import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
print(f"Loaded GitHub Token: {GITHUB_TOKEN}")  # Debugging line

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
}

response = requests.get('https://api.github.com/user', headers=headers)
print(response.json())
