from django.core.mail import send_mail
import threading
import os

def sendMail(code , name, mail):
    thread = threading.Thread(
        target=send_mail,
        args=(
            "Код подтверждения",
            f"Здравствуйте {name}, ваш код подтверждения:\n{code}.",
            os.getenv('MAIL_BACK'),
            [mail],
        ),
        kwargs={'fail_silently': False}
    )
    print("Письмо отправлено")
    thread.start()
    return thread