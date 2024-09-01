import sys
import os

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


    @classmethod
    def get_folder_path(cls):
        # Get the input path
        ...
    
    def get_files(folder_path):
        folder_path = Path(sys.argv[1])

        files = [file.name for file in folder_path.iterdir() if file.is_file()]
        
        return (files)


def main():
    
    test = Folder(sys.argv[1], sys.argv[2])
    print(test.get_files())
    
    # Loop through the contents of the file
        # Get the metadata of files
        # Store the metadata
    
    # Create a CSV file 
    ...


if __name__ == "__main__":
    main()