# lit_email component
A ⚡ [Lightning component](lightning.ai) ⚡ to enable you to send an email from any email account.


## 1. Install component
First, install lit_email

```bash
lightning install component lightning/lit-email
```


## 2. Gmail users
If you're not a GMAIL user, skip this step.

If you're a GMAIL user, you must use an **app password** instead of your gmail password. 

To create an app password, go to your [account dashboard](https://myaccount.google.com/) and follow these steps:    

1. Enable 2-factor auth
![enable 2-factor auth](/images/1_two_factor.jpg)

2. Create an app password
![enable 2-factor auth](/images/2_app_secret.jpg)


## 3. Use the component like this
Once the component is installed, use it in an app:

```python
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
```
