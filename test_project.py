import sys
import pytest
import os
import csv

from datetime import datetime
from pathlib import Path

from project import check_argc, get_metadata, Folder, export_contents


def test_check_argc_valid(monkeypatch):

    monkeypatch.setattr(sys, "argv", ["project.py", "folder_path_arg", "csv_file_arg.csv"])

    path, save_file = check_argc()

    assert path == "folder_path_arg"
    assert save_file == "csv_file_arg.csv"


def test_check_argc_invalid_arguments(monkeypatch):
    # Invalid incomplete arguments
    monkeypatch.setattr(sys, "argv", ["project.py", "folder_path_arg"])

    with pytest.raises(SystemExit):
        check_argc()
    
    # Invalid output extension file
    monkeypatch.setattr(sys, "argv", ["project.py", "folder_path_arg", "csv_file_arg.txt"])

    with pytest.raises(SystemExit):
        check_argc()
    
    # Invalid folder path
    invalid_path = "Invalid/Folder/Path"

    with pytest.raises(SystemExit, match="The specified path does not exist"):
        folder_path_checker = Folder(invalid_path)


def test_get_metadata(tmp_path):
    # Create temporary files
    # Verify correct numbers of element passed
    # Verify data

    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    file1.write_text("Test content for file 1")
    file2.write_text("Test content for file 2")

    result = get_metadata([file1, file2])

    assert len(result) == 2

    assert result[0]["path"] == file1.resolve().parent
    assert result[0]["parent folder"] == file1.resolve().parent.name
    assert result[0]["file name"] == file1.stem
    assert result[0]["file extension"] == file1.suffix
    assert result[0]["last modified"] == datetime.fromtimestamp(file1.stat().st_mtime).strftime("%m/%d/%Y %H:%M")
    assert result[0]["file size"] == file1.stat().st_size

    assert result[1]["path"] == file2.resolve().parent
    assert result[1]["parent folder"] == file2.resolve().parent.name
    assert result[1]["file name"] == file2.stem
    assert result[1]["file extension"] == file2.suffix
    assert result[1]["last modified"] == datetime.fromtimestamp(file2.stat().st_mtime).strftime("%m/%d/%Y %H:%M")
    assert result[1]["file size"] == file2.stat().st_size


def test_export_contents(monkeypatch, tmp_path):
    # Create a temporary CSV file
    csv_file = tmp_path / "output.csv"

    # Simulate sys.argv[2] pointing to the CSV file
    monkeypatch.setattr(sys, "argv", ["script_name", "test_argument", str(csv_file)])

    # Sample metadata to write to the CSV
    sample_files = [
        {
            "path": "/test/path1",
            "parent folder": "path1",
            "file name": "file1",
            "file extension": ".txt",
            "last modified": "01/01/2024 12:00",
            "file size": 100
        },
        {
            "path": "/test/path2",
            "parent folder": "path2",
            "file name": "file2",
            "file extension": ".csv",
            "last modified": "01/02/2024 13:00",
            "file size": 200
        }
    ]

    # Run the export_contents function
    export_contents(sample_files)

    # Verify that the CSV file was created and has the correct content
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Check that the correct rows were written
    assert len(rows) == 2
    assert rows[0]["LOCATION"] == "/test/path1"
    assert rows[1]["LOCATION"] == "/test/path2"
    assert rows[0]["FILE NAME"] == "file1"
    assert rows[1]["FILE NAME"] == "file2"