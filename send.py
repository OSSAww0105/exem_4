import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "abdulboriy0207@gmail.com"
receiver_email = "absaitovdev@gmail.com"
password = "jnydkcubncpvtlms"
message = """\
Subject: 
    https://github.com/OSSAww0105/exem_4.git
    dcoker image: spiker007/my_exam_bot:latest
"""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
