class MainMenu:


    def start(self):

        while True:

            print("""
==============================
MAIN MENU
==============================

1. Termux Packages
2. Python Packages
3. Node.js Packages
4. C / C++ Development
5. Git & GitHub Tools
6. Storage Manager
7. System Repair
8. Settings

0. Exit

""")

            choice = input("Select: ")

            if choice == "0":
                print("Goodbye.")
                break

            elif choice == "1":
                print("Termux Package Manager loading...")

            elif choice == "2":
                print("Python Package Manager loading...")

            else:
                print("Feature will be added.")

            input("\nPress Enter...")
