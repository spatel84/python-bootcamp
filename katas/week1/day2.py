"""
Day 2 Python Katas - Week 1
Focus: Lists, dictionaries, loops, basic data manipulation
Instructions: Complete each function below. Run pre-commit hooks to check formatting and linting.
"""


def find_max(numbers: list[int]) -> int:
    """
    Returns the maximum number in the list.

    Raises:
        ValueError: if the list is empty
    """
    # TODO: Implement function
    if not isinstance(numbers, list):
        raise TypeError(
            f"find_max expected list of int but got {type(numbers).__name__}"
        )
    if len(numbers) == 0:
        raise ValueError("find_max expected a non-empty list")
    else:
        return max(numbers)


def count_vowels(s: str) -> int:
    """
    Returns the number of vowels in the string (case-insensitive).
    """
    # TODO: Implement function
    # Check if the string has any of the following character in it aeiou.
    # Create a list to append the matching vowels to and then do a len check.
    if not isinstance(s, str):
        raise TypeError(f"count_vowels expected string but got {type(s).__name__}")
    else:
        vowel = {"a", "i", "e", "o", "u"}
        number_of_vowels = []
        for x in s.lower():
            if x in vowel:
                number_of_vowels.append(x)
        return len(number_of_vowels)


def word_frequency(text: str) -> dict[str, int]:
    """
    Returns a dictionary where keys are words and values are their counts.
    Case-insensitive. Ignores punctuation.
    """
    # TODO: Implement function
    # string = "blue cat blue fan"
    words = text.lower().split(" ")
    count_of_words = {}
    for x in words:
      count_of_words[x] = words.count(x)
    
    return count_of_words


# -----------------------------
# TESTING HARNESS (FOR LEARNING)
# -----------------------------
def test_find_max():
    test_cases = [
        ([1, 2, 3, 4], 4),
        ([-5, -10, -3], -3),
        ([42], 42),
    ]
    for nums, expected in test_cases:
        result = find_max(nums)
        if result == expected:
            print(f"find_max({nums}) -> {result} ✅")
        else:
            print(f"find_max({nums}) -> {result}, expected {expected} ❌")

    # Edge case: empty list
    try:
        find_max([])
    except ValueError:
        print("find_max([]) correctly raised ValueError ✅")
    else:
        print("find_max([]) did not raise ValueError ❌")


def test_count_vowels():
    test_cases = [
        ("hello", 2),
        ("PYTHON", 1),
        ("Sky", 0),
        ("A quick brown fox", 5),
    ]
    for text, expected in test_cases:
        result = count_vowels(text)
        if result == expected:
            print(f"count_vowels('{text}') -> {result} ✅")
        else:
            print(f"count_vowels('{text}') -> {result}, expected {expected} ❌")


def test_word_frequency():
    text = "The cat sat on the mat. The cat was happy!"
    expected = {"the": 3, "cat": 2, "sat": 1, "on": 1, "mat": 1, "was": 1, "happy": 1}
    result = word_frequency(text)
    if result == expected:
        print("word_frequency test passed ✅")
    else:
        print(f"word_frequency test failed ❌\nGot: {result}\nExpected: {expected}")


if __name__ == "__main__":
    test_find_max()
    test_count_vowels()
    test_word_frequency()


# -----------------------------
# HINTS + EXPECTED BEHAVIOR
# -----------------------------
# find_max:
#   Hint: Loop through the list and keep track of the largest number seen so far.
#   Example: find_max([1, 2, 3]) -> 3
#
# count_vowels:
#   Hint: Use a set {"a", "e", "i", "o", "u"} and loop through string.lower().
#   Example: count_vowels("Hello") -> 2
#
# word_frequency:
#   Hint: Use text.lower(). Replace punctuation with spaces, then split into words.
#   Example: "The cat sat on the mat." -> {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}
