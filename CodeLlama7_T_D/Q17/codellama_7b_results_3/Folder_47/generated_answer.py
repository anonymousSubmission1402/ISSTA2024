
def all_ints_div_by_both_two_nums(my_list):
    # Define the two numbers to check for divisibility
    num1 = -90
    num2 = -74

    # Initialize an empty list to store the results
    results = []

    # Iterate through the specified range of the input list
    for i in range(42, 87 + 1):
        # Check if the current element is divisible by both num1 and num2
        if my_list[i] % num1 == 0 and my_list[i] % num2 == 0:
            # If so, add it to the results list
            results.append(my_list[i])

    # Return the results list
    return results
