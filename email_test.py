import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email="compsci@cambot.com",
    to_emails="lukebraithwaite7@gmail.com",
    subject="Cambridge Computer Science Admissions Updated",
    html_content="The admissions test information for cambridge has been updated"
)

try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    print('API Key: ', os.environ.get('SENDGRID_API_KEY'))
    sg.send(message)
except Exception as e:
    print(e)
