#!/usr/bin/env python3
from selenium import webdriver
from time import sleep
from datetime import datetime
import platform, sys, argparse, subprocess
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException

if platform.system()=="Windows":
    subprocess.Popen("cls", shell=True).communicate()
else:
    print("\033c", end="")
print("""\
██╗    ██╗██╗  ██╗ ██████╗ ██╗███████╗██╗  ██╗███████╗███████╗
██║    ██║██║  ██║██╔═══██╗██║██╔════╝╚██╗██╔╝██╔════╝██╔════╝
██║ █╗ ██║███████║██║   ██║██║███████╗ ╚███╔╝ ███████╗███████╗
██║███╗██║██╔══██║██║   ██║██║╚════██║ ██╔██╗ ╚════██║╚════██║
╚███╔███╔╝██║  ██║╚██████╔╝██║███████║██╔╝ ██╗███████║███████║
 ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝    
~~~ \033[0;107m\033[1;91mFind XSS in real-time with WHOISxss!\033[0m\033[0m    ^^^ +++
        +++ ^^^ Powered by \033[1;97mBINIT GHIMIRE (@WHOISbinit)\033[0m! ~~~
    """)

print("WHOISxss will only work if you either pass a URL with -u or insert a list of URLs in a text file and use -f to pass it.\n")
parser = argparse.ArgumentParser(description="Which domain do you want to try attacking on?")
parser.add_argument("-u", help="Your Target URL")
parser.add_argument("-f", help="File Name consisting of list of URLs, i.e. list.txt")
args = parser.parse_args()
if(args.u == None and args.f == None):
    parser.print_help()
    exit()
elif args.u is not None and args.f is not None:
    print("Please choose any one of the options, not both!")
    parser.print_help()
    exit()
elif args.u is not None and args.f is None:
    targets = [args.u]
    print("WHOISxss will crawl over \033[1;33m"+targets[0]+"\033[0m.")
elif args.u is None and args.f is not None:
    targets = [domains.rstrip() for domains in open(args.f)]
    print("WHOISxss is going to attack the websites listed in \033[1;33m"+args.f+"\033[0m file.")
else:
    targets = [input("Enter a domain to try attacking: ")]

payloads = [payload.rstrip() for payload in open('payloads.txt')]

whoisbrowser = webdriver.Firefox()
mouseEnter = ActionChains(whoisbrowser)
targetInput = "//input[@type='text']"

XSSed = 0
count = 0
now = datetime.now()
start_time = datetime.timestamp(now)
for target in range(len(targets)):
    confirmed = False
    for payload in range(len(payloads)):
        total = len(payloads)
        count+=1
        whoisbrowser.get(targets[target])
        sleep(1)
        print("\nTrying in "+targets[target]+"!\nUsing payload ("+str(count)+"/"+str(total)+ "): "+payloads[payload])
        try:
            targetField = whoisbrowser.find_element_by_xpath(targetInput)
            targetField.send_keys(payloads[payload]+Keys.ENTER)
            targetField.submit()
            sleep(1)
        except:
            pass
        try:
            try:
                mouseEnter.move_to_element(whoisbrowser.find_element_by_xpath('//*[@onmouseenter]')).perform()
            except:
                pass
            try:
                WebDriverWait(whoisbrowser, 5).until(EC.alert_is_present(), "Nothing!")
                alertBox = whoisbrowser.switch_to.alert
                alertText = alertBox.text
                alertBox.accept()
                if(alertText=="31337"):
                    confirmed = True
                    print("\n\033[1;101m\033[1;96m| XSS Detected! |\033[0m\033[0m\n\033[1;93mURL:\033[0m \033[1m"+targets[target]+"\033[0m\n\033[1;93mPayload:\033[0m \033[1m"+payloads[payload]+"\033[0m\n")
                    output = open("xss.txt","a")
                    output.write("URL: "+targets[target]+"\nPayload: "+payloads[payload]+"\n\n")
                    output.close()
                    print("+---------------------------------------------+")
            except:
                pass
        except:
            pass
        if confirmed:
            XSSed += 1
            break
now = datetime.now()
end_time = datetime.timestamp(now)
print("\n\033[1;94mAttack Completed\033[0m in \033[1;97m" +str(round(((end_time-start_time)/60),2)) +" minutes\033[0m!")
if(XSSed==0): ("~~~~~~ \033[1;94mNo XSS Found!\033[0m ~~~~~~")
else:
    if args.u is not None and args.f is None:
        print("\n\033[1;101m\033[1;96m| XSS Found! |\033[0m\033[0m \033[1;104m| Check xss.txt! |\033[0m")
    else:
        print("\n\033[1;101m\033[1;96m| " + str(XSSed)+" XSS Found! |\033[0m\033[0m \033[1;104m| Check xss.txt! |\033[0m")
whoisbrowser.close()
print("""\

~~~ Thank You for using WHOISxss!
                   ~ \033[1;94m@WHOISbinit\033[0m
    """)