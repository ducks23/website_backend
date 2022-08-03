import os
import requests


def send_email(email, name):
    response = requests.post(
        url="https://api.mailgun.net/v3/sandbox45433563933546f49e003dba4adbfd26.mailgun.org/messages",
        auth=("api", os.environ["MAIL_GUN_KEY"]),
        data={
            "from": "Mailgun Sandbox <postmaster@sandbox45433563933546f49e003dba4adbfd26.mailgun.org>",
            "to": f"{name} {email}>",
            "subject": f"Hello {name}",
            "text": f"Congratulations {name}, welcome to my group",
        },
    )
    print(response.reason)
    print(response.status_code)
    return response
