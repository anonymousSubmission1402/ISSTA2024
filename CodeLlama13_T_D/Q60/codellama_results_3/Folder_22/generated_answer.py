
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over all numbers up to x
    for i in range(2, x+1):
        # Check if the number is prime
        if is_prime(i):
            # Check if the number contains no 0
            if '0' not in str(i):
                # Check if the number remains prime when the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
                if is_left_right_truncatable_prime(i):
                    result.append(i)
    
    # Sort the list in ascending order
    result.sort()
    
    return result
