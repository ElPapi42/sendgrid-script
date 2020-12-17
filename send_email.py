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

sg = SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))

from_email = Email("test@example.com")
to_email = To("test@example.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")

mail = Mail(from_email, to_email, subject, content)

response = sg.client.mail.send.post(request_body=mail.get())

print(response.status_code)
print(response.body)
print(response.headers)
