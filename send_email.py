import os
import sendgrid
from sendgrid.helpers.mail import Mail

# Load environment variables
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
TO_EMAIL = os.getenv('TO_EMAIL')
FROM_EMAIL = os.getenv('FROM_EMAIL')

def send_email(subject, content):
    """
    Send an email using SendGrid API.
    """
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    email = Mail(
        from_email=FROM_EMAIL,
        to_emails=TO_EMAIL,
        subject=subject,
        plain_text_content=content
    )
    try:
        response = sg.send(email)
        print(f"Email sent! Status code: {response.status_code}")
        print(f"Response body: {response.body}")
        print(f"Response headers: {response.headers}")
    except Exception as e:
        print(f"Error sending email: {e}")

def main():
    """
    Main function to read reports and send an email with the results.
    """
    try:
        with open("pylint_report.txt", "r") as pylint_file:
            pylint_score = pylint_file.readlines()[-2].split()[-1]
    except Exception as e:
        print(f"Error reading pylint report: {e}")
        pylint_score = "N/A"
    
    try:
        with open("code_analysis_report.txt", "r") as analysis_file:
            code_analysis = analysis_file.read()
    except Exception as e:
        print(f"Error reading code analysis report: {e}")
        code_analysis = "N/A"
    
    email_body = f"Pylint Score: {pylint_score}\n\nCode Analysis:\n{code_analysis}"
    print(f"Email body:\n{email_body}")
    send_email("PR Code Analysis Results", email_body)

if __name__ == "__main__":
    main()
    