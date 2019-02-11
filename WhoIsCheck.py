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
    # sleep(20)
    now = datetime.now()
    domains = ['www.google.com', 'www.facebook.com', 'https://www.amazon.com/',
               'ebay.com', 'www.stackoverflow.com', 'https://www.yahoo.com/']

    for doms in domains:
        # Getting WhoIs Information
        ins = whois.whois(doms)
        dcreate = ins.creation_date
        dexplist = ins.expiration_date
        dregistrar = ins.registrar

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
            dayremain = str(dayremain.days)

        else:
            # Runs the code below if domain has only one expiration date
            # Getting Year, Month and Date for Domain and Calculating days remaining
            expYear = dexplist.strftime("%Y")
            expMonth = dexplist.strftime("%-m")
            expDay = dexplist.strftime("%-d")
            expDate = date(int(expYear), int(expMonth), int(expDay))
            nowDate = date(int(now.year), int(now.month), int(now.day))
            dayremain = expDate - nowDate
            dayremain = str(dayremain.days)

        # Would you like a desktop notification or Terminal Output. [True for Notification | False for Output]
        sendNotification = True

        if(sendNotification == True):
            sendmessage("[" + doms + "] & [" + dayremain + " Days]")
        else:
            # Converts Expiration Date List to String if possible
            if isinstance(dexplist,(list,)):
                dexpDis = str(dexplist[0])
            else:
                dexpDis = str(dexplist)

            # Converts Creation Date List to String if possible
            if isinstance(dcreate,(list,)):
                dcreateDis = str(dcreate[0])
            else:
                dcreateDis = str(dcreate)

            print("Domain Name: \t" + doms)
            print("Registrar: \t" + dregistrar)
            print("Registration: \t" + dcreateDis)
            print("Expiration: \t" + dexpDis)
            print("Days Remaining: " + dayremain + "\n")

        # Needs to 'Reset' or Sleep to do more than 3 searches quickly
        sleep(1)

whoisDsp()
