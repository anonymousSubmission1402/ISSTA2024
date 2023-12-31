
def gcf_two_nums(my_list):
    # Get the indices of the two numbers
    idx1 = 48
    idx2 = 74
    # Get the two numbers
    num1 = my_list[idx1]
    num2 = my_list[idx2]
    # Initialize the greatest common factor as 1
    gcf = 1
    # Iterate from 1 to the smaller of num1 and num2
    for i in range(1, min(num1, num2) + 1):
        # If num1 and num2 are both divisible by i, then i is a common factor
        if num1 % i == 0 and num2 % i == 0:
            # Update the greatest common factor
            gcf = i

    # Return the greatest common factor
    return gcf
