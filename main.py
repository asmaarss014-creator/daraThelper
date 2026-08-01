from helper import (
    load_packages,
    search_package,
    install_package,
    update_database
)


def show_packages(packages):

    print("\n==== Available Packages ====\n")

    for i, item in enumerate(packages, 1):

        print(
            f"{i}. {item['name']}"
        )

        print(
            f"   Package: {item['package']}"
        )

        print(
            f"   Category: {item['category']}"
        )

        print(
            f"   Info: {item['description']}"
        )

        print()



def select_install(packages):

    choice = input(
        "\nSelect package number(s): "
    ).strip()


    selected = []


    try:

        # Install all
        if choice.lower() == "all":

            selected = packages


        # Multiple selection: 1,2,5
        elif "," in choice:

            numbers = choice.split(",")

            for number in numbers:

                index = int(number) - 1

                if 0 <= index < len(packages):
                    selected.append(
                        packages[index]
                    )


        # Range: 1-5
        elif "-" in choice:

            start, end = choice.split("-")

            start = int(start) - 1
            end = int(end)


            selected = packages[start:end]


        # Single number
        else:

            index = int(choice) - 1

            if 0 <= index < len(packages):

                selected.append(
                    packages[index]
                )


    except:

        print(
            "Invalid selection"
        )


    for item in selected:

        install_package(
            item["package"]
        )



def menu():

    while True:

        packages = load_packages()


        print(
            "\n====== Dara Termux Helper ======\n"
        )


        print(
            "1. Show All Commands"
        )

        print(
            "2. Search Package"
        )

        print(
            "3. Update Database"
        )

        print(
            "0. Exit"
        )


        choice = input(
            "\nChoose: "
        )


        if choice == "1":

            show_packages(
                packages
            )

            select_install(
                packages
            )


        elif choice == "2":

            text = input(
                "Search: "
            )


            results = search_package(
                text
            )


            if results:

                show_packages(
                    results
                )

                select_install(
                    results
                )

            else:

                print(
                    "No package found"
                )


        elif choice == "3":

            update_database()


        elif choice == "0":

            print(
                "Goodbye!"
            )

            break


        else:

            print(
                "Invalid option"
            )



if __name__ == "__main__":

    menu()
