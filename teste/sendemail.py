import smtplib
# email options
SERVER = "10.10.0.128"
FROM = "fagundes@cedae.com.br"
TO = ["ricky@cedae.com.br"]
SUBJECT = "Alert!"
TEXT = "This message was sent with Python's smtplib."


message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

server = smtplib.SMTP(SERVER)
server.set_debuglevel(3)
server.sendmail(FROM, TO, message)
server.quit()