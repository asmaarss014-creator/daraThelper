import os
import platform
import shutil


class SystemChecker:

    def __init__(self):
        self.info = {}

    def run(self):

        self.info["python"] = platform.python_version()
        self.info["architecture"] = platform.machine()
        self.info["storage"] = self.storage()

        self.display()


    def storage(self):

        try:
            total, used, free = shutil.disk_usage("/")

            return {
                "total": round(total / (1024**3),2),
                "free": round(free / (1024**3),2)
            }

        except:
            return None


    def display(self):

        print("System Information")
        print("------------------")

        print(
            "Python:",
            self.info["python"]
        )

        print(
            "CPU:",
            self.info["architecture"]
        )

        if self.info["storage"]:
            print(
                "Free Storage:",
                self.info["storage"]["free"],
                "GB"
            )

        print()
