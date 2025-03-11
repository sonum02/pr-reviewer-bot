import os
import sendgrid
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
TO_EMAIL = os.getenv('TO_EMAIL')
FROM_EMAIL = os.getenv('FROM_EMAIL')

def send_email(subject, content):
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    email = Mail(
        from_email=FROM_EMAIL,
        to_emails=TO_EMAIL,
        subject=subject,
        plain_text_content=content
    )
    response = sg.send(email)
    print(response.status_code)
    print(response.body)
    print(response.headers)

def main():
    with open("pylint_report.txt", "r") as pylint_file:
        pylint_score = pylint_file.readlines()[-2].split()[-1]
    
    with open("code_analysis_report.txt", "r") as analysis_file:
        code_analysis = analysis_file.read()
    
    email_body = f"Pylint Score: {pylint_score}\n\nCode Analysis:\n{code_analysis}"
    send_email("PR Code Analysis Results", email_body)

if __name__ == "__main__":
    main()