# tests/test_week1_mocked.py
import pytest
from unittest.mock import patch
import pytest
from unittest.mock import patch
from week1_project.core import (list_directory_content, content_of_directory, sort_by_size, sort_by_modified)

def test_list_directory_content_mocked():
    fake_output = ".\n..\nfile1.txt\nfile2.py\nsubdir"
    with patch("subprocess.getoutput", return_value=fake_output):
        result = list_directory_content("/fake/path")

    assert "file1.txt" in result
    assert "file2.py" in result
    assert "subdir" in result
    assert "." in result  # because of -a flag

def test_content_of_directory_mocked():
    content = ["journals", "katas", "project.txt", "homework.txt", "README.md"]
    result = content_of_directory(content)
    assert result["dir"] == 2
    assert result[".txt"] == 2
    assert result[".md"] == 1


def test_sort_by_size_mocked():
    fake_output = "file2.py 2K\nfile1.txt 1K"
    with patch("subprocess.getoutput", return_value=fake_output):
        result = sort_by_size("/fake/path")

    assert result == {"file2.py": "2K", "file1.txt": "1K"}
    assert list(result.keys())[0] == "file2.py"  # larger first

def test_sort_by_modified_mocked():
    fake_output = "file1.txt 01-01-2025-10:00:00\nfile2.py 02-01-2025-10:00:00"
    with patch("subprocess.getoutput", return_value=fake_output):
        result = sort_by_modified("/fake/path")

    assert result["file1.txt"] == "01-01-2025-10:00:00"
    assert result["file2.py"] == "02-01-2025-10:00:00"
