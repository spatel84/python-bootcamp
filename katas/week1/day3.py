"""
Day 3 Python Katas - Week 1
Focus: Sets, loops, list/dictionary manipulations, basic algorithms
Instructions: Complete each function below. Run pre-commit hooks to check formatting and linting.
"""


def unique_elements(lst: list[int]) -> list[int]:
    """
    Returns a list of unique elements from the input list, preserving order.

    Raises:
        TypeError: if input is not a list of integers
    """
    # TODO: Implement function
    # Take list as an input and find unique values within the list.
    # [1,2,4,4,5,7]
    if not isinstance(lst, list):
        raise TypeError(f"unique_elements expected list but got {type(lst).__name__}")
    if not all(isinstance(x, int) for x in lst):
        raise TypeError("unique_elements expected list[int], but found non-int values")
    else:
        return list(set(lst))


def common_elements(lst1: list[int], lst2: list[int]) -> list[int]:
    """
    Returns a list of elements that are present in both lst1 and lst2.
    """
    # TODO: Implement function
    lst1 = set(lst1)
    lst2 = set(lst2)

    lst3 = lst1.intersection(lst2)
    return list(lst3)


def remove_duplicates(lst: list[int]) -> list[int]:
    """
    Returns a new list with duplicates removed.
    """
    # TODO: Implement function
    return list(set(lst))


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


# -----------------------------
# HINTS + EXPECTED BEHAVIOR
# -----------------------------
# unique_elements:
#   Hint: Use a set to check for duplicates, but preserve original order.
#   Example: [1, 2, 2, 3] -> [1, 2, 3]
#
# common_elements:
#   Hint: Use set intersection to find common values.
#   Example: [1,2,3], [2,3,4] -> [2,3]
#
# remove_duplicates:
#   Hint: Can use a set or loop with checking membership.
#   Example: [1,1,2,2,3] -> [1,2,3]
