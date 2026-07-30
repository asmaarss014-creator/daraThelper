import json
import os


class PackageDatabase:


    def __init__(self):

        self.path = "database"



    def load(self, filename):

        file = os.path.join(
            self.path,
            filename
        )


        if not os.path.exists(file):

            return {}


        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)



    def categories(self, filename):

        data = self.load(filename)

        return list(
            data.keys()
        )



    def get_packages(
            self,
            filename,
            category
    ):

        data = self.load(filename)

        return data.get(
            category,
            []
        )



    def search(
            self,
            filename,
            keyword
    ):

        data = self.load(filename)

        results = []


        for category, packages in data.items():

            for package in packages:

                if keyword.lower() in package.lower():

                    results.append(
                        {
                            "category": category,
                            "package": package
                        }
                    )


        return results
