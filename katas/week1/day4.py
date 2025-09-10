"""
Day 4 Python Katas - Week 1
Focus: Strings, algorithms, loops, conditionals
Instructions: Complete each function below. Run pre-commit hooks to check formatting and linting.
"""

import re


def is_palindrome(s: str) -> bool:
    """
    Returns True if the input string is a palindrome (case-insensitive, ignores spaces).
    Example: "Racecar" -> True, "hello" -> False
    """
    # take a string and reverse and then compare if its the same
    if not isinstance(s, str):
        raise TypeError(f"is_palindrome expected str but got {type(s).__name__}")
    else:
        s = s.lower()
        s = "".join(s.split())
        reverse_of_s = s[::-1]

        if s == reverse_of_s:
            return True
        else:
            return False


def factorial(n: int) -> int:
    """
    Returns the factorial of n using a loop.
    Raises ValueError if n is negative.
    Example: factorial(5) -> 120
    """
    # take value n and then do n*m-1 until m=2. n=5, 5x(5-1)x(4-1)x(3-1)x(2-1).
    # Recursive function
    if not isinstance(n, int):
        raise TypeError(f"factorial expected int but got {type(n).__name__}")
    if n < 0:
        raise ValueError("expects +ve int only")
    else:
        # if n == 1 or n == 0:
        #    return 1
        # else:
        #  return n * factorial(n - 1)
        factorial_n = n
        while n > 1:
            factorial_n = factorial_n * (n - 1)
            n -= 1
        return factorial_n


def fibonacci(n: int) -> list[int]:
    """
    Returns a list containing the first n Fibonacci numbers.
    Example: fibonacci(5) -> [0, 1, 1, 2, 3]
    """
    if not isinstance(n, int):
        raise TypeError(f"fibonacci expected int but got {type(n).__name__}")
    if n < 0:
        raise ValueError("fibonacci() expected non-negative integer")
    # F(0) = 0
    # F(1) = 1
    # F(2) = F(1) + F(0) = 1
    # F(3) = F(2) + F(1) = 2
    # F(4) = F(3) + F(2) = 3
    # F(5) = F(4) + F(3) = 5
    if n == 0:
        fib_list = []
        return fib_list
    if n == 1:
        fib_list = [0]
        return fib_list
    else:
        fib_list = [0, 1]
        for x in range(2, n):
            fib_to_add = fib_list[x - 1] + fib_list[x - 2]
            fib_list.append(fib_to_add)
    return fib_list


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
        (3, 6),
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
