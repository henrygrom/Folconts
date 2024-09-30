# Folconts
#### Video Demo:

### What does this program do?
Folconts is a python cli application project that extracts folder contents metadata and generates a CSV report of it. The main goal of  this project is to simplify the process of gathering detailed information about files within a specified folder, including file paths, types, sizes, and other metadata. This can be especially useful for tasks such as data organization, file management, and project audits.

The primary function of Folconts is to automate the otherwise tedious task of manually recording file information. It ensures accuracy, efficiency, and consistency across large datasets.

### Features
* File metadata extraction: Automatically extracts information like file name, size, and modification date.
* CSV report generation: Outputs the extracted metadata into a neatly formatted CSV file.
* Command-line interface: The program is designed to be run from the terminal.
* Error handling: Proper validation and error handling for arguments and file path inputs.

### project.py
The `project.py` file contains the main source code of the program, which is structured into a set of classes and functions. These components work together to validate input, process folder contents, extract metadata, and generate a CSV report. Below is an overview of the key components:
1. `class Folder`:
The `Folder` class is responsible for handling operations related to folder paths. It contains methods that verify the validity of a folder path, ensuring that the program can access and process the folder's contents correctly.

2. `class File`:
The `File` class is used to represent individual files within a folder. It includes methods that ensure the validity of a file path and filter out any invalid or inaccessible files.

3. `main()`:
The main() function is the entry point of the program. This function ensures that all steps, from argument validation to report generation, are executed smoothly. It organizes the folder processing, metadata extraction, and CSV export.

4. `check_arg()`:
The `check_arg()` function handles the validation of command-line arguments passed through the terminal. It checks whether the correct number of arguments has been provided and whether those arguments are valid. The function returns a tuple containing the processed arguments (such as folder path and CSV file name), which are then used in subsequent steps.

5. `get_files()`:
The `get_files()` function takes the validated folder path as an argument and retrieves all the files within that folder. It returns a list of dictionaries, where each dictionary represents a file and contains its basic attributes (such as file name and path). This function provides the raw data needed for further metadata extraction.

6. `get_metadata()`:
The `get_metadata()` function takes the list of files obtained from get_files() and processes each file to extract detailed metadata, such as path, parent folder, file name, file extension, last modified date, and size. It returns a list of dictionaries, where each dictionary contains comprehensive metadata for a specific file.

7. `export_contents()`:
The `export_contents()` function generates the final CSV report. It takes the list of file metadata and writes it to a CSV file, which is then saved to the location specified by the user. This function formats the data into a structured report.

### Installation
1. Clone the repository:
  ```
   git clone https://github.com/henrygrom/Folconts.git
  ```
2. Go to project directory:
   ```
   cd Folconts
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Usage
To run the program, use the following command in your terminal:
```
python project.py <folder_path> <output_csv_file>
```
For example:
```
python project.py /home/user/documents report.csv
```
This command will process all the files in /home/user/documents and output a CSV report named report.csv containing the extracted metadata.


## All thanks to CS50 team!
