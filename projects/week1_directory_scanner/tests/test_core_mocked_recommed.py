import pytest
from unittest.mock import MagicMock, patch
from week1_project.core import list_directory_content, content_of_directory, sort_by_size, sort_by_modified
from pathlib import Path

def test_list_directory_content_mocked():
    fake_files = [MagicMock(name="file1.txt"), MagicMock(name="file2.py"), MagicMock(name="subdir")]
    for f, n in zip(fake_files, ["file1.txt", "file2.py", "subdir"]):
        f.name = n
    with patch("pathlib.Path.iterdir", return_value=fake_files):
        result = list_directory_content(Path("/fake/path"))
    assert "file1.txt" in result
    assert "file2.py" in result
    assert "subdir" in result

def test_content_of_directory_mocked():
    content = ["folder1", "folder2", "script.py", "data.json"]
    result = content_of_directory(content)
    assert result["dir"] == 2
    assert result[".py"] == 1
    assert result[".json"] == 1

def test_sort_by_size_mocked():
    file1 = MagicMock(spec=Path)
    file1.name = "small.txt"
    file1.is_file.return_value = True
    file1.stat.return_value.st_size = 10

    file2 = MagicMock(spec=Path)
    file2.name = "large.txt"
    file2.is_file.return_value = True
    file2.stat.return_value.st_size = 1000

    with patch("pathlib.Path.iterdir", return_value=[file1, file2]):
        result = sort_by_size(Path("/fake/path"))

    keys = list(result.keys())
    assert keys[0] == "large.txt"
    assert keys[1] == "small.txt"
    assert result["large.txt"] == 1000
    assert result["small.txt"] == 10

def test_sort_by_modified_mocked():
    file1 = MagicMock(spec=Path)
    file1.name = "old.txt"
    file1.is_file.return_value = True
    file1.stat.return_value.st_mtime = 1000

    file2 = MagicMock(spec=Path)
    file2.name = "new.txt"
    file2.is_file.return_value = True
    file2.stat.return_value.st_mtime = 2000

    with patch("pathlib.Path.iterdir", return_value=[file1, file2]):
        result = sort_by_modified(Path("/fake/path"))

    keys = list(result.keys())
    assert keys[0] == "new.txt"
    assert keys[1] == "old.txt"
    assert result["new.txt"] == 2000
    assert result["old.txt"] == 1000
