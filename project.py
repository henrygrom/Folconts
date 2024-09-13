import sys
import os
import csv

from datetime import datetime
from pathlib import Path


class Folder:
    def __init__(self, folder_path: str, save_file: str) -> None:
        self.folder_path = Path(folder_path)
        self.savefile = save_file

    @property
    def folder_path(self):
        return self._folder_path
    
    # Verify if the path exists
    # Setter for folder_path
    @folder_path.setter
    def folder_path(self, folder_path):
        if not folder_path.exists:
            raise ValueError("The specified path does not exist.")


class File:
    def __init__(self, files: list[str]) -> list[str]:
        self.files = files

    @property
    def files(self):
        return self._files
    
    @files.setter
    def files(self, files):
        validated_files = []

        for file in files:
            file = Path(file)
            if not file.is_file():
                raise ValueError("There was something wrong with the file.")
            validated_files.append(file)

        self._files = validated_files


def main():
    test = Folder(sys.argv[1], sys.argv[2])
    files = get_files(test)
    files = get_metadata(files)
    export_contents(files)


def get_files(folder_path: str) -> list[dict]:
    folder_path = Path(sys.argv[1])
    files = [file.name for file in folder_path.iterdir() if file.is_file()]

    return File(files).files


def get_metadata(files: list[str]) -> list[dict]:
    # Loop through the contents of the file
    # Get the metadata of files
    # Store the metadata

    return [
            {
                "file name": file.name,
                "file extension": file.suffix, 
                "file size": file.stat().st_size,
                "last modified": datetime.fromtimestamp(file.stat().st_mtime).strftime("%m/%d/%Y %H:%M"),
                "parent folder": file.parent,
                "path": file.resolve()
            } 
            for file in files
    ]
   

def export_contents(files):
    with open(sys.argv[2], "w", newline="") as save_file:
        fieldnames = ["LOCATION","PARENT FOLDER","FILE NAME","FILE EXTENSION","LAST MODIFIED","SIZE"]

        writer = csv.DictWriter (save_file, fieldnames=fieldnames)
        writer.writeheader()
        for file in files:
            writer.writerow(
                {
                    "LOCATION": file["path"],
                    "PARENT FOLDER": file["parent folder"],
                    "FILE NAME": file["file name"],
                    "FILE EXTENSION": file["file extension"],
                    "LAST MODIFIED": file["last modified"],
                    "SIZE": file["file size"]
                }
            )


if __name__ == "__main__":
    main()