import subprocess
import shutil
import os
import time
from datetime import datetime


class Installer:

    def __init__(self):
        self.log_file = "logs/install.log"

        os.makedirs("logs", exist_ok=True)


    def log(self, message):

        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(
                f"[{datetime.now()}] {message}\n"
            )


    def command_exists(self, command):

        return shutil.which(command) is not None


    def run_command(self, command):

        try:

            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )


            for line in process.stdout:
                print(line.strip())


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
                "\nInstallation cancelled."
            )

            self.log(
                "CANCELLED: " + command
            )

            return False



    def check_installed(self, manager, package):

        checks = {

            "pkg":
                f"pkg list-installed | grep {package}",

            "pip":
                f"pip show {package}",

            "npm":
                f"npm list -g {package}",

            "cargo":
                f"cargo install --list | grep {package}"

        }


        if manager in checks:

            result = subprocess.run(
                checks[manager],
                shell=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            return result.returncode == 0


        return False



    def build_command(self, manager, package):

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


        return commands.get(manager)



    def install(self, manager, package):


        print(
            f"\nChecking {package}..."
        )


        if self.check_installed(
            manager,
            package
        ):

            print(
                "Already installed."
            )

            return True



        command = self.build_command(
            manager,
            package
        )


        if not command:

            print(
                "Unknown package manager."
            )

            return False



        print(
            "\nReady to install:"
        )

        print(command)


        confirm = input(
            "\nContinue? (y/n): "
        )


        if confirm.lower() != "y":

            print(
                "Skipped."
            )

            return False



        attempts = 3


        while attempts:

            print(
                f"\nInstalling... Attempts left: {attempts}"
            )


            if self.run_command(command):

                print(
                    "Installation complete."
                )

                return True


            attempts -= 1

            time.sleep(2)



        print(
            "Installation failed."
        )

        return False
