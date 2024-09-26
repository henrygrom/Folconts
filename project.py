import sys
import csv

from datetime import datetime
from pathlib import Path


class Folder:
    def __init__(self, folder_path: str) -> None:
        self.folder_path = Path(folder_path)

    @property
    def folder_path(self):
        return self._folder_path
    
    # Verify if the path exists
    @folder_path.setter
    def folder_path(self, folder_path):
        try:
            if not folder_path.exists():
                raise ValueError
            self._folder_path = folder_path
        
        except ValueError:
            sys.exit("The specified path does not exist")


class File:
    def __init__(self, files: list[str]) -> list[str]:
        self.files = files

    # Verify if the file exists
    @property
    def files(self) -> list:
        return self._files
    
    @files.setter
    def files(self, files) -> None:
        validated_files = []
        for file in files:
            file = Path(file)
            try:
                if not file.is_file():
                    raise ValueError("There was something wrong with the file")
                validated_files.append(file)
            
            except ValueError as e:
                continue

        self._files = validated_files


def main() -> None:
    path, save_file = check_argc()
    report = Folder(path)
    files = get_files(report)
    files = get_metadata(files)
    export_contents(files)
    print("Succesful!")


def check_argc() -> tuple[str, str]:
    try:
        if len(sys.argv) != 3:
            raise IndexError

        elif not sys.argv[2].endswith(".csv"):
            raise ValueError
        
        else:
            return sys.argv[1], sys.argv[2]

    except (IndexError, ValueError):
        sys.exit("Usage: python project.py [Folder/Path/] [Output].csv")


def get_files(folder_path: str) -> list[dict]:
    folder_path = Path(sys.argv[1])
    files = [file.name for file in folder_path.iterdir() if file.is_file()]

    return File(files).files


def get_metadata(files: list[str]) -> list[dict]:
    # Loop through the contents of the file
    # Get the metadata of files
    # Store the metadata
    try:
        return [
                {
                    "path": file.resolve().parent,
                    "parent folder": file.resolve().parent.name,
                    "file name": file.stem,
                    "file extension": file.suffix, 
                    "last modified": datetime.fromtimestamp(file.stat().st_mtime).strftime("%m/%d/%Y %H:%M"),
                    "file size": file.stat().st_size
                } 
                for file in files
        ]
    except PermissionError:
        print("Error: File Permission Denied")
  

def export_contents(files: list[str]) -> None:
    
    try:
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
    except PermissionError:
        sys.exit("Error: File Permission Denied")
    except csv.Error:
        sys.exit("CSV Error: Make sure the arguments are correct")
    except OSError:
        sys.exit("OS Error: Make sure the arguments are correct")


if __name__ == "__main__":
    main()