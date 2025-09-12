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
    # raise NotImplementedError
    # take the the two string, put them both in lower cases and remove spaces.
    # Then arrange the letters in order.
    # Perform a check if both letter are a match.
    s1 = s1.lower()
    s1 = "".join(s1.split())
    s1 = list(s1)
    s1.sort()
    s2 = s2.lower()
    s2 = "".join(s2.split())
    s2 = list(s2)
    s2.sort()
    if s1 == s2:
        return True
    else:
        return False


def char_frequency(s: str) -> dict[str, int]:
    """
    Returns a dictionary where keys are characters and values are their frequency in the string.
    Case-insensitive.
    Example: "hello" -> {"h":1, "e":1, "l":2, "o":1}
    """
    # TODO: Implement function
    # raise NotImplementedError
    # string to dictionary.
    # Count the number of letters 
    s = s.lower()
    count_of_letter = {}
    for x in s:
	    count_of_letter[x] = s.count(x)

    return count_of_letter


def longest_word(sentence: str) -> str:
    """
    Returns the longest word in the sentence.
    If multiple words have the same length, return the first one.
    Example: "The quick brown fox" -> "quick"
    """
    # TODO: Implement function
    # senetence = s.lower()
    sentence = sentence.lower().split(" ")
    longest = max(sentence,key=len)

    return longest
    #count_of_words = {}
    #for x in sentence:
	#    count_of_words[x] = sentence.count(x)
    
    #return max(count_of_words.keys())



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
    for text, expected in test_cases:
        result = char_frequency(text)
        if result == expected:
            print(f"char_frequency('{text}') -> {result} ✅")
        else:
            print(f"char_frequency('{text}') -> {result}, expected {expected} ❌")


def test_longest_word():
    test_cases = [
        ("The quick brown fox", "quick"),
        ("I love programming", "programming"),
        ("One two three", "three"),
        ("", ""),
    ]
    for sentence, expected in test_cases:
        result = longest_word(sentence)
        if result == expected:
            print(f"longest_word('{sentence}') -> '{result}' ✅")
        else:
            print(f"longest_word('{sentence}') -> '{result}', expected '{expected}' ❌")


if __name__ == "__main__":
    test_is_anagram()
    test_char_frequency()
    test_longest_word()
