"""
Day 1 Python Katas - Week 1
Focus: Functions, loops, conditionals
Instructions: Complete each function below. Run pre-commit hooks to check formatting and linting.
"""


def is_even(n: int) -> bool:
    """
    Returns True if n is even, False otherwise.

    Raises:
        TypeError: if input is not an integer an exception is raised. isinstance is used to check n.
    """
    # TODO: Implement function
    if not isinstance(n, int):
        raise TypeError(f"is_even() expected int but got {type(n).__name__}")
    else:
        return n % 2 == 0


def reverse_string(s: str) -> str:
    """
    Returns the reversed version of the input string without using slicing.

    Raises:

    """
    # TODO: Implement function
    # Take the input as a string and store each element as a list. Then return the list in reverse order.
    if not isinstance(s, str):
        raise TypeError(f"reverse_string() expected str but got {type(s).__name__}")
    else:
        string_to_reverse = ""
        for x in range(len(s) - 1, -1, -1):
            string_to_reverse = string_to_reverse + s[x]
        return string_to_reverse


def fizzbuzz(n: int) -> None:
    """
    Prints numbers from 1 to n with the following rules:
      - "Fizz" for multiples of 3
      - "Buzz" for multiples of 5
      - "FizzBuzz" for multiples of both 3 and 5
    """
    # TODO: Implement function
    # print fizz if number is divisible by 3
    # print buzz if number is divisible by 5
    # print fizzbuzz if number is divisible by 3 and 5
    # use cases to check if the value of n is as above.
    if not isinstance(n, int):
        raise TypeError(f"fizzbuzz() expected int but got {type(n).__name__}")
    else:
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)


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
    else:
        print("Not all is_even tests have passed check test_case number ⚠️")


def test_reverse_string():
    test_cases = [
        ("Python", "nohtyP"),
        ("test", "tset"),
        ("Space 12", "21 ecapS"),
        (12254, TypeError),
    ]
    passed = True
    for i, (input_val, expected) in enumerate(test_cases):
        try:
            result = reverse_string(input_val)
            if result != expected:
                print(
                    f"Test {i+1} FAILED: reverse_string({input_val}) -> {result}, expected {expected}"
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
    else:
        print("Not all is_even tests have passed check test_case number ⚠️")


if __name__ == "__main__":
    # Run test harness
    test_is_even()
    # Manual checks (optional)
    test_reverse_string()
    # print(reverse_string("Python"))  # Expected: "nohtyP"
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
