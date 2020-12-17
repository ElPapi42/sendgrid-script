import sys
import csv
import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Email, To, Content, Mail

emails = []

with open(sys.argv[1], newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        emails.append(row['email'])

template = '<h1>You dont supply an html template to the script</h1>'

with open(sys.argv[2], 'r') as htmlfile:
    template = htmlfile.read()

sg = SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))

from_email = Email('whitman-2@hotmail.com')
subject = 'Sending with SendGrid is Fun'
content = Content('text/html', template)

mail = Mail(from_email, emails, subject, content)

response = sg.client.mail.send.post(request_body=mail.get())

print(response.status_code)
print(response.body)
print(response.headers)
