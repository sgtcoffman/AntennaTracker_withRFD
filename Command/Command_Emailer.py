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

def imeiSelection(menuChoice):
    if(menuChoice == 1):
        IMEI = str(300234060252680)
    elif(menuChoice == 2):
        IMEI = str(300234063043420)
    else:
        print("Invalid selection, please enter IMEI:")
        IMEI = str(raw_input())

print("Choose IMEI")
print("\n1: 300234060252680\n")
print("2: 300234063043420\n")
firstChoice = int(raw_input())
imeiSelection(firstChoice)

print("\n1: Send Valve Open Command\n")
print("2: Send Fan Start Command\n")
print("3: Send Fan Off Command\n")
print("4: Send Valve Close Command\n")
print("5: Send Nichrome Cutdown Command\n")
menuSelect = int(raw_input())

if(menuSelect==1):
    fileOut = 'cutdown.sbd'
    send(fileOut)
elif(menuSelect==2):
    fileOut = 'fanStart.sbd'
    send(fileOut)
elif(menuSelect==3):
    fileOut = 'fanOff.sbd'
    send(fileOut)
elif(menuSelect==4):
    fileOut = 'valveClose.sbd'
    send(fileOut)
elif(menuSelect==5):
    fileOut = 'nichrome.sbd'
    send(fileOut)
else:
    print("Invalid Selection sending Idle command")
    fileOut = 'idle.sbd'
    send(fileOut)
'''
else:
    wait = True
    path = os.getcwd()
    for file in os.listdir(path):
        if file.endswith(".sbd"):
            wait = True
            # print(file)
            command = str(file)
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

            part.add_header('Content-Disposition','attachment; filename=%s' % command)

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
            while(wait == True):
                nxt_key = str(raw_input())
                if(nxt_key == 'n'):
                    wait = False
'''
