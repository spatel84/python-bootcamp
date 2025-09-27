# tests/test_week1.py
import os
import tempfile
import pathlib
import pytest
from week1_project.core import (
    list_directory_content,
    content_of_directory,
    sort_by_size,
    sort_by_modified,
)

def test_list_directory_content(tmp_path):
    # create test files
    (tmp_path / "file1.txt").write_text("hello")
    (tmp_path / "file2.py").write_text("print('hi')")
    os.mkdir(tmp_path / "subdir")

    result = list_directory_content(str(tmp_path))
    assert "file1.txt" in result
    assert "file2.py" in result
    assert "subdir" in result

def test_content_of_directory():
    content = ["journals", "katas", "project.txt", "homework.txt", "README.md"]
    result = content_of_directory(content)
    assert result["dir"] == 2
    assert result[".txt"] == 2
    assert result[".md"] == 1

def test_sort_by_size(tmp_path):
    small = tmp_path / "small.txt"
    large = tmp_path / "large.txt"
    small.write_text("hi")
    large.write_text("a" * 1000)

    result = sort_by_size(str(tmp_path))
    assert "small.txt" in result
    assert "large.txt" in result
    # file sizes are strings like '2B', '1000B'
    assert result["large.txt"] != result["small.txt"]

def test_sort_by_modified(tmp_path):
    file1 = tmp_path / "old.txt"
    file2 = tmp_path / "new.txt"
    file1.write_text("old file")
    file2.write_text("new file")

    result = sort_by_modified(str(tmp_path))
    assert "old.txt" in result
    assert "new.txt" in result
