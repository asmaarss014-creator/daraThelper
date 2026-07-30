import json
import os

from core import CoreSystem
from installer import Installer
from storage import StorageManager


APP = "Termux Developer Helper"


def clear():
    os.system("clear")


def load_database():

    with open(
        "database.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



class DeveloperHelper:


    def __init__(self):

        self.database = load_database()

        self.core = CoreSystem()

        self.installer = Installer()

        self.storage = StorageManager()



    def banner(self):

        print("""
====================================
     TERMUX DEVELOPER HELPER
             Version 1.0
====================================
""")



    def package_menu(self):

        while True:

            clear()

            print("""
PACKAGE MANAGER

1. Termux Packages
2. Python Packages
3. Developer Profiles
0. Back
""")

            choice = input(
                "Select: "
            )


            if choice == "1":

                self.install_termux()


            elif choice == "2":

                self.install_python()


            elif choice == "3":

                self.profile_menu()


            elif choice == "0":

                break



    def install_termux(self):

        categories = list(
            self.database["packages"].keys()
        )


        while True:

            print("\nTermux Categories")

            for i, c in enumerate(
                categories,
                1
            ):

                print(
                    i,
                    c
                )


            print("0 Back")


            choice = input(
                "Select: "
            )


            if choice == "0":
                break


            try:

                category = categories[
                    int(choice)-1
                ]


                for package in self.database["packages"][category]:

                    self.installer.install(
                        "pkg",
                        package
                    )


            except:

                print(
                    "Invalid option"
                )



    def install_python(self):

        categories = list(
            self.database["python_packages"].keys()
        )


        print("\nPython Categories")


        for i,c in enumerate(
            categories,
            1
        ):

            print(
                i,
                c
            )


        choice = input(
            "Select: "
        )


        try:

            category = categories[
                int(choice)-1
            ]


            for package in self.database["python_packages"][category]:

                self.installer.install(
                    "pip",
                    package
                )


        except:

            print(
                "Invalid option"
            )



    def profile_menu(self):

        profiles = list(
            self.database["profiles"].keys()
        )


        print("\nDeveloper Profiles")


        for i,p in enumerate(
            profiles,
            1
        ):

            print(
                i,
                p
            )


        choice = input(
            "Select: "
        )


        try:

            profile = profiles[
                int(choice)-1
            ]


            data = self.database["profiles"][profile]


            for package in data["termux"]:

                self.installer.install(
                    "pkg",
                    package
                )


            for package in data["pip"]:

                self.installer.install(
                    "pip",
                    package
                )


        except:

            print(
                "Invalid option"
            )



    def storage_menu(self):

        while True:

            print("""
STORAGE MANAGER

1. Setup Developer Folder
2. Show Location
3. Create Project
4. List Files
0. Back
""")

            choice=input(
                "Select: "
            )


            if choice=="1":

                self.storage.setup()


            elif choice=="2":

                self.storage.show_location()


            elif choice=="3":

                name=input(
                    "Project name: "
                )

                self.storage.create_project(
                    name
                )


            elif choice=="4":

                self.storage.list_files()


            elif choice=="0":

                break



    def start(self):

        clear()

        self.banner()

        self.core.compatibility_report()


        input(
            "\nPress Enter to continue..."
        )


        while True:

            clear()

            print("""
MAIN MENU

1. Package Manager
2. Storage Manager
3. Device Report
4. Exit
""")


            choice=input(
                "Select: "
            )


            if choice=="1":

                self.package_menu()


            elif choice=="2":

                self.storage_menu()


            elif choice=="3":

                self.core.compatibility_report()

                input(
                    "\nEnter..."
                )


            elif choice=="4":

                print(
                    "Goodbye."
                )

                break




if __name__=="__main__":

    app = DeveloperHelper()

    app.start()
