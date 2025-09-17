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
    # TODO: Implement function
    # covert to lower case
    # only consider A-Z characters
    # Add the words to a list
    sentence = re.sub(r"[^a-zA-Z0-9 ]", "", sentence)
    sentence = (sentence.lower()).split()
    # print(sentence)
    count_of_word = {}
    for x in sentence:
        count_of_word[x] = sentence.count(x)

    return count_of_word


def most_common_word(sentence: str) -> str:
    """
    Returns the most frequent word in the sentence.
    If multiple words have the same frequency, return the first one.
    Example: "apple banana apple orange banana" -> "apple"
    """
    # TODO: Implement function
    # Create dictonary of words and return max count.
    if sentence == "":
        return ""

    else:
        sentence = sentence.split()
        # print(sentence)
        count_of_words = {}
        for x in sentence:
            count_of_words[x] = sentence.count(x)

    return max(count_of_words, key=count_of_words.get)


def merge_dicts(d1: dict[str, int], d2: dict[str, int]) -> dict[str, int]:
    """
    Merges two dictionaries, summing values of common keys.
    Example: {"a": 2, "b": 3}, {"a": 1, "c": 4} -> {"a": 3, "b": 3, "c": 4}
    """
    # TODO: Implement function
    # loop or iter through each dict if keys are the same add the values and store the key a new list.
    sum_dict = {}
    for x in d1:
        if x in d2:
            sum_dict[x] = d1[x] + d2[x]
        else:
            sum_dict[x] = d1[x]
    for x in d2:
        if x not in sum_dict:
            sum_dict[x] = d2[x]
    print(sum_dict)
    return sum_dict


# -----------------------------
# TESTING HARNESS (FOR LEARNING)
# -----------------------------
def test_word_count():
    text = "The cat sat on the mat. The cat was happy!"
    expected = {
        "the": 3,
        "cat": 2,
        "sat": 1,
        "on": 1,
        "mat": 1,
        "was": 1,
        "happy": 1,
    }
    result = word_count(text)
    if result == expected:
        print("word_count test passed ✅")
    else:
        print(f"word_count test failed ❌\nGot: {result}\nExpected: {expected}")


def test_most_common_word():
    test_cases = [
        ("apple banana apple orange banana", "apple"),
        ("one two three two three three", "three"),
        ("unique words only", "unique"),
        ("", ""),
    ]
    for text, expected in test_cases:
        result = most_common_word(text)
        if result == expected:
            print(f"most_common_word('{text}') -> '{result}' ✅")
        else:
            print(f"most_common_word('{text}') -> '{result}', expected '{expected}' ❌")


def test_merge_dicts():
    test_cases = [
        ({"a": 2, "b": 3}, {"a": 1, "c": 4}, {"a": 3, "b": 3, "c": 4}),
        ({}, {"x": 5}, {"x": 5}),
        ({"x": 1}, {}, {"x": 1}),
    ]
    for d1, d2, expected in test_cases:
        result = merge_dicts(d1, d2)
        if result == expected:
            print(f"merge_dicts({d1}, {d2}) -> {result} ✅")
        else:
            print(f"merge_dicts({d1}, {d2}) -> {result}, expected {expected} ❌")


if __name__ == "__main__":
    test_word_count()
    test_most_common_word()
    test_merge_dicts()
