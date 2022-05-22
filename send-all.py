import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def main():
    message_alice = Mail(
        from_email="from@example.com",
        to_emails="to1@email.com",
        # to_emails=["to1@example.com", "to2@example.com"],
        # 上記の方法で複数アドレスに送信可能
        global_substitutions={"-name-": "alice"},
        # global_substitutions=[{"-name-": "alice"},{"-name-": "bob"}],
        # だと全てのアドレスに対してbobに上書きされる
        is_multiple=True,
        subject="Sending with Twilio SendGrid is Fun",
        html_content="Hi -name- !<br><strong>and easy to do anywhere, even with Python</strong>"
    )
    message_bob = Mail(
        from_email="from@gmail.com",
        to_emails="to2@example.com",
        # to_emails=["to1@example.com", "to2@example.com"],
        global_substitutions={"-name-": "bob"},
        is_multiple=True,
        subject="Sending with Twilio SendGrid is Fun",
        html_content="Hi -name- !<br><strong>and easy to do anywhere, even with Python</strong>"
    )
    try:
        sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
        response = sg.send(message_alice)
        response = sg.send(message_bob)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()