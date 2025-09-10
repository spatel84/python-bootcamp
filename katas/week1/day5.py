"""
Day 5 Python Katas - Week 1
Focus: String parsing, simple algorithms, conditionals
Instructions: Complete each function below. Run pre-commit hooks to check formatting and linting.
"""

from collections import Counter


def is_anagram(s1: str, s2: str) -> bool:
    """
    Returns True if s1 and s2 are anagrams of each other (case-insensitive, ignores spaces).
    Example: "listen", "silent" -> True
    """
    # TODO: Implement function
    raise NotImplementedError


def char_frequency(s: str) -> dict[str, int]:
    """
    Returns a dictionary where keys are characters and values are their frequency in the string.
    Case-insensitive.
    Example: "hello" -> {"h":1, "e":1, "l":2, "o":1}
    """
    # TODO: Implement function
    raise NotImplementedError


def longest_word(sentence: str) -> str:
    """
    Returns the longest word in the sentence.
    If multiple words have the same length, return the first one.
    Example: "The quick brown fox" -> "quick"
    """
    # TODO: Implement function
    raise NotImplementedError


# -----------------------------
# TESTING HARNESS (FOR LEARNING)
# -----------------------------
def test_is_anagram():
    test_cases = [
        ("listen", "silent", True),
        ("Hello", "Olelh", True),
        ("Python", "Java", False),
        ("anagram", "nag a ram", True),
    ]
    for s1, s2, expected in test_cases:
        result = is_anagram(s1, s2)
        if result == expected:
            print(f"is_anagram('{s1}', '{s2}') -> {result} ✅")
        else:
            print(f"is_anagram('{s1}', '{s2}') -> {result}, expected {expected} ❌")


def test_char_frequency():
    test_cases = [
        ("hello", {"h": 1, "e": 1, "l": 2, "o": 1}),
        ("Test", {"t": 2, "e": 1, "s": 1}),
        ("", {}),
    ]
    for text, expec
