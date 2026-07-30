#!/usr/bin/env python3

import os
import sys
import time

from modules.system_check import SystemChecker
from modules.menu import MainMenu


VERSION = "1.0.0"


def clear():
    os.system("clear")


def banner():
    print("""
==============================================
        TERMUX DEVELOPER HELPER
              Version {}
==============================================
""".format(VERSION))


def loading():
    steps = [
        "Checking Python",
        "Detecting Android",
        "Checking Termux",
        "Checking Storage",
        "Checking Architecture",
        "Loading Modules"
    ]

    for step in steps:
        print("✓ " + step)
        time.sleep(0.3)

    print("\nSystem Ready.\n")


def main():

    clear()
    banner()

    loading()

    checker = SystemChecker()
    checker.run()

    menu = MainMenu()
    menu.start()


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\n\nInstallation cancelled by user.")
        sys.exit(0)
