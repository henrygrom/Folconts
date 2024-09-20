import sys
import pytest

from project import get_files
from project import check_argc


def test_check_argc_valid(monkeypatch):

    monkeypatch.setattr(sys, "argv", ["project.py", "folder_path_arg", "csv_file_arg.csv"])

    path, save_file = check_argc()

    assert path == "folder_path_arg"
    assert save_file == "csv_file_arg.csv"


def test_check_argc_invalid_extension(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["project.py", "folder_path_arg"])

