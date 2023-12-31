
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate through the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is prime
        if my_list[i] == 1:
            continue

        for j in range(2, int(my_list[i]) ** 0.5 + 1):
            # If the current number is divisible by any number between 2 and its square root, it is not prime
            if my_list[i] % j == 0:
                break

        else:

            # If the loop completes without breaking, the current number is prime
            composite_nums.add(my_list[i])
    return composite_nums
