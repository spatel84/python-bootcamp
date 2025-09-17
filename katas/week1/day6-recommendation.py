"""
Day 6 Python Katas - Week 1
Focus: Dictionaries, word parsing, text manipulation
Instructions: Complete each function below. Run pre-commit hooks to check formatting and linting.
"""

import re


def word_count(sentence: str) -> dict[str, int]:
    """
    Returns a dictionary of word frequencies in the sentence.
    Case-insensitive. Ignores punctuation.
    Example: "Hello hello world!" -> {"hello": 2, "world": 1}
    """
    # Normalize: lowercase and remove punctuation
    sentence = re.sub(r"[^a-zA-Z0-9 ]", "", sentence.lower()).split()
    count_of_words = {}
    for word in sentence:
        count_of_words[word] = count_of_words.get(word, 0) + 1
    return count_of_words


def most_common_word(sentence: str) -> str:
    """
    Returns the most frequent word in the sentence.
    If multiple words have the same frequency, return the first one.
    Example: "apple banana apple orange banana" -> "apple"
    """
    if not sentence.strip():
        return ""

    # Normalize like in word_count
    sentence = re.sub(r"[^a-zA-Z0-9 ]", "", sentence.lower()).split()
    count_of_words = {}
    for word in sentence:
        count_of_words[word] = count_of_words.get(word, 0) + 1

    return max(count_of_words, key=count_of_words.get)


def merge_dicts(d1: dict[str, int], d2: dict[str, int]) -> dict[str, int]:
    """
    Merges two dictionaries, summing values of common keys.
    Example: {"a": 2, "b": 3}, {"a": 1, "c": 4} -> {"a": 3, "b": 3, "c": 4}
    """
    sum_dict = {}
    for key in d1:
        sum_dict[key] = d1[key] + d2.get(key, 0)
    for key in d2:
        if key not in sum_dict:
            sum_dict[key] = d2[key]
    return sum_dict


# -----------------------------
# TESTING HARNESS (FOR LEARNING)
# -----------------------------
def test_word_count():
    text = "The cat sat on the mat. The cat was happy!"
    expected = {"the": 3, "cat": 2, "sat": 1, "on": 1, "mat": 1, "was": 1, "happy": 1}
    result = word_count(text)
    print(
        "word_count test passed ✅"
        if result == expected
        else f"word_count test failed ❌\nGot: {result}\nExpected: {expected}"
    )


def test_most_common_word():
    test_cases = [
        ("apple banana apple orange banana", "apple"),
        ("one two three two three three", "three"),
        ("unique words only", "unique"),
        ("", ""),
    ]
    for text, expected in test_cases:
        result = most_common_word(text)
        print(
            f"most_common_word('{text}') -> '{result}' ✅"
            if result == expected
            else f"most_common_word('{text}') -> '{result}', expected '{expected}' ❌"
        )


def test_merge_dicts():
    test_cases = [
        ({"a": 2, "b": 3}, {"a": 1, "c": 4}, {"a": 3, "b": 3, "c": 4}),
        ({}, {"x": 5}, {"x": 5}),
        ({"x": 1}, {}, {"x": 1}),
    ]
    for d1, d2, expected in test_cases:
        result = merge_dicts(d1, d2)
        print(
            f"merge_dicts({d1}, {d2}) -> {result} ✅"
            if result == expected
            else f"merge_dicts({d1}, {d2}) -> {result}, expected {expected} ❌"
        )


if __name__ == "__main__":
    test_word_count()
    test_most_common_word()
    test_merge_dicts()
