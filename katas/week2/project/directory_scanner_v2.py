"""
Directory Scanner CLI – Week 2 Extension
Features:
- JSON output (--json flag)
- Logging (to console + file)
- Error handling for invalid paths
"""

import os
import sys
import argparse
import json
import logging


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("scanner.log"),
            logging.StreamHandler(sys.stdout)
        ]
    )


def scan_directory(path: str) -> dict:
    """
    Scans the given directory and returns metadata.
    """
    if not os.path.exists(path):
        logging.error(f"Invalid path: {path}")
        return {}

    contents = os.listdir(path)
    return {"path": path, "files": contents}


def main():
    parser = argparse.ArgumentParser(description="Directory Scanner v2")
    parser.add_argument("path", nargs="?", default=".", help="Directory to scan")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    setup_logging()
    result = scan_directory(args.path)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(result)


if __name__ == "__main__":
    main()
