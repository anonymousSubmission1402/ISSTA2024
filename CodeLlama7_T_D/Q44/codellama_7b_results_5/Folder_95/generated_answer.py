
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate through the list and check if each number is prime or not
    for i in range(len(my_list)):
        if my_list[i] > 1:
            # Check if the number is divisible by any number between 2 and the square root of the number
            for j in range(2, int(my_sqrt(my_list[i])) + 1)):
                if my_list[i] % j == 0:
                    break
            else:
                # If the number is not divisible by any number between 2 and the square root of the number, it is prime
                composite_nums.add(my_list[i])
    # Return the set of all composite numbers in the given list that are between index 26 to index 52, both inclusive
    return composite_nums
