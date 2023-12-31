
def composite_nums_between_indices(numbers):
    # Create a set to store the composite numbers
    composite_nums = set()
    
    # Iterate through the list of positive integers
    for i in range(21, 98):
        # Check if the current number is composite
        if all(numbers[i] % x != 0 for x in range(2, int(numbers[i] ** 0.5) + 1)):
            # If it is composite, add it to the set
            composite_nums.add(numbers[i])
    
    # Return the set of all composite numbers between indices 21 and 97, both inclusive
    return composite_nums
