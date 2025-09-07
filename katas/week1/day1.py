"""
Day 1 Python Katas - Week 1
Focus: Functions, loops, conditionals
Instructions: Complete each function below. Run pre-commit hooks to check formatting and linting.
"""


def is_even(n: int) -> bool:
    """
    Returns True if n is even, False otherwise.
    """
    # TODO: Implement function
    if not isinstance(n, int):
        raise TypeError(f"is_even() expected int but got {type(n).__name__}")
    else:
        return n % 2 == 0
    pass


def reverse_string(s: str) -> str:
    """
    Returns the reversed version of the input string without using slicing.
    """
    # TODO: Implement function
    pass


def fizzbuzz(n: int) -> None:
    """
    Prints numbers from 1 to n with the following rules:
      - "Fizz" for multiples of 3
      - "Buzz" for multiples of 5
      - "FizzBuzz" for multiples of both 3 and 5
    """
    # TODO: Implement function
    pass


# -----------------------------
# TESTING HARNESS (FOR LEARNING)
# -----------------------------
def test_is_even():
    test_cases = [
        (2, True),
        (3, False),
        (0, True),
        (-4, True),
        (-5, False),
        ("five", TypeError),
    ]
    passed = True
    for i, (input_val, expected) in enumerate(test_cases):
        try:
            result = is_even(input_val)
            if result != expected:
                print(
                    f"Test {i+1} FAILED: is_even({input_val}) -> {result}, expected {expected}"
                )
                passed = False
            else:
                print(f"Test {i+1} passed ✅")
        except Exception as e:
            if isinstance(e, expected):
                print(f"Test {i+1} passed ✅ (raised {expected.__name__})")
            else:
                print(
                    f"Test {i+1} FAILED: raised {type(e).__name__}, expected {expected.__name__}"
                )
                passed = False
    if passed:
        print("All is_even tests passed ✅")


if __name__ == "__main__":
    # Run test harness
    test_is_even()

    # Manual checks (optional)
    print(reverse_string("Python"))  # Expected: "nohtyP"
    fizzbuzz(15)  # Expected: FizzBuzz sequence
# -----------------------------
# HINTS + EXPECTED BEHAVIOR
# -----------------------------
# is_even:
#   Hint: Use the remainder operator (%) to check divisibility by 2.
#   Examples:
#     is_even(2) -> True
#     is_even(3) -> False

# reverse_string:
#   Hint: Iterate backwards or build a new string by prepending characters.
#   Examples:
#     reverse_string("Python") -> "nohtyP"

# fizzbuzz:
#   Hint: Loop 1 to n, check multiples using % operator.
#   Examples (n=5):
#     1
#     2
#     Fizz
#     4
#     Buzz
