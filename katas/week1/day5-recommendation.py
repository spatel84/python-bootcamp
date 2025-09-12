from collections import Counter


def is_anagram(s1: str, s2: str) -> bool:
    """
    Returns True if s1 and s2 are anagrams of each other (case-insensitive, ignores spaces).
    Example: "listen", "silent" -> True
    """
    def normalize(s: str) -> list[str]:
        return sorted("".join(s.lower().split()))
    return normalize(s1) == normalize(s2)


def char_frequency(s: str) -> dict[str, int]:
    """
    Returns a dictionary where keys are characters and values are their frequency in the string.
    Case-insensitive.
    Example: "hello" -> {"h":1, "e":1, "l":2, "o":1}
    """
    return dict(Counter(s.lower()))


def longest_word(sentence: str) -> str:
    """
    Returns the longest word in the sentence.
    If multiple words have the same length, return the first one.
    Example: "The quick brown fox" -> "quick"
    """
    words = sentence.split()
    return max(words, key=len) if words else ""
