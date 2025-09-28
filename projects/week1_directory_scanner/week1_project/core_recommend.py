# core.py
# Clean Python-native implementation for Week 1 project
# Features:
# - Ask user for a directory (default: current working directory)
# - List all files and subdirectories
# - Count files by type (extension) and directories
# - Sort files by size
# - Sort files by last modified time
# - Cross-platform, fully testable

import json
from pathlib import Path
from typing import Dict, List


def user_input() -> Path:
    """
    Ask the user to input a directory path.
    Default: current working directory.
    Returns a Path object.
    """
    directory = input(
        "Enter directory name or full path (defaults to current directory): "
    ).strip()
    if directory:
        path = Path(directory).expanduser().resolve()
    else:
        path = Path.cwd()
    print(f"Using directory: {path}")
    return path


def list_directory_content(directory: Path) -> List[str]:
    """
    List all files and directories in the given directory.
    Returns a list of names (str).
    """
    return [p.name for p in directory.iterdir()]


def content_of_directory(content: List[str]) -> Dict[str, int]:
    """
    Count files by type and directories.
    Returns a dictionary like: {'dir': 3, '.txt': 2, '.py': 1}
    """
    counts = {}
    for name in content:
        if "." not in name:
            counts["dir"] = counts.get("dir", 0) + 1
        else:
            ext = "." + name.split(".")[-1]
            counts[ext] = counts.get(ext, 0) + 1
    return counts


def sort_by_size(directory: Path) -> Dict[str, int]:
    """
    Sort files by size (largest first).
    Returns a dictionary {filename: size_in_bytes}.
    Directories are ignored.
    """
    files = [p for p in directory.iterdir() if p.is_file()]
    sorted_files = sorted(files, key=lambda f: f.stat().st_size, reverse=True)
    return {f.name: f.stat().st_size for f in sorted_files}


def sort_by_modified(directory: Path) -> Dict[str, float]:
    """
    Sort files by last modified time (newest first).
    Returns a dictionary {filename: modified_timestamp}.
    Directories are ignored.
    """
    files = [p for p in directory.iterdir() if p.is_file()]
    sorted_files = sorted(files, key=lambda f: f.stat().st_mtime, reverse=True)
    return {f.name: f.stat().st_mtime for f in sorted_files}


def save_to_json(filename: str, data: dict):
    """
    Save the data dictionary to a JSON file.
    """
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def main():
    dir_path = user_input()
    content = list_directory_content(dir_path)
    counts = content_of_directory(content)
    sizes = sort_by_size(dir_path)
    modified = sort_by_modified(dir_path)

    print("Directory content:", content)
    print("Counts by type:", counts)
    print("Sorted by size:", sizes)
    print("Sorted by modified:", modified)

    result = {
        "directory": str(dir_path),
        "content": content,
        "counts": counts,
        "sorted_by_size": sizes,
        "sorted_by_modified": modified,
    }

    save_to_json("output.json", result)
    print("Results saved to output.json")


if __name__ == "__main__":
    main()
