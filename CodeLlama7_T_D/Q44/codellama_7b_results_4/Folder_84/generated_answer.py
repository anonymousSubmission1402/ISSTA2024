
def composite_nums_between_indices(my_list):
    # Create a set to store the composite numbers
    composite_nums = set()

    # Loop through the list and check for composite numbers between indices 30 to 48, both inclusive
    for i in range(30, 48+1):
        if is_composite(my_list[i]):
            composite_nums.add(my_list[i])

    # Return the set of composite numbers
    return composite_nums

# Check if a number is composite using the Euclidean algorithm
def is_composite(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, int(math.sqrt(n)))+1):
        if n % i == 0:
            return True

    return False
