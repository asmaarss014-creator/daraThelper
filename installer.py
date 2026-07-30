import subprocess
import shutil
import os
from datetime import datetime


class Installer:


    def __init__(self):

        os.makedirs(
            "logs",
            exist_ok=True
        )

        self.log_file = "logs/install.log"



    def log(self, text):

        with open(
            self.log_file,
            "a",
            encoding="utf-8"
        ) as file:

            file.write(
                f"[{datetime.now()}] {text}\n"
            )



    def available(self, command):

        return shutil.which(command) is not None



    def run(self, command):

        try:

            print(
                "\nRunning:",
                command
            )


            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )


            for line in process.stdout:

                print(
                    line.strip()
                )


            process.wait()


            if process.returncode == 0:

                self.log(
                    "SUCCESS: " + command
                )

                return True


            else:

                self.log(
                    "FAILED: " + command
                )

                return False



        except KeyboardInterrupt:

            print(
                "\nCancelled by user."
            )

            self.log(
                "CANCELLED: " + command
            )

            return False



    def command(self, manager, package):

        commands = {

            "pkg":
                f"pkg install -y {package}",


            "pip":
                f"pip install {package}",


            "npm":
                f"npm install -g {package}",


            "cargo":
                f"cargo install {package}",


            "gem":
                f"gem install {package}",


            "go":
                f"go install {package}"

        }


        return commands.get(
            manager
        )



    def install(
            self,
            manager,
            package
    ):


        cmd = self.command(
            manager,
            package
        )


        if not cmd:

            print(
                "Unknown manager."
            )

            return False



        print(
            "\nPackage:",
            package
        )

        print(
            "Manager:",
            manager
        )


        answer = input(
            "Install? (y/n): "
        )


        if answer.lower() != "y":

            print(
                "Skipped."
            )

            return False



        attempts = 3


        while attempts > 0:


            if self.run(cmd):

                print(
                    "Installed successfully."
                )

                return True


            print(
                "Installation failed."
            )


            retry = input(
                "Retry? (y/n): "
            )


            if retry.lower() != "y":

                break


            attempts -= 1



        return False



    def update(self, manager):

        commands = {

            "pkg":
                "pkg update && pkg upgrade -y",

            "pip":
                "pip list --outdated",

            "npm":
                "npm update -g",

            "cargo":
                "rustup update"

        }


        if manager in commands:

            self.run(
                commands[manager]
            )



    def remove(
            self,
            manager,
            package
    ):

        commands = {

            "pkg":
                f"pkg uninstall -y {package}",

            "pip":
                f"pip uninstall -y {package}",

            "npm":
                f"npm uninstall -g {package}"

        }


        if manager in commands:

            self.run(
                commands[manager]
          )
