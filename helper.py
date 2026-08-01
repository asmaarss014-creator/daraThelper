import os
import urllib.request
import subprocess


DATABASE_FILES = [
    "data1.txt",
    "data2.txt"
]


DATABASE_URLS = {
    "data1.txt":
    "https://raw.githubusercontent.com/asmaarss014-creator/daraThelper/main/database/data1.txt",

    "data2.txt":
    "https://raw.githubusercontent.com/asmaarss014-creator/daraThelper/main/database/data2.txt"
}



def load_packages():
    """
    Load packages from database files
    Format:
    ID|Name|Package|Description|Category
    """

    packages = []


    for file in DATABASE_FILES:

        if not os.path.exists(file):
            continue


        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:


            for line in f:

                line = line.strip()


                if (
                    not line
                    or line.startswith("#")
                ):
                    continue


                parts = line.split("|")


                if len(parts) >= 5:

                    packages.append(
                        {
                            "id": parts[0],
                            "name": parts[1],
                            "package": parts[2],
                            "description": parts[3],
                            "category": parts[4]
                        }
                    )


    return packages




def search_package(text):

    packages = load_packages()

    results = []


    for item in packages:

        search_data = (
            item["id"]
            + item["name"]
            + item["package"]
            + item["description"]
            + item["category"]
        )


        if text.lower() in search_data.lower():

            results.append(item)


    return results




def get_categories():

    packages = load_packages()

    categories = {}


    for item in packages:

        category = item["category"]


        if category not in categories:

            categories[category] = []


        categories[category].append(item)


    return categories




def install_package(package):

    print(
        f"\nInstalling {package}...\n"
    )


    try:

        subprocess.run(
            [
                "pkg",
                "install",
                package,
                "-y"
            ],
            check=True
        )


        print(
            f"{package} installed successfully."
        )


    except subprocess.CalledProcessError:

        print(
            f"Failed installing {package}"
        )




def update_database():

    print(
        "\n==== Updating Dara Database ====\n"
    )


    for filename, url in DATABASE_URLS.items():


        try:

            print(
                f"Downloading {filename}..."
            )


            urllib.request.urlretrieve(
                url,
                filename
            )


            print(
                f"{filename} updated."
            )


        except Exception as e:


            print(
                f"{filename} update failed:"
            )

            print(e)



    print(
        "\nDatabase update complete."
    )




def database_count():

    packages = load_packages()

    return len(packages)
