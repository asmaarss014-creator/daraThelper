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
    Read data1.txt and data2.txt
    """

    packages = []


    for file in DATABASE_FILES:

        if os.path.exists(file):

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                for line in f:

                    line = line.strip()

                    if (
                        line
                        and not line.startswith("#")
                    ):

                        parts = line.split("|")


                        if len(parts) >= 4:

                            packages.append({
                                "name": parts[0],
                                "package": parts[1],
                                "description": parts[2],
                                "category": parts[3]
                            })


    return packages



def search_package(text):

    packages = load_packages()

    results = []


    for item in packages:

        if text.lower() in (
            item["name"].lower()
            + item["package"].lower()
            + item["category"].lower()
        ):

            results.append(item)


    return results



def install_package(package):

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



def update_database():

    print(
        "\nUpdating Dara Database...\n"
    )


    for filename, url in DATABASE_URLS.items():

        try:

            urllib.request.urlretrieve(
                url,
                filename
            )

            print(
                filename,
                "updated"
            )


        except Exception as e:

            print(
                filename,
                "failed:",
                e
            )


    print(
        "\nDatabase update finished."
    )
