import platform
import shutil
import subprocess


class CompatibilityChecker:

    def __init__(self):

        self.system = {
            "architecture": platform.machine(),
            "platform": platform.platform(),
            "available": [],
            "unavailable": []
        }


    def command_available(self, command):

        return shutil.which(command) is not None



    def check_architecture(self):

        arch = self.system["architecture"]

        supported = [
            "aarch64",
            "arm64",
            "arm",
            "x86_64",
            "x86"
        ]

        return arch in supported



    def check_android(self):

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



    def check_tool(self, name, command, reason):

        if self.command_available(command):

            self.system["available"].append(
                {
                    "name": name,
                    "status": "available"
                }
            )

        else:

            self.system["unavailable"].append(
                {
                    "name": name,
                    "status": "unavailable",
                    "reason": reason
                }
            )



    def run(self):

        print(
            "Checking device compatibility..."
        )


        print(
            "Architecture:",
            self.system["architecture"]
        )


        print(
            "Android:",
            self.check_android()
        )


        self.check_tool(
            "Python",
            "python",
            "Python is not installed"
        )


        self.check_tool(
            "Git",
            "git",
            "Git is not installed"
        )


        self.check_tool(
            "Node.js",
            "node",
            "Node.js is not installed"
        )


        self.check_tool(
            "Rust",
            "cargo",
            "Rust compiler is not installed"
        )


        self.check_tool(
            "C/C++ Compiler",
            "clang",
            "Compiler is not available"
        )


        return self.system



    def show(self):

        print("\nAvailable:")
        print("----------------")

        for item in self.system["available"]:

            print(
                "✓",
                item["name"]
            )


        print("\nUnavailable:")
        print("----------------")

        for item in self.system["unavailable"]:

            print(
                "✗",
                item["name"],
                "-",
                item["reason"]
            )
