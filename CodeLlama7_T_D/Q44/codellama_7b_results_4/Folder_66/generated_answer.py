
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Find the indices of the specified range
    start_index = my_list.index(62)
    end_index = my_list.index(63)
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate over the list between the specified indices
    for i in range(start_index, end_index + 1):
        # Check if the current element is a prime number
        if my_list[i] > 1:
            # If it is, check if it is divisible by any other prime numbers between the specified indices
            for j in range(start_index, end_index + 1):
                if i != j and my_list[j] > 1 and my_list[i] % my_list[j] == 0:
                    # If it is divisible by any other prime number, it is not a composite number
                    break
            else:
                # If it is not divisible by any other prime number, it is a composite number
                composite_numbers.add(my_list[i])

    return composite_numbers
