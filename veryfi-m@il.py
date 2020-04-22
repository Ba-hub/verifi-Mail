#!/usr/bin/python
########################################
# Script : veryfi-m@il                 #
#    JOB : Verify Email Address        #
# CodedBy: ghosthub (b@b@y)            #
########################################
#
#Colors#
#
rd="\033[1;31m"
gr="\033[1;32m"
yl="\033[1;33m"
wi="\033[1;37m"
#
#
#Libraries#
try:
    from os import system as sy, path; sy("cls||clear");import requests,socket,optparse,re
except ImportError:
    print(rd+"\n["+yl+"!"+rd+"] "+yl+"Error: Please Install [ "+gr+"Requests"+yl+" ] "+rd+" !!!"+wi)
    print(wi+"["+gr+"*"+wi+"] Use This Command:>"+gr+" pip install requests"+wi)
    exit(1)
#
# Check Internet Connection #
def cnet():
    try:
        ip = socket.gethostbyname("www.google.com")
        con = socket.create_connection((ip, 80), 2)
        return True
    except socket.error:
        pass
    return False
#
#Check-Email-Valiteion#
checkmail = lambda email: any(re.match(reg, email) for reg in [r"(\W|^)[\w.+\-]*@gmail\.com(\W|$)", r"[a-zA-Z0-9_\.+]+@hotmail(\.[a-z]{2,3}){1,2}"])
#
#Check-Email-Function#
#
def ISMAIL(email):
    try:
        data = {"email": email}
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24'}
        response = requests.post("https://verifyemailaddress.com/result", headers=headers, data=data).text
        if "is valid" in response:
            print(wi+"["+gr+"+"+wi+"] Email["+gr+email+wi+"] STATUS["+gr+" FOUND "+wi+"]")
        else:
            #try another website
            response = requests.post("https://www.infobyip.com/verifyemailaccount.php", headers=headers, data=data).text
            if "Email account exists." in response:
                print(wi+"["+gr+"+"+wi+"] Email["+gr+email+wi+"] STATUS["+gr+" FOUND "+wi+"]")
            else:
                print(yl+"["+rd+"-"+yl+"] Email["+rd+email+yl+"] STATUS["+rd+" NOTFD "+yl+"]"+wi)
    except(KeyboardInterrupt,EOFError):
        print(wi+" ")
        exit(1)

parse = optparse.OptionParser("""
USAGE: python2 veryfi-m@il.py [OPTIONS...]
-------------
OPTIONS:
       |
    |--------                                                           
    |  -s --single [Email]                 ::> Check Single Email   
    |--------
    |  -m --many   [Email,Email2,etc]      ::> Check Many Emails
    |--------
    |  -f --file   [Email_file]            ::> Check All Emails From File
-------------
Examples:
        |
     |--------
     | python2 veryfi-m@il.py -s abc@gmail.com
     |--------
     | python2 veryfi-m@il.py -m abc@gmail.com,abc12@gmail.com,abc123@hotmail.com
     |--------
     | python2 veryfi-m@il.py -f emails.txt
     |--------

                        .:: Valid Emails To Check ::.
                        [ Gmail.com ,,, hotmail.com ]

""",version="2.0")
def Main():
    parse.add_option('-s','-S','--single','--SINGLE', dest="Smail",type="string")
    parse.add_option('-m','-m','--many','--MANY', dest="Mmail",type="string")
    parse.add_option('-f','-F','--file','--FILE', dest="Fmail",type="string")
    (opt,args) = parse.parse_args()
    if opt.Smail !=None:
        if cnet() !=True:
            print(rd+"\n["+yl+"!"+rd+"]"+yl+" Error: Please Check Your Internet Connection "+rd+"!!!"+wi)
            exit(1)
        email = opt.Smail
        if not email.strip() or "@" not in email.strip() or not checkmail(email.strip()):exit(yl+"["+rd+"!"+yl+"]"+rd+" ERROR"+yl+": Email["+rd+email.strip()+yl+"] STATUS["+rd+" Invalid "+yl+"]"+wi)
        email = email.strip()
        print(gr+"["+yl+"~"+gr+"]"+yl+" Checking....\n"+wi)
        ISMAIL(email)
    elif opt.Mmail !=None:
        if cnet() !=True:
            print(rd+"\n["+yl+"!"+rd+"]"+yl+" Error: Please Check Your Internet Connection "+rd+"!!!"+wi)
            exit(1)
        many_email = opt.Mmail
        print(gr+"["+yl+"~"+gr+"]"+yl+" Checking....\n"+wi)
        if ',' in many_email:
            emails = many_email.split(",")
        else:
            print(yl+"\n["+rd+"!"+yl+"] Error: Please Use[ "+wi+","+yl+" ] To Split The Emails"+rd+" !!!"+wi)
            exit(1)
        try:
            for email in emails:
                if not email.strip(): continue
                if "@" not in email.strip() or not checkmail(email.strip()):print(yl+"["+rd+"!"+yl+"]"+rd+" ERROR"+yl+": Email["+rd+email.strip()+yl+"] STATUS["+rd+" Invalid "+yl+"]"+wi);continue
                email = email.strip()
                ISMAIL(email)
        except (KeyboardInterrupt,EOFError):
            print(wi+" ")
            exit(1)
            
    elif opt.Fmail !=None:
        emails_file = opt.Fmail
        print(gr+"["+yl+"~"+gr+"]"+yl+" Checking....\n"+wi)
        if not path.isfile(emails_file):
            print(yl+"\n["+rd+"!"+yl+"]"+rd+" Error:"+yl+" No Such File: [ "+rd+emails_file+yl+" ]"+rd+" !!!"+wi)
            print(wi+"["+yl+"!"+wi+"]"+yl+" Please:"+wi+" Check Your Emails File Path."+yl+"!"+wi)
            exit(1)
        try:
            with open(emails_file) as fop:
                for email in fop:
                    if not email.strip():continue
                    if not "@" in email or not checkmail(email.strip()): print(yl+"["+rd+"!"+yl+"]"+rd+" ERROR"+yl+": Email["+rd+email.strip()+yl+"] STATUS["+rd+" Invalid "+yl+"]"+wi);continue
                    email = email.strip()
                    ISMAIL(email)
            fop.close()
        except (KeyboardInterrupt,EOFError):
            print(rd+"\n["+yl+"!"+yl+"] Aborting..."+rd+"!")
            exit(1)
    else:
        print(parse.usage)
        exit(1)

if __name__=="__main__":
    Main()
