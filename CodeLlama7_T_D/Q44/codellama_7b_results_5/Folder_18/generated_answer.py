
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(25, 87 + 1):

        # Check if the current number is a prime number using the Sieve of Eratosthenes
        if my_list[i] > 1:
            for j in range(2, int(my_list[i]) ** 0.5 + 1):
                if my_list[i] % j == 0:
                    break
            else:
                composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 25 to index 87, both inclusive
    return composite_nums
