import os
import shutil
import zipfile


class StorageManager:

    def __init__(self):
        self.base = "/storage/emulated/0/Developer"

        self.folders = [
            "Projects",
            "Backups",
            "Downloads",
            "Templates",
            "Logs"
        ]


    def check_storage(self):

        if os.path.exists("/storage/emulated/0"):
            return True

        return False



    def setup(self):

        if not self.check_storage():

            print(
                "Phone storage not available."
            )

            return False


        os.makedirs(
            self.base,
            exist_ok=True
        )


        for folder in self.folders:

            os.makedirs(
                os.path.join(
                    self.base,
                    folder
                ),
                exist_ok=True
            )


        print(
            "Storage folders created."
        )

        return True



    def show_location(self):

        print(
            "\nDeveloper Folder:"
        )

        print(
            self.base
        )



    def list_files(self, path=None):

        if path is None:
            path = self.base


        if not os.path.exists(path):

            print(
                "Folder not found."
            )

            return


        print("\nFiles:")

        for item in os.listdir(path):

            print(
                "-",
                item
            )



    def create_project(self, name):

        project = os.path.join(
            self.base,
            "Projects",
            name
        )


        os.makedirs(
            project,
            exist_ok=True
        )


        print(
            "Project created:"
        )

        print(project)



    def backup(self, source):

        if not os.path.exists(source):

            print(
                "Source not found."
            )

            return


        name = os.path.basename(source)

        destination = os.path.join(
            self.base,
            "Backups",
            name
        )


        shutil.copytree(
            source,
            destination,
            dirs_exist_ok=True
        )


        print(
            "Backup complete."
        )



    def extract_zip(self, file):

        if not zipfile.is_zipfile(file):

            print(
                "Not a valid ZIP file."
            )

            return


        folder = os.path.dirname(file)


        with zipfile.ZipFile(file) as z:

            z.extractall(folder)


        print(
            "Extraction complete."
        )
