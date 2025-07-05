 #! /usr/bin/env python

import os
import sys

if not os.geteuid() == 0:
    sys.exit("Only root can run this script")

def menue():
    print("")
    print("")
    print("	[ 1 ]	[ Create a backup of your Bluetooth settings ]")
    print("")
    print("		- Please check your files next to this Python script -")
    print("")
    print("")
    print("	[ 2 ]	[ Install that backup !! Your System will reboot immediately !! ]")
    print("")
    print("		-  Make sure that the Bluetooth backup files are next to this program")
    print("")
    print("")
    print("	[ 3 ]	[ Reset your Bluetooth settings. !! Each device will be removed !! ]")
    print("")
    print("		- Use that only if you have messed up your Bluetooth settings -")
    print("")
    print("")
    print("	[ 4 ]	[ Exit ]")
    print("")
    print("		- Leave this script -")
    print("")
    print("")
    auswahl = input("Choose an Option ")
    if auswahl == "1":
        os.system('cp -p -r /var/lib/bluetooth bluetooth && chmod -R 555 bluetooth')
    elif auswahl == "2":
        os.system('rsync -au bluetooth /var/lib && reboot')
    elif auswahl == "3":
        os.system('rm -rf /var/lib/bluetooth')
    elif auswahl == "4":
        os.system("exit")
    else:
        print("invalid section")

menue()



