# core.py

import os
import platform
import shutil
import subprocess


class CoreSystem:


    def __init__(self):

        self.info = {}


    def command_exists(self, command):

        return shutil.which(command) is not None



    def get_android_version(self):

        try:

            result = subprocess.run(
                "getprop ro.build.version.release",
                shell=True,
                capture_output=True,
                text=True
            )

            return result.stdout.strip()

        except:

            return "Unknown"



    def get_storage(self):

        try:

            total, used, free = shutil.disk_usage("/")

            return {
                "total": round(total/(1024**3),2),
                "free": round(free/(1024**3),2)
            }

        except:

            return {
                "total":0,
                "free":0
            }



    def detect(self):

        self.info = {

            "python":
                platform.python_version(),

            "architecture":
                platform.machine(),

            "system":
                platform.system(),

            "android":
                self.get_android_version(),

            "storage":
                self.get_storage()

        }


        return self.info



    def check_tools(self):

        tools = {

            "Python":"python",
            "Git":"git",
            "Node.js":"node",
            "Rust":"cargo",
            "C/C++":"clang",
            "Java":"java"

        }


        result = {

            "available":[],
            "missing":[]

        }


        for name, command in tools.items():


            if self.command_exists(command):

                result["available"].append(name)

            else:

                result["missing"].append(name)


        return result



    def compatibility_report(self):

        data = self.detect()

        tools = self.check_tools()


        print("""
============================
DEVICE REPORT
============================
""")


        print(
            "Android:",
            data["android"]
        )

        print(
            "Architecture:",
            data["architecture"]
        )

        print(
            "Python:",
            data["python"]
        )

        print(
            "Free Storage:",
            data["storage"]["free"],
            "GB"
        )


        print("\nAvailable Tools")

        for item in tools["available"]:

            print(
                "✓",
                item
            )


        print("\nMissing Tools")

        for item in tools["missing"]:

            print(
                "✗",
                item
            )


        return {
            "device":data,
            "tools":tools
        }
