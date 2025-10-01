import pytest
from pathlib import Path
from week1_project.core import list_directory_content, content_of_directory, sort_by_size, sort_by_modified

def test_content_of_directory():
    content = ["folder", "file.txt", "script.py", "README.md"]
    counts = content_of_directory(content)
    assert counts["dir"] == 1
    assert counts[".txt"] == 1
    assert counts[".py"] == 1
    assert counts[".md"] == 1

def test_list_and_sort(tmp_path):
    # Create files and a subdirectory
    small = tmp_path / "small.txt"
    large = tmp_path / "large.txt"
    small.write_text("hi")
    large.write_text("a" * 1000)
    (tmp_path / "subdir").mkdir()

    content = list_directory_content(tmp_path)
    assert "small.txt" in content
    assert "large.txt" in content
    assert "subdir" in content

    sizes = sort_by_size(tmp_path)
    keys = list(sizes.keys())
    assert keys[0] == "large.txt"
    assert keys[1] == "small.txt"
    assert sizes["large.txt"] > sizes["small.txt"]

    modified = sort_by_modified(tmp_path)
    assert set(modified.keys()) == {"small.txt", "large.txt"}
