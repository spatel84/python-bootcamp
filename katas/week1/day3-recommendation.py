"""
Day 3 Python Katas - Week 1 (Recommendations)
Focus: Sets, loops, list/dictionary manipulations, basic algorithms
This version preserves order where needed and ensures stable outputs.
"""


def unique_elements(lst: list[int]) -> list[int]:
    """
    Returns a list of unique elements from the input list, preserving order.

    Raises:
        TypeError: if input is not a list of integers
    """
    if not isinstance(lst, list):
        raise TypeError(f"unique_elements expected list but got {type(lst).__name__}")
    if not all(isinstance(x, int) for x in lst):
        raise TypeError("unique_elements expected list[int], but found non-int values")

    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            result.append(x)
            seen.add(x)
    return result


def common_elements(lst1: list[int], lst2: list[int]) -> list[int]:
    """
    Returns a list of elements that are present in both lst1 and lst2.
    Result is sorted for consistency.
    """
    return sorted(list(set(lst1) & set(lst2)))


def remove_duplicates(lst: list[int]) -> list[int]:
    """
    Returns a new list with duplicates removed, preserving order.
    """
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            result.append(x)
            seen.add(x)
    return result


# -----------------------------
# TESTING HARNESS (FOR LEARNING)
# -----------------------------
def test_unique_elements():
    test_cases = [
        ([1, 2, 2, 3], [1, 2, 3]),
        ([4, 4, 4, 4], [4]),
        ([], []),
    ]
    for lst, expected in test_cases:
        result = unique_elements(lst)
        if result == expected:
            print(f"unique_elements({lst}) -> {result} ✅")
        else:
            print(f"unique_elements({lst}) -> {result}, expected {expected} ❌")


def test_common_elements():
    test_cases = [
        ([1, 2, 3], [2, 3, 4], [2, 3]),
        ([5, 6], [7, 8], []),
        ([], [1, 2], []),
    ]
    for lst1, lst2, expected in test_cases:
        result = common_elements(lst1, lst2)
        if result == expected:
            print(f"common_elements({lst1}, {lst2}) -> {result} ✅")
        else:
            print(
                f"common_elements({lst1}, {lst2}) -> {result}, expected {expected} ❌"
            )


def test_remove_duplicates():
    test_cases = [
        ([1, 2, 2, 3], [1, 2, 3]),
        ([4, 4, 4, 4], [4]),
        ([], []),
    ]
    for lst, expected in test_cases:
        result = remove_duplicates(lst)
        if result == expected:
            print(f"remove_duplicates({lst}) -> {result} ✅")
        else:
            print(f"remove_duplicates({lst}) -> {result}, expected {expected} ❌")


if __name__ == "__main__":
    test_unique_elements()
    test_common_elements()
    test_remove_duplicates()
