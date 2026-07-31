from helper import (
    load_categories,
    load_packages,
    install_package,
    search_package,
    update_database
)


def choose_packages(package_list):
    """
    Convert user input:
    1
    1,2,5
    1-5
    all
    into package names
    """

    selected = []

    choice = input("\nSelect package: ").strip().lower()

    if choice == "all":
        return package_list


    try:
        # Multiple numbers
        if "," in choice:
            numbers = choice.split(",")

            for n in numbers:
                index = int(n.strip()) - 1

                if 0 <= index < len(package_list):
                    selected.append(package_list[index])


        # Range
        elif "-" in choice:
            start, end = choice.split("-")

            start = int(start) - 1
            end = int(end)

            selected = package_list[start:end]


        # Single number
        else:
            index = int(choice) - 1

            if 0 <= index < len(package_list):
                selected.append(package_list[index])


    except:
        print("Invalid selection")


    return selected



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

                category_packages = categories[name]


                print("\nPackages:\n")

                for i, pkg in enumerate(category_packages, 1):
                    print(f"{i}. {pkg}")


                selected = choose_packages(category_packages)


                for pkg in selected:
                    install_package(pkg)


            except Exception:
                print("Invalid category")



        elif choice == "2":

            print("\nAll Commands:\n")

            for i, pkg in enumerate(packages, 1):
                print(f"{i}. {pkg}")


            selected = choose_packages(packages)


            for pkg in selected:
                install_package(pkg)



        elif choice == "3":

            text = input("Search: ")

            results = search_package(text)


            if results:

                for i, r in enumerate(results, 1):
                    print(f"{i}. {r}")


                selected = choose_packages(results)


                for pkg in selected:
                    install_package(pkg)

            else:
                print("No package found")



        elif choice == "4":

            update_database()

            packages = load_packages()



        elif choice == "0":

            break



        else:

            print("Invalid option")



if __name__ == "__main__":
    menu()
