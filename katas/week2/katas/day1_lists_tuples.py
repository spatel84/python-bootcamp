"""
Day 1 – Lists & Tuples
Focus: Practice list and tuple operations.
"""


def remove_duplicates(seq: list) -> list:
    """
    Removes duplicates from a list while keeping order.
    Example: [1,2,2,3] -> [1,2,3]
    """
    # TODO: implement
    duplicate_list = []
    for x in seq:
        if x not in duplicate_list:
            duplicate_list.append(x)
    return duplicate_list


def second_largest(numbers: list) -> int | None:
    """
    Returns the second largest number in the list.
    Returns None if not possible.
    Example: [1, 5, 3, 5, 2] -> 3  [1,2,3,5]
    """
    # TODO: implement
    if len(numbers) <= 2 and numbers[0] == numbers[1]:
        return None
    else:
        unique_numbers = remove_duplicates(numbers)
        unique_numbers.sort()
        return unique_numbers[-2]


if __name__ == "__main__":
    print(remove_duplicates([1, 2, 2, 4, 3, 1]))
    print(second_largest([1, 5, 3, 5, 2]))
