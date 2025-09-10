import re

def is_palindrome(s: str) -> bool:
    if not isinstance(s, str):
        raise TypeError(f"is_palindrome expected str but got {type(s).__name__}")
    # Normalize: lowercase + remove non-alphanumeric
    s = re.sub(r'[^a-z0-9]', '', s.lower())
    return s == s[::-1]


def factorial(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError(f"factorial expected int but got {type(n).__name__}")
    if n < 0:
        raise ValueError("factorial expects a non-negative integer")

    if n in (0, 1):
        return 1

    factorial_n = 1
    for i in range(2, n + 1):
        factorial_n *= i
    return factorial_n


def fibonacci(n: int) -> list[int]:
    if not isinstance(n, int):
        raise TypeError(f"fibonacci expected int but got {type(n).__name__}")
    if n < 0:
        raise ValueError("fibonacci expected non-negative integer")

    if n == 0:
        return []
    if n == 1:
        return [0]

    fib_list = [0, 1]
    for x in range(2, n):
        fib_list.append(fib_list[-1] + f
