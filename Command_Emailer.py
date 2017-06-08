from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import Encoders
import time
import os
import smtplib

IMEI = ''

# Method used to send an email.
def send(sendFile):
    command = str(sendFile)
    print("Sendng: %s" % command)
    fromaddr = "msgc.borealis@gmail.com"
    toaddr = "data@sbd.iridium.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = IMEI
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(command, "rb").read())
    Encoders.encode_base64(part)

    part.add_header('Content-Disposition', 'attachment; filename=%s' % command)

    body = ""
    msg.attach(MIMEText(body, "plain"))
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("msgc.borealis", "FlyHighN0w")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)


menuSelect = int(raw_input())

if(menuSelect==1):
    fileOut = 'cutdown.sbd'
    send(fileOut)

else:
    print("Invalid Selection sending Idle command")
    fileOut = 'idle.sbd'
    send(fileOut)
