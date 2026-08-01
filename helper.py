import os
import json
import subprocess
import urllib.request


# Database files
DATA_FILES = [
    "data1.txt",
    "data2.txt"
]

DATABASE_URLS = {
    "data1.txt": "",
    "data2.txt": "",
    "categories.json": ""
}


def load_packages():
    """
    Load packages from data1.txt and data2.txt
    """

    packages = []

    for file in DATA_FILES:

        if os.path.exists(file):

            with open(file, "r", encoding="utf-8") as f:

                for line in f:

                    package = line.strip()

                    # Ignore empty lines and comments
                    if package and not package.startswith("#"):
                        packages.append(package)


    # Remove duplicates
    return sorted(set(packages))



def load_categories():

    """
    Load category database
    """

    if not os.path.exists("categories.json"):

        return {}


    with open(
        "categories.json",
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def install_package(package):

    """
    Install Termux package
    """

    print(
        f"\nInstalling {package}...\n"
    )


    subprocess.run(
        [
            "pkg",
            "install",
            package,
            "-y"
        ]
    )


    print(
        f"\n{package} installation finished."
    )



def search_package(text):

    """
    Search packages
    """

    packages = load_packages()


    return [
        package
        for package in packages
        if text.lower() in package.lower()
    ]



def update_database():

    """
    import urllib.request
import os


DATABASE_FILES = {
    "data1.txt":
    "https://raw.githubusercontent.com/asmaarss014-creator/daraThelper/main/database/data1.txt",

    "data2.txt":
    "https://raw.githubusercontent.com/asmaarss014-creator/daraThelper/main/database/data2.txt"
}


def update_database():

    print("\n==== Updating Dara Database ====\n")

    database_folder = "database"

    if not os.path.exists(database_folder):
        os.makedirs(database_folder)


    for filename, url in DATABASE_FILES.items():

        path = os.path.join(
            database_folder,
            filename
        )

        try:

            print(
                f"Downloading {filename}..."
            )

            urllib.request.urlretrieve(
                url,
                path
            )

            print(
                f"{filename} updated successfully"
            )


        except Exception as e:

            print(
                f"Failed {filename}: {e}"
            )


    print(
        "\nDatabase update complete."
    )
