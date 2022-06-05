# lit_email component

This ⚡ [Lightning component](lightning.ai) ⚡ was generated automatically with:

```bash
lightning init component lit_email
```

## To run lit_email

First, install lit_email (warning: this app has not been officially approved on the lightning gallery):

```bash
lightning install component https://github.com/theUser/lit_email
```

Once the app is installed, use it in an app:

```python
from lit_email import TemplateComponent
import lightning as L


class LitApp(L.LightningFlow):
    def __init__(self) -> None:
        super().__init__()
        self.lit_email = TemplateComponent()

    def run(self):
        print(
            "this is a simple Lightning app to verify your component is working as expected"
        )
        self.lit_email.run()


app = L.LightningApp(LitApp())
```
