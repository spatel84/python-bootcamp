"""
Day 4 Python Katas - Week 1
Focus: Strings, algorithms, loops, conditionals
Instructions: Complete each function below. Run pre-commit hooks to check formatting and linting.
"""


def is_palindrome(s: str) -> bool:
    """
    Returns True if the input string is a palindrome (case-insensitive, ignores spaces).
    Example: "Racecar" -> True, "hello" -> False
    """
    if not isinstance(s, str):
        raise TypeError(f"is_palindrome expected str but got {type(s).__name__}")
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


def factorial(n: int) -> int:
    """
    Returns the factorial of n using a loop.
    Raises ValueError if n is negative.
    Example: factorial(5) -> 120
    """
    if not isinstance(n, int):
        raise TypeError(f"factorial expected int but got {type(n).__name__}")
    if n < 0:
        raise ValueError("factorial() not defined for negative values")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def fibonacci(n: int) -> list[int]:
    """
    Returns a list containing the first n Fibonacci numbers.
    Example: fibonacci(5) -> [0, 1, 1, 2, 3]
    """
    if not isinstance(n, int):
        raise TypeError(f"fibonacci expected int but got {type(n).__name__}")
    if n < 0:
        raise ValueError("fibonacci() expected non-negative integer")

    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


# -----------------------------
# TESTING HARNESS (FOR LEARNING)
# -----------------------------
def test_is_palindrome():
    test_cases = [
        ("Racecar", True),
        ("hello", False),
        ("A man a plan a canal Panama", True),
        ("", True),
    ]
    for text, expected in test_cases:
        result = is_palindrome(text)
        if result == expected:
            print(f"is_palindrome('{text}') -> {result} ✅")
        else:
            print(f"is_palindrome('{text}') -> {result}, expected {expected} ❌")


def test_factorial():
    test_cases = [
        (0, 1),
        (1, 1),
        (5, 120),
    ]
    for n, expected in test_cases:
        result = factorial(n)
        if result == expected:
            print(f"factorial({n}) -> {result} ✅")
        else:
            print(f"factorial({n}) -> {result}, expected {expected} ❌")

    # Edge case: negative input
    try:
        factorial(-1)
    except ValueError:
        print("factorial(-1) correctly raised ValueError ✅")
    else:
        print("factorial(-1) did not raise ValueError ❌")


def test_fibonacci():
    test_cases = [
        (0, []),
        (1, [0]),
        (5, [0, 1, 1, 2, 3]),
    ]
    for n, expected in test_cases:
        result = fibonacci(n)
        if result == expected:
            print(f"fibonacci({n}) -> {result} ✅")
        else:
            print(f"fibonacci({n}) -> {result}, expected {expected} ❌")


if __name__ == "__main__":
    test_is_palindrome()
    test_factorial()
    test_fibonacci()
