from lit_email import LitEmail
import lightning as L


class LitApp(L.LightningFlow):
    def __init__(self) -> None:
        super().__init__()
        self.lit_email = LitEmail(
            email='name@email.com',
            password='yourPassword'
        )

    def run(self):
        self.lit_email.send(
            to_emails=['personA@email.com', 'personB@email.com'],
            subject='Hello from ⚡ Lightning ⚡',
            body='I can send emails whenever! including when models train, deploy, etc...'
        )

app = L.LightningApp(LitApp())
