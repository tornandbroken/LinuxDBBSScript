 #! /usr/bin/env python

import os
import sys
import getpass

password = getpass.getpass("Enter root password: ")


def menue():
    print("")
    print("")
    print("   1 󰉙  Create a backup of your Bluetooth settings")
    print("")
    print(" - - -  Before running this script set up all your Bluetooth devices - - - - - - - ")
    print("")
    print("")
    print("   2 󰉍  Installing the backup   󱈸 System will reboot immediately 󱈸 ")
    print("")
    print(" - - -  Make sure that your Bluetooth backup files are next to this program  - - -")
    print("")
    print("")
    print("   3 󰉘  Reset your Bluetooth settings   󱈸 Each device will be removed 󱈸")
    print("")
    print(" - - -  Use that only if you have messed up your Bluetooth settings  - - - - - - -")
    print("")
    print("")
    print("   4 󰉒  Exit")
    print("")
    print(" - - -  Leave this script  - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("")

    auswahl = input("  ")

    print("")

    if auswahl == "1":
        os.system('cp -p -r /var/lib/bluetooth bluetooth && chmod -R 555 bluetooth');
        print(" + + +  Backup 󰉗 bluetooth created in", os.getcwd(), " + + + + + + +")
    elif auswahl == "2":
        os.system('rsync -au bluetooth /var/lib && reboot')
    elif auswahl == "3":
        os.system('rm -rf /var/lib/bluetooth');
        print(" x x x  Bluetooth removed  󰉘   x x x x x x x x x x x x x x x x x x x x x x x x x x")
    elif auswahl == "4":
        os.system("exit");
        print(" : : :  Goodbye  : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :")
    else:
        print(" # # #  Invalid  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")

menue()

