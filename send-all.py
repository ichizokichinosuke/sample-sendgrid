import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def main():
    message = Mail(
        from_email="from@example.com",
        to_emails=["to1@example.com", "to2@example.com"],
        subject="Sending with Twilio SendGrid is Fun",
        html_content="<strong>and easy to do anywhere, even with Python</strong>"
    )
    try:
        sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()