import smtplib
import logging
from typing import List
from email.mime.text import MIMEText

import lightning as L

logger = logging.getLogger(__name__)


class LitEmail(L.LightningFlow):
    def __init__(
        self,
        email: str,
        password: List[str],
        smtp_server: str = 'smtp.gmail.com',
        smtp_port: int = 465
    ) -> None:

        super().__init__()
        self.email = email
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

        if smtp_server is None:
            self.smtp_server = 'smtp.gmail.com'
            m = f"""
            smtp_server not specified. Using smtp.gmail.com as the default.
            if your email provider is not gmail, please find the smtp_server

            (try googling: 'smtp server for @yourDomain.com')
            """
            logger.warn(m)

    def send(self, to_emails: str, subject: str, body: str):
        self.run('send', to_emails, subject, body)

    def run(self, action, *args, **kwargs):
        if action == 'send':
            self._send(*args, **kwargs)

    def _send(self, to_emails: List[str], subject: str, body: str):

        gmail_user = self.email
        gmail_password = self.password

        sent_from = gmail_user

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = gmail_user
        msg['To'] = ', '.join(to_emails)

        try:
            server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to_emails, msg.as_string())
            server.close()

            logger.info('email sent!')
        except Exception as e:
            logger.error('failed to send email...')
            logger.error(e)
