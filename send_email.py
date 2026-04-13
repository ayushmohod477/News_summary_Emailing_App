import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "ayushmohod008@gmail.com"
    password = "extf rokh mdae cixx"

    receiver = "ayushmohod008@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


