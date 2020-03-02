import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import os
import sys

if len(sys.argv) < 2:
    exit(1)
smtp = 'smtp.something.com:587'
login = 'someone@someone.com'
password = 'pass'
sender = 'me@me.com'
receivers = [sys.argv[1]]

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = ", ".join(receivers)
msg['Subject'] = "Subject"

if len(sys.argv) == 3:
    TEXT = "Hi "+sys.argv[2]+","
else:
    TEXT = "Hi,"

TEXT = TEXT + """
body
body
"""


msg.attach(MIMEText(TEXT))

filenames = ["attachment.png"]
for file in filenames:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(file, 'rb').read())
    encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"'
                    % os.path.basename(file))
    msg.attach(part)

smtpObj = smtplib.SMTP(smtp)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(login, password)
smtpObj.sendmail(sender, receivers, msg.as_string())
