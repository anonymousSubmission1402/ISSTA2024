
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(len(my_list)):
        # If the current number is greater than 1, check if it is a prime number
        if my_list[i] > 1:
            # Initialize a flag to indicate whether the current number is composite or not
            is_composite = False

            # Iterate over the list of prime numbers up to the square root of the current number
            for j in range(len(my_list[:int(math.sqrt(my_list[i])))])):
                # If the current number is divisible by any prime number in the list, it is not composite
                if my_list[i] % my_list[j] == 0:
                    is_composite = True
                    break

            # If the current number is composite, add it to the set of composite numbers
            if is_composite:
                composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 1 to index 1, both inclusive
    return composite_nums
