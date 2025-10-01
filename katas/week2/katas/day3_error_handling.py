"""
Day 3 – Error Handling & Logging
Focus: Practice try/except and logging basics.
"""

import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)


def safe_divide(a: float, b: float) -> float | None:
    """
    Divide a by b with error handling.
    If division by zero, log an error and return None.
    """
    # TODO: implement with try/except
    pass


def read_file(path: str) -> str | None:
    """
    Read file content safely.
    Logs error if file not found.
    """
    # TODO: implement with try/except
    pass


def parse_int(value: str) -> int | None:
    """
    Convert string to int safely.
    Logs error if conversion fails.
    """
    # TODO: implement with try/except
    pass


if __name__ == "__main__":
    # Example runs (you can expand with your own tests)
    print(safe_divide(10, 2))  # expect 5.0
    print(safe_divide(5, 0))  # expect None + log error
    print(parse_int("42"))  # expect 42
    print(parse_int("notanumber"))  # expect None + log error
