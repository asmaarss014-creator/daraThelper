from helper import (
    load_categories,
    load_packages,
    install_package,
    search_package,
    update_database
)

def menu():
    categories = load_categories()
    packages = load_packages()

    while True:
        print("\n==== Dara Termux Helper ====\n")

        print("1. Categories")
        print("2. All Commands")
        print("3. Search")
        print("4. Update Database")
        print("0. Exit")

        choice = input("\nChoose: ")

        if choice == "1":
            for i, cat in enumerate(categories, 1):
                print(f"{i}. {cat}")

            c = input("\nCategory: ")

            try:
                name = list(categories.keys())[int(c)-1]

                print("\nPackages:")
                for pkg in categories[name]:
                    print("-", pkg)

                install = input("\nInstall package? (name/enter skip): ")

                if install:
                    install_package(install)

            except:
                print("Invalid category")


        elif choice == "2":
            print("\nAll Commands:")
            for pkg in packages:
                print("-", pkg)


        elif choice == "3":
            text = input("Search: ")
            results = search_package(text)

            for r in results:
                print("-", r)


        elif choice == "4":
            update_database()


        elif choice == "0":
            break


if __name__ == "__main__":
    menu()
