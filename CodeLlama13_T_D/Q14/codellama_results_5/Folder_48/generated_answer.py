
def find_second_smallest_num(numbers):
    # Find the smallest number in the list
    smallest = min(numbers)

    # Filter out the smallest number from the list
    filtered = [x for x in numbers if x != smallest]

    # Return the second smallest number, or None if there is no such number
    return filtered[1] if len(filtered) > 1 else None
