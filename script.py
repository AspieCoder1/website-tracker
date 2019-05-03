import requests
from bs4 import BeautifulSoup
import os
import time
import pause
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

while True:
    url = "https://www.undergraduate.study.cam.ac.uk/courses/computer-science"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.find(
        "fieldset", id="entry-requirements").find("h3").next_sibling.next_sibling.get_text()

    os.environ['cam-text'] = text

    if os.environ['cam-text'] == text:
        pause.days(1)
        continue
    else:
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
