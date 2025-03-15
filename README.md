# Auto PR Reviewer


## Project Overview
The GitHub Pull Request Reviewer Bot is an AI-powered automation tool that reviews pull requests (PRs) using Large Language Models (LLMs). Whenever a PR is created the bot sends automated email feedback on code quality, security vulnerabilities, best practices, Lint score and documentation completeness.


## Benefits
- Improved Code Quality: Automated checks help maintain high code quality by catching issues early in the development process.
- Consistency: Enforces consistent coding standards across the codebase.
- Efficiency: Saves time for developers by automating repetitive tasks and providing immediate feedback.
- Collaboration: Keeps the team informed about code quality issues through automated notifications, facilitating better collaboration and quicker resolution of issues.

## Purpose
- Automated Code Analysis: Utilize OpenAI's GPT-4 model to analyze code for potential issues and improvements.
- Linting: Integrate Pylint to enforce coding standards and detect code quality issues.
- Continuous Integration: Use GitHub Actions to automate the workflow, ensuring that code analysis and linting are performed on every pull request.
- Notifications: Send detailed email notifications with the results of the code analysis and linting to keep the development team informed.
- Error Handling: Implement robust error handling and retry logic to manage API rate limits and other potential issues.

## Key Features
- Automated code analysis
- Linting
- Email notification

## Libraries and frameworks used
- Open AI: To analyze code
- GitHub Actions
- SendGrid: Send automated email
- Requests: GitHub API interaction
- Dotenv: Load env variables

## PR Monitor Overview
![Image](https://github.com/user-attachments/assets/7601ce15-b206-41f2-a0d9-1c87bc2c5bea)
