#! /usr/bin/env python

import os, sys, subprocess

if not os.geteuid() == 0:
    print()
    sys.exit(" : : : Only root can run this script  : : : : : : : : : : : : : : : : : : : :");
    print()

def menue():
    print()
    print()
    print(" - - - ", os.getcwd()," - - - - - - - - - - - - - - - - - - - - - -")
    print()
    print()
    print("   1    󰉙  Create a backup of your Bluetooth settings")
    print()
    print("        Before running this option, you'd set up all of your Bluetooth devices")
    print()
    print()
    print("   2    󰉍  Installing the backup   󱈸 System will reboot immediately 󱈸 ")
    print()
    print("        Make sure that your Bluetooth backup files are next to this program")
    print()
    print()
    print("   3    󰉘  Reset your Bluetooth settings   󱈸 Each device will be removed 󱈸")
    print()
    print("        Use that only if you have messd up your Bluetooth settings")
    print()
    print()
    print("   4    󰉒  Exit")
    print()
    print(" - - -  Leave this script  - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print()

    auswahl = input("  ")

    print("")

    if auswahl == "1":
        subprocess.run(['cp', '-p', '-r', '/var/lib/bluetooth', 'bluetooth'], shell=False);
        subprocess.run(['chmod','-R','555', 'bluetooth'], shell=False);
        print(" + + +  󰉗 bluetooth folder created in", os.getcwd(), " + + + + + + +")
        print()
    elif auswahl == "2":
        subprocess.run(['rsync', '-au', 'bluetooth', '/var/lib'], shell=False);
        subprocess.run(['reboot'], shell=False);
    elif auswahl == "3":
        subprocess.run(['rm', '-rf', '/var/lib/bluetooth'], shell=False);
        print(" x x x  Bluetooth removed  󰉘   x x x x x x x x x x x x x x x x x x x x x x x x")
        print()
    elif auswahl == "4":
        print(" : : :  Goodbye  : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :")
        print()
        exit();
    else:
        print(" # # #  Invalid  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")

menue()

