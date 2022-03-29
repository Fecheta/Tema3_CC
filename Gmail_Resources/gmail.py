import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from Gmail_Resources.Google import Create_Service


def sendmail():
    CLIENT_SECRET_FILE = 'client_secret.json'
    API_NAME = 'gmail'
    API_VERSION = 'v1'
    SCOPES = ['https://mail.google.com/']
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    emailMsg = "test"
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = "martiscafilip8@gmail.com"
    mimeMessage['subject'] = 'Test'
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
