# email threading
import threading
from sendgrid import SendGridAPIClient
from django.conf import settings
from django.db.models import F
from sendgrid.helpers.mail import Mail
from django.conf import settings

class SendGridEmailThread(threading.Thread):
    def __init__(self, message):
        self.message = message
        threading.Thread.__init__(self)
    
    def run(self):
        sendgrid = SendGridAPIClient(settings.SENDGRID_API_KEY)
        sendgrid.send(self.message)


def SendGridSendMail(to_email, from_email, subject, message):
    message = Mail(
        from_email = from_email,
        to_emails = to_email,
        subject=subject,
        html_content=message
    )
    SendGridEmailThread(message).start()