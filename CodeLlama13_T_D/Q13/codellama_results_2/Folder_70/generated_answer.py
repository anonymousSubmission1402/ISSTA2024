
def find_second_largest_num(numbers):
    # Find the largest element in the list
    largest = max(numbers)

    # Find the second largest element by removing the largest element from the list and finding the max again
    second_largest = max(filter(lambda x: x != largest, numbers))

    # Return the second largest element if it falls within index 28 to 32 inclusive
    return second_largest if 28 <= numbers.index(second_largest) <= 32 else None
