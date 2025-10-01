"""
Day 2 – Dicts & Sets
Focus: Practice dict and set operations.
"""

from collections import Counter


def word_frequency(words: list) -> dict:
    """
    Count the frequency of each word in the list.
    Example: ["apple", "banana", "apple"] -> {"apple": 2, "banana": 1}
    """
    return Counter(words)  # Clean, efficient, Pythonic


def unique_items(seq: list) -> set:
    """
    Return a set of unique items from the list.
    Example: [1,2,2,3] -> {1,2,3}
    """
    return set(seq)  # Using set directly


def invert_dict(d: dict) -> dict:
    """
    Invert a dictionary (swap keys and values).
    Example: {"a": 1, "b": 2} -> {1: "a", 2: "b"}
    Assumes values are unique and hashable.
    """
    return {v: k for k, v in d.items()}  # Dict comprehension


if __name__ == "__main__":
    print(word_frequency(["apple", "banana", "apple", "orange", "banana"]))
    print(unique_items([1, 2, 2, 3, 4, 1]))
    print(invert_dict({"a": 1, "b": 2, "c": 3}))
