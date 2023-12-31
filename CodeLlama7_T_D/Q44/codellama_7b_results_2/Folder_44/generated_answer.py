
def composite_nums_between_indices(my_list):
    # Find the indices of the first and last composite numbers in the list
    first_composite_index = None
    for i, num in enumerate(my_list):
        if is_composite(num):
            first_composite_index = i
            break

    last_composite_index = None
    for i, num in enumerate(my_list[::-1])):
        if is_composite(num):
            last_composite_index = len(my_list) - 1 - i
            break

    # Return the set of composite numbers between the first and last indices
    return set(my_list[first_composite_index:last_composite_index+1])

def is_composite(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True

    return False
