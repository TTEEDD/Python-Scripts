import whois
from datetime import datetime
from datetime import date
import subprocess
from time import sleep

def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return

def whoisDsp():

    #Waiting for PC to boot up
    sleep(20)
    now = datetime.now()
    domains = ['www.google.com', 'www.facebook.com']

    for doms in domains:
        # Getting WhoIs Information
        ins = whois.whois(doms)
        dname = doms
        dcreate = str(ins.creation_date)
        dexplist = ins.expiration_date

        if isinstance(dexplist,(list,)):
            # Runs the code below if domain has multiple expiration dates (Ex: Google, Yahoo or anything that uses MarkMonitor services)
            # Code also uses the first date it can find in the list
            # Getting Year, Month and Date for Domain and Calculating days remaining
            expYear = dexplist[0].strftime("%Y")
            expMonth = dexplist[0].strftime("%-m")
            expDay = dexplist[0].strftime("%-d")
            expDate = date(int(expYear), int(expMonth), int(expDay))
            nowDate = date(int(now.year), int(now.month), int(now.day))
            dayremain = expDate - nowDate
            dayremain = str(dayremain)
            dayremain = dayremain[:4]

        else:
            # Runs the code below if domain has only one expiration date
            # Getting Year, Month and Date for Domain and Calculating days remaining
            expYear = dexplist.strftime("%Y")
            expMonth = dexplist.strftime("%-m")
            expDay = dexplist.strftime("%-d")
            expDate = date(int(expYear), int(expMonth), int(expDay))
            nowDate = date(int(now.year), int(now.month), int(now.day))
            dayremain = expDate - nowDate
            dayremain = str(dayremain)
            dayremain = dayremain[:4]

        # Would you like a desktop notification or Terminal Output. [True for Notification | False for Output]
        sendNotification = True

        if(sendNotification == True):
            sendmessage(dname + " || " + dayremain + " Days")
        else:
            print("Domain Name: " + dname)
            print("Domain  Reg: " + dcreate)
            print("Domain  Exp: " + dexp)
            print("Days    Rem: " + dayremain + "\n")

whoisDsp()
