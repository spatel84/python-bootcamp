"""
Day 2 Python Katas - Week 1 (Recommended Version)
Focus: Lists, dictionaries, loops, basic data manipulation
Improvements: Efficient word counting, punctuation handling, optional max loop.
"""

import string


def find_max(numbers: list[int]) -> int:
    """
    Returns the maximum number in the list.

    Raises:
        TypeError: if input is not a list
        ValueError: if the list is empty
    """
    if not isinstance(numbers, list):
        raise TypeError(
            f"find_max expected list of int but got {type(numbers).__name__}"
        )
    if len(numbers) == 0:
        raise ValueError("find_max expected a non-empty list")

    # Optional: Manual loop implementation (instead of max())
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val
    # return max(numbers)  # Alternative using built-in


def count_vowels(s: str) -> int:
    """
    Returns the number of vowels in the string (case-insensitive).
    """
    if not isinstance(s, str):
        raise TypeError(f"count_vowels expected string but got {type(s).__name__}")

    vowels = {"a", "e", "i", "o", "u"}
    # Build list of vowels found
    found = [ch for ch in s.lower() if ch in vowels]
    print("Vowels found:", found)  # optional for learning
    return len(found)


def word_frequency(text: str) -> dict[str, int]:
    """
    Returns a dictionary where keys are words and values are their counts.
    Case-insensitive. Ignores punctuation.
    """
    if not isinstance(text, str):
        raise TypeError(f"word_frequency expected string but got {type(text).__name__}")

    # Lowercase and remove punctuation
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()

    count_of_words = {}
    for word in words:
        count_of_words[word] = count_of_words.get(word, 0) + 1

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

    # Additional test: empty string
    empty_result = word_frequency("")
    if empty_result == {}:
        print("word_frequency('') correctly returned empty dict ✅")
    else:
        print(f"word_frequency('') returned {empty_result} ❌")


if __name__ == "__main__":
    test_find_max()
