import os
from lit_email import LitEmail
import io
from contextlib import redirect_stdout


def test_send_message():
    email = os.environ['TEST_EMAIL_ADDRESS']
    password = os.environ['TEST_EMAIL_PASSWORD']

    emailer = LitEmail(email, password)

    with io.StringIO() as buf, redirect_stdout(buf):
        emailer.send(
            to_emails=[os.environ['TEST_EMAIL_ADDRESS']],
            subject='Hello from ⚡ Lightning CI/CD ⚡',
            body='test body'
        )
        output = buf.getvalue()
        print(output)
        assert 'sent!' in output
